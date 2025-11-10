# treasury

Comprehensive balance analysis from structured JSON input.

## Usage

```bash
pocketknife treasury --file <treasury.json> [OPTIONS]
```

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `--file` | Path to JSON file with treasury addresses | Required |
| `--max-workers` | Maximum concurrent requests | `10` |

## JSON File Format

```json
{
  "liquid": [
    "pokt1liquid1address...",
    "pokt1liquid2address..."
  ],
  "app_stakes": [
    "pokt1app1address...",
    "pokt1app2address..."
  ],
  "node_stakes": [
    "pokt1node1address...",
    "pokt1node2address..."
  ],
  "validator_stakes": [
    "poktvaloper1validator1...",
    "poktvaloper1validator2..."
  ],
  "delegator_stakes": [
    "pokt1delegator1...",
    "pokt1delegator2..."
  ]
}
```

**Notes:**
- All sections are optional
- Empty arrays are ignored
- Addresses can appear in multiple sections
- Duplicate detection prevents double-counting

## Examples

### Basic Usage
```bash
pocketknife treasury --file treasury.json
```

### Custom Concurrency
```bash
# More concurrent requests for faster processing
pocketknife treasury --file treasury.json --max-workers 20

# Fewer concurrent requests (rate limiting)
pocketknife treasury --file treasury.json --max-workers 5
```

## Address Types

### Liquid Balances
Query liquid balances only:
```json
{
  "liquid": ["pokt1abc..."]
}
```

### App Stakes
Query liquid + staked balances for applications:
```json
{
  "app_stakes": ["pokt1app..."]
}
```

### Node Stakes
Query liquid + staked balances for nodes/suppliers:
```json
{
  "node_stakes": ["pokt1node..."]
}
```

### Validator Stakes
Query liquid + staked + commission:
```json
{
  "validator_stakes": ["poktvaloper1..."]
}
```
**Note:** Use validator operator addresses (`poktvaloper1...`), not consensus addresses. Commission represents validator operator earnings from all delegations.

### Delegator Stakes
Query liquid + delegated stake + rewards:
```json
{
  "delegator_stakes": ["pokt1delegator..."]
}
```
**Note:** Uses account addresses (`pokt1...`). Includes the delegated stake amount across all validators plus earned rewards.

## Output Example

```
============================================================
TREASURY BALANCE REPORT
============================================================

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LIQUID BALANCES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Address                                      Balance (POKT)
────────────────────────────────────────────────────────
pokt1abc...                                      1,000.50
pokt1def...                                      2,500.00
────────────────────────────────────────────────────────
Total Liquid:                                    3,500.50

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
NODE STAKES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Address              Liquid (POKT)    Staked (POKT)
────────────────────────────────────────────────────────
pokt1node...              100.00          15,000.00
pokt1node2...              50.00          15,000.00
────────────────────────────────────────────────────────
Total Node Stakes:                               30,150.00

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
GRAND TOTAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Category                                      Total (POKT)
────────────────────────────────────────────────────────
Liquid                                            3,500.50
Node Stakes                                      30,150.00
────────────────────────────────────────────────────────
GRAND TOTAL:                                     33,650.50
```

## Individual Balance Tools

For focused analysis, use `treasury-tools` subcommands:

```bash
# Only liquid balances
pocketknife treasury-tools liquid-balance --file treasury.json

# Only app stakes
pocketknife treasury-tools app-stakes --file treasury.json

# Only node stakes
pocketknife treasury-tools node-stakes --file treasury.json

# Only validator stakes
pocketknife treasury-tools validator-stakes --file treasury.json

# Only delegator stakes
pocketknife treasury-tools delegator-stakes --file treasury.json
```

## Use Cases

### Complete Treasury Analysis
```bash
# Single command for all balance types
pocketknife treasury --file treasury.json
```

### Progressive Analysis
```bash
# 1. Start with liquid
pocketknife treasury-tools liquid-balance --file treasury.json

# 2. Check node stakes
pocketknife treasury-tools node-stakes --file treasury.json

# 3. Full analysis
pocketknife treasury --file treasury.json
```

### Performance Tuning
```bash
# Large treasury with many addresses - use more workers
pocketknife treasury --file large-treasury.json --max-workers 50

# Rate-limited RPC - use fewer workers
pocketknife treasury --file treasury.json --max-workers 3
```

## Technical Details

### Parallel Processing
- Uses concurrent requests for speed
- Configurable worker pool (default: 10)
- Efficient for large address lists

### Balance Calculations

**Liquid:** Direct balance query
**App Stakes:** Liquid + application stake
**Node Stakes:** Liquid + supplier stake
**Validator Stakes:** Liquid + validator stake + commission
**Delegator Stakes:** Liquid + delegated stake + rewards

### Duplicate Detection
- Prevents double-counting across sections
- Addresses can appear in multiple sections safely
- First occurrence takes precedence

## Related Commands

- [**fetch-suppliers**](fetch-suppliers.md) - Get node addresses for treasury
- [**unstake**](unstake.md) - Mass unstake operations

## Troubleshooting

### "File not found"
```bash
# Use absolute path
pocketknife treasury --file /full/path/to/treasury.json

# Verify file exists
ls -la treasury.json
```

### "Invalid JSON format"
```bash
# Validate JSON
cat treasury.json | python -m json.tool
```

### Slow Performance
```bash
# Increase workers for faster processing
pocketknife treasury --file treasury.json --max-workers 30
```

### RPC Rate Limiting
```bash
# Reduce workers to avoid rate limits
pocketknife treasury --file treasury.json --max-workers 5
```

### Some Balances Show 0
- Verify addresses are correct
- Check address has balance on-chain
- Ensure address type matches section (validator addresses start with `poktvaloper1`)

[← Back to Main Documentation](../README.md)

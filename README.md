# Pocket Knife

> Syntactic sugar for `pocketd` – a Swiss army knife of common helpful commands and operations

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## Overview

**Pocket Knife** is a powerful Python-based CLI wrapper for Pocket Network's `pocketd` command line tool. It streamlines complex blockchain operations with beautiful output, sensible defaults, and user-friendly commands.

## Quick Start

```bash
# Install
git clone https://github.com/buildwithgrove/pocket-knife.git
cd pocket-knife
make install

# Use anywhere
pocketknife --help
```

## Commands

| Command | Description | Documentation |
|---------|-------------|---------------|
| **add-services** | Add or modify services from file | [📖 Docs](docs/add-services.md) |
| **delete-keys** | Delete keys from keyring (all or by pattern) | [📖 Docs](docs/delete-keys.md) |
| **export-keys** | Export private keys in hex format | [📖 Docs](docs/export-keys.md) |
| **fetch-suppliers** | Get all operator addresses for an owner | [📖 Docs](docs/fetch-suppliers.md) |
| **generate-keys** | Generate multiple keys with mnemonics | [📖 Docs](docs/generate-keys.md) |
| **import-keys** | Import keys from mnemonic or hex | [📖 Docs](docs/import-keys.md) |
| **stake-apps** | Stake applications (single or batch) | [📖 Docs](docs/stake-apps.md) |
| **treasury** | Comprehensive balance analysis | [📖 Docs](docs/treasury.md) |
| **treasury-tools** | Individual balance queries (liquid, stakes, etc.) | [📖 Docs](docs/treasury.md#individual-balance-tools) |
| **unstake** | Batch unstake operator addresses | [📖 Docs](docs/unstake.md) |

## Installation

### Quick Install (Recommended)

```bash
git clone https://github.com/buildwithgrove/pocket-knife.git
cd pocket-knife
make install
```

### Manual Installation

```bash
# Prerequisites: Python 3.8+, pipx, pocketd CLI

# Install pipx if you don't have it
brew install pipx  # macOS
# or: pip install pipx

# Clone and install
git clone https://github.com/buildwithgrove/pocket-knife.git
cd pocket-knife
pipx install .

# Or install in development mode
pipx install -e .
```

## Keyring Backends

The `os` backend is used by default. For testing and development, you can use other backends:

```bash
# Example: Using test backend (no password required)
pocketknife generate-keys 5 myapp 0 --keyring-backend test
pocketknife export-keys mykey --keyring-backend test
```

## Configuration

### Default Settings
- **Home directory:** `~/.pocket/`
- **Keyring backend:** `os` (most commands) or `test` (unstake)
- **Network:** `main`
- **Default password:** `12345678` (⚠️ always override with `--pwd` for `os` keyring!)

### Network Endpoints
- **Main RPC:** `https://shannon-grove-rpc.mainnet.poktroll.com`
- **Beta RPC:** `https://shannon-testnet-grove-rpc.beta.poktroll.com`

## Development

Built with:
- [**Typer**](https://typer.tiangolo.com/) - Modern CLI framework
- [**Rich**](https://rich.readthedocs.io/) - Beautiful terminal output
- **pocketd** - Pocket Network CLI tool

## License

MIT License - see [LICENSE](LICENSE) file for details.

---

<div align="center">

**Made with ❤️ for the Pocket Network community**

[Report Bug](https://github.com/buildwithgrove/pocket-knife/issues) • [Request Feature](https://github.com/buildwithgrove/pocket-knife/issues)

</div>

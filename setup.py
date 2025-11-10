from setuptools import setup, find_packages

setup(
    name="pocket-knife",
    version="1.0.3",
    packages=find_packages(),
    install_requires=[
        "typer>=0.9.0",
        "rich>=13.0.0",
        "pyyaml>=6.0.0",
    ],
    entry_points={
        "console_scripts": [
            "pocketknife=pocketknife.__main__:main",
        ],
    },
)
# Getting started with [woke 3.4.2](https://github.com/Ackee-Blockchain/woke)

1. Setup python environment with Python 3.7 and above

   ```zsh
   python -m venv venv
   source ./venv/bin/activate
   pip install woke
   ```

1. Create Counter contract in `contracts/`

1. Create deploy scripts in `scripts/`

## Local deployment with anvil

1. Setup configuration in `woke.toml`

   ```zsh
   # ./woke.toml
   [testing]
   cmd = "anvil"
   ```

1. Run anvil in terminal as our node

   ```zsh
   anvil
   ```

1. Set up woke accounts, recommended to import with private key from your anvil accounts

   ```zsh
   woke accounts import ALIAS=deployment
   ```

1. Generate pytypes

   ```zsh
   woke init pytypes
   ```

1. Deploy contract

   ```zsh
   woke run scripts/deploy.py
   ```

## Fuzzing and Testing

1. Create tests in `tests/`

1. Run tests

   ```zsh
   woke test tests/test_counter.py

   # or

   woke test
   ```

1. Run fuzzer

   ```zsh
   woke fuzz
   ```

# Importing library

You can use `npm install` to import `@openzeppelin/contracts` or `@uniswap/v3-core` etc.

```zsh
pnpm i @openzeppelin/contracts @uniswap/v3-core
```

Add contract in `contracts/Imports.sol`

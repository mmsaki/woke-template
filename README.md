# Getting started: Woke template

1. Create a new working directory

   ```zsh
   mkdir woke-template && cd woke-template
   ```

1. Create python environment with Python 3.7 and above

   ```zsh
   python -m venv venv
   source ./venv/bin/activate
   pip install woke
   ```

1. Create `contracts/`, `scripts/` and `tests/` directories and `woke.toml`

   ```zsh
   mkdir contracts scripts tests
   touch woke.toml
   ```

1. Setup configuration in `woke.toml`

   ```zsh
   # ./woke.toml
   [testing]
   cmd = "anvil"
   ```

1. Create simple Counter contract in `contracts/`

1. Create deploy scripts in `scripts/`

1. Run anvil in terminal, we will use `http://localhost:8545` as our node

   ```zsh
   anvil
   ```

1. Set up woke deployment account alias, you can import a private key from any anvil account

   ```zsh
   woke accounts import ALIAS=deployment
   ```

1. Generate pytypes

   ```zsh
   woke init pytypes
   ```

1. Deploy

   ```zsh
   woke run scripts/deploy.py
   ```

## Fuzzing and Testing

1. Create tests in `tests/`

1. Then run tests

   ```zsh
   woke test tests/test_counter.py

   # or

   woke test
   ```

1. Run fuzzer

   ```zsh
   woke fuzz
   ```

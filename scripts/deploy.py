from woke.deployment import *
from pytypes.contracts.Counter import Counter

NODE_URL = "http://localhost:8545"


@default_chain.connect(NODE_URL)
def main():
    default_chain.set_default_accounts(Account.from_alias("deployment"))
    counter = Counter.deploy()
    counter.setCount(10)

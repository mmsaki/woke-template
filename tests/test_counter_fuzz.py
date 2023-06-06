from woke.testing import *
from woke.testing.fuzzing import *
from pytypes.contracts.Counter import Counter


class CounterTest(FuzzTest):
    def pre_sequence(self) -> None:
        self.counter = Counter.deploy()
        self.count = 0

    @flow()
    def increment(self) -> None:
        self.counter.increment()
        self.count += 1

    @flow()
    def decrement(self) -> None:
        with may_revert(Panic(PanicCodeEnum.UNDERFLOW_OVERFLOW)) as e:
            self.counter.decrement()

        if e.value is not None:
            assert self.count == 0
        else:
            self.count -= 1

    @invariant(period=10)
    def count(self) -> None:
        assert self.counter.count() == self.count


@default_chain.connect()
def test_counter():
    default_chain.set_default_accounts(default_chain.accounts[0])
    CounterTest().run(sequences_count=30, flows_count=100)

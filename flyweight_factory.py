from .flyweight.flyweight import Flyweight

class FlyweightFactory:
    def __init__(self, initial_flyweights: list[list] | None = None) -> None:
        self._flyweights: dict[str, Flyweight] = {}
        if initial_flyweights:
            for state in initial_flyweights:
                key = self._get_key(state)
                self._flyweights[key] = Flyweight(state)

    @staticmethod
    def _get_key(state: list) -> str:

        return "_".join(sorted(str(s) for s in state))

    def get_flyweight(self, shared_state: list) -> Flyweight:
        key = self._get_key(shared_state)
        if key not in self._flyweights:
            print(f"FlyweightFactory: Creating new flyweight for key '{key}'.")
            self._flyweights[key] = Flyweight(shared_state)
        else:
            print(f"FlyweightFactory: Reusing existing flyweight for key '{key}'.")
        return self._flyweights[key]

    def list_flyweights(self) -> None:
        count = len(self._flyweights)
        print(f"FlyweightFactory: {count} flyweight(s) cached:")
        for key in self._flyweights:
            print(f"  - {key}")

class Flyweight:
    def __init__(self, shared_state: list) -> None:
        self._shared_state = tuple(shared_state)  

    def operation(self, unique_state: str) -> None:
        s = str(self._shared_state)
        u = str(unique_state)
        print(f"Flyweight: shared ({s}) + unique ({u}) state.")

from .flyweight_factory import FlyweightFactory

def add_car_to_database(
    factory: FlyweightFactory,
    license_plate: str,
    owner: str,
    brand: str,
    model: str,
    color: str,
) -> None:

    flyweight = factory.get_flyweight([brand, model, color])
    flyweight.operation(f"{license_plate}, {owner}")


def main() -> None:
    # Pre-populate the factory with known car types
    factory = FlyweightFactory([
        ["Chevrolet", "Camaro2018", "pink"],
        ["Mercedes", "C300", "black"],
        ["BMW", "M5", "red"],
        ["BMW", "X6", "white"],
    ])
    factory.list_flyweights()

    print("\n--- Client: Adding cars ---\n")

    add_car_to_database(factory, "AA-12-BB", "James Doe", "BMW", "M5", "red")

    add_car_to_database(factory, "CC-34-DD", "Jane Doe", "BMW", "X1", "silver")

    print()
    factory.list_flyweights()


if __name__ == "__main__":
    main()

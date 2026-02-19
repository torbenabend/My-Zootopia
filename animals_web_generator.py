import json


ANIMAL_CHARACTERISTICS = {
    "Name": lambda d: d.get("name"),
    "Diet": lambda d: d.get("characteristics", {}).get("diet"),
    "Location": lambda d: (
        ", ".join(d.get("locations")) if d.get("locations") else None
    ),
    "Type": lambda d: d.get("characteristics", {}).get("type")
}


def load_data(file_path):
    """ Load a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def print_field(label, value):
    """ Print a label and its value """
    if value:
        print(f"{label}: {value}")


def print_animal_information(animal_info):
    """ Print animal information """
    for characteristic, extractor in ANIMAL_CHARACTERISTICS.items():
        value = extractor(animal_info)
        print_field(characteristic, value)
    print()


def main():
    animals_data = load_data("animals_data.json")
    for animal in animals_data:
        print_animal_information(animal)


if __name__ == "__main__":
    main()

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


def load_html_template(file_path):
    """ Load an HTML template """
    with open(file_path, "r") as handle:
        return handle.read()


def create_webpage(html_input):
    """ Create html file for webpage """
    with open("animals.html", "w") as html:
        html.write(html_input)


def get_animal_characteristics(animal_info):
    """ Collect animal characteristics """
    characteristics = ""
    for characteristic, extractor in ANIMAL_CHARACTERISTICS.items():
        value = extractor(animal_info)
        if value is not None:
            characteristics += f"{characteristic}: {value}\n"
    return characteristics + "\n"


def render_animal_characteristics(animals):
    """ Render animal characteristics for each animal """
    animals_html = ""
    for animal in animals:
        animals_html += get_animal_characteristics(animal)
    return animals_html


def main():
    animals_data = load_data("animals_data.json")
    template_data = load_html_template("animals_template.html")
    animals_html = render_animal_characteristics(animals_data)
    animals_webpage = template_data.replace(
        "__REPLACE_ANIMALS_INFO__", animals_html
    )
    create_webpage(animals_webpage)


if __name__ == "__main__":
    main()

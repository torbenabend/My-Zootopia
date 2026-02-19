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


def render_animal_name(animal_info):
    rendered_name = ""
    animal_name = ANIMAL_CHARACTERISTICS["Name"](animal_info)
    if animal_name is not None:
        rendered_name += '<div class="card__title">'
        rendered_name += f'{animal_name}'
        rendered_name += '</div>'
    return rendered_name


def render_animal_characteristic(characteristic, animal_info):
    rendered_characteristic = ""
    animal_characteristic = ANIMAL_CHARACTERISTICS[characteristic](animal_info)
    if animal_characteristic is not None:
        rendered_characteristic += (f'<strong>{characteristic.capitalize()}'
                                    f':</strong> ')
        rendered_characteristic += f'{animal_characteristic}<br/>'
    return rendered_characteristic


def get_animal_characteristics(animal_info):
    """ Collect animal characteristics """
    characteristics = ""
    for characteristic, extractor in ANIMAL_CHARACTERISTICS.items():
        value = extractor(animal_info)
        if value is not None:
            if characteristics == "Name":
                characteristics += '<div class="card__title">'
                characteristics += f'{value}<br/>\n'
    return characteristics + "\n"


def render_animal_characteristics(animals):
    """ Render animal characteristics for each animal """
    animals_html = ""
    for animal in animals:
        animals_html += '<li class="cards__item">'
        animals_html += render_animal_name(animal)
        animals_html += '<p class="card__text">'
        animals_html += render_animal_characteristic("Diet", animal)
        animals_html += render_animal_characteristic("Location", animal)
        animals_html += render_animal_characteristic("Type", animal)
        animals_html += '</p>'
        animals_html += "</li>"
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

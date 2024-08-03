def find_favs(data: dict):
    dt = {}
    for key, value in data.items():
        if key.startswith("fav_") and value:
            color = key.replace("fav_color_", "")
            animal = key.replace("fav_animal_", "")
            if "color" in key:
                dt["fav_color"] = color.title()
            elif "animal" in key:
                dt["fav_animal"] = animal.title()
    return dt
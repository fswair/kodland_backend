from pydantic import BaseModel
import typing

class Item(BaseModel):
    name: str
    interests: str
    fav_animal_dog: typing.Optional[str] = None
    fav_animal_cat: typing.Optional[str] = None
    fav_animal_parrot: typing.Optional[str] = None
    fav_color_red: typing.Optional[str] = None
    fav_color_blue: typing.Optional[str] = None
    fav_color_green: typing.Optional[str] = None
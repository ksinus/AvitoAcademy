from keyword import iskeyword
import json


class JsonToObj:
    """
    Converts JSON objects to python objects
    with access to attributes via a point
    """

    def __init__(self, mapping) -> None:
        for key, value in mapping.items():
            if iskeyword(key) is True:
                key += '_'
            self.__dict__[key] = JsonToObj(value) \
                if isinstance(value, dict) else value


class ColorizeMixin:
    """ Mixin class for changing repr color """

    def __init__(self, color_code=35) -> None:
        self.repr_color_code = color_code

    def __str__(self) -> str:
        return f"\033[1;{self.repr_color_code};40m {self.__repr__()} \033[m"


class Advert(ColorizeMixin):
    """ Transform JSON adverts into class objects """

    def __init__(self, mapping) -> None:
        super().__init__()
        self.__dict__.update(JsonToObj(mapping).__dict__)
        if self.__dict__.get('price', 0) < 0:
            raise ValueError('Price must be non-negative')

    def __repr__(self) -> str:
        return f'{self.title} | {self.price} ₽'

    @property
    def price(self) -> str:
        return self.__dict__.get('price', 0)

    @property
    def title(self) -> str:
        return self.__dict__.get('title')


if __name__ == '__main__':
    lesson_str = """{
    "title": "python", "price": 0,
    "location": {
    "address": "город Москва, Лесная, 7",
    "metro_stations": ["Белорусская"]
    }
    }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    print(lesson_ad.location.address)

    lesson_str = """{
        "title": "Вельш-корги"
    
    }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    print(lesson_ad.repr_color_code)

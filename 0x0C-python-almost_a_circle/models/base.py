#!/usr/bin/python3
"""
This module defines a base model class
"""
import json


class Base:
    """
    This class Represents the base model

    This class is the “base” of all other classes
    in this project
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes the base class instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        This function returns JSON string representation
        of `list_dictionaries`
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        This function writes the JSON string representation
        of `list_objs` to a file
        """
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        This function returns the list of JSON string
        representation `json_string`
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        This function returns an instance with all
        attributes already
        """
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        else:
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """
        This function returns a list
        of instances
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**obj) for obj in list_dicts]
        except IOError:
            return []

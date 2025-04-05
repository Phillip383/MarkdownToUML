from src.diagrams.umltype import UMLType


class UMLDiagram():

    def __init__(self, typ, name, methods=[], attributes=[]):
        self.__type = typ
        self.__name = name
        self.__methods = methods
        self.__attributes = attributes

    def get_type(self) -> UMLType:
        return self.__type

    def get_name(self) -> str:
        return self.__name

    def get_methods(self) -> list:
        return self.__methods

    def get_attributes(self) -> list:
        return self.__attributes


from src.umldiagram import UMLDiagram
from src.umltype import UMLType

class Splitter():
    def __init__(self):
        self.__diagrams = []

    def get_diagrams(self):
        return self.__diagrams

    def split_file_to_diagrams(self, file) -> list:
        name = self.__split_name(file)
        typ = self.__split_type(file)
        attributes = self.__split_attributes(file)
        methods = self.__split_methods(file)
        print(attributes)
        self.__diagrams.append(UMLDiagram(typ=typ, name=name, methods=methods, attributes=attributes))
        return self.__diagrams

    def __split_type(self, file):
        match file[file.find("## "): file.find("\n")].lower():
            case "class":
                return UMLType.CLASS

    def __split_name(self, file):
        return file[file.find("## "): file.find("\n")]

    def __split_attributes(self, file):
        lines = file.split("\n")
        attributes = []
        for line in lines:
            line = line.strip()
            if line.startswith("-") and not "(" in line:
                attributes.append(line.replace("- ", ""))
        return attributes


    def __split_methods(self, file):
        lines = file.split("\n")
        methods = []
        for line in lines:
            if line.startswith("-") and "()" in line:
                methods.append(line)
        return methods


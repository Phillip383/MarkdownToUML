from src.diagrams.umldiagram import UMLDiagram

class ClassDiagram(UMLDiagram):
    def __init__(self, typ, name, methods, attributes):
        super().__init__(typ, name)
        self.__methods = methods
        self.__attributes = attributes
    
    def get_methods(self) -> list:
        return self.__methods

    def get_attributes(self) -> list:
        return self.__attributes
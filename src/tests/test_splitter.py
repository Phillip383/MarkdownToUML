import unittest
from src.splitter import Splitter
from src.diagrams.umldiagram import UMLDiagram
from src.diagrams.umltype import UMLType

class TestSplitter(unittest.TestCase):
    def test_attributes(self):
        splitter = Splitter()
        md = """
        # Class
        ## Person

        - -name: String
        - -age: int
        - -height: float
        - +GetName(): String
        - +SetName(name: String): void
        - +GetAge(): int
        - +SetAge(age: int): void
        - +GetHeight(): float
        - +SetHeight(height: float): void
        """
        diagrams = splitter.split_file_to_diagrams(md)
        for diagram in diagrams:
            self.assertEqual(diagram.get_attributes(), 
                            ["-name: String", "-age: int", "-height: float"])
            self.assertEqual(diagram.get_methods(),
                            ["+GetName(): String", "+SetName(name: String): void", "+GetAge(): int", "+SetAge(age: int): void", "+GetHeight(): float", "+SetHeight(height: float): void"])
            self.assertEqual(diagram.get_type(), UMLType.CLASS)
            self.assertEqual(diagram.get_name(), "Person")

if __name__ == "__main__":
    unittest.main()

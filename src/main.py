from src.splitter import Splitter
from src.generator import Generator


def main():
    splitter = Splitter()
    generator = Generator()
    
    splitter.split_file_to_diagrams("""
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
        """)
    generator.generate_image(None, splitter)



if __name__ == "__main__":
    main()
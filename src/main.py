from src.splitter import Splitter
from src.generator import Generator


def main():
    splitter = Splitter()
    generator = Generator()
    
    splitter.split_file_to_diagrams("# Class\n ## Person\n - -name: str\n - -age: int\n")
    generator.generate_image(None, splitter)



if __name__ == "__main__":
    main()
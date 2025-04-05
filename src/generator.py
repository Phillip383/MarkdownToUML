from src.constants import *
from src.splitter import Splitter
from PIL import Image, ImageDraw


class Generator():
    def __init__(self):
        ...

    def generate_image(self, type, splitter: Splitter):
        img = Image.new("RGB",(500, 500), (255, 0, 0)) # type: ignore
        
        draw = ImageDraw.Draw(img)

        draw.rectangle([5, 5, 495, 495], (0, 0, 0), (34, 34, 20), 5)

        
        img.save("test.png")
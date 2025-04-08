from src.splitter import Splitter
from src.diagrams.umltype import UMLType


from PIL import Image, ImageDraw


class Generator:
    def __init__(self): ...

    def generate_image(self, type, splitter: Splitter):
        img = Image.new("RGB", (500, 500), (255, 255, 255))  # type: ignore

        draw = ImageDraw.Draw(img)
        vert_draw_pos = 30
        for diagram in splitter.get_diagrams():
            draw.text(
                [240, 0], # type: ignore
                diagram.get_name(),
                fill=(0, 0, 0),
                font_size=12,
                align="center",
            ) 
            draw.line([0, 25, 500, 25], fill=(0, 0, 0))
            if diagram.get_type() == UMLType.CLASS:
                self.generate_class_info(draw, diagram, vert_draw_pos)

        img.save("test.png")

    def generate_class_info(self, draw, diagram, vert_draw_pos):
        for attribute in diagram.get_attributes():
            draw.text(
                [15, vert_draw_pos],
                attribute,
                fill=(0, 0, 0),
                font_size=12,
                align="center",
            )
            vert_draw_pos += 15

        vert_draw_pos += 5
        draw.line([0, vert_draw_pos, 500, vert_draw_pos], fill=(0, 0, 0))
        vert_draw_pos += 5

        for method in diagram.get_methods():
            draw.text(
                [15, vert_draw_pos],
                method,
                fill=(0, 0, 0),
                font_size=12,
                align="center",
            )
            vert_draw_pos += 15

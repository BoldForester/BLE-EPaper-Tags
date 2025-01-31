from PIL import Image

def convert_image_to_tag_format(image_path):
    """Converts an image to a format suitable for E-Paper Tag."""
    image = Image.open(image_path).convert('1').resize((200, 200))
    data = bytearray()
    pixels = image.load()
    for y in range(image.height):
        for x in range(image.width):
            pixel = pixels[x, y]
            data.append(0xFF if pixel == 0 else 0x00)
    return bytes(data)

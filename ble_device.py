import asyncio
from bleak import BleakClient

class EPaperTagDevice:
    def __init__(self, hass, mac_address: str):
        self._hass = hass
        self._mac_address = mac_address
        self._client = None

    async def connect(self):
        """Connect to the BLE device."""
        self._client = BleakClient(self._mac_address)
        await self._client.connect()

    async def send_graphics(self, image_path):
        """Convert image and send to the E-Paper tag."""
        from PIL import Image
        # Convert image to monochrome format (1-bit)
        image = Image.open(image_path).convert('1').resize((200, 200))
        data = self._convert_image_to_data(image)
        await self._client.write_gatt_char(0x1234, data)

    def _convert_image_to_data(self, image):
        """Convert image to raw data format for the tag."""
        # Convert the image to bytes, this is where you adjust for specific tag format
        data = bytearray()
        pixels = image.load()
        for y in range(image.height):
            for x in range(image.width):
                pixel = pixels[x, y]
                data.append(0xFF if pixel == 0 else 0x00)
        return bytes(data)

    async def disconnect(self):
        """Disconnect from the BLE device."""
        if self._client:
            await self._client.disconnect()

from homeassistant.components.sensor import SensorEntity
from homeassistant.const import TEMP_CELSIUS

class EPaperTagSensor(SensorEntity):
    """Representation of the E-Paper Tag sensor."""

    def __init__(self, device: EPaperTagDevice):
        self._device = device
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return "E-Paper Tag"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    async def async_update(self):
        """Update the sensor state."""
        self._state = await self._device.read_vital_parameters()

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .ble_device import EPaperTagDevice

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the E-Paper tag device integration."""
    # Register services or device in Home Assistant
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up E-Paper tag device from a config entry."""
    device = EPaperTagDevice(hass, entry.data["mac_address"])
    hass.data[entry.entry_id] = device
    return True

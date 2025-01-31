from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from .ble_device import EPaperTagDevice

class EPaperTagConfigFlow(config_entries.ConfigFlow, domain="epaper_tag"):
    """Handle a config flow for the E-Paper tag."""
    
    async def async_step_user(self, user_input=None):
        """Handle the user step to add the BLE device."""
        if user_input is None:
            return self.async_show_form(step_id="user")
        
        mac_address = user_input["mac_address"]
        device = EPaperTagDevice(self.hass, mac_address)
        await device.connect()
        await device.disconnect()
        
        return self.async_create_entry(title="E-Paper Tag", data={"mac_address": mac_address})

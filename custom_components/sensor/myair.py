from homeassistant.const import TEMP_CELSIUS
from homeassistant.helpers.entity import Entity
import requests
import json
import voluptuous as vol
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import CONF_SCAN_INTERVAL
from homeassistant.util import Throttle
import homeassistant.helpers.config_validation as cv

ZONE = 'zone'
URL = 'url'

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(ZONE): cv.string,
    vol.Required(URL): cv.string
})

def setup_platform(hass, config, add_devices, discovery_info=None):
    """Setup the sensor platform."""
    czone = config.get(ZONE)
    import_url = config.get(URL)
    czone_list = czone.split(",")
    for ind_zone in czone_list:    
     add_devices([MyairSensor(ind_zone,import_url)])

class MyairSensor(Entity):
    """Representation of a Sensor."""

    def __init__(self,czone={},import_url={}):
        """Initialize the sensor."""
        self._state = None
        self._czone = czone
        self._import_url = import_url

    @property
    def name(self):
        """Return the name of the sensor."""
        return str(self._czone) + ' Temperature'

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        return TEMP_CELSIUS

    def update(self):
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """
        myair_url = "http://" + str(self._import_url) + "/getSystemData"
        response = requests.get(myair_url)
        parsed_json=json.loads(response.text)
        jsonjson = parsed_json['aircons']['ac1']['zones'] 
        for k,v in jsonjson.items():
          if v['name'] == self._czone:
           temp = v['measuredTemp']  
           self._state = temp

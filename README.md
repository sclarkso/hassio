# hassio
Required in your configuration.yaml to configure this sensor:

```
sensor:
  - platform: myair
    zone: "ZONE NAMES SEPERATED BY COMMAS"
    url: 192.168.0.1:2025 (IP Address and Port of Controller)

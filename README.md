# hassio
Required in your configuration.yaml to configure this sensor:

```
sensor:
  - platform: myair
    zone: "ZONE NAMES SEPERATED BY COMMAS"
    url: 192.168.0.1:2025 (IP Address and Port of Controller)
```
I used mitmproxy/fiddler to track down the url for my controller.

Example of actual code in configuration.yaml:

```
sensor:
  - platform: myair
    zone: "MEDIA,LIVING,MAIN BEDROOM,GUEST"
    url: 10.0.0.110:2025
```
This is what it looks like in Home Assistant:

![Imgur](https://i.imgur.com/8tbQ18i.png)

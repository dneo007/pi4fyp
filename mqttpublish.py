# MQTT Publish Demo
# Publish two messages, to two different topics

import paho.mqtt.publish as publish

publish.single("CoreElectronics/test", "Hello", hostname="192.168.1.3")
publish.single("CoreElectronics/topic", "World!", hostname="192.168.1.3")
print("Done")

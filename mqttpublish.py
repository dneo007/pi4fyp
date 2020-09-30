# MQTT Publish Demo
# Publish two messages, to two different topics

import paho.mqtt.publish as publish

#192.168.1.3

#hotspot
#publish.single("myoware/results", "10", hostname="192.168.43.19")
#desktop
publish.single("myoware/results", "World!", hostname="192.168.1.3")
print("Done")

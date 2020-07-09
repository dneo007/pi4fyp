# MQTT Publish Demo
# Publish two messages, to two different topics

import paho.mqtt.publish as publish

publish.single("myoware/results", "10", hostname="192.168.1.3")
#publish.single("myoware/results2", "World!", hostname="192.168.1.3")
print("Done")

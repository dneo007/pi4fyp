# MQTT Publish Demo
# Publish two messages, to two different topics

import paho.mqtt.publish as publish
import sys

#192.168.1.3

#hotspot
#publish.single("myoware/results", "10", hostname="192.168.43.19")
#desktop
#publish.single("myoware/results", "10", hostname="192.168.126.151")
#Router
publish.single("myoware/results", sys.argv[1], hostname="192.168.0.196")
print("Done")

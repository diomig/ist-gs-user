import paho.mqtt.client as mqtt_client

globalName = "myGS/"

class Topics:
    freq = f'{globalName}radio/freq'
    bw = f'{globalName}radio/bw'
    cr = f'{globalName}radio/cr'
    plen = f'{globalName}radio/plen'
    sf = f'{globalName}radio/sf'
    txpwr = f'{globalName}radio/txpwr'
    lnag = f'{globalName}radio/lnag'
    chksum = f'{globalName}radio/chksum'
    ackdelay = f'{globalName}radio/ackd'
    ackwait = f'{globalName}radio/ackw'
    rxto = f'{globalName}radio/rxto'


# Define the MQTT topics
pub_topics = ["radio/freq", "radio/bw", "radio/br", "radio/chksum", "msg/cmd"]
sub_topics = ["msg/telemetry", "msg/payload", "msg/reply"]

# Define the MQTT broker address and port
# broker_address = "10.42.0.236"
# broker_address = "test.mosquitto.org"  # "localhost"
# broker_port = 1883


# Define the on_connect callback function


def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # Subscribe to all topics
    for topic in sub_topics:
        print(globalName + topic)
        client.subscribe(globalName + topic)


# Define the on_message callback function


# def on_message(client, userdata, msg):
#     print(f"Received message on {msg.topic}: {msg.payload.decode()}")


# Initialize the MQTT client
mqttC = mqtt_client.Client()

# Assign the callback functions
mqttC.on_connect = on_connect
# mqttC.on_message = on_message

# Connect to the broker
# mqttC.connect(broker_address, broker_port)

# Start the MQTT client loop
# mqttC.loop_start()

# Publish messages to the topics
# try:
#     while True:
#         cmd = input("user cmd:").split()
#         if len(cmd) > 1:
#             topic, value = cmd
#         else:
#             continue
#
#         if topic not in pub_topics:
#             print("Topic not available")
#         print(mqttC.publish(globalName + topic, value))
#         """
#         for i, topic in enumerate(topics):
#             message = f"Message from Program 2 to {topic}"
#             mqttC.publish(topic, message)
#             print(f"Published message to {topic}: {message}")
#             time.sleep(1)
#         time.sleep(5)  # Delay between each round of publishing
#         """
# except KeyboardInterrupt:
#     mqttC.loop_stop()
#     mqttC.disconnect()
#
# # Stop the MQTT client loop and disconnect
# mqttC.loop_stop()
# mqttC.disconnect()

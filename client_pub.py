# install instructions for paho.mqtt.client
'''
//the latest stable version is available in the Python Package Index (PyPi) and can be installed using

pip install paho-mqtt
or 

//To obtain the full code, including examples and tests, you can clone the git repository:

git clone https://github.com/eclipse/paho.mqtt.python
//Once you have the code, it can be installed from your repository as well:

'''
import paho.mqtt.client as mqtt
import time


def on_publish(client, userdata, mid):
    print('message published')


client = mqtt.Client("rpi_client2")  # this name should be unique
client.on_publish = on_publish
client.connect('127.0.0.1', 1883)
# start a new thread
client.loop_start()

k = 0
while True:
    k = k + 1
    if k > 20:
        k = 1

    try:
        msg = str(k)
        pubMsg = client.publish(
            topic='rpi/broadcast',
            payload=msg.encode('utf-8'),
            qos=0,
        )
        pubMsg.wait_for_publish()
        print(pubMsg.is_published())

    except Exception as e:
        print(e)

    time.sleep(2)

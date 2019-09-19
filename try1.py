import paho.mqtt.client as mqtt
import ssl
import json
import time

###### Configuration ##########
# Pick Local our Cloud Access #
#
# Local Access
#host = "localhost"
#host = "10.0.0.254"
#port = 1883
#topic = "tags" 
#
# Via "Cloud" stream
host = "mqtt.cloud.pozyxlabs.com"
fp = open("secrets.json")
dataDict = json.load(fp)
port = dataDict["port"]
topic = dataDict["topic"]
username=topic
apikey = dataDict["apikey"]
password=apikey
#### End Configuration #######

def on_connect(client, userdata, flags, rc):
    print(mqtt.connack_string(rc))

# callback triggered by a new Pozyx data packet
def on_message(client, userdata, msg):
    ''' NOTE: errors/bugs here will fail silently, which is very bad.
        You cannot call out or refer to functions, must be global variables,
        I think.  Needs more investigation.
    '''
    unixtime = time.time()
    #print("DEBUG: Positioning update:", msg.payload.decode() ) #DEBUG
    payload = msg.payload
    #print("DEBUG: type:", type(payload) ) #DEBUG
    decoded = msg.payload.decode()
    #print("DEBUG: Positioning update:", decoded ) #DEBUG
    datastore = json.loads(decoded)
    tagLst = datastore
    #print("DEBUG: tagLst dtype:", type(tagLst) ) #DEBUG
    for tag in tagLst :
        #print("DEBUG: tag dict:", str(tag)) #DEBUG
        #print("DEBUG: tag dtype:", type(tag) ) #DEBUG
        tagid = int(tag[ "tagId" ])
        success = tag["success"]
        if success :
            #print("DEBUG: parseTagObj") #DEBUG
            #print("DEBUG: tag ID:", tagid)
            timestamp = tag[ "timestamp" ]
            #print("DEBUG: timestamp",timestamp) #DEBUG
            data = tag[ "data" ]
            tagData = data["tagData"]
            blinkindex = tagData["blinkIndex"]
            #print("DEBUG: blinkindex",blinkindex) #DEBUG
            coordinates = data[ "coordinates" ]
            #print("DEBUG: coordinates", coordinates) #DEBUG
            #print("DEBUG: parseTagObj") #DEBUG
            x = coordinates['x']
            y = coordinates['y']
            z = coordinates['z']
            #print("DEBUG: %d" % (blinkindex)) #DEBUG
            print("%f,%d,%d,%d,%d,%d" % (unixtime, tagid, blinkindex,x,y,z))
        else :
            print("ERROR: tag error:", tag["errorCode"])
    #print("type:", type(datastore)) #DEBUG
    #print("Number of tags:", len(tagLst) )

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed to topic!")


# Pick Local our Cloud Access  ######
# This goes with local access
#client = mqtt.Client()
#
# This goes with cloud access
client = mqtt.Client(transport="websockets")
client.username_pw_set(username, password=password)
####### Local or Cloud ##############

# sets the secure context, enabling the WSS protocol
client.tls_set_context(context=ssl.create_default_context())

# set callbacks
client.on_connect = on_connect
client.on_message = on_message
client.on_subscribe = on_subscribe
client.connect(host, port=port)
client.subscribe(topic)

# works blocking, other, non-blocking, clients are available too.
client.loop_forever()

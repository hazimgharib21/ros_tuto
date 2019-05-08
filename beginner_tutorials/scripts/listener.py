#!/usr/bin/env python

# Simple listener demo that subscribed messages from 'chatter' topic
#
# Create executable script
#   chmod +x listener.py
#
# Run script (without launch file)
#   rosrun beginner_tutorials listener.py
#
# Run script (with launch file)
#   roslaunch beginner_tutorials talker_listener.launch


import rospy
from std_msgs.msg import String

# Subscriber callback function
def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def listener():

    # Initialize our node with name listener
    rospy.init_node('listener', anonymous=True)

    # Node subscribes to the chatter topic which is of type String
    # When new messages are received, callback is invoded with the
    # message as the first argument
    rospy.Subscriber("chatter", String, callback)

    # keeps the node from exiting untile the node has been shutdown
    rospy.spin()

if __name__ == '__main__':
    listener()

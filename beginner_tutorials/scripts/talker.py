#!/usr/bin/env python

# Simple talker demo that published std_msgs/String messages to the 'chatter' topic
#
# Create executable script
#   chmod +x talker.py
#
# Run script (without launch file)
#   rosrun beginner_tutorials talker.py
#
# Run script (with launch file)
#   roslaunch beginner_tutorials talker_listener.launch

import rospy
from std_msgs.msg import String

def talker():

    # Initialize our node with name talker
    rospy.init_node('talker', anonymous=True)

    # Node are publish to the chatter topic using the message type String
    pub = rospy.Publisher('chatter', String, queue_size=10)

    # Looping at desired rate
    # loop 10 times every second
    rate = rospy.Rate(10) #10hz

    # Check shutdown flag
    while not rospy.is_shutdown():

        hello_str = "hello world %s" % rospy.get_time()

        # Message printed to the screen
        # Message written to the Node's log file
        # Message written to rosout
        rospy.loginfo(hello_str)

        # Publish a String to our chatter topic
        pub.publish(hello_str)

        # Sleep long enough to maintain desired rate
        # Specify in rospy.Rate(10)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

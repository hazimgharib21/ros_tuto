#!/usr/bin/env python

PKG = 'beginner_tutorials'
NAME = 'test_talker_listener'

import sys, unittest, time

import rospy, rostest
from std_msgs.msg import *

class TestTalkerListener(unittest.TestCase):

    def __init__(self, *args):

        super(TestTalkerListener, self).__init__(*args)
        self.success = False

    def callback(self, data):
        self.success = data.data and data.data.startswith('hello world')

    def test_talker_listener(self):
        rospy.init_node(NAME, anonymous=True)
        rospy.Subscriber("chatter", String,self.callback)
        timeout_t = time.time() + 10.0
        while not rospy.is_shutdown() and not self.success and time.time() < timeout_t:
            time.sleep(0.1)
        self.assertTrue(self.success)

if __name__ == '__main__':
    rostest.rosrun(PKG, NAME, TestTalkerListener, sys.argv)

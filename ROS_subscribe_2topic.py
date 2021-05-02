#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Point, Pose,Quaternion, Twist, Vector3, Pose2D

class nodod(object):
	def __init__(self):
		self.from1 = 1
		self.from2 = 1
		self.loopr = rospy.Rate(10)
		rospy.Subscriber("/twt",Twist,self.call1)
		rospy.Subscriber("/wtw",Twist,self.call2)
		self.pub = rospy.Publisher("werwrerw",Twist,queue_size=10)
	def call1(self,msg):
		self.from1 = msg.linear.x
	def call2(self,msg):
		self.from2 = msg.linear.x
	def start(self):
		rospy.loginfo("start")
		while not rospy.is_shutdown():
			twtaa = Twist()
			twtaa.linear.x = self.from1 + self.from2
			self.pub.publish(twtaa)
			self.loopr.sleep()

if __name__ == '__main__':
	rospy.init_node("Efffefefefefef")
	nod = nodod()
	nod.start()
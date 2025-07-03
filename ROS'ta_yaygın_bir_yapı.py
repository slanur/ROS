#!/usr/bin/env python3


import rospy

if __name__=='__main__':
    rospy.init_node('test_node') 
    rospy.loginfo('test node has been started')
    
    rate = rospy.Rate(10) #1 saniyede 10 kez Hello yazilacak
    while not rospy.is_shutdown():
        rospy.loginfo("Hello")
        rate.sleep()
        

# rate = rospy.Rate(10)-> döngü saniyede 10 defa çalışsın
# rate.sleep()-> döngünün belirlenen hızda çalışmasını sağlar.
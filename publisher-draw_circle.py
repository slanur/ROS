#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist

if __name__ == '__main__':
    rospy.init_node("draw_circle")
    rospy.loginfo("Node has been started")

    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    
    rate = rospy.Rate(2)  # 2 Hz: Her 0.5 saniyede bir komut gönder
    while not rospy.is_shutdown():
        msg = Twist()
        msg.linear.x = 2.0      # ileri hız
        msg.angular.z = 1.0     # açısal dönüş (sağa/sola dönüş)
        pub.publish(msg)        # mesajı yayınla
        rate.sleep()

#  pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10) 
# "/turtle1/cmd_vel"-> topic adı.  Twist->topiğe yayınladığımız mesaj türü

# bu örneği yapmak için bir terminalde -roscore-u çalıştırdık, diğerinde de -rosrun turtlesim turtlesim_node- u çalıştırdık.
# -rostopic list- ile topiclerin listesini gördük ve -/turtle1/cmd_vel- topiğine hız komutu yayınlamaya karar verdik.
# -rostopic info /turtle1/cmd_vel- ile bu topiğin bilgilerini aldık ve bu topiğe gelen mesaj türünün Twist olduğunu gördük
# sonrasında kodumuzu yazdık.
# çalıştırmak için yine ilk önce terminalde -roscore- u çalıştırdık, diğerinde -rosrun turtlesim turtlesim_node- u , diğerinde de -rosrun paketimizinAdi düğümünAdi- ni çalıştırdık

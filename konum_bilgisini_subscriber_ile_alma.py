#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from turtlesim.msg import Pose


def pose_callback(msg):
    rospy.loginfo(msg)

if __name__=='__main__':
    rospy.init_node("turtle_pose_subscriber")
    
    
    sub = rospy.Subscriber("/turtle1/pose", Pose, callback=pose_callback)
    
    rospy.loginfo("Node has been started")
    
    rospy.spin()
    

#-----------------örneğin yapım aşamaları
# bu örneği yapmak için bir terminalde -roscore-u çalıştırdık, diğerinde de -rosrun turtlesim turtlesim_node- u çalıştırdık.
# -rostopic list- ile topiclerin listesini gördük ve -/turtle1/pose- topiğinden konum verilerini almaya karar verdik.
# -rostopic info /turtle1/pose- ile bu topiğin bilgilerini aldık ve bu topiğe gelen mesaj türünün turtlesim/Pose olduğunu gördük
# sonrasında kodumuzu yazmaya başladık
# turtlesim.msg kütüphanesi içinden Pose'i import ettik. Sonrada bu kütüphane için XML dosyasında bağımlılıklar ekledik
# sub objesini oluşturduk ve her mesaj geldiğinde çalıştırılacak callback fonksiypnunu yazdık
# msg parametresi, Pose türündedir ve mesaj içeriğini içerir.
# spin(), bu node’un aktif kalmasını sağlar. ROS sürekli olarak gelen mesajları dinler ve pose_callback() fonksiyonunu çağırır.

#--------------------örneğin çalıştırılması
# bir terminalde -roscore-, diğerinde -rosrun turlesim turtlesim_node-, diğerinde de -rosrun paketAdı düğümAdı- 
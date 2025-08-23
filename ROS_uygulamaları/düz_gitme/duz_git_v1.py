#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Uygulama 1: Tek Eksen Boyunca Hareket I
"""

import rospy
from geometry_msgs.msg import Twist
#Twist: Robotun hız bilgisini taşıyan mesaj türüdür. Lineer (x, y, z) ve açısal (roll, pitch,yaw / z) hızları içerir.

def hareket():
    rospy.init_node("duz_git")
    
    pub = rospy.Publisher("cmd_vel",Twist,queue_size=10)
    #biz robota 5m ileri git komutunu göndermek istediğimiz için publisher komutu oluşturduk
    #"cmd_vel": ROS’da genellikle hareket komutlarının gönderildiği standart konudur (command velocity).
    #Twist: Twist mesajı, robotun hem lineer (doğrusal) hem de angular (açısal) hız bilgilerini içerir.

    hiz_mesaji = Twist()
    hiz_mesaji.linear.x = 0.5 #ileri yönde 0.5 m/s hız
    mesafe = 5
    yer_degistirme = 0
    t0 = rospy.Time.now().to_sec() #başlangıç zamanı
    
    while (yer_degistirme < mesafe):
        pub.publish(hiz_mesaji) #Robota şu hızda git komutunu gönderir
        t1 = rospy.Time.now().to_sec()
        yer_degistirme = hiz_mesaji.linear.x * (t1-t0)
    hiz_mesaji.linear.x = 0.0
    pub.publish(hiz_mesaji)
    rospy.loginfo("Hedefe varildi !")

hareket()

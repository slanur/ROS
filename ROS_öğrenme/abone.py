#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Publisher-Subscriber Uygulaması: Abone Düğümü
"""

import rospy
from ogretici_paket.msg import BataryaDurum

def bataryaFonksiyonu(mesaj):
    rospy.loginfo("Robot şarjı: %s"%mesaj.batarya)

def mesajDinle():
    rospy.init_node("abone_dugumu")
    rospy.Subscriber("batarya_konusu",BataryaDurum,bataryaFonksiyonu)
    rospy.spin() #sayesinde sürekli dinleme açık kalır.

mesajDinle()



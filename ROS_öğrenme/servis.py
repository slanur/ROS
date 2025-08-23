#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Service-Client Uygulaması: Servis Düğümü
"""

import rospy
from ogretici_paket.srv import GecenZaman

def gecenZamanFonksiyonu(istek): #servise gelen isteği işleyecek olan callback fonksiyonu
    robot_hiz = 0.5
    sure = istek.hedef_konum / robot_hiz #istek.hedef_konum->istemciden gelen konumdur
    return sure

def cevapGonder():
    rospy.init_node("server_dugumu")
    rospy.Service("zaman",GecenZaman,gecenZamanFonksiyonu)
    #servis adı:zaman-Servis tipi:GecenZaman-geri çağırılacak fonksiyon:gecenZamanFonksiyonu
    rospy.spin()

cevapGonder()

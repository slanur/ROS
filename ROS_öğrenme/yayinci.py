#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Publisher-Subscriber Uygulaması: Yayıncı Düğümü
"""
import rospy
from ogretici_paket.msg import BataryaDurum

def mesajYayinla():
    rospy.init_node("yayinci_dugumu",anonymous=True)
    pub = rospy.Publisher("batarya_konusu",BataryaDurum,queue_size=10)
    rate = rospy.Rate(1) #Yayın döngüsünün 1 Hz (yani saniyede 1 kez) çalışmasını sağlar.
    
    while not rospy.is_shutdown():
        mesaj = BataryaDurum()
        mesaj.batarya="%25"
        rospy.loginfo(mesaj)
        pub.publish(mesaj)
        rate.sleep() #Döngüde tanımlanan hıza uygun olarak bir sonraki döngüye kadar bekler

mesajYayinla()

#pub = rospy.Publisher("batarya_konusu",BataryaDurum,queue_size=10) bu satırla bir publisher oluşturuyoruz
#pub.publish(mesaj) bununlada belrlenen topiğe mesaj yolluyoruz


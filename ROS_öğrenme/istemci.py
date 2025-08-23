#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Service-Client Uygulaması: İstemci Düğümü
"""

import rospy
from ogretici_paket.srv import GecenZaman

def istekteBulun(x):
    rospy.wait_for_service("zaman") #Servis bağlantısı kurulana kadar bekler.
    try:
        servis = rospy.ServiceProxy("zaman",GecenZaman) #servis nesnesine atama yaptık
        #ServiceProxy, istemcinin servise bağlanmasını sağlar.
        #"zaman": servis adı.
        #GecenZaman: servis tipi
        cevap = servis(x)
        return cevap.gecen_sure
        
    except rospy.ServiceException:
        print("Servisle alakalı hata !!!")
        
rospy.init_node("istemci_dugumu")
hedefkonum = float(input("Hedef konum giriniz: "))
t = istekteBulun(hedefkonum)
print("Hedefe varana kadar gecen sure: ", t)

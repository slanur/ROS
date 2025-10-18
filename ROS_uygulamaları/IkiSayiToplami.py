#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from ogretici_paket.srv import AddTwoIntsRequest, AddTwoIntsResponse


def handle_addition(req):
    result = req.a + req.b
    rospy.loginfo(f"Gelen istek: {req.a} + {req.b} = {result}")
    return AddTwoIntsResponse(result)

if __name__=='__main__':
    rospy.init_node("add_two_ints_server")

    service = rospy.Service("add_two_ints", AddTwoInts, handle_addition)

    rospy.loginfo("Toplama servisi başlatıldı.")
    rospy.spin()
    
    
    
    
# buradaki kodlari yazmaya baslamadan once paketimizin icinde srv dosyasi olusturuyoruz. 
# srv dosyasinin icine de .srv uzantili dosyalar olusturuyoruz

# ben buradaki toplama islemi icin AddTwoInts.srv diye bir dosya olusturdum. icerigi su sekilde 
#int64 a     (client a ve b sayılarını gönderiyor) 
#int64 b 
#--- 
#int64 sum     (server’da sum olarak toplamını döndürüyor) 

# burada ROS otomatik olarak a ve b degiskenlerini AddTwoIntsRequest olarak adlandiriyor
# sum degiskenini de AddTwoIntsResponse olarak adlandiriyor

# rospy.Service(...)-> yeni bir servis baslatir
# "add_two_ints"->servisin adi,  istemci bu isma baglanir
# handle_addition->istek gelince calisacak fonksiyon
    
# AddTwoIntsResponse(...)-> geri donen cevap turu 	

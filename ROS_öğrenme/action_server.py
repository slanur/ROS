#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Action Service-Client Uygulaması: Server Düğümü
"""

import rospy
import actionlib
#ROS action protokolünü sağlayan kütüphane
from ogretici_paket.msg import GorevDurumAction, GorevDurumFeedback, GorevDurumResult
#GorevDurumAction, GorevDurumFeedback, GorevDurumResult:.action dosyasından otomatik oluşturulmuş ROS mesajları

class ActionServer():
    def __init__(self):
        rospy.init_node("action_server_dugumu")
        self.a_server = actionlib.SimpleActionServer("gorev",GorevDurumAction,auto_start=False,execute_cb=self.cevapUret)
        #SimpleActionServer: Action server sınıfı.
        #"gorev": Action'ın adı. Client bu isimle server'a ulaşır.
        #GorevDurumAction: Beklenen mesaj tipi.
        #auto_start=False: Otomatik başlatma kapalı; biz manuel başlatacağız.
        #execute_cb=self.cevapUret: Client'dan istek geldiğinde çağrılacak geri çağırma fonksiyonu (cevapUret).
        self.a_server.start()
        #Yukarıda auto_start=False olduğu için burada elle başlatıyoruz.
        rospy.spin()
        
    
    def cevapUret(self,istek):
        geri_bildirim = GorevDurumFeedback()
        sonuc = GorevDurumResult()
        #Geri bildirim (feedback) ve sonuç (result) için boş mesaj nesneleri oluşturuluyor.
        rate = rospy.Rate(1)
        #döngü hızı ayarlanıyor
        
        for i in range(1,istek.birim):
            durum = "%" + str(i*100/istek.birim)  #Görev yüzdesi hesaplanır.
            geri_bildirim.oran = durum #oran adlı geri bildirim alanına bu yüzde yazılır.
            self.a_server.publish_feedback(geri_bildirim) #publish_feedback() ile client'a gönderilir.
            rate.sleep()  #ile bir saniye beklenir.
        


        sonuc.sonuc = "Gorev tamamlandi!"
        self.a_server.set_succeeded(sonuc) #set_succeeded() ile client'a başarı mesajı gönderilir.

a_s = ActionServer()

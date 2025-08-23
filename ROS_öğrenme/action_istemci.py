#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Action Service-Client Uygulaması: Client Düğümü
"""

import rospy
import actionlib
from ogretici_paket.msg import GorevDurumAction, GorevDurumGoal

def bildirimFonksiyonu(bilgi):
    print("Gorev tamamlanma durumu: ", bilgi.oran)
    #Bu bir geri bildirim (feedback) fonksiyonudur.Server, her adımda bize oran (yüzde) gönderir.
    #Bu bilgi bilgi.oran ile alınır ve terminale yazdırılır.
def istekteBulun():
    rospy.init_node("action_istemci_dugumu") #istemci düğümü oluşturuldu
    istemci = actionlib.SimpleActionClient("gorev",GorevDurumAction)
    #"gorev": Server’ın adı. Server da bu ismi kullanıyordu.
    #GorevDurumAction: Mesajın tipi. Server ve client aynı tipte mesaj kullanmalı.
    
    istemci.wait_for_server() #server hazır olana kadar bekler
    
    istek = GorevDurumGoal() #yeni bir görev(goal) oluşturuluyor
    istek.birim = 10 #Server’a diyoruz ki, “Bu görevi 10 birimde yap."
    
    istemci.send_goal(istek,feedback_cb=bildirimFonksiyonu)
    #görev server'a gönderilir ve her feedback geldiğinde bildirim fonk. çalışır
    
    istemci.wait_for_result() #server bitirene kadar beklenir
    x = istemci.get_result().sonuc #görev sonucu alınır("görev tamamlandı" gibi)
    return x

cikti = istekteBulun()
print("Gorevin son durumu: ", cikti)

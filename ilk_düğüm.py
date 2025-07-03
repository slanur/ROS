#!/usr/bin/env python3


import rospy 

rospy.init_node('ilk_node') #dugumun adi
rospy.loginfo('merhaba ros bu benim ilk node`um') #terminale yazi yaz

# chmod +x ilk_dugum.py ile dosyayi calistirilabilir hale getirioruz

#derleme ortamini guncelliyoruz
#cd ~/catkin_ws
#catkin_make

#calistirmak icin bir terminalde -roscore- 
#diger terminalde -rosrun paketadi dugumadi- ni calistiriyoruz


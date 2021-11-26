import cv2
import datetime
import numpy as np
import os
from matplotlib import pyplot as plt


Blist = []
Glist = []
Rlist = []


a = input("Please write how many photos you want")

i = 1

while i <= int(a) :


        camera = cv2.VideoCapture(0)
        return_value,image = camera.read()
        
        cv2.imwrite(datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S") + ".jpeg", image)   ## Saving the photo taken
       

        histr1 = cv2.calcHist([image],[0],None,[256],[0,256]) ##blue
        histr2 = cv2.calcHist([image],[1],None,[256],[0,256]) ##green
        histr3 = cv2.calcHist([image],[2],None,[256],[0,256]) ##red

        plt.title('Histogram Chart') ## Graph Name
        plt.xlabel('Intensity Value')  ##  X axis
        plt.ylabel('Count')  ## Y axis

       
        #########################################################
        plt.plot(histr1)
        hist1_max = max(histr1)
        hist1_min = min(histr1)
        sayi1 = max(histr1)
        Blist.append(int(sayi1))
        
              

        #########################################################
        plt.plot(histr2)
        hist2_max = max(histr2)
        hist2_min = min(histr2)
        sayi2 = max(histr2)
        Glist.append(int(sayi2))
       
        
        #########################################################
        plt.plot(histr3)
        hist3_max = max(histr3)
        hist3_min = min(histr3)
        sayi3 = max(histr3)
        Rlist.append(int(sayi3))
        
        
        
        plt.savefig(datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S") + ".png")          ## Saving Histogram Graph
        plt.show()
        
        

        i = i+1

while i == int(a)+1 :

        print(Blist)
        max_Blist = max(Blist)
        numb1 = Blist.index(max(Blist)) 
        min_Blist = min(Blist)
        numb11 = Blist.index(min(Blist))

        print ("Max B :", max_Blist)
        print ("Which Photo:", numb1+1)
        print ("Min B :", min_Blist)
        print ("Which Photo:", numb11+1)
        

        
        print(Glist)
        max_Glist = max(Glist)
        numb2 = Glist.index(max(Glist)) 
        min_Glist = min(Glist)
        numb22 = Glist.index(min(Glist))

        print ("Max G :", max_Glist)
        print ("Which Photo:", numb2+1)
        print ("Min G :", min_Glist)
        print ("Which Photo:", numb22+1)

        
        print(Rlist)
        max_Rlist = max(Rlist)
        numb3 = Rlist.index(max(Rlist))
        min_Rlist = min(Rlist)
        numb33 = Rlist.index(min(Rlist))

        print ("Max R :", max_Rlist)
        print ("Which Photo:", numb3+1)
        print ("Min R değeri:", min_Rlist)
        print ("Which Photo:", numb33+1)

        i = i+1
        


                
        

        
       

        


        
                


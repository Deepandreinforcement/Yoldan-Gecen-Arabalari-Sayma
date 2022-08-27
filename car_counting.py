

import numpy as np
import cv2

kamera= cv2.VideoCapture('video1.mp4')


net = cv2.dnn.readNet( "yolov4-tiny.cfg","yolov4-tiny.weights") 

classes = []
with open("coco.names", "r") as f:  
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
# alttaki satırdan dolayı hata alabilirsiniz. İnternette basit bir çözümü var.
# Hata olursa buradan sebebi opencv sürümü oluyor genelde. 
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

colors = np.random.uniform(0, 255, size=(len(classes), 3))


to=0 # çıkış yapan araba sayısı
gi=0 # giriş yapan araba sayısı
while True:

    
    ret,img=kamera.read()

    img = cv2.resize(img, (416,416))
    height, width, channels = img.shape
    

    # Detecting objects
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)
    
    
    
    
    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.1: 
                # Object detected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
                
    
    
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.4, 0.4)

    
    sayi=0  # o anki  araba sayısı için
    font = cv2.FONT_HERSHEY_SIMPLEX
    for i in range(len(boxes)):
        
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])

            color = colors[i]
            if label=='car': # sadece araç sayımı yapıyoruz

        

                color=(255,255,255)
                
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                
                sayi=sayi+1  
                if x>200 and y+h//2>330 and y+h//2<341: # çıkış yapılan konum, bu konumlar videodan videoya değişir
                    to=to+1
                   
                    
                if x<200 and y+h//2>332 and y+h//2<339: # giriş yapılan konum, bu konumlar videodan videoya değişir
                    gi=gi+1
                    #print(y+h//2)
                    

    cv2.line(img,(0,335),(416,335),(255,0,0),2) # bunun temel bir amacı yok. Yardımcı amaçlı çizgi
    cv2.putText(img,"Cikis:"+ str(to), (220, 40), font, 1.5, (0,0,255), 2)
    cv2.putText(img,"Giris:"+ str(gi), (0, 40), font, 1.5, (255,0,255), 2)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
kamera.release()
cv2.destroyAllWindows()
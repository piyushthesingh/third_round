#Section 1: Importing required libraries

import cv2 #OpenCV  
import os

#Section 2: Scanning the required file(s)

dir = 'D:/Assignment_3/Diameter Variability Test/OK Images/' #File(s) path
count = 0 #Scanned files count
print('\nDirectory path;', dir, '\n')
for img in os.scandir(dir):
    count += 1
    print('File S.No.',count)
    image1 = cv2.imread(img.path)   #Reading image
    image = cv2.resize(image1, (1050, 700))     #Image resize to 1050 pixels × 700 pixels; bigger files would be too large for the screen

# Section 3: Finding bounding rectangle for the reference bench, and printing out the width in pixels
    
    crop_1 = image[240:440, 320:660].copy()     #Cropping the copy of the image to the region of interest
#    cv2.imshow("crop_1", crop_1)   #To visualize if the cropped region is okay
    gray_1 = cv2.cvtColor(crop_1, cv2.COLOR_BGR2GRAY)   #grayscaling the image
    _, thresh_1 = cv2.threshold(gray_1,90,255,cv2.THRESH_BINARY_INV) #Threshold the image with threshold value as 90 here, and then inverting the colors
    x,y,w1,h1 = cv2.boundingRect(thresh_1)      #Bounding Rectangle dimensions
    cv2.rectangle(thresh_1, (x, y), (x + w1, y + h1), (36,255,12), 2)   #Drawing the rectangle
    cv2.rectangle(crop_1, (x, y), (x + w1, y + h1), (36,255,12), 2)
    cv2.putText(crop_1, 'Ref.; ' "w1={},h1={}".format(w1,h1), (x,y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (36,255,12), 2)        #Putting text on image in terms of w and h
#    cv2.imshow("thresh", crop_1)
#    print('Ref. width', count, ',', w1)

#Section 4: Finding bounding rectangle for the test piece, and printing out the width in pixels
    
    crop_2 = image[240:335, 320:660].copy()
    gray_2 = cv2.cvtColor(crop_2, cv2.COLOR_BGR2GRAY)
    _, thresh_2 = cv2.threshold(gray_2,90,255,cv2.THRESH_BINARY_INV)
    x,y,w2,h2 = cv2.boundingRect(thresh_2)
    cv2.rectangle(thresh_2, (x, y), (x + w2, y + h2), (36,255,12), 2)
    cv2.rectangle(crop_2, (x, y), (x + w2, y + h2), (36,255,12), 2)
#    print('Test piece. width', count, ',', w2)
#    cv2.imshow("", crop_2)

#Section 5: Dia calculations

#    print('ratio', w2/w1)
    spec_dia = ((w2/w1)*38.739169)  #Specimen dia, value 38.739169 is the work bench horizontal distance as calculated using w1 and w2

#section 6: Concuding the code

#    print(w2/w1)
    if 0.1525<(w2/w1)<0.1569:
        print('Specimen dia is permissible \nSpecimen dia ~', round(spec_dia, 2), 'mm \n')
    else:
        print('Specimen dia is "NOT" permissible \nSpecimen dia ~', round(spec_dia, 2), 'mm \n')
#    cv2.waitKey(20000)
    if count >= 5: #inputting no of images succeding to initial count value that we are planning to scan
        break
#    break
#break
#exit(0)
            





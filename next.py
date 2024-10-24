import cv2 as cv
print (cv.__version__)

image = cv.imread("PICTURE.jpg",cv.IMREAD_COLOR)
#gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
#faceCascade=cv.CascadeClassifier('haarcascade_frontalface_default.xml')

#faces = faceCascade.detectMultiScale(
 #   gray,
  #  scaleFactor=1.1,
   # minNeighbors=5,
    #minSize=(30, 30),
    #flags = cv.cv.CV_HAAR_SCALE_IMAGE
#)

#print (f"Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
#for (x, y, w, h) in faces:
 #   cv.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)



#start_point =(5,5)

#end_point=(220,220)

#color = (255,0,0)

#thickness = 2

#image = cv.rectangle(img, start_point, end_point, color, thickness)


#cv.imshow("Faces found", image)

cv.VideoCapture(0)

cv.waitKey(0)

cv.destroyAllWindows()

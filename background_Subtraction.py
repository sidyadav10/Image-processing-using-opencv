# # # Back ground removal using grabcut
# # # Grabcut algo :cutoff any foreground obj from img or video
# # # It works like rectangle protion mark on the img 
# # # This algo removes it completely 
# # # guassian mixture model help to achive the target

import cv2 as c ,numpy as np

img = c.imread(r"C:\Users\HP\Desktop\python_opencv\Images\pexels-erik-mclean-5727367.jpg")
# img  =	c.imread(r"C:\Users\HP\Desktop\python_opencv\Images\car.jpg")
img = c.resize(img, (800,800))
mask = np.zeros(img.shape[:2],np.uint8)

bgd_model = np.zeros((1,65),np.float64)
fgd_model = np.zeros((1,65),np.float64)

# Parameter (img ,mask, rect, bgdmodel.fgdmodel,iter ,model)
# rect (238,352:524,1052)
rect = (227,233,525,705)
c.grabCut(img, mask, rect, bgd_model, fgd_model, 5,c.GC_INIT_WITH_RECT)
mask2 = np.where((mask == 2)|(mask == 0),0,1).astype('uint8')
img = img * mask2[:,:,np.newaxis]


c.imshow("result", img)
c.waitKey(0)
c.destroyAllWindows()


# """
# #GrabCut Algoritm with the help of this algoritm we easily
# #cutoff any foreground object from image or video.
# #It works like a rectangle portion mark on the image
# #and area outise the rectangle is treat as a extra part
# #so this algo remove it completely.
# #Gaussian mixtuere model help to achieve the target



# import	numpy  as  np
# import	cv2

# img = cv2.resize(img,(800,800))
# mask =	np.zeros(img.shape[:2],np.uint8)
 
 
# bgdModel =  np.zeros((1,65),np.float64)*255
# fgdModel =  np.zeros((1,65),np.float64)*255
 
# #parameter(img,mask,rect,bgmodel,fgmodel,iter,method) 
# rect =	(134,150,660,730)
# cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,
#             cv2.GC_INIT_WITH_RECT)
 
 
# mask2  =  np.where((mask==2)|(mask==0),0,1).astype('uint8')
# img  =	img*mask2[:,:,np.newaxis]
 
# cv2.imshow("res==",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
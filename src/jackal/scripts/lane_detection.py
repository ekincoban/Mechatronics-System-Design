import matplotlib.pyplot as plt
import numpy as np
import cv2

image=cv2.imread("lane_detection.png")
image_c=image
plt.figure()
plt.imshow(image)
plt.title("Orjinal Fotoğraf")
print(image.shape)

"""Image'ı Grayscale hale getiriyoruz."""

image=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
plt.figure()
plt.imshow(image,cmap="gray")
plt.title("Gray Scale Hale Getirilmiş Fotoğraf")
print(image.shape)

"""Gaussian Bluring ve Canny Edge Detection Yöntemlerini Uyguluyoruz"""

image_blurred=cv2.GaussianBlur(image,(7,7),0)
plt.figure()
plt.imshow(image_blurred)
plt.title("Blurlanmış Fotoğraf")

threshold_low=10
threshold_high=100
image_canny=cv2.Canny(image_blurred,threshold_low,threshold_high)
plt.figure()
plt.imshow(image_canny,cmap="gray")
plt.title("Canny Edge Detection Yöntemi Uygulanmış Resim.")


"""Region Of Interest (ROI) Belirliyoruz"""

vertices=np.array([[(80,320),(280,200), (320,200),(550,320)]],dtype=np.int32) 
mask=np.zeros_like(image)
cv2.fillPoly(mask,vertices,255)
masked_image=cv2.bitwise_and(image,mask)
plt.figure()
plt.imshow(masked_image)
plt.title("Region of Interest (ROI)")

masked_image=cv2.bitwise_and(image_canny,mask)
plt.figure()
plt.imshow(masked_image)
plt.title("Yol Çizgilerinin Çıkartılmış Hali")


""""Hough lines tespit ediyoruz ve fonksiyonu çizdiriyoruz"""
rho=2 #distance resolution in pixels
theta=np.pi/180 #angular resolution of radians
threshold=40 # min number of votes
min_line_len=100 #minimum pixels making up line
max_line_gap=50 #max gap between pixels
lines=cv2.HoughLinesP(masked_image,rho,theta,threshold,np.array([]),minLineLength=min_line_len,maxLineGap=max_line_gap)

""""Boş siyah görsel yaratma"""
line_image=np.zeros((masked_image.shape[0],masked_image.shape[1],3),dtype=np.uint8)
for line in lines:
    for x1,y1,x2,y2 in line:
        cv2.line(line_image,(x1,y1),(x2,y2),[255,0,0],20)
              
a=1
b=1
t=0
image_with_lines=cv2.addWeighted(image_c,a,line_image,b,t)
plt.figure()
plt.imshow(image_with_lines)
plt.title("Gerçek Resim Üzerinde Lane Detection")








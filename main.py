import cv2
# print(cv2.__version__)

image=cv2.imread('/home/sbkim21/Documents/python/OpenCVpractice/download/lena.png')

if image is None:
    print("Error: Could not read image.")
else:
    cv2.imwrite('outpudddt.png',image)
    print("Image saved as output.png")





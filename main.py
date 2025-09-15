import cv2
# print(cv2.__version__)

# loading the image
image=cv2.imread('/home/sbkim21/Documents/python/OpenCVpractice/download/lena.png')

if image is not None:
    cv2.imwrite('output.png',image)
    print("Image has been saved as output.png")
    # resizing the image
    resized_image=cv2.resize(image,(300,200))
    # rotating the image
    rotated_image=cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    # cropping the image
    cropped_image=image[100:200,50:150]
    cv2.imwrite('resized_image.jpg',resized_image)
    cv2.imwrite('rotated_image.jpg',rotated_image)
    cv2.imwrite('cropped_image.jpg',cropped_image)
    print("Images have been resized, rotated, cropped successfully.")
else:
    print("Error: Could not load the image.")










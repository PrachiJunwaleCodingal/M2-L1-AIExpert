#pip install opencv-python(on cmd or terminal)

import cv2
image = cv2.imread('img.jpg')
cv2.namedWindow('Image', cv2.WINDOW_NORMAL)  # resizable window
cv2.resizeWindow('Image', 400, 400)  
cv2.imshow('Image', image)
cv2.waitKey(0)  
cv2.destroyAllWindows()  
print(f"Dimensions: {image.shape}")  

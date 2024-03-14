import cv2

cam = cv2.VideoCapture(0)

cam.set(3, 100)
cam.set(4, 100)

number_of_images = 10
i = 0 
while i < number_of_images:
    _, frame = cam.read() 
    cv2.imshow('display', frame) 
    cv2.imwrite(f'HappyImages/IMG_{i}.png', frame)

    if cv2.waitKey(20) == ord('q'):
        break
    i += 1 

cam.release()
cv2.destroyAllWindows()

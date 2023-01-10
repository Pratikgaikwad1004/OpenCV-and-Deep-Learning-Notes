import cv2

img = cv2.imread("deadpool.jpg")

print("Running....")
while True:
    cv2.imshow('Deadpool', img)
    
    # If we have waited at least 1 ms or we pressed Esc
    if (cv2.waitKey(1) & 0xFF == 27):
        break
        
cv2.destroyAllWindows()
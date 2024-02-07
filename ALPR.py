import cv2
import pytesseract

# Load the pre-trained OCR model
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

# Connect to the IP CCTV camera
camera = cv2.VideoCapture('https://www.youtube.com/watch?v=73REqZM1Fy0')

while True:
    # Read the frame from the camera
    ret, frame = camera.read()
    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply image processing techniques to enhance the license plate
    # ...
    
    # Use OCR to extract the license plate number
    plate_number = pytesseract.image_to_string(gray, config='--psm 7')
    
    # Display the license plate number
    print(plate_number)
    
    # Display the frame with the license plate highlighted
    cv2.imshow('ALPR', frame)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
camera.release()
cv2.destroyAllWindows()
import cv2
import pytesseract
import os
import PIL as Image 

# Load the pre-trained OCR model
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

# Replace 'path/to/your/images' with the path to the directory containing your saved images
image_directory = r'C:\Users\Akutty\Desktop\New folder'


# Loop through each image in the directory
for image_filename in os.listdir(image_directory):
    # Construct the full path to the image
    image_path = os.path.join(image_directory, image_filename)
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
    # Read the image
    frame = cv2.imread(image_path)
    text = pytesseract.image_to_string(binary_image)
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Example preprocessing (you may need to adjust these based on your images)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresholded = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


    # Apply image processing techniques to enhance the license plate
    # ...

    # Use OCR to extract the license plate number
    plate_number = pytesseract.image_to_string(thresholded)#, config='--psm 7')

    # Display the license plate number
    print(f"License Plate ({image_filename}): {plate_number}: {text}")

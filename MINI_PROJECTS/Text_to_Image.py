from PIL import Image
import pytesseract

# Open image
img = Image.open("image.png")

# Extract text
text = pytesseract.image_to_string(img)

# Print text
print(text)

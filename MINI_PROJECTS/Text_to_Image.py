from PIL import Image, ImageDraw

img = Image.new("RGB", (500, 200), "white")

draw = ImageDraw.Draw(img)
draw.text((150, 80), "Hello World!", fill="black")

img.save("output.png")
img.show()

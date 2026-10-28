from PIL import Image ,ImageDraw, ImageFont
text=input("Enter your text:")
#create image
image=Image.new("RGB",(800,300),"white") # width= 800   height= 300


draw=ImageDraw.Draw(image)
#load font
font=ImageFont.load_default() # font size , font style

#draw text on image
draw.text((50,100),text,fill="black",font=font) #left=50px top to bottom=100px , fill mean= text color

# save image 
image.save("txt_image.png")
print("Image generated successfully")

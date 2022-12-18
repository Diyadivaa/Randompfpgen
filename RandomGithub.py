import random
from PIL import Image, ImageDraw

# Create a new image with a size of 300x300 pixels
image = Image.new('RGB', (300, 300))

# Generate a random color for the background
bg_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Fill the image with the background color
image.paste(bg_color, [0, 0, 300, 300])

#generate a random color for the foreground
fg_colorrand = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Use ImageDraw to draw the GitHub logo shape on the image
draw = ImageDraw.Draw(image)
#I prefer but not traditional 
#outline = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#draw.rectangle((25, 25, 75,75), fill =fg_colorrand,outline=outline) 
#draw.rectangle((225, 25, 275,75), fill =fg_colorrand,outline=outline) 
#draw.rectangle((75, 75, 225,125), fill =fg_colorrand,outline=outline) 
#draw.rectangle((125, 125, 175,225), fill =fg_colorrand,outline=outline) 
#draw.rectangle((25, 225, 125,275), fill =fg_colorrand,outline=outline) 
#draw.rectangle((175, 225, 275,275), fill =fg_colorrand,outline=outline) 
#draw.rectangle((25, 125, 75,275), fill =fg_colorrand,outline=outline) 
#draw.rectangle((225, 125, 275,275), fill =fg_colorrand,outline=outline) 


draw.rectangle((25, 25, 75,75), fill =fg_colorrand) 
draw.rectangle((225, 25, 275,75), fill =fg_colorrand) 
draw.rectangle((75, 75, 225,125), fill =fg_colorrand) 
draw.rectangle((125, 125, 175,225), fill =fg_colorrand) 
draw.rectangle((25, 225, 125,275), fill =fg_colorrand) 
draw.rectangle((175, 225, 275,275), fill =fg_colorrand) 
draw.rectangle((25, 125, 75,275), fill =fg_colorrand) 
draw.rectangle((225, 125, 275,275), fill =fg_colorrand) 

# Save the image
image.save('random_color_avatar.bmp')

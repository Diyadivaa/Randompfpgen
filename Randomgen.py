import random
from PIL import Image

# Create a new image with a random size
width = random.randint(100, 200)
height = random.randint(100, 200)
image = Image.new('RGB', (width, height))

# Fill the image with random colors
for x in range(width):
    for y in range(height):
        # Generate a random color
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = (r, g, b)
        
        image.putpixel((x, y), color)

# Save the image
image.save('random_color.png')

# Import libraries from the wand
from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

with Drawing() as draw:
    # Set Stroke color the circle to black
    draw.stroke_color = Color('black')
    # Set Width of the circle to 2
    draw.stroke_width = 1
    # Set the fill color to 'White (# FFFFFF)'
    draw.fill_color = Color('white')

    # Invoke Circle function with center at 50, 50 and radius 25
    draw.circle((200, 200),  # Center point
                (100, 100))  # Perimeter point
    # Set the font style
    draw.font = '../Helvetica.ttf'
    # Set the font size
    draw.font_size = 30

    with Image(width=400, height=400, background=Color('# 45ff33')) as pic:
        # Set the text and its location
        draw.text(int(pic.width / 3), int(pic.height / 2), 'EvertJvr !')
        # Draw the picture
        draw(pic)
        # Import the watermark image
        with Image(filename='panel.jpg') as water:
            # Invoke watermark function with watermark image, transparency as 0.5
            # left as 10 and top as 20
            pic.watermark(water, 0.5, 10, 20)
            # Save the image
            pic.save(filename='watermark2.jpg')

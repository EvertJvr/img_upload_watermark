# https://stackoverflow.com/questions/67965574/watermarking-image-using-pillow

from PIL import Image

working_path = './working files/'
file = 'panel'
asset_path = './assets/'
water_img = 'confidential(bk-s)'  # (300)'

background = Image.open(f'{working_path}{file}.jpg')
x, y = background.size

foreground = Image.open(f'{asset_path}{water_img}.jpg')
# foreground.resize(x, y)

background.paste(foreground, box=(0, 0), mask=foreground.convert('RGBA'))
background.show()

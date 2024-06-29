# PNG watermark to a PDF file - https://products.aspose.com/pdf/python-net/images/add/
# Adds a nucense  copywriter text and not the image as requested
import aspose.pdf as ap


file = 'progress'

input_file = './working files/' + f"{file}.pdf"
output_pdf = './working files/' + f"{file}(WM).pdf"
image_file = './assets/' + "confidential.png"

# Open document
document = ap.Document(input_file)

document.pages[1].add_image(image_file, ap.Rectangle(20, 730, 120, 830, True))

document.save(output_pdf)

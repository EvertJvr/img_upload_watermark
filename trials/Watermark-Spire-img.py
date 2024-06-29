# An image watermark in a PDF is a visible overlay
# https://medium.com/@alice.yang_10652/add-watermarks-to-pdf-with-python-385964faae40#5b0c
# adds ghost image 100% (image should not be transparent) - add the evaluation copy message to the top og the page

from spire.pdf import *
from spire.pdf.common import *

working_path = './working files/'
file = 'progress'

# Create a PdfDocument object
pdf = PdfDocument()
# Load a PDF file
pdf.LoadFromFile(f"{working_path}{file}.pdf")

# Load the watermark image
image = PdfImage.FromFile("./assets/confidential.png")

# Get the width and height of the image
imageWidth = float(image.Width)
imageHeight = float(image.Height)

# Loop through the pages of the document
for i in range(pdf.Pages.Count):
    # Get the current page
    page = pdf.Pages.get_Item(i)
    # Set the transparency of the page
    page.Canvas.SetTransparency(0.5)
    # Get the width and height of the page
    pageWidth = page.ActualSize.Width
    pageHeight = page.ActualSize.Height
    # Draw the watermark image on the center of the page
    page.Canvas.DrawImage(image, pageWidth/2 - imageWidth/2, pageHeight/2 - imageHeight/2, imageWidth, imageHeight)

# Save the resulting PDF file
pdf.SaveToFile(f"{working_path}{file}(wm1).pdf")
pdf.Close()

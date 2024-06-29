# A text watermark in a PDF is a visible overlay
# https://medium.com/@alice.yang_10652/add-watermarks-to-pdf-with-python-385964faae40#id_token=eyJhbGciOiJSUzI1NiIsImtpZCI6IjJhZjkwZTg3YmUxNDBjMjAwMzg4OThhNmVmYTExMjgzZGFiNjAzMWQiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiIyMTYyOTYwMzU4MzQtazFrNnFlMDYwczJ0cDJhMmphbTRsamRjbXMwMHN0dGcuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJhdWQiOiIyMTYyOTYwMzU4MzQtazFrNnFlMDYwczJ0cDJhMmphbTRsamRjbXMwMHN0dGcuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJzdWIiOiIxMDY5Mjc0NDk4NDg3NjAxNzMyNjUiLCJlbWFpbCI6ImV2ZXJ0anZyQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJuYmYiOjE3MTk1ODI4MjEsIm5hbWUiOiJFdmVydCBKYW5zZW4gdmFuIFJlbnNidXJnIiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FDZzhvY0pYNnFoUHFCbjd0ZDFDbUZyVUNUWWFBX0ZBLXMwc1RIWTVxdmJ3a08teHk1SWZ3Zz1zOTYtYyIsImdpdmVuX25hbWUiOiJFdmVydCIsImZhbWlseV9uYW1lIjoiSmFuc2VuIHZhbiBSZW5zYnVyZyIsImlhdCI6MTcxOTU4MzEyMSwiZXhwIjoxNzE5NTg2NzIxLCJqdGkiOiI4MmRiMDJlMDBiYjM0ZTMyZjRiMWQ1Mzk2MjUwZmE0ZDIxYjg5OTYyIn0.rEoyQYhrEO9qaQhOmagfW70NHdyJFBUCnTcJugz747Rof2Uq-gCSx9NG8oohNgG0h5MLHMGOh3qHlhIQfiZQSFIg9SluBTWy2HaA29R9kZMs30hg2mb4x2hJndcrfWqUyb1SOT-mLQbt2xAllOfzVg12HkmvkgiZMKofCL0vonfLiD-MOCmrP1vnh89duc9XitZS6b3uRxMv8xLNuGniSiXj6lpaCsbzLIrcuFwxid8GLK08bqH6paqO7FA4HdYw6yyzfGs-UFJo2JdBt02JMGFl3kYfAbstPmmdv66SmMzU8gH5Bf9baCU5LXJdTzDCax_Xe1WzXC5Q4_QZux2l_A
# adds the text as it should 100% but also adds the "evaluation copy" message

from spire.pdf import *
from spire.pdf.common import *
import math

working_path = './working files/'
file = 'progress'

# Create a PdfDocument object
pdf = PdfDocument()
# Load a PDF file
pdf.LoadFromFile(f"{working_path}{file}.pdf")

# Create a PdfTrueTypeFont object
font = PdfTrueTypeFont("Arial", 50.0, 0, True)

# Specify the watermark text
text = "Confidential"

offset1 = float(font.MeasureString(text).Width * math.sqrt(2) / 4)
offset2 = float(font.MeasureString(text).Height * math.sqrt(2) / 4)

# Loop through the pages of the document
for i in range(pdf.Pages.Count):
    # Get the current page
    page = pdf.Pages.get_Item(i)
    # Set the transparency of the page
    page.Canvas.SetTransparency(0.5)
    # Translate the page coordinate system to a specified position
    page.Canvas.TranslateTransform(page.Canvas.Size.Width / 2 - offset1 - offset2, page.Canvas.Size.Height / 2 + offset1 - offset2)
    # Rotate the coordinate system 45 degrees counterclockwise
    page.Canvas.RotateTransform(-45.0)
    # Draw the watermark text on the page
    page.Canvas.DrawString(text, font, PdfBrushes.get_Gray(), 0.0, 0.0)

# Save the resulting PDF file
pdf.SaveToFile(f"{working_path}{file}(wm1).pdf")
pdf.Close()

import google.generativeai as ai
import sys
import base64
from vertexai.preview.generative_models import GenerativeModel, Part

# This will take the image file handed over as first arguement and have AI describe it

# To get it run:
# pip install vertexai

API_KEY = 'AIreplacebyyoursV0'

ai.configure(api_key=API_KEY)

model = GenerativeModel("gemini-pro-vision")

try:
    imagefile=sys.argv[1]
except:
    print("This script will read your gas counter. Please add a picture of your gas counter as parameter.")
    exit(1)

if (imagefile[-3:]=="jpg"):
    imagetype="jpeg"
if (imagefile[-3:]=="png"):
    imagetype="png"

filehandle=open(imagefile,"rb")
base64_image=base64.b64encode(filehandle.read())
image0=Part.from_data(data=base64.b64decode(base64_image), mime_type="image/"+imagetype)

print(model.generate_content(["This picture shows a gas meter. What number does it show?",image0]).candidates[0].content.parts[0].text)

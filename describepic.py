import google.generativeai as ai
import sys
import base64
from vertexai.preview.generative_models import GenerativeModel, Part

# This will take the png file handed over as first arguement and have AI describe it

API_KEY = 'AIreplacebyyoursV0'

ai.configure(api_key=API_KEY)

model = GenerativeModel("gemini-pro-vision")

imagefile=sys.argv[1]
filehandle=open(imagefile,"rb")
base64_image=base64.b64encode(filehandle.read())
image0=Part.from_data(data=base64.b64decode(base64_image), mime_type="image/png")

print(model.generate_content(["can you describe this picture?",image0]).candidates[0].content.parts[0].text)

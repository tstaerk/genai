import google.generativeai as ai
import os

# This program lets AI tell a joke
# It is useful not only to put a smile on your face, but also to check if you have set up libraries and API keys correctly

API_KEY = os.environ['APIKEY']

ai.configure(api_key=API_KEY)

model = ai.GenerativeModel("gemini-pro")

print(model.generate_content("tell a joke").candidates[0].content.parts[0].text)

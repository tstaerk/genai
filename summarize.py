import google.generativeai as ai
import sys

# This program summarizes the text file given as first argument

API_KEY = 'AIreplacebyyourkeyV0'

ai.configure(api_key=API_KEY)

model = ai.GenerativeModel("gemini-pro")

chat = model.start_chat()

filename=sys.argv[1]
filecontent=open(filename, "r").read();

print(model.generate_content(["can you summarize this?",filecontent]).candidates[0].content.parts[0].text)

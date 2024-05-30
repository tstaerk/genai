import google.generativeai as ai
import sys

# This program summarizes the text file given as first argument

# To get it to run, in Google Cloud Console, start a project, create an API key, enable Generative Language AI
# On the OS console, install python and pip, then pip install google.generativeai
# In this script, replace the API_KEY with yours
# Call the script with a text file as parameter

API_KEY = 'AIreplacebyyourkeyV0'

ai.configure(api_key=API_KEY)

model = ai.GenerativeModel("gemini-pro")

chat = model.start_chat()

filename=sys.argv[1]
filecontent=open(filename, "r").read();

print(model.generate_content(["can you summarize this?",filecontent]).candidates[0].content.parts[0].text)

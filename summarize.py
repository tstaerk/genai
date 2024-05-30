import google.generativeai as ai
import sys

# This program summarizes the text file given as first argument

# To get it to run, in Google Cloud Console, start a project, create an API key, enable Generative Language AI
# On the OS console, install python and pip, then pip install google.generativeai
# In this script, replace the API_KEY with yours
# Call the script with a text file as parameter

API_KEY = 'APIKEY'

ai.configure(api_key=API_KEY)

model = ai.GenerativeModel("gemini-pro")

try:
    filename=sys.argv[1]
except:
    print("This script summarizes a text. Please hand over a text file as parameter.")
    exit(1)

filecontent=open(filename, "r").read();

print(model.generate_content(["can you summarize this?",filecontent]).candidates[0].content.parts[0].text)

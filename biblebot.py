import google.generativeai as ai
import sys
import os

# This lets you query a document using natural language

# To get it to run, in Google Cloud Console, start a project, create an API key, enable Generative Language AI
# On the OS console, install python and pip, then pip install google.generativeai
# In this script, replace the API_KEY with yours
# Call the script with a text file as parameter

API_KEY = os.environ['APIKEY']

ai.configure(api_key=API_KEY)

model = ai.GenerativeModel("gemini-pro")

try:
    filename=sys.argv[1]
except:
    print("This script summarizes a text. Please hand over a text file as parameter.")
    exit(1)

filecontent=open(filename, "r").read();

while True:
    question=input("What question do you have to the text (bye to exit)? ")
    if question=="bye":
        exit(0)
    print(model.generate_content(["answer the following question based on the attachment:"+question,filecontent]).candidates[0].content.parts[0].text)

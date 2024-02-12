from flask import Flask, request, redirect
import google.generativeai as genai
import os
from dotenv import load_dotenv


app = Flask(__name__)
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)  # Laden der Variablen
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-pro')

def askgemini(prompt):
    response = model.generate_content(contents=prompt)
    return response.text

@app.route('/')
def home():
    #Weiterleitung zu github
    return redirect("https://github.com/speetzial/GeminiAPIProxy", code=302)


@app.route('/text', methods=['POST', 'GET'])
def gemini():
    apikey=request.headers.get('key')
    if apikey != os.getenv('SERVER_API_KEY'):
        return "Invalid API Key"
    else:
        promt = request.form['promt']
        print(promt)
        return askgemini(promt)


if __name__ == '__main__':
    app.run()

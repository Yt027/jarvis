import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Get Your Google API Key from https://aistudio.google.com/app/apikey
# and create a .env file with: GOOGLE_API_KEY='YOUR_API_KEY'
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))





class Gemini:
    def __init__(self):
        # Initialize the Gemini model
        self.model = genai.GenerativeModel("gemini-2.5-flash")
        self.basePrompt = "Tu es Jarvis, tu as été créé par Yaya Tangara comme assistant personnel. Tu es inspiré du film Ironman. Toutes tes réponses doivent être en français et être concises formatées en texte brut."
        self.load()

    def load(self):
        self.generate("Bonjour")
        
    def generate(self, prompt):
        # Generate a response from the Gemini model
        response = self.model.generate_content(f"{self.basePrompt} {prompt}")
        return response.text
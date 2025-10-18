import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
KEY = os.getenv("KEY")
genai.configure(api_key=KEY)
model = genai.GenerativeModel(
'gemini-2.5-flash', 
system_instruction="Passionate tour guide about all local areas to help people explore new adventures!")
def ask_questions():
    questList = ["Nights Budget ","City/Town ","Neighborhood(if you want a less specific search can jsut ask for region) ","Type of food (ie vegitarian seafood etc) ","what time of the day? "]
    searchTerms = []
    print("May I help you find a sutible place to eat? ")
    for question in questList:
        help = input(question)
        searchTerms.append(help)
    return searchTerms


def get_ai_response(prompt: str) -> str:
    """Generates content using the Gemini model and returns the text."""
    response = model.generate_content(prompt)
    return response.text

def dineout(searchterms):
    question = "Can you help me find a place to eat for"
    for item in searchterms:
        question += item + "and"
    return question

def main():
    terms = ask_questions()
    prompt = dineout(terms)
    print(get_ai_response(prompt))
    

if __name__ == "__main__":
    main()

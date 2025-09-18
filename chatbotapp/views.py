import os
import json
from django.http import JsonResponse
from django.shortcuts import render
from dotenv import load_dotenv
import google.generativeai as genai
from django.views.decorators.csrf import csrf_exempt  


load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def index(request):
    return render(request, "chatbotapp/index.html")

@csrf_exempt 
def chatbot_response(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_input = data.get("prompt", "")
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(user_input)
            return JsonResponse({"reply": response.text})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Invalid request"}, status=400)

def welcome(request):
    return render(request, "chatbotapp/welcome.html")

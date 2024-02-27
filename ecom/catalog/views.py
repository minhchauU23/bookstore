from django.shortcuts import render
import requests
# Create your views here.
def home(request):
    api_url = f"http://127.0.0.1:8000/category/api/"
    response = requests.get(api_url)
    categories = response.json()
    return render(request, "index.html", {"categories": categories})
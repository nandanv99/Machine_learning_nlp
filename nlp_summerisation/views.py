from django.shortcuts import render

# Create your views here.

import requests

API_URL = "https://api-inference.huggingface.co/models/sshleifer/distilbart-cnn-12-6"
API_TOKEN="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"
headers = {"Authorization": f"Bearer {API_TOKEN}"}
# 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
def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
# output = query({
# 	"inputs": "The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world, a title it held for 41 years until the Chrysler Building in New York City was finished in 1930. It was the first structure to reach a height of 300 metres. Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct.",
# })
output = query({
	"inputs": "cool man ",
})


def home(request):
	return render(request,"index.html")

def nlp1(request):
	return render(request,"index.html")
#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
import base64
import io
from PIL import Image
import numpy as np

def index(request):
    return render(request, 'recognizer/index.html')

def predict(request):
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        image_data = data['image'].split(',')[1]
        image_bytes = base64.b64decode(image_data)
        image = Image.open(io.BytesIO(image_bytes)).convert('L').resize((28, 28))

        # Later, replace this with your model prediction logic
        dummy_prediction = 'A'

        return JsonResponse({'prediction': dummy_prediction})


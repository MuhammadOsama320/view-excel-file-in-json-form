import pandas as pd
from django.http import JsonResponse

from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "upload.html")


def file(request):
    file1 = request.FILES.get('upload')
    read_file = pd.read_csv(file1)
    json_data = read_file.to_json()
    return JsonResponse({'json_data': json_data})

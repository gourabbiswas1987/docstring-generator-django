from django.http import HttpResponse
from django.shortcuts import render
from .docstringgenerator import generate_docstring
import time

# Create your views here.

def home(request):
    ts = time.time()
    if request.method == 'POST':
        code = request.POST.get('code')
        language = request.POST.get('language')
        # print(language)
        result = generate_docstring(code, language)
        return render(request,'index.html', {'result': result})
    else:
        return render(request,'index.html', {'result': ''})
    

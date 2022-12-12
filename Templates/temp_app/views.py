from django.shortcuts import render
from django.template.response import TemplateResponse

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contacts(request):
    data = {'telephone': 79896306933, 'telegram': '@codick'}
    content = {'main': data}
    return TemplateResponse(request, 'contacts.html', context=content)

def forms(request):
     return render(request, 'form.html')
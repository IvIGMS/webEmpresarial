from django.shortcuts import render, HttpResponse

# Dentro de la app core solo vamos a dejar las paginas que son estaticas y no merecen
# que hagamos una app para si mismas.

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def store(request):
    return render(request, 'core/store.html')

def contact(request):
    return render(request, 'core/contact.html')
    
def sample(request):
    return render(request, 'core/sample.html')

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'index.html')

def codiWorldcup(request):
    a = [1,2]
    context = {
        'top1':a, 
        'top2':a ,
        'bot1':a ,
        'bot2':a ,
        'out1':a ,
        'out2':a ,
        'ran_one':a 
    }
    return render(request, 'codi/codiWorldcup.html', context)
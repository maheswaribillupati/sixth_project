from django.shortcuts import render

# Create your views here.
def mohammad(request):
    d={'n':'he is the first hockey player in india'}
    return render(request,'hockey.html',context=d)
def ajitpal(request):
    d={'n':'he is the second hockey player in india'}
    return render(request,'hockey.html',context=d)
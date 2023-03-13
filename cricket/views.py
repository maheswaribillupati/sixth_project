from django.shortcuts import render

# Create your views here.
def virat(request):
    d={'name':'virat is the best bats man'}
    return render(request,'cricket.html',context=d)
def dhoni(request):
    d={'name':'dhoni is the best cricketer'}
    return render(request,'cricket.html',context=d)
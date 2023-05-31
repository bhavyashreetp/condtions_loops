from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':100,'b':500,'c':800}
    return render(request,'conditions.html',context=d)

def loop(request):
    d={'name':'bhavya'}
    return render(request,'loop.html', d)
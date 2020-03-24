from django.shortcuts import render

# Create your views here.
def ind(req):
    context={

    }
    
    return render(req, "base.html", context=context)
def day(request):
    context={}
    return render(request, "day.html",context=context)
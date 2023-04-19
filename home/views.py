from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {"variable1": "This is sent", "variable2": "great"}
    # return render(request, "index.html", context)
    return render(request, "bootstartindex.html", context)


# return HttpResponse("This is Homepage")
def Introduction(request):
    return HttpResponse("This Is Starting point")


def about(request):
    return HttpResponse("This is about page")


def services(request):
    return HttpResponse(" This is services page")


def contact(request):
    return HttpResponse(" This is contact page")

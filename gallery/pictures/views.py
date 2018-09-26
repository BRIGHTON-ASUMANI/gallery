from django.shortcuts import HttpResponse,render

# Create your views here.
def picture(request):
    return render(request, picture.html')

from django.http import HttpResponse

def index(request):
    return HttpResponse("✅ WebCraft is Live!")

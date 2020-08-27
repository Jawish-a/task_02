from django.shortcuts import render
from django.http import HttpResponse

context = {
    "msg": "Hello World!",
}
def index(request):
    return render(request, 'index.html', context)
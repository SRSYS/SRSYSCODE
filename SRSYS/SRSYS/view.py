#from django.http import HttpResponse
from django.shortcuts import render
from DjangoVerifyCode import Code


def code(request):
    code = Code(request)
    #code.img_width = 83
    #code.img_height = 30
    #code.font_color = ['black','darkblue','darkred']
    font_size = 30
    return code.display()


def index(request):
    return render(request, 'index.html')

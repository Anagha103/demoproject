from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def index(request):
#     return HttpResponse("hello world")

# def about(request):
#     return HttpResponse("Hi Anagha, welcome")

# def contact(request):
#     return HttpResponse("hi hello")

# def self(request):
#     return render(request,'self.html')

# def contact1(request):
#     return render(request,'contact1.html')

# def about(request):
#     return render(request,'about.html', context={'name':'Anagha', 'age':23})

# def basic(request):
#     var1 = {}
#     var1['name'] = 'Anagha'
#     var1['age'] = '23'
#     var1['address'] = 'Kasaragod'
#     var1['products'] = ['Book','Pen','Pencil']
#     var1['gender'] = 0
#     var1['phone'] = '9876543210'
#     return render(request=request, template_name='context.html', context=var1)

# def base(request):
#     return render(request,'base.html')

# def home(request):
#     return render(request,'home.html')

# def contact2(request):
#     return render(request,'contact2.html')



def about(request):
    return render(request,'about.html')

def home(request):
    return render(request,'home.html')

def contact1(request):
    return render(request,'contact1.html')
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')
def images(request):
    return render(request,'Gallery.html')
def about(request):
    return render(request,'About.html')
def form(request):
    return render(request,'Form.html')
def product(request):
    return render(request,'Products.html')



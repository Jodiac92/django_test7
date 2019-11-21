from django.shortcuts import render, render_to_response
from mysangpum.models import Maker, Product

# Create your views here.
def Main(request):
    #return render(request, 'main.html')
    return render_to_response('main.html') #요놈두 가능

def List1(request):
    makers = Maker.objects.all()
    return render(request, 'list1.html', {'makers':makers})

def List2(request):
    products = Product.objects.all()
    pcount = len(products)
    return render(request, 'list2.html', {'products':products, 'pcount':pcount})

def List3(request):
    mid = request.GET['id']
    mproducts = Product.objects.all().filter(maker_name=mid) #filter를 통해서 조건에 맞는 경우만 데려오기
    mpcount = len(mproducts)
    return render(request, 'list2.html', {'products':mproducts, 'pcount':mpcount})
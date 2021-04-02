from django.shortcuts import render, redirect
import requests 
import json

from .models import Stock
from django.contrib import messages

# Create your views here.
def home(request):
    api = requests.get('https://cloud.iexapis.com/stable/stock/aapl/quote?token=')
    api_python =json.loads(api.content)
   
    
    context={
        "api_data": api_python
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html', {})


def addstock(request):
    all_Stocks= Stock.objects.all()
    if request.method =="POST":
        ticker = request.POST['stock']
        print(ticker)
        api = requests.get('https://cloud.iexapis.com/stable/stock/' + ticker + '/quote?token=')
        api_python =json.loads(api.content)
    else:
        ticker ='aapl'
        api = requests.get('https://cloud.iexapis.com/stable/stock/' + ticker + '/quote?token=')
        api_python =json.loads(api.content)
    

    
    context ={
        "all_stock": all_Stocks,
        "api_data": api_python
    }

    if request.method =="POST":
        ticker = request.POST["stock"]
        data= Stock(ticker=ticker)
        data.save()
        messages.success(request, ("Stock has been added"))
     

        
        return render(request, 'add_stock.html',context)
    else:    
        return render(request, 'add_stock.html',context)


def deleteStock(request,pk):
    one_stock= Stock.objects.get(id=pk)
    one_stock.delete()
    return redirect(addstock)


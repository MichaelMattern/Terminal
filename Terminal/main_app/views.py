# main_app/views.py
import yfinance as yf
from django.shortcuts import render

def index(request):
    return render(request, 'main_app/index.html')

def account(request):
    return render(request, 'main_app/account.html')

def company(request):
    return render(request, 'main_app/company.html')

def tools(request):
    return render(request, 'main_app/tools.html')

def stock_search_view(request):
    if request.method == 'POST':
        stock_symbol = request.POST.get('stock_symbol').upper()
        
        try:
            stock = yf.Ticker(stock_symbol)
            current_price = stock.history(period='1d')['Close'].iloc[-1]
            return render(request, 'stock_search.html', {'stock_symbol': stock_symbol, 'current_price': current_price})
        except (IndexError, KeyError):
            return render(request, 'stock_search.html', {'error': 'Stock not found or data unavailable'})
    
    return render(request, 'main_app/index.html', {'stock_symbol': stock_symbol, 'current_price': current_price})

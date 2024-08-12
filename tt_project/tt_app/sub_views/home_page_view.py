from django.shortcuts import render

def home_page_view(request):
    return render(request, 'tt_html/home_page.html')

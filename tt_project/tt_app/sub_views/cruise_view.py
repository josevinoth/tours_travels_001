from django.shortcuts import render

def cruise_view(request):
    return render(request, 'tt_html/cruise.html')

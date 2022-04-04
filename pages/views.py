from django.shortcuts import render

# Create your views here.


def home(request):
    # print(request.method)
    # print(request.content_type)
    # print(request.headers)
    # print(request.POST)
    # print(request.GET)
    return render(request, 'pages\\home.html', {'page_title': 'home'})

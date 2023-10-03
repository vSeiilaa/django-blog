from django.shortcuts import render

# Create your views here.
def index(request):
    title = 'Hexlet django bot'
    return render(
        request,
        'articles/index.html',
        context={'title': title}
    )

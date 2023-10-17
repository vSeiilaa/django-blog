from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.
def index(request, tags, article_id):

    return redirect(reverse('article', kwargs={'article_id': article_id, 'tags': tags}))

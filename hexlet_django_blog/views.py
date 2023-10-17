from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    #template_name = "index.html"
    template_name = ('articles/index.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'World'
        return context
    
#   def index(self, **kwargs):
#       return redirect(reverse_lazy('article', kwargs={'article_id': 42, 'tags':'python'}))



def about(request):
    tags = ['обучение', 'программирование', 'python', 'oop']

    return render(
        request, 
        'about.html', 
        context={'tags': tags})

from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views import generic

from login.models import STATUS, Post
# Create your views here.

def index(request):
    # return HttpResponse('Hello world!')
    return render(request,'index.html')

class BlogView(generic.DetailView):
    model = Post
    template_name='index.html'

# class HomeView(generic.TemplateView):
#     template_name='index1.html'

class AboutView(generic.TemplateView):
    template_name='About.html'

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('data_created')
    template_name='index1.html'
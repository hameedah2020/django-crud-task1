from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .models import Post
from django.urls import reverse_lazy
class PostListView(ListView):
    model = Post
    template_name= "blog/post_list.html"

class PostCreateView(CreateView): 
      model = Post
      fields = "__all__"
      success_url  = reverse_lazy ("blog:all")
      template_name = "blog/post_form.html"

class PostDetailView(DetailView):
        model = Post
        template_name="blog/post_detail.html"
    
class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")
    template_name = "blog/post.form.html"

class PostDeleteView(DeleteView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")
    template_nmae = "blog/post_confirm_delete.html"

 



 

# Create your views here.

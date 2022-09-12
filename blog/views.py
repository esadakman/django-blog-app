from urllib import request
from django.shortcuts import render , get_object_or_404

from blog.forms import CommentForm
from .models import Post,Comment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context) 


def about(request):
    return render(request, 'blog/about.html') 

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))
    # return render( request, 'blog/likes.html', args=[str(pk)])
    instance = Post.objects.get(id=id)
    # if request.method == "POST":
    #     instance = get_object_or_404(Post, id=request.POST.get('post_id')) 
    #     if not instance.likes.filter(id=request.user.id).exists():
    #         instance.likes.add(request.user)
    #         instance.save()  
    #         return render( request, 'blog/likes.html', context={'post':instance})
    #     else:
    #         instance.likes.remove(request.user)
    #         instance.save()  
    #         return render( request, 'blog/likes.html', context={'post':instance})


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        # for author id
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content','image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post 

    #? view count part
    def get_object(self,):
        views = super().get_object()
        views.blog_view += 1
        views.save()

        return views

    def get_object_like(self,*args, **kwargs): 
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes() 

        return total_likes

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/add_comment.html' 
    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.name = self.request.user
        return super().form_valid(form)

    # success_url: reverse_lazy('post-detail')
    success_url = '/'
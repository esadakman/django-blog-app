from django.shortcuts import render, get_object_or_404 ,redirect
from .models import Post, Comment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
) 
from .forms import CommentForm, PostUpdateForm
from django.contrib.auth.decorators import login_required

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


# def about(request):
#     return render(request, 'blog/about.html')


def like_post(request, id):
    if request.method == "POST":
        instance = Post.objects.get(id=id)
        if not instance.likes.filter(id=request.user.id).exists():
            instance.likes.add(request.user)
            instance.save()
            return render(request, 'blog/likes_area.html', context={'post': instance})
        else:
            instance.likes.remove(request.user)
            instance.save()
            return render(request, 'blog/likes_area.html', context={'post': instance})


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']



class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        # for author id
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'image']

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

    # ? view count part
    def get_object(self,):
        views = super().get_object()
        views.blog_view += 1
        views.save()

        return views

    def get_object_like(self, *args, **kwargs):
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        return total_likes

@login_required
def blog_detail(request, pk):
    post = Post.objects.get(id=pk) 
    form = CommentForm()
    form_blog= PostUpdateForm()
    comments = Comment.objects.filter(post=post.id)
    post.blog_view += 1
    post.save()  
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid(): 
            comment = form.save(commit=False)
            comment.post = post
            post.blog_comment +=1 
            comment.user = request.user
            post.blog_view -= 2
            post.save()
            comment.save()
            return redirect("post-detail", pk)
    return render(request, 'blog/post_detail.html', {'post': post, 'form': form, 'comments': comments})
 

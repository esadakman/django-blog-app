from django.urls import path
from . import views
from .views import (
    # AddCommentView,
    like_post,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    blog_detail
)

urlpatterns = [ 
    path('', PostListView.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('post/<int:pk>/', blog_detail, name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'), 
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'), 
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('like/<int:id>', like_post, name='like_post'), 
]
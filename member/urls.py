from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views

urlpatterns = [
    path('',PostListView.as_view(), name='member-home'),
    path('user/<str:username>',UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/',PostDetailView.as_view(), name='post-detail'),
    path('post/new/',PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(), name='post-delete'),
    path('users/approve/<int:pk>',views.approve_user, name='approve-user'),
    path('users/delete/<int:pk>', views.delete_user, name='delete-user'),
    path('posts/approve/<int:pk>', views.approve_post, name='approve-post'),
    path('posts/delete/<int:pk>', views.delete_post, name='delete-post'),
    path('allpost/',views.allpost, name='all-post'),
    path('allnewmember/',views.allnewmember, name='all-new-member'),    
    
]
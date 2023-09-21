from django.urls import path
from . import views

urlpatterns = [
    path('', views.starting_page, name='starting-page'),
    path('posts', views.posts, name='posts-page'),
    path('posts/<slug:slug>', views.post_detail, name='post-detail-page'),
    path('posts/<slug:slug>/readlater', views.ToggleReadLater.as_view(), name='toggle-read-later'),
    path('readlater', views.ListPostsMarked4Readlater.as_view(), name='readlater'),
    path('add-post', views.AddPostView.as_view(), name='add-post'),
]

from django.shortcuts import render, get_object_or_404
from datetime import date
from .models import Post, Author, Tag

def starting_page(request):
    latest_posts = Post.objects.all().order_by('-date')[:3]
    # sorted_post = sorted(all_posts, key=lambda p : p['date'])
    # latests_posts = all_posts[-3:]
    return render(request, 'blog/index.html', {
        'posts': latest_posts,
    })


def posts(request):
    all_posts = Post.objects.all()
    return render(request, 'blog/all-posts.html',{
                  'all_posts': all_posts,
                  })

def post_detail(request, slug):
    # post = Post.objects.get(slug=slug)
    post = get_object_or_404(Post, slug=slug)
    # post = next(post for post in all_posts if post
    #  ['slug'] == slug)
    return render(request, 'blog/post-detail.html', {
        'post': post,
        'tags': post.tags.all(),
    })

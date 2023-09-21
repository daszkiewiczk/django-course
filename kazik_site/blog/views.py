from django.shortcuts import render, get_object_or_404
from datetime import date
from .models import Post, Author, Tag, Comment
from django.views.generic import CreateView, View
from .forms import AddCommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView

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
    if request.method == 'POST':
        add_comment_form = AddCommentForm(request.POST)
        if add_comment_form.is_valid():
            new_comment = add_comment_form.save(commit=False)
            new_comment.post_id = Post.objects.get(slug=slug).id
            new_comment.save()
            return HttpResponseRedirect(reverse('post-detail-page', args=[slug]))
    # post = Post.objects.get(slug=slug)
    post = get_object_or_404(Post, slug=slug)
    # post = next(post for post in all_posts if post
    #  ['slug'] == slug)
    comments_list = post.comments.all()
    print(post.image.url)
    posts_4_readlater = request.session.get('posts_marked_for_readlater') 
    if posts_4_readlater is not None:
        is_marked_for_readlater = post.slug in posts_4_readlater
    else:
        is_marked_for_readlater = False
    return render(request, 'blog/post-detail.html', {
        'post': post,
        'tags': post.tags.all(),
        'add_comment_form': AddCommentForm(),
        'comments': comments_list,
        'marked': is_marked_for_readlater,
    })

# class AddCommentView(CreateView):
#     model = Comment
#     fields = '__all__'

class ToggleReadLater(View):
    def post(self, request, slug):
        posts = request.session.get('posts_marked_for_readlater')
        if posts == None:
            posts = []
        post_id = slug
        if post_id in posts:
            posts.remove(post_id)
        else:
            posts.append(post_id)
        print(posts)
        request.session['posts_marked_for_readlater'] = posts
        return HttpResponseRedirect(reverse('post-detail-page', args=[slug]), {
        })

class ListPostsMarked4Readlater(ListView):
    model = Post
    template_name = 'blog/readlater.html'
    paginate_by = 3
    # def get(self, request):
    #     self.post_id = request.session.get('posts_marked_for_read')
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context[""] = 
        return context
    
class AddPostView(CreateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('posts-page')
from django.shortcuts import render, get_object_or_404, redirect
from .models import  BlogPosts
from .forms import post_create

# Create your views here.
def blog_index(request):
    blog_posts = BlogPosts.objects.filter()

    return render(request, 'blog_index.html', {"blog":blog_posts})

def blog_viewpost(request, id):
    post = get_object_or_404(BlogPosts, pk=id)
    return render(request, 'blog_post.html', {'post':post})

def blog_admin(request):
    if request.method == "POST":
        form = post_create(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.username
            post.save()
            return render(request, 'blog_admin.html', {'form': form})
        else:
            return render(request, 'blog_admin.html', {'form': form})
    else:
        form = post_create()
        return render(request, 'blog_admin.html', {'form': form})

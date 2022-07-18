from django.shortcuts import render, get_object_or_404
from .models import Post, Category

def blog(request):

    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {'posts':posts})

def category(request, category_id):

    # Hay que hacer esto para comprobar que existe un id asociado al Path parameter.
    category = get_object_or_404(Category, id=category_id)
    return render(request, 'blog/category.html', {"category":category})

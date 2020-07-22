from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def home_view(request):
    context = {
        "color":"light",
        "home_status":"active",
        "home_highlight":"navactive"
    }
    return render(request, 'mainapp/index.html', context)

def about_view(request):
    context = {
        "color":"dark",
        "about_status":"active",
        "about_highlight":"navactive"
    }
    return render(request, 'mainapp/about.html', context)

def portfolio_view(request):
    context = {
        "color":"light",
        "portfolio_status":"active",
        "portfolio_highlight":"navactive"
    }
    return render(request, 'mainapp/portfolio.html', context)

def blog_posts_view(request):
    posts = BlogPost.objects.all()
    context = {
        'posts':posts,
        "color":"dark",
        "blog_status":"active",
        "blog_highlight":"navactive"
    }
    return render(request, 'mainapp/blog.html', context)

def blog_detail_view(request, **kwargs):
    slug = kwargs.get('slug')
    context = {
        'post':BlogPost.objects.get(slug=slug),
        "color":"dark",
        "blog_detail_status":"active",
        "blog_detail_highlight":"navactive"
    }
    return render(request, 'mainapp/blog-detail.html', context)

def contact_view(request):
    context = {
        "color":"light",
        "contact_status":"active",
        "contact_highlight":"navactive"
    }
    return render(request, 'mainapp/contact.html', context)
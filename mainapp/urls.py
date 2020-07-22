from django.urls import path
from . import views

app_name='mainapp'
urlpatterns = [
    path('', views.home_view, name='home'),
    path('about', views.about_view, name='about'),
    path('portfolio', views.portfolio_view, name='portfolio'),
    path('blog', views.blog_posts_view, name='blog'),
    path('blog/<slug:slug>/', views.blog_detail_view, name='blog-detail'),
    path('contact', views.contact_view, name='contact')
]
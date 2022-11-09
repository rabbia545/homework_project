from django.urls import path
from .views import index
from .views import about
from .views import blog
from .views import blog_single
from .views import contact
from .views import pricing
from .views import portfolio
from .views import portfolio_details
from .views import services
from .views import team

urlpatterns = [
    path('',index,name='home'),
    path('about/',about,name='about'),
    path('blog/',blog,name='blog'),
    path('blog_single/',blog_single,name='blog2'),
    path('contact/',contact,name='contact'),
    path('pricing/',pricing,name='pricing'),
    path('portfolio/',portfolio,name='portfolio'),
    path('portfolio_details/',portfolio_details,name='portfolio_details'),
    path('services/',services,name='services'),
    path('team/',team,name='team'),
]
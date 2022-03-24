from . import views
from django.urls import path, include

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('detail/',views.detail,name='detail'),
    path('thanks/',views.thanks,name='thanks'),
    path('operate/',views.operations,name='operations')

]
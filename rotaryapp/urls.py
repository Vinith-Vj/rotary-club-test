from django.urls import path
from . import views

app_name = 'rotaryapp'

urlpatterns = [
    path('', views.home, name='home'),

    # path("contactform_message/", views.contactform_message, name="contactform_message"),

    path('about', views.about, name='about'),

    path('project', views.project, name='project'),

    path('gallery', views.gallery, name='gallery'),

    path('contact', views.contact_view, name='contact'),

    # path('contact_msge/', views.contact_msge, name='contact_msge'),

    path('joinus', views.joinus, name='joinus'),
    
    # path('register/', views.register, name='register'),

    path('donate', views.donate, name='donate'),

    # path('sponsor_now/', views.sponsor_now, name='sponsor_now'),

    path('uyare/', views.uyare, name='uyare'),
    
    # path('uyare_register/', views.uyare_register, name='uyare_register'),

    path('essential/', views.essential, name='essential'),

    path('events/', views.events_view, name='events'),
]
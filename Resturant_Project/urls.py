from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Base_App.views import *
from Base_App import views


urlpatterns = [
    path('admin/', admin.site.urls, name='admin_pannel'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),

    path('', HomeView, name='Home'),
   
    path('menu/', MenuView, name='Menu'),
    path('about/', AboutView, name='About'),
    path('feedback/', FeedbackView, name='Feedback_Form'),
    
 path('order/', views.order_page, name='order_page'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path
from .views import MainView, home, about, contact, user_login, user_register, LoginMainView, SecondView

urlpatterns = [
    path('', MainView.as_view(), name='main'),  # This is the default URL for the root path
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),
    path('loginmain/', LoginMainView.as_view(), name='loginmain'),
    path('second/', SecondView.as_view(), name='second'),
]





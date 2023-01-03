"""blog_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from Blog import views
from django.contrib.auth import views as auth_views


# from blog_project.blog_app.views import register


urlpatterns = [
    path('', views.home, name='homeblog'),
    path('register', views.register, name='blogregister'),
    path('login', views.login, name='bloglogin'),
    path('logout', views.logoutblog, name='logout_blog'),
    path('uploadblog', views.Post_blog, name='uploadpost'),
    path('contactus_blog', views.contact_form, name='contactus_blog'),
    path('change_pswd', views.change_password, name='change_pswd'),
    path('reset_password', auth_views.PasswordResetView.as_view(
        template_name='password_reset_blog.html'), name="reset_password"),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(
        template_name='sent_resetpswd_blog.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='reset_confirm_blog.html'), name="password_reset_confirm"),
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(
        template_name='reset_complete_blog.html'), name="password_reset_complete"),
    path('search', views.search, name='search'),
    path('user', views.user_data, name='bloguserdata'),

]

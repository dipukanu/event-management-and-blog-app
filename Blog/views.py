from django.shortcuts import redirect, render
from .models import blog
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import contact_frm, blog_frm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.


def home(request):
    data = blog.objects.all()
    return render(request, 'bloghome.html', {'d': data})


def register(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:

            if User.objects.filter(username=username).exists():

                messages.info(request, "Username already exist!")
                return redirect("/blog/blogregister")

            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already exist!")
                return redirect("/blog/blogregister")

            else:
                user = User.objects.create_user(
                    first_name=first_name, last_name=last_name, email=email, username=username, password=password1)
                user.save()
                messages.info(request, "Registered successfully")
                return render(request, 'bloglogin.html')

        else:
            messages.info(request, "Password did not match, Please check!")
            return render(request, 'blogregister.html')

    else:
        return render(request, 'blogregister.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/blog/')
        else:
            messages.info(request, 'Invalid Username/Password')
            return redirect('/blog/bloglogin')
    else:
        return render(request, 'bloglogin.html')


def logoutblog(request):
    auth.logout(request)
    return redirect('/blog')


def contact_form(request):
    if request.method == "GET":
        form = contact_frm()
    else:
        form = contact_frm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'form.html', {'f': form})


def change_password(request):
    if request.method == "GET":
        pc = PasswordChangeForm(user=request.user)
        return render(request, 'changepassword_blog.html', {'context': pc})
    elif request.method == "POST":
        aa = PasswordChangeForm(user=request.user, data=request.POST)
        if aa.is_valid():
            user = aa.save()
            update_session_auth_hash(request, user)
            messages.info(request, "Password changed successfully!")
            return redirect('/blog/bloglogin')


def user_data(request):
    return render(request, 'bloguser.html')


@login_required(login_url='bloglogin')
def Post_blog(request):
    if request.method == "GET":
        form_post = blog_frm()
    else:
        form_post = blog_frm(request.POST, request.FILES)
        if form_post.is_valid():
            form_post.save()
    return render(request, 'post.html', {'f': form_post})


def search(request):
    search = request.POST['search']
    data = blog.objects.filter(blog_heading__icontains=search)
    return render(request, 'bloghome.html', {'d': data})

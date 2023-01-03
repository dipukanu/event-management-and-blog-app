from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Family, Charity, Business, Culture, Book_event, Contact_us
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.


def home(request):
    if request.method == "POST":
        Name = request.POST['name']
        Mobile = request.POST['mobile']
        Email = request.POST['email']
        Message = request.POST['message']
        enquiry = Contact_us(name=Name, mobile=Mobile,
                             email=Email, message=Message)
        enquiry.save()
        messages.info(request, "Your Query has been sent successfully!")
        return redirect('/')
    return render(request, 'home.html')


def family(request):
    fam = Family.objects.all()
    return render(request, 'family.html', {'f': fam})


def charity(request):
    char = Charity.objects.all()
    return render(request, 'charity.html', {'c': char})


def business(request):
    bus = Business.objects.all()
    return render(request, 'business.html', {'b': bus})


def culture(request):
    cul = Culture.objects.all()
    return render(request, 'culture.html', {'cu': cul})


@login_required(login_url='login')
def book_event(request):
    if request.method == "POST":
        Name = request.POST['name']
        Mobile = request.POST['mobile']
        Email = request.POST['email']
        Location = request.POST['location']
        People = request.POST['people']
        Date = request.POST['date']
        Event = request.POST['event']
        Food = request.POST['food']
        Address = request.POST['address']
        Message = request.POST['message']
        if ((Mobile and Email and Address) == ""):
            messages.info(request, 'Warning field required')
            return redirect('/bookevent')
        else:
            guest = Book_event(name=Name, mobile=Mobile, email=Email, location=Location,
                               people=People, date=Date, event=Event, food=Food, address=Address, message=Message)
            guest.user = request.user
            guest.name = request.user
            guest.save()
            messages.info(
                request, "Your Event is booked successfully! Thank you for booking an event with us!")
            return redirect('/user_cart')
    return render(request, 'book.html')


def contactus(request):
    return render(request, 'contact.html')


def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exist!")
                return redirect('/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already exist!")
                return redirect('/register')
            else:
                user = User.objects.create_user(
                    first_name=first_name, last_name=last_name, username=username, email=email, password=password1)
                user.save()
                messages.info(
                    request, 'Your account has been created successfully! Please login')
                return redirect('/login')
        else:
            messages.info(request, "Password didn't match")
            return redirect('/register')

    else:

        return render(request, 'register.html')


def user_data(request):
    #     data=Studnet.objects.all()
    return render(request, 'user.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid username/ password!')
            return redirect('/login')
    else:
        return render(request, 'login.html')


def change_password(request):
    if request.method == "GET":
        pc = PasswordChangeForm(user=request.user)
        return render(request, 'changepassword.html', {'context': pc})
    elif request.method == "POST":
        aa = PasswordChangeForm(user=request.user, data=request.POST)
        if aa.is_valid():
            user = aa.save()
            update_session_auth_hash(request, user)
            messages.info(
                request, "Password changed successfully! Please Login")
            return redirect('/login')


@login_required(login_url='login')
def usercart(request):
    my_cart = Book_event.objects.filter(user=request.user)
    return render(request, 'user_cart.html', {'my_cart': my_cart})


def aboutus(request):
    return render(request, 'aboutus.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

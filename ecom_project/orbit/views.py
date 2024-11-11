from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Product,Customer
from django.contrib.auth.models import User
from .forms import RegisterForm,UserInfoForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
import json
from cart.cart import Cart


# Create your views here.
from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Customer
from .forms import UserInfoForm

def update_info(request):
    if request.user.is_authenticated:
        try:
            # Fetch Customer linked to the logged-in user
            current_user = Customer.objects.get(user=request.user)
        except Customer.DoesNotExist:
            messages.error(request, "No profile found. Please create a profile first.")
            return redirect('home')  # Redirect to an appropriate page if no Customer is found

        # Use the instance of the current_user to populate the form
        form = UserInfoForm(request.POST or None, instance=current_user)

        if form.is_valid():
            form.save()
            messages.success(request, "Your info has been updated!")
            return redirect('home')
        
        return render(request, "update_info.html", {'form': form})

    else:
        messages.error(request, "You must be logged in to update your info.")
        return redirect('home')

 

def product(request,pk):
     product = Product.objects.get(id=pk)
     return render(request,'product.html', {'product':product})

def home(request):
    products = Product.objects.all()
    return render(request,'home.html', {'products':products})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Create the User
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name']
            )
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            login(request,user) 
            return redirect('update_info')  # Redirect after registration
        else:
             return redirect('register')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

def login_user(request):
        if request.method=='POST':
             username=request.POST['username']
             password=request.POST['password']
             user = authenticate(request,username=username,password=password) 
             if user is not None:
                login(request,user)

                # shopping cart stuffs
                current_user= Customer.objects.get(user__id=request.user.id)
                saved_cart= current_user.old_cart
                #   convert database string back to dictionary to gove it to the session
                if saved_cart:
                    converted_cart=json.loads(saved_cart)
                    cart=Cart(request)

                    for key, value in converted_cart.items():
                        cart.db_add(product=key,quantity=value)


                messages.success(request,("You have been logged in"))
                return redirect('home')
             else:
                  messages.success(request,("there was an error"))
                  return redirect('login')
        else:
            return render(request,'login.html', {})

def logout_user(request):
     logout(request)
     messages.error(request,("You have been logged out!!..ThankYou"))
     return redirect('home')

def football(request):
     products = Product.objects.filter(category__name='Football')  # Adjust the filter as necessary
     return render(request, 'football.html', {'products': products})
    

def basketball(request):
     products = Product.objects.filter(category__name='Basketball')  # Adjust the filter as necessary
     return render(request, 'basketball.html', {'products': products})

def allproducts(request):
     products = Product.objects.all().order_by('?')
     return render(request,'allproducts.html', {'products':products})





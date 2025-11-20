from django.shortcuts import render, redirect, get_object_or_404
from .models import  Category, Products  # Or 'Product' if that's your model name!
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from .forms import SignUpForm

def home(request):
    products = Products.objects.all()
    return render(request, 'home.html', {'products': products})

def about(request):
    products = Products.objects.all()  # Now you pass products to about.html
    return render(request, 'about.html', {'products': products})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password. Please try again.")
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out....")
    return redirect('home')


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, "Account created and logged in.")
                return redirect('home')
            messages.success(request, "Account created. Please log in.")
            return redirect('login')
        else:
            # Fall through to re-render the form with errors
            messages.error(request, "Please correct the errors below.")
    else:
        form = SignUpForm()

    return render(request, 'register.html', {'form': form})

def product(request, pk):
    item = get_object_or_404(Products, pk=pk)
    return render(request, 'product.html', {'product': item})

def category(request, foo):
    # Replace hyphens with spaces to match admin names
    name = foo.replace('-', ' ')
    category = get_object_or_404(Category, name__iexact=name)
    products = Products.objects.filter(category=category)  # or Product.objects.filter(...)

    return render(request, 'category.html', {
        'category': category,
        'products': products,
    })

# Optional: category summary page that lists categories to click into
def category_summary(request):
    categories = Category.objects.all().order_by('name')
    return render(request, 'category_summary.html', {'categories': categories})
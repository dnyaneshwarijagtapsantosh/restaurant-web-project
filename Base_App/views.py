from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView as AuthLoginView
from django.urls import reverse_lazy
from Base_App.models import BookTable, AboutUs, Feedback, ItemList, Items, Cart,Order
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User 


# ORDER PAGE 

@csrf_exempt
def order_page(request):
    """
    Order Now page: GET → show form / items
    POST → process order → show Order Success + Bill
    """
    if request.method == "POST":
        item_name = request.POST.get("item_name", "Cake")
        price = float(request.POST.get("price", 0))
        quantity = int(request.POST.get("quantity", 1))
        address = request.POST.get("address", "")
        payment_method = request.POST.get("payment_method", "COD")
        total = price * quantity
        s=Order.objects.create(
    item_name = item_name,
    price =  price,
    quantity = quantity,
    address = address ,
    payment_method = payment_method,
  
        )


        s.save()

    

    

        return render(request, 'order.html', {
            'success': True,
            'item_name': item_name,
            'price': price,
            'quantity': quantity,
            'address': address,
            'payment_method': payment_method,
            'total': total
        })

    
    items = Items.objects.all() 
    return render(request, 'order.html', {
        'success': False,
        'items': items,
        'item_name': '',
        'price': '',
        'quantity': 1
    })



# LOGIN / SIGNUP / LOGOUT

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Home')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')

    
    return render(request, 'login.html')



def logout_view(request):
    logout(request)
    return redirect('Home')


def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('login')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('login')

        User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )

        messages.success(request, "Signup successful. Please login.")
        return redirect('login')

    return redirect('login')



# HOME / ABOUT / MENU

def HomeView(request):
    items = Items.objects.all()
    list = ItemList.objects.all()
    review = Feedback.objects.all().order_by('-id')[:5]
    return render(request, 'home.html', {'items': items, 'list': list, 'review': review})


def AboutView(request):
    data = AboutUs.objects.all()
    return render(request, 'about.html', {'data': data})


def MenuView(request):
    items = Items.objects.all()
    list = ItemList.objects.all()
    return render(request, 'menu.html', {'items': items, 'list': list})





# FEEDBACK

def FeedbackView(request):
    if request.method == 'POST':
        name = request.POST.get('User_name')
        feedback = request.POST.get('Description')
        rating = request.POST.get('Rating')
        image = request.FILES.get('Selfie')

        if name != '':
            feedback_data = Feedback(
                User_name=name,
                Description=feedback,
                Rating=rating,
                Image=image
            )
            feedback_data.save()
            messages.success(request, 'Feedback submitted successfully!')
            return render(request, 'feedback.html', {'success': 'Feedback submitted successfully!'})

    return render(request, 'feedback.html')




from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import User
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        contact_no = request.POST.get('contact_no')

        
        user = User(
            name=name,
            email=email,
            password=make_password(password),
            gender=gender,
            dob=dob,
            contact_no=contact_no
        )
        user.save()

        return redirect('login')

    return render(request, 'register.html')

from django.contrib.auth import authenticate, login
from django.contrib import messages

@csrf_protect
def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password.')
            return redirect('login')
            # Handle invalid login

    return render(request, 'login.html')

from django.shortcuts import render
from django.http import JsonResponse
from .models import User, Chat

def chat_screen(request):
    # Get the list of users
    users = User.objects.all()

    context = {
        'users': users
    }

    return render(request, 'chat_screen.html', context)

def fetch_chat_history(request):
    user_id = request.GET.get('user_id')

    # Fetch chat history from the database based on user_id
    chat_history = Chat.objects.filter(senderId=user_id)

    history = []
    for chat in chat_history:
        history.append({
            'sender': chat.senderId.name,
            'message': chat.msg,
            'timestamp': chat.created_at.strftime("%I:%M %p")
        })

    response = {
        'history': history
    }

    return JsonResponse(response)

def send_message(request):
    if request.method == 'POST':
        sender_id = request.POST.get('sender_id')
        recipient_id = request.POST.get('recipient_id')
        message = request.POST.get('message')

        # Save the new chat message to the database
        chat=Chat.objects.create(
            senderId=User.objects.get(id=sender_id),
            RecId=User.objects.get(id=recipient_id),
            msg=message
        )

        response = {
            'success': True
        }

        return JsonResponse(response)

    response = {
        'success': False
    }

    return JsonResponse(response)

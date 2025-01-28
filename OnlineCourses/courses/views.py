import os
import smtplib
import time
from email.message import EmailMessage
import logging

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.db.models import Avg
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ContactForm, ReviewForm, CustomLoginForm
from .models import Review, CourseMaterial

logger = logging.getLogger('django')

# Create your views here.

def home(request):
    current_year = time.time()
    current_year = time.localtime(current_year).tm_year
    context = {"current_year" : current_year}
    return render(request, "courses/home.html", context = context)


def reviews(request):
    # Get all approved reviews
    approved_reviews = Review.objects.filter(approved=True).order_by('-created_at')

    # Calculate the mean rating
    mean_rating = approved_reviews.aggregate(Avg('rating'))['rating__avg'] or 0
    print(mean_rating)
    if request.method == 'POST':
        form = ReviewForm(request.POST, user=request.user)
        if form.is_valid():
            review = form.save(commit=False)
            # Auto-approve for authenticated users
            if request.user.is_authenticated:
                review.approved = True
            review.save()
            messages.success(request, 'Dziękujemy za opinię! Po weryfikacji pojawi się na stronie.')
            return redirect('reviews')
    else:
        form = ReviewForm(user=request.user)

    context = {
        'reviews': approved_reviews,
        'form': form,
        'mean_rating': mean_rating
    }
    return render(request, 'courses/reviews.html', context)


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save to database
            contact_message = form.save()

            # Send email
            subject = f"Nowa wiadomość Physics&Math Academy: {contact_message.reason}"
            message_body = f"""
            <html>
            <body>
                <h2>Nowa wiadomość ze strony Physics&Math Academy:</h2>
                <p><strong>Imię:</strong> {contact_message.name or 'Nie podano'}</p>
                <p><strong>Email:</strong> {contact_message.email}</p>
                <p><strong>Powód:</strong> {contact_message.reason}</p>
                <p><strong>Wiadomość:</strong></p>
                <p>{contact_message.message}</p>
            </body>
            </html>
            """

            msg = EmailMessage()
            msg.set_content(message_body, subtype = 'html')
            msg['Subject'] = subject
            msg['From'] = 'hkowalski.fizyka@gmail.com'
            msg['To'] = 'hkowalski.fizyka@gmail.com'

            try:
                email_password = os.getenv('EMAIL_HOST_PASSWORD')
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                    server.login('hkowalski.fizyka@gmail.cm', email_password)
                    server.send_message(msg)
                print("Email sent successfully!")
            except Exception as e:
                logger.error(f"Error sending email: {str(e)}."
                             f"The client's email is: {contact_message.email}.")

            return render(request, "courses/contact.html", {
                "message": "Wiadomość wysłana! Odpowiem najszybciej jak to możliwe.",
                "form": ContactForm()
            })

    else:
        form = ContactForm()

    return render(request, "courses/contact.html", {"form": form})

@login_required(login_url="/courses/login/")
def courses(request):
    materials = CourseMaterial.objects.all().order_by('subject', 'order')

    context = {
        "materials": materials
    }
    return render(request, "courses/courses.html", context=context)


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            username = user.get_username()
            messages.success(request, f"Witaj {username}! Konto zostało utworzone i zostałeś/aś zalogowany/a.")
            return redirect("home")

    else:
        form = UserCreationForm()

    context = {
        "form": form
    }
    return render(request, "courses/register.html", context=context)

class CustomLoginView(LoginView):
    """
    CustomLoginView is used for customization of the login form.
    It uses a custom login form and a specific template for rendering the login page.
    """
    form_class = CustomLoginForm
    template_name = 'courses/login.html'

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = CustomLoginForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Witaj {username}! Zostałeś zalogowany.")
                if "next" in request.POST:
                    return redirect(request.POST.get("next"))
                else:
                    return redirect('home')
    else:
        form = CustomLoginForm(request)

    context = {
        "form": form
    }

    return render(request, "courses/login.html", context = context)

def logout_view(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, "Zostałeś wylogowany.")
        return redirect('home')
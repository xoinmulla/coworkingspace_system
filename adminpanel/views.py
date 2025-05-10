from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from spaces.models import Space
from bookings.models import Booking
from reviews.models import Review
from payments.models import Payment

# Dashboard overview
@staff_member_required
def dashboard(request):
    total_spaces = Space.objects.count()
    total_bookings = Booking.objects.count()
    total_payments = Payment.objects.filter(status='completed').count()
    total_reviews = Review.objects.count()
    context = {
        'total_spaces': total_spaces,
        'total_bookings': total_bookings,
        'total_payments': total_payments,
        'total_reviews': total_reviews,
    }
    return render(request, 'adminpanel/dashboard.html', context)

# Space management view (list spaces with admin options)
@staff_member_required
def space_management(request):
    spaces = Space.objects.all()
    return render(request, 'adminpanel/space_management.html', {'spaces': spaces})

# Booking management view
@staff_member_required
def booking_management(request):
    bookings = Booking.objects.all().order_by('-booking_date')
    return render(request, 'adminpanel/booking_management.html', {'bookings': bookings})

# Reporting view (a simple representation of reports)
@staff_member_required
def reporting(request):
    # For demonstration, we simply show counts and leave charting to future iterations.
    report = {
        'space_utilization': Booking.objects.count(),
        'revenue': Payment.objects.filter(status='completed').count() * 50,  # assuming fixed amount
        'feedback_count': Review.objects.count(),
    }
    return render(request, 'adminpanel/reporting.html', {'report': report})

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'adminpanel/register.html', {'form': form})

# myapp/views.py
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View

class LogoutViaGet(View):
    def get(self, request):
        logout(request)
        return redirect('/')
    

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin-dashboard')
        else:
            return render(request, 'adminpanel/login.html', {'error': 'Invalid credentials'})
    return render(request, 'adminpanel/login.html')

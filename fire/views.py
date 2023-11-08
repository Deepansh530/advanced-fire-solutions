# fire/views.py

from django.shortcuts import render, get_object_or_404
from .models import Staff
from .models import Review
from django.urls import reverse
from django.http import JsonResponse
from .models import ContactMessage

def home(request):
    reviews = Review.objects.all()  # Query all reviews
    return render(request, 'fire/home.html', {'reviews': reviews})

def staff_list(request):
    staff_members = Staff.objects.all()
    return render(request, 'fire/staff/our-staff.html', {'staff_members': staff_members})

def staff_detail(request, slug):
    staff_member = get_object_or_404(Staff, slug=slug)
    return render(request, 'fire/staff/staff-detail.html', {'staff_member': staff_member})

def contact_submit(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        message = request.POST.get("message")

        # Save the form data to the database
        contact_message = ContactMessage(
            name=name, email=email, phone_number=phone_number, message=message
        )
        contact_message.save()

        # Return a success response
        return JsonResponse({"success": True})

    return JsonResponse({"success": False})

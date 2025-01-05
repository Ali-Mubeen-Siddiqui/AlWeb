from django.shortcuts import render
from .models import Contact, Gallery,Review
from django.contrib import messages
import datetime
  # Import transaction for atomic operations

from asgiref.sync import sync_to_async

# Create your views here.
async def validate_form(name, number, email, area, marriageDate):
    # Function to validate form data
    errors = []
    if len(name) < 3 or len(name) > 50:
        errors.append("Name should be between 3 and 50 characters")
    if not number.replace(' ', '').replace('+', '').isdigit() or not 10 <= len(number.replace(' ', '')) <= 15:
        errors.append("Invalid phone number")
    if len(email) < 5 or len(email) > 100:
        errors.append("Email should be between 5 and 100 characters")
    if len(area) < 3 or len(area) > 100:
        errors.append("Area should be between 3 and 100 characters")
    if len(marriageDate) < 8 or len(marriageDate) > 10:
        errors.append("Invalid marriage date")
    return errors

async def index(request):
    # View for the index page
    message = None
    if request.method == "POST":
        # Extract form data
        name = request.POST.get("name")
        number = request.POST.get("number")
        email = request.POST.get("gmailId")
        area = request.POST.get("area")
        marriageDate = request.POST.get("marriageDate")
        
        # Validate form data
        errors = await validate_form(name, number, email, area, marriageDate)
        if errors:
            # If errors, display them
            for error in errors:
                messages.error(request, error)
        else:
            # If no errors, save the data
            data = Contact(name=name, phone=number, email=email, area=area, marriageDate=marriageDate, date=datetime.date.today())
            try:
                await sync_to_async(data.save)()  # Ensure saving is async
                message = messages.success(request, "form sent successfully, we will contact you soon")
            except Exception as e:
                message = messages.error(request, e)

    
    return render(request, "index.html", {"message": message})

async def contact(request):
    # View for the contact page
    return render(request, "contact.html")

async def gallery(request):
    # View for the gallery page
    galleries = await sync_to_async(Gallery.objects.all)()
    galleries = await sync_to_async(lambda: list(galleries.values('name', 'date', 'image','place')))()
    return render(request, "gallery.html", {"galleries": galleries})
    



async def review_page(request):
    reviews = await sync_to_async(Review.objects.all)()
    reviews = await sync_to_async(lambda: list(reviews.values("date", "gmailId", "review", "stars")))()  # Convert to list asynchronously

    return render(request,"review.html",{"reviews": reviews})



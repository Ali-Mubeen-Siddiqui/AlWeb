from django.shortcuts import render
from .models import *
from django.contrib import messages
import datetime
  # Import transaction for atomic operations

from asgiref.sync import sync_to_async

# Create your views here.
async def validate_form(name, number, email, area, marriageDate):
    # Function to validate form data
    errors = [
        "Name should be between 3 and 50 characters" if len(name) < 3 or len(name) > 50 else None,
        "Invalid phone number" if not number.replace(' ', '').replace('+', '').isdigit() or not 10 <= len(number.replace(' ', '')) <= 15 else None,
        "Email should be between 5 and 100 characters" if len(email) < 5 or len(email) > 100 else None,
        "Area should be between 3 and 100 characters" if len(area) < 3 or len(area) > 100 else None,
        "Invalid marriage date" if len(marriageDate) < 8 or len(marriageDate) > 10 else None
    ]
    errors = [error for error in errors if error is not None]
    return errors

async def validate_contact_form(name, number, email):
    # Function to validate partial form data
    errors = [
        "Name should be between 3 and 50 characters" if len(name) < 3 or len(name) > 50 else None,
        "Invalid phone number" if not number.replace(' ', '').replace('+', '').isdigit() or not 10 <= len(number.replace(' ', '')) <= 15 else None,
        "Email should be between 5 and 100 characters" if len(email) < 5 or len(email) > 100 else None
    ]
    errors = [error for error in errors if error is not None]
    return errors

async def index(request):
    # View for the index page
    message = None
    if request.method == "POST":
        # Extract form data
        name = request.POST.get("name")
        number = request.POST.get("number")
        email = request.POST.get("gmailId")
       
        
        # Validate form data
        errors = await validate_contact_form(name, number, email)
        if errors:
            # If errors, display them
            for error in errors:
                messages.error(request, error)
        else:
            # If no errors, save the data
            data = Contact(name=name, phone=number, email=email)
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



async def add_review(request):
    message = None
    if request.method == "POST":
        email = request.POST.get("gmail")
        ratings = request.POST.get("rating")
        review = request.POST.get("review")
        try:
            review_instance = Review(gmailId=email, stars=ratings, review=review, date=datetime.date.today())
            await sync_to_async(review_instance.save)()  # Ensure saving is async
            message = "Review sent successfully :  Thanks for your review,your review matters a lot to us."
        except Exception as e:
            message = messages.error(request, str(e))

    return render(request,"addReview.html",{"message": message})



async def policies(request):
    return render(request,"policies.html")


    

async def book_us(request):
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
            return render(request, "index.html", {"message": message})
        else:
            # If no errors, save the data
            data = Book(name=name, phone=number, email=email, area=area, marriageDate=marriageDate, date=datetime.date.today())
            try:
                await sync_to_async(data.save)()  # Ensure saving is async
                message = messages.success(request, "form sent successfully, we will contact you soon")
                return render(request, "index.html", {"message": message})
            except Exception as e:
                message = messages.error(request, e)
                return render(request, "index.html", {"message": message})
    else:
        return render(request,"book_us.html")


    
    




from django.shortcuts import render
from .models import homeCoverImage, History, Contact, Membership, Sponsor, Uyare
from django.shortcuts import render, redirect
from django.contrib import messages
# import pywhatkit as kit
# import pywhatkit
from django.http import HttpResponse
# from django.utils.timezone import now
# from datetime import datetime, timedelta
# import time

# Create your views here.

def home(request):
    cover = homeCoverImage.objects.all()
    context = {'cover': cover}
    return render(request, "index.html", context)

# def contactform_message(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         email = request.POST.get("email")
#         phone = request.POST.get("phone")
#         subject = request.POST.get("sub")
#         message = request.POST.get("msg")

#         # Save to the database
#         Contact.objects.create(
#             name=name,
#             email=email,
#             phone=phone,
#             subject=subject,
#             message=message
#         )

#         # Send WhatsApp message
#         try:
#             whatsapp_message = (
#                 f"New Contact Form Submission :\n\n"
#                 f"Name : {name}\n"
#                 f"Email : {email}\n"
#                 f"Phone : {phone}\n"
#                 f"Subject : {subject}\n"
#                 f"Message : {message}"
#             )
#             kit.sendwhatmsg_instantly("+918547501092", whatsapp_message, wait_time=10)
#             messages.success(request, "Your message was successfully sent!")
#         except Exception as e:
#             messages.error(request, f"Failed to send WhatsApp message: {e}")

#         # Redirect to the homepage
#         return redirect("rotaryapp:home")

#     return render(request, "index.html")


def about(request):
    history = History.objects.all().order_by('-start_year')
    context = {
        'history': history
    }
    return render(request, 'about.html', context)

def project(request):
    return render(request, 'project.html', {})

def gallery(request):
    return render(request, 'gallery.html', {})

def contact_view(request):
    return render(request, 'contact.html')

# def contact_msge(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         subject = request.POST.get('sub')
#         message = request.POST.get('msg')

#         # Save the data to the database
#         contact = Contact(name=name, email=email, phone=phone, subject=subject, message=message)
#         contact.save()

#         # Format the WhatsApp message
#         whatsapp_message = f"New Contact Form Submission:\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nSubject: {subject}\nMessage: {message}"

#         # Send the message via WhatsApp
#         try:
#             kit.sendwhatmsg_instantly("+918547501092", whatsapp_message, wait_time=10)
#             messages.success(request, "Message sent successfully via WhatsApp!")
#         except Exception as e:
#             messages.error(request, f"Failed to send WhatsApp message: {e}")

#         return redirect('contact')

#     return render(request, 'contact.html')

def joinus(request): 
    return render(request, 'joinus.html', {})

# def register(request):
#     if request.method == 'POST':
#         # Capture form data
#         firstname = request.POST.get('firstname')
#         lastname = request.POST.get('lastname')
#         email = request.POST.get('email')
#         profession = request.POST.get('profession', '')
#         age = request.POST.get('age', '')
#         phone_number = request.POST.get('phone_number')
#         secondary_number = request.POST.get('secondary_number', '')
#         phone_type = request.POST.get('phone_type', '')

#         # Save to database
#         membership = Membership(
#             firstname=firstname,
#             lastname=lastname,
#             email=email,
#             profession=profession,
#             age=age,
#             phone_number=phone_number,
#             secondary_number=secondary_number,
#             phone_type=phone_type,
#             created_at=datetime.now()
#         )
#         try:
#             membership.save()

#             # Send WhatsApp message
#             whatsapp_number = '+918547501092'
#             message = f"New Membership Form Submitted :\n\nName : {firstname} {lastname}\nEmail : {email}\nPhone : {phone_number}\nSecondary Phone : {secondary_number}\nProfession : {profession}\nAge : {age}\nPhone Type : {phone_type}"

#             pywhatkit.sendwhatmsg_instantly(
#                 phone_no=whatsapp_number,
#                 message=message,
#                 wait_time=10  # Adjust wait time as needed
#             )

#             # Send success message to user
#             messages.success(request, "Form submitted successfully, and WhatsApp message sent.")
#             return redirect('rotaryapp:joinus')  # Redirect to the 'joinus' page

#         except Exception as e:
#             # Handle any exceptions and show error message
#             messages.error(request, f"Error occurred: {str(e)}")
#             return redirect('rotaryapp:joinus')  # Redirect to the 'joinus' page on failure

#     return render(request, 'joinus.html')

def donate(request):
    return render(request, 'donate.html', {})

# def sponsor_now(request):
#     if request.method == 'POST':
#         # Retrieve data from the form
#         orgname = request.POST.get('orgname')
#         contactname = request.POST.get('contactname')
#         email = request.POST.get('email')
#         address = request.POST.get('address')
#         city = request.POST.get('city')
#         country = request.POST.get('country')
#         amount = request.POST.get('amount')

#         # Save to the database
#         sponsor = Sponsor(
#             organization_name=orgname,
#             contact_name=contactname,
#             email=email,
#             address=address,
#             city=city,
#             country=country,
#             amount=amount if amount else None
#         )
#         sponsor.save()

#         # Prepare the WhatsApp message
#         whatsapp_number = "+918547501092"  # Target number
#         message = (
#             f"New Sponsorship Submission :\n\n"
#             f"Organization Name : {orgname}\n"
#             f"Contact Name : {contactname}\n"
#             f"Email : {email}\n"
#             f"Address : {address}\n"
#             f"City : {city}\n"
#             f"Country : {country}\n"
#             f"Donation Amount : {amount if amount else 'Not specified'}"
#         )

#         try:
#             # Send the WhatsApp message instantly
#             kit.sendwhatmsg_instantly(whatsapp_number, message)
#             messages.success(request, 'Thank you for your sponsorship! A confirmation message has been sent.')
#         except Exception as e:
#             print(f"Error sending WhatsApp message: {e}")
#             messages.error(request, 'Thank you for your sponsorship! Failed to send WhatsApp confirmation.')

#         # Use redirect to correct 'donate' URL pattern
#         return redirect('rotaryapp:donate')  # This should work now

#     else:
#         return redirect('rotaryapp:donate')  # Use redirect to 'donate' if GET request


def uyare(request):
    return render(request, 'uyare.html')

# def uyare_register(request):
#     if request.method == "POST":
#         # Extract form data
#         firstname = request.POST.get('firstname')
#         lastname = request.POST.get('lastname')
#         email = request.POST.get('email')
#         age = request.POST.get('age')
#         phone_number = request.POST.get('phone_number')
#         qualification = request.POST.get('qualification')

#         try:
#             # Save form data to the database
#             Uyare.objects.create(
#                 firstname=firstname,
#                 lastname=lastname,
#                 email=email,
#                 age=int(age),
#                 phone_number=phone_number,
#                 qualification=qualification
#             )

#             # Prepare WhatsApp message
#             current_hour = datetime.now().hour
#             current_minute = datetime.now().minute + 1  # Schedule for a minute later

#             message = (f"New registration:\n\n"
#                       f"Name : {firstname} {lastname}\n"
#                       f"Email : {email}\n"
#                       f"Age : {age}\n"
#                       f"Phone : {phone_number}\n"
#                       f"Qualification : {qualification}")
#             try:
#                 # Attempt to send WhatsApp message
#                 kit.sendwhatmsg("+7306244170", message, current_hour, current_minute, wait_time=10)
#                 time.sleep(15)  # Allow time for message to send

#                 messages.success(request, "Form submitted successfully! WhatsApp message sent.")
#             except Exception as e:
#                 print("WhatsApp Error:", e)
#                 messages.warning(request, "Form submitted, but failed to send WhatsApp message.")

#         except Exception as e:
#             print("Error Saving Data:", e)
#             messages.error(request, "Form submission failed. Please try again.")

#         # Redirect back to the uyare page
#         return redirect('rotaryapp:uyare')

#     return render(request, 'uyare.html')
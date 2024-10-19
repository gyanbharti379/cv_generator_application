from django.shortcuts import render
from .models import Profile
from .forms import RegistrationForm
import pdfkit
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404
import io

# Create your views here.

def userForm(request):
     
    form = RegistrationForm()
    return render(request, 'UserForm.html', {'form': form})

def submitform(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        city = request.POST.get('city')
        country = request.POST.get('country')
        summary = request.POST.get('summary')
        degree = request.POST.get('degree')
        school = request.POST.get('school')
        university = request.POST.get('university')
        previous_work = request.POST.get('previous_work')
        skills = request.POST.get('skills')

        profile = Profile(
            name = name,
            email = email,
            phone = phone,
            address = address,
            city = city,
            country = country,
            summary = summary,
            degree = degree,
            school = school,
            university = university,
            previous_work = previous_work,
            skills = skills
        )
        profile.save()
        success = True
        return render(request, 'SuccessPage.html',{
            "name":profile.name,
            "success":success,
            "id":profile.id})  
    else:
        success = False 
        return render(request, 'SuccessPage.html',{"success":success}) 
    
    return render(request, 'accept.html')

def showdetails(request,id):
    userprofile = get_object_or_404(Profile, id=id)
    print(userprofile.name)
     
    # userprofile = Profile.objects.get(pk=id)
    return render(request, 'generateResume.html',{"userprofile":userprofile})


def generatePDF(request,id):
    user_profile = Profile.objects.get(pk=id)
    template = loader.get_template('generateResume.html')
    html = template.render({'user_profile':user_profile})
    options = {
        'page-size': 'A4',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'no-outline': None  

    }
    pdf = pdfkit.from_string(html, False,options)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment' 
    filename="resume.pdf"


    return response

def list_of_all_users(request):
    userprofile = Profile.objects.all()
    return render(request, 'list_of_users.html',{"userprofile":userprofile}) 
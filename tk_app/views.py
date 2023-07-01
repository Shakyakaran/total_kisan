from django.shortcuts import render,redirect,HttpResponse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from django.views.generic import View
from django.contrib.auth import authenticate,logout as auth_logout
from django.contrib.auth import login as auth_login
from .models import *
from datetime import date

def home(request):

    crops = AddCrop.objects.all().order_by('-startDate')

    totalArea = 0

    for x in crops:
        totalArea = totalArea + x.cropArea

    context = {'crop':crops,'area':totalArea}

    return render(request, 'home.html',context)

def signup(request):

    if (request.method == "POST"):
        # name = request.POST['name']
        email = request.POST['email']
        password = request.POST['pass1']
        confirm_password = request.POST['pass2']
        
        if password != confirm_password:
            messages.warning(request, 'Password is not matching !')
            return render(request, 'signup.html')
        
        try:
            if User.objects.get(username = email):
                return HttpResponse('email already exists')
        
        except:
            pass

        user = User.objects.create_user(email, email, password)
        user.is_active=True
        user.save()

        params = {'email':email,}

        return render(request, 'login.html' ,params)

        # email_subject = "Activate your account "
        # message = render_to_string('activate.html',{
        #     'user':user,
        #     'domain':'127.0.0.1:8002',
        #     'uid':urlsafe_base64_encode(force_bytes(user.pk)),
        #     'token':generate_token.make_token(user)
        # })

        # email_message = EmailMessage(email_subject,message,settings.EMAIL_HOST_USER,[email],)
        # email_message.send()
        # messages.success(request,'Activate your account by clicking the link in your gmail account')

        # return redirect('/auth/login/')


    return render(request, 'signup.html')

def login(request):
    if request.method=="POST":
        username = request.POST['email']
        userpassword = request.POST['pass1']
        myuser = authenticate(username=username, password=userpassword)

        if myuser is not None:
            auth_login(request, myuser)
            messages.success(request,'Login success')
            return redirect('/home')
        else:
            messages.error(request,'Invalid credentials')
            return redirect('/login')
        
    return render(request, 'login.html')

def logout(request):

    auth_logout(request)
    messages.info(request, 'Logout success')

    return redirect('/login')

def add_crop(request):

    

    if request.user.is_authenticated:

        if request.method == 'POST':

            userEmail = request.user.email
            state = request.POST['state']
            dist = request.POST['city']
            block = request.POST['block']
            vill = request.POST['vill']

            crop_name = request.POST['crop_name']
            crop_variety = request.POST['crop_variety']
            crop_area = request.POST['crop_area']

            start_date = request.POST['start_date']
            end_date = request.POST['end_date']

            newCrop = AddCrop(
                userEmail = userEmail,
                state = state,
                dist = dist,
                block = block,
                vill = vill,
                cropName = crop_name,
                cropVariety = crop_variety,
                cropArea = crop_area,
                startDate = start_date,
                endDate = end_date,
            )

            newCrop.save()

            

        return render(request, 'add_crop.html')
    
    else:

        return render(request, 'login.html')
       
def current_user(request):

    user_id = request.user.email
    print(user_id)

    return HttpResponse(user_id)

def data_filter(request):

    if request.method == "POST":

        state = request.POST['state']
        city = request.POST['city']
        block = request.POST['block']
        vill = request.POST['vill']
        cropName = request.POST['crop_name']

        crop = AddCrop.objects.all().order_by('-startDate')

        if state:
            crop = crop.filter(state=state)

        if city: 
            crop = crop.filter(dist= city)

        if block:
            crop = crop.filter(block = block)
        
        if vill: 
            crop = crop.filter(vill = vill)

        if cropName:
            crop = crop.filter(cropName=cropName)

        # if state and city and block and vill and cropName:
        #     crop = AddCrop.objects.filter(dist=city, state=state,block=block,vill=vill,cropName=cropName).order_by('-startDate')

        # elif state and city and block and cropName:
        #     crop = AddCrop.objects.filter(dist=city, state=state,block=block,cropName=cropName).order_by('-startDate')

        # elif state and city and block and vill:
        #     crop = AddCrop.objects.filter(dist=city, state=state,block=block,vill=vill).order_by('-startDate')

        # elif state and block and vill and cropName:
        #     crop = AddCrop.objects.filter(state=state,block=block,vill=vill,cropName=cropName).order_by('-startDate')

        # elif state and city and cropName:
        #     crop = AddCrop.objects.filter(dist=city, state=state,cropName=cropName).order_by('-startDate') 

        # elif state and city and vill :
        #     crop = AddCrop.objects.filter(dist=city, state=state,vill=vill).order_by('-startDate')

        # elif block and vill and cropName:
        #     crop = AddCrop.objects.filter(block=block,vill=vill,cropName=cropName).order_by('-startDate')

        # elif state and block and cropName:
        #     crop = AddCrop.objects.filter(state=state,block=block,cropName=cropName).order_by('-startDate')

        # elif state and block and vill:
        #     crop = AddCrop.objects.filter(state=state,block=block,vill=vill).order_by('-startDate')

        # elif block and vill:
        #     crop = AddCrop.objects.filter(block=block,vill=vill).order_by('-startDate') 

        # elif block and cropName:
        #     crop = AddCrop.objects.filter(block=block,cropName=cropName).order_by('-startDate')

        # elif vill and cropName:
        #     crop = AddCrop.objects.filter(vill=vill,cropName=cropName).order_by('-startDate')

        # elif state and vill:
        #     crop = AddCrop.objects.filter(state=state,vill=vill).order_by('-startDate')

        # elif state and cropName:
        #     crop = AddCrop.objects.filter(state=state,cropName=cropName).order_by('-startDate') 

        # elif state: 
        #     crop = AddCrop.objects.filter(state=state).order_by('-startDate') 

        # elif cropName:
        #     crop = AddCrop.objects.filter(cropName=cropName).order_by('-startDate') 

        # elif vill: 
        #     crop = AddCrop.objects.filter(vill=vill).order_by('-startDate')

        # elif block:
        #     crop = AddCrop.objects.filter(block=block).order_by('-startDate')

        # else:
        #     crop = ''


        

        totalarea = 0
        for x in crop:
            totalarea = totalarea+x.cropArea
            

        context = {'crop':crop,'area':totalarea,}
        return render(request, 'home.html', context)
    
    return render(request, 'data_filter.html')
from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import karbar
from django.shortcuts import render, redirect
from .forms import karbarform
from io import BytesIO
from django.core.files.storage import default_storage
from PIL import Image
from django.core.files.storage import default_storage
from django.contrib.auth.decorators import login_required
from .forms import homeworkform
from .models import homework
import pyttsx3

def index(request): 
    return render(request, 'index.html')


def a(request):
    return render(request, 'panel_student.html')


def check_login(request):
    phone = request.POST['phone']
    password = request.POST['password']
    if karbar.objects.filter(phone=phone).exists():
        t = karbar.objects.get(phone=phone)
        if t.password == password:
            context = {
                'homeworks': homework.objects.filter(cm=t.cm),
                "karbar": karbar.objects.get(phone=phone)
            }
            return render(request, 'panel_student.html', context)
        else:
            messages.info(request, 'رمز اشتباه است')
            return redirect('panel')
    else:
        messages.info(request, 'کاربری با شماره تلفن درج شده ثبت نشده است')
        return redirect('panel')


def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        lastname = request.POST['fname']
        address = request.POST['address']
        phone = request.POST['phone']
        password = request.POST['password']
        rpassword = request.POST['rpassword']
        email = request.POST['email']
        cm = request.POST['cm']
        if karbar.objects.filter(cm=cm).exists():
            messages.info(request, 'کدملی قبلا به کار رفته است')
            return redirect('register')
        else:
            if karbar.objects.filter(email=email).exists():
                messages.info(request, 'ایمیل قبلا به کار رفته است')
                return redirect('register')
            else:
                if karbar.objects.filter(phone=phone).exists():
                    messages.info(request, 'شماره تلفن قبلا به کار رفته است')
                    return redirect('register')
                else:
                    if password != rpassword:
                        messages.info(request, 'دو رمز وارد شده مشابه نیستند')
                        return redirect('register')
                    else:
                        new_karbar = karbar.objects.create(
                            name=name, lastname=lastname, address=address, phone=phone, password=password, email=email, cm=cm)
                        new_karbar.save()
                        messages.info(request, 'کاربر با موفقیت ثبت نام شد')
                        return redirect('register')
    else:
        return render(request, "register.html")


def panel(request):
    return render(request, "panel_login.html")


def manager(request):
    context = {
        "karbars": karbar.objects.all()
    }
    return render(request, 'manager.html', context)


def delete_accounts(request):
    phone = request.GET['phonekarbar']
    t = karbar.objects.filter()
    t.filter(phone=phone).delete()
    return HttpResponseRedirect('manager')


def settingd(request):
    context = {
        "karbar": karbar.objects.get(phone=request.GET['phonekarbar'])
    }
    return render(request, 'settingd.html', context)


def changename(request):
    phone = request.GET['phonekarbar']
    newname = request.GET['newname']
    fun = request.GET['fun']
    if fun == 'name':
        karbar.objects.filter(phone=phone).update(name=newname)
    else:
        if fun == 'fname':
            karbar.objects.filter(phone=phone).update(lastname=newname)
        else:
            if fun == 'phone':
                if (newname.isnumeric()):
                    karbar.objects.filter(phone=phone).update(phone=newname)
                    phone = newname
            else:
                if fun == 'address':
                    karbar.objects.filter(phone=phone).update(address=newname)
                else:
                    if fun == 'email':
                        karbar.objects.filter(
                            phone=phone).update(email=newname)
                    else:
                        if fun == 'pass':
                            karbar.objects.filter(
                                phone=phone).update(password=newname)
                        else:
                            if fun == 'link':
                                karbar.objects.filter(
                                    phone=phone).update(linkclass=newname)
                            else:
                                if fun == 'cm':
                                    karbar.objects.filter(
                                        phone=phone).update(cm=newname)

    context = {
        "karbar": karbar.objects.get(phone=phone)
    }
    return render(request, 'settingd.html', context)

def unsafe(request):
    return render(request, 'unsafe.html')


def change_profile(request):
    if request.method == 'POST':
        form = karbarform(request.POST, request.FILES)
        cm=request.POST['cm']
        if form.is_valid:
            karbar.objects.get(cm=cm).delete()
            form.save() 
            context = {
                'homeworks': homework.objects.filter(cm=cm),
                "karbar": karbar.objects.get(cm=cm)
            }
            return render(request, 'panel_login.html')
    else:
        cm = request.GET['cm']
        karbar_bycm= karbar.objects.get(cm=cm)
        form = karbarform()
        context = {
            'karbar': karbar_bycm,
            'form': form
        }
        return render(request, 'panel_profile.html', context)


def change_profile1(request):
    image = request.FILES.get('file')
    cm = request.POST['kodemeli']
    if image:
        image_data = image.read()
        image = Image.open(BytesIO(image_data))
    else:
        return HttpResponse("Image not found")
    filename = str(cm)+'.jpg'
    default_storage.save(filename, image)
    karbar.objects.filter(cm=cm).update(profile=image)
    return HttpResponseRedirect('index')


def panel_homework(request):
    if request.method == 'POST':
        form = homeworkform(request.POST, request.FILES)
        cm=request.POST['cm']
        if form.is_valid:
            form.save()
            context = {
                'homeworks': homework.objects.filter(cm=cm),
                "karbar": karbar.objects.get(cm=cm)
            }
            return render(request, 'panel_login.html')
    else:
        cm = request.GET['cm']
        form = homeworkform()
        context = {
            'cm': cm,
            'form': form
        }
        return render(request, 'panel_homework.html', context)


def homework_delete(request):
    url = request.GET['url']
    cm = request.GET['cm']
    url= url[7:]
    print(url)
    homework.objects.get(file=url, cm=cm).delete()
    default_storage.delete(url)
    context = {
        'homeworks': homework.objects.filter(cm=cm),
        "karbar": karbar.objects.get(cm=cm)
    }
    return render(request, 'panel_login.html')

from django.shortcuts import render
from django.views.decorators.cache import cache_control
from .models import Register,contact,donatethings,sharethoughts,pet
from django.http import HttpResponse
from django.views.generic import *
from soul.models import *
from django.shortcuts import render,redirect,get_object_or_404
from django.core.mail import send_mail,BadHeaderError
from django.core.validators import validate_email

# Create your views here.


def homepage(request):
    return render(request,"home.html")


def app(request):
   return render(request,"app.html")


def ngoConsultation(request):
    return render(request, "ngoConsultation.html")


def vetConsultation(request):
    return render(request, "vetConsultation.html")


def login_render(request):
    return render(request, "login_render.html")


#def log(request):
 #   return render(request,"pet_finder.html")


register_success = False
login_success = False
login_s = True
change_success = False

def donate(request):
    if request.method == 'POST':
        if request.POST.get('firstname') and request.POST.get('lastname') \
                and request.POST.get('address') and request.POST.get('country') \
                and request.POST.get('state') and request.POST.get('city') \
                and request.POST.get('email') and request.POST.get('phone') \
                and request.POST.get('message'):
            post = donatethings()
            post.firstname = request.POST.get('firstname')
            post.lastname = request.POST.get('lastname')
            post.address = request.POST.get('address')
            post.country = request.POST.get('country')

            post.state = request.POST.get('state')

            post.city = request.POST.get('city')

            post.email = request.POST.get('email')
            post.phone = request.POST.get('phone')
            post.message=request.POST.get('message')
            post.save()

            try:
                send_mail('Rescue soul',"thank you for your donation. your request has been recieved by us.our team member will soon connect to you at your given address.","gauttamdivisha96@gmail.com",[post.email])
            except BadHeaderError:
                return HttpResponse('invalid header found')
            return redirect("soul:success")


        else:
            return render(request, "fail.html")
    return render(request,"donate_things.html")

def petfinder(request):
    return render(request,"pet_finder.html")

def share(request):
    print("Share")
    saved = False
    if request.method == 'POST':
            post=sharethoughts()
            post.sharetext = request.POST.get('sharetext')
            if 'sharefile' in request.FILES:
                post.sharefile = request.FILES['sharefile']
                print(post.sharetext, post.sharefile)
            else:
                post.sharefile = 'img/bird.jpg'

            post.save()
            saved = True

            return render(request, "login_render.html", {'success':saved})
    return render(request,"login_render.html")


def petfinderform(request):
    if request.method == 'POST':
        if request.POST.get('firstname') and request.POST.get('lastname') \
                and request.POST.get('address') and request.POST.get('country') \
                and request.POST.get('state') and request.POST.get('city') \
                and request.POST.get('email') and request.POST.get('phone') \
                and request.POST.get('message'):
            post = pet()
            post.firstname = request.POST.get('firstname')
            post.lastname = request.POST.get('lastname')
            post.address = request.POST.get('address')
            post.country = request.POST.get('country')

            post.state = request.POST.get('state')

            post.city = request.POST.get('city')

            post.email = request.POST.get('email')
            post.phone = request.POST.get('phone')
            post.message=request.POST.get('message')
            post.save()

            try:
                send_mail('Rescue soul',"we are apreciating your effort "
                "to adobt a soul, we will surely connect you soon. "
                "thank you !!","gauttamdivisha96@gmail.com",[post.email])
            except BadHeaderError:
                return HttpResponse('invalid header found')
            return render(request,"adoptpet.html")


        else:
            return render(request, "f.html")
    return render(request,"adoptpet.html")


def contacts(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('email') \
                and request.POST.get('subject') and request.POST.get('message'):
            post = contact()
            post.name = request.POST.get('name')
            post.email = request.POST.get('email')
            post.subject = request.POST.get('subject')
            post.message=request.POST.get('message')
            post.save()

            return render(request, "contact.html")
        else:
            return render(request, "fail.html")
    return render(request,"contact.html")


def register(request):
    global register_success
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('email') \
                and request.POST.get('password'):
            post = Register()
            post.name = request.POST.get('name')
            post.email = request.POST.get('email')
            post.password = request.POST.get('password')
            post.save()
            register_success = True
            return render(request, "registration.html",
                          {"register_success": register_success})
        else:
            return render(request, "fail.html")
    return render(request,"registration.html")


def update(request):
    global update_users
    u_password = request.POST.get('oldPassword')
    #print(u_password)
    try:
        print("In try")
        update_users = Register.objects.get(email=l_email, password=u_password)
        #print("pass=",update_users)

    except Exception as e:
        print("exception = ",e)
        change_success = False
        return render(request, "fail.html",
                      {"change_success": change_success})

    try:
        if update_users.password == u_password:

        #p = Register()
            new_password = request.POST.get('newPassword')
            Register.objects.all().filter(email= l_email,
            password = u_password).update(password=new_password)
            change_success = True
            return render(request, "success.html",
                          {"change_success": change_success})

    except Exception as e:
        print("2nd Exception = ", e)
        change_success = False
        return render(request, "fail.html",
                      {"change_success": change_success})


def check_login(request):
    global users, l_email, l_password
    if request.method == 'GET':
       # print("In get")
        render(request, "login.html")
    
    else:
        l_email = request.POST.get('email')
        l_password = request.POST.get('password')
        #print(l_email, l_password)
        try:
            print("in try")
            users = Register.objects.get(email=l_email, password=l_password)
            print("users in try= ", users)
        except Exception as e:
            login_success = True
            request.session['username'] = None
            print(e)
            return render(request, "login.html",
                          {"login_success": login_success})

        print(users.email, users.password)

        if users.email == l_email and users.password == l_password:
            request.session['username'] = users.name
            return render(request, "login_render.html",
                          {"username": request.session['username']})

    return render(request, "login.html")


def forgotPage(request):
    return render(request, "forgot_password.html")
def forgot(request):
    global users, f_email , f_pass
    f_email = request.POST.get('email')
    print(f_email)
    users = Register.objects.get(email=f_email)
    print(users)
    print("pass = ",users.password)
    '''if f_email == users.email:
        users=Register.objects.get(password=f_pass)
    try:
            send_mail('Rescue soul',"your password:"+users.email and users.password,"gauttamdivisha96@gmail.com", [users.email])
    except BadHeaderError:
        return HttpResponse('invalid header found')
    return redirect("soul:success")
    return HttpResponse("Hello")
    '''
    try:
        send_mail('Rescue the Soul',
                  "Your new password is "+users.password+". Please, login again and don't "
                  "forget to change your password for the security reasons. Thank You!",
                  "gauttamdivisha96@gmail.com", [users.email])
    except BadHeaderError:
        return HttpResponse('invalid header found')
    pass_success = True
    return render(request, "forgot_password.html",
                  {"pass_success": pass_success})


def success(request):
    return render(request,"success.html")


def changePassword(request):
    return render(request, "changePassword.html")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout(request):
    try:
        del request.session["username"]
        request.session.flush()
    except KeyError:
        pass
    return render(request, "home.html")
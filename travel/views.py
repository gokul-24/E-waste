from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from travel.models import PickUp
from .models import Buy
from .models import ConfirmPickUp,Cart,order,number
# Create your views here.

def is_seller(request):
    dests=Buy.objects.filter(seller=request.user)
    if not dests:
        return False
    else:
        return True

def selling(request):
    x=is_seller(request)
    dests=Buy.objects.filter(seller=request.user)
    return render(request,"destinations.html",{'dests': dests, 'flag1':4, 'x':x})

def selling1(request):
    x=is_seller(request)
    dests=order.objects.filter(seller=request.user)

    return render(request,"destinations.html",{'dests': dests, 'flag1': 5, 'x': x})

def about(request):
    return render(request,"about.html")



def logout(request):
    auth.logout(request)
    return redirect('/')

def destinations(request):
    x=is_seller(request)
    print(x)
    return render(request,"destinations.html",{'x':x})

def destinations1(request):
    dests=Buy.objects.all()
    return render(request,"destinations1.html",{'dests':dests})

def search(request):
    name1=request.POST['name']
    dests=Buy.objects.filter(name__icontains=name1)       
    return render(request,"destinations1.html",{'dests':dests})

def searchseller(request):
    pin1=request.POST['pin1']
    dests=PickUp.objects.filter(Pin=pin1, Buyer="Local")
    return render(request,"destinations.html",{'dests':dests,'flag1':1})

def displaypickup(request):
    if request.user.last_name != "local":
        dests=ConfirmPickUp.objects.filter(Buyer=request.user.last_name)
    else:
        dests=ConfirmPickUp.objects.filter(Buyer=request.user)
    return render(request,"destinations.html",{'dests':dests,'flag1':2})

def pickedup(request):
    id1=request.POST['id1']
    dests=ConfirmPickUp.objects.filter(id=id1).delete()
    return render(request,"destinations.html")

def add(request):
    id1=request.POST['id1']
    dests=PickUp.objects.filter(id=id1)
    for dest in dests:
        dest1=ConfirmPickUp(Name=dest.Name,Phone=dest.Phone,Pin=dest.Pin,Address=dest.Address,Description=dest.Description,Buyer=request.user)
    dest1.save()
    dests.delete()
    return render(request,"destinations.html")

def addToCart(request):
    if request.user.is_authenticated:
        id1=request.POST['id1']
        dests=Buy.objects.filter(id=id1)
        for dest in dests:
            dest1=Cart(name=dest.name,img=dest.img,desc=dest.desc,price=dest.price,seller=dest.seller,buyer=request.user)
        dest1.save()
        dests=Buy.objects.all()
        return render(request,"destinations1.html",{'dests':dests})
    else:
        messages.info(request,"Login To Continue")
        return redirect('destinations1')

def doro(request):
    if 'btn1' in request.POST:
        id1=request.POST['id1']
        dest=Cart.objects.filter(id=id1).delete()
    else:
        id1=request.POST['id1']
        dests=Cart.objects.filter(id=id1)
        n1=number.objects.filter(username=request.user)
        for d in n1:
            num=d.phone
        for dest in dests:
            des=order(name=dest.name,img=dest.img,desc=dest.desc,price=dest.price,seller=dest.seller,buyer=request.user,number=num)
        des.save()
        dests=Cart.objects.filter(id=id1).delete()
    return redirect('http://127.0.0.1:8000/displaycart')

def displayorder(request):
    x=is_seller(request)
    dests=order.objects.filter(buyer=request.user)
    return render(request,"destinations.html",{'dests':dests,'flag1':3,'x':x})

def cancelorder(request):
    id1=request.POST['id1']
    dests=order.objects.filter(id=id1).delete()
    return redirect('displayorder')
def confirm(request):
    id1=request.POST['id1']
    dests=order.objects.filter(id=id1).delete()
    return redirect('http://127.0.0.1:8000/selling1')

def displaycart(request):
    x=is_seller(request)
    dests=Cart.objects.filter(buyer=request.user)
    return render(request,"destinations.html",{'dests':dests,'flag1':0,'x':x})
def index(request):
    return render(request,"index1.html.html")
def request(request):
    d={'Junkart':[1,11222,12234,231234,453456],
    'Crapbin':[2,21321,12321321,2323213,23433],
    'ScrapQ':[3,3454365,4324,4323,234],
    'Local':[4,345,34543,23423],
    }
    if request.method=="POST":
        username1=request.user
        name1=request.POST['name']
        phone1=request.POST['number']
        phone1=int(phone1)
        pin1=request.POST['pin']
        address1=request.POST['address']
        description1=request.POST['description']
        buyer1=request.POST['cars']
        if buyer1 != "Local":
            if int(pin1) in d[buyer1]:
                pick=ConfirmPickUp(Name=name1,Phone=phone1,Pin=pin1,Address=address1,Description=description1,Buyer=buyer1)
                pick.save()
                messages.info(request,"pick up confirmed")
                return redirect('/')
            else:
                messages.info(request,"Selected Buyer Not Available in that area")
                return redirect('request')
        else:
            if int(pin1) in d[buyer1]:
                pick=PickUp(Username=username1,Name=name1,Phone=phone1,Pin=pin1,Address=address1,Description=description1,Buyer=buyer1) 
                pick.save()
                messages.info(request,"pick up confirmed")
                return redirect('/')
            else:
                messages.info(request,"Selected Buyer Not Available in that area")
                return redirect('request')
    else:
        if request.user.is_authenticated:
            return render(request,"request.html")
        else:
            messages.info(request,"Login To Continue")
            return redirect('/')
def login(request):
    if request.method == "POST":
        email=request.POST['email']
        password3=request.POST['password']
        if(email=="" or password3==""):
            messages.info(request,"fill all the details")
        user1=auth.authenticate(username=email,password=password3)
        if user1 is not None:
            auth.login(request,user1)
            messages.info(request,"logged in")
            return redirect('/')
        else:
            messages.info(request,"invalid details")
            return redirect('login')
    else:
        return render(request,"login.html")
def signup(request):
    if request.method == "POST":
        email= request.POST['email']
        username=request.POST['name']
        phone=request.POST['phone']
        p1=request.POST['password1']
        p2=request.POST['password2']
        if email=="" or username=="" or p1=="" or p2=="":
            messages.info(request,"enter all fields")
            return redirect('/login')
        if p1==p2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already taken")
                return redirect('/login')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already taken")
                return redirect('/login')
            else:
                user=User.objects.create_user(username=username,password=p1,email=email)
                user.save()
                n1=number(username=username,phone=phone)
                n1.save()
                messages.info(request,"User Created")
                return redirect('login')
        else:
            messages.info(request,"Passwords doesnt match")
            return redirect('login')

    else:
        return render(request,"login.html")



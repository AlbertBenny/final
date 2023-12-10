from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.contrib.auth import authenticate,login,logout
from . models import *
from django.db.models import Q
from django.core.paginator import Paginator
from django.core import paginator







# Create your views here.


def getform(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        cpassword = request.POST.get("confirmpassword")
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                return redirect('home')
            else:
                user=User.objects.create_user(username=username, email=email, password=password )
                user.save()
                return redirect('log')
        else:
            messages.info(request,"password incorrect")
            return redirect('register.html')

    return render(request, "register.html")


def log(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'invalid user')
            return redirect('getform')
    return render(request,"login.html")
def out(request):
    logout(request)
    return redirect('getform')


def shop(request):
    k = Product.objects.all()
    p = Paginator(k, 8)
    page_num = request.GET.get("page")
    data_obj = p.get_page(page_num)
    return render(request,"shop.html",{'data':data_obj,'p':p,'k':k})

def about(request):
    return render(request,"about.html")
def service(request):
    return render(request,"service.html")

def discrption(request):
    return render(request,'discription.html')


def click(request,do):
    l = Product.objects.filter(id=do)
    return render(request,'view.html',{'flower':l})



def add(request,did):

    m = Product.objects.get(id=did)
    n,s = Cart_User.objects.get_or_create(user=request.user)
    if Cart.objects.filter(user=n,product=m).exists():
        cart = Cart.objects.get(user=n,product=m)
        cart.quantity += 1
        cart.save()
    else:

        cart = Cart(quantity=1, user=n, product=m)
        cart.save()

    return redirect('showcart')

def minus(request,did):
    m = Product.objects.get(id=did)
    n = Cart_User.objects.get(user=request.user)
    cart = Cart.objects.get(user=n, product=m)
    cart.quantity -= 1
    cart.save()
    return redirect('showcart')

@login_required(login_url='/log')
def show_cart(request):
    sum = 0
    count = 0
    try:
        h = Cart_User.objects.get(user=request.user)
        n = Cart.objects.filter(user=h.id)
        for i in n:
            sum += i.quantity * i.product.price
            count += 1

    except:
        messages.info("no product were added to your cart")
        return redirect(request, "home.html")


    return render(request, 'cart.html', {'tab': n, 'sum': sum, 'count': count})


def delete(request,dlt):
    Cart.objects.get(id=dlt).delete()


    return redirect('showcart')
def home(request):
    product = Catagory.objects.all()
    return render(request,"home.html", {'catagory': product})
def catagory(request,done):
    p = Product.objects.filter(catagory=done)
    return render(request, "catagory.html",{'db': p})

def search(request):
    b = None
    if 'word' in request.GET:
        w = request.GET['word']
        b = Product.objects.all().filter(Q(name__icontains=w) | Q(discription__icontains=w))
        print(("search", w))

    return render(request,"search.html", {'data': b})


def billing(request):
    # adding product to checkout page

    n=None
    sum = 0
    h = Cart_User.objects.get(user=request.user)
    n = Cart.objects.filter(user=h)
    for i in n:
        sum += (i.quantity * i.product.price)
    return render(request, 'checkout.html', {'lap': n,'sum': sum})



def demo(request):
    if request.method == 'POST':
        new_order = Billing()
        new_order.country = request.POST.get('country')
        new_order.first_name = request.POST.get('firstname')
        new_order.last_name = request.POST.get('lastname')
        new_order.address = request.POST.get('address')
        new_order.email = request.POST.get('email')
        new_order.state = request.POST.get('state')
        new_order.postal = request.POST.get('postal')
        new_order.phone = request.POST.get('phone')
        p = Cart_User.objects.get(user=request.user)
        cart = Cart.objects.filter(user=p)
        cart_total = 0
        for item in cart:
            cart_total += item.product.price * item.quantity

        new_order.sub_total = cart_total
        new_order.save()

        w = Cart_User.objects.get(user=request.user)
        cart_user = Cart.objects.filter(user=w)

        for item in cart_user:
            Item_order.objects.create(
                product_name=item.product,
                price=item.product.price,
                quantity=item.quantity,
                order=new_order)
            order_product = Product.objects.filter(id=item.product_id).first()
            order_product.stock = order_product.stock - item.quantity
            order_product.save()




    c = Cart_User.objects.get(user=request.user)
    cart_new = Cart.objects.filter(user=c).delete()
    messages.success(request,"order has successfully added")
    return redirect('billing')



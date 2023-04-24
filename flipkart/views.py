from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
from . models import *

from django.contrib.auth.hashers import check_password,make_password

def index(request):
    if request.method =='POST':
       
        product_id = request.POST.get("cartid")
        remove = request.POST.get("minus")
        # print('product id value',product_id)

        cart_id =request.session.get('cart')

        # print('initally cart_id value',cart_id)

        if cart_id:
            quantity = cart_id.get(product_id)
            if quantity:
                cart_id[product_id] = quantity+1  
                if remove:
                    if quantity <=1:
                        cart_id.pop(product_id)
                    else:
                        cart_id[product_id] = quantity -1
                else:
                    cart_id[product_id] = quantity +1 
                    
            else:
                cart_id[product_id] = 1
        else:
            cart_id={}
            cart_id[product_id] = 1
        request.session['cart'] = cart_id
        print(request.session['cart'])



    catid =request.GET.get('cat_id')
    pr_name = request.GET.get('name')


    category_info = Category.objects.all()
    if catid:
        product_info = Product.objects.filter(Category=catid)
    else:
        product_info = Product.objects.all()

    if pr_name:
        product_info =Product.objects.filter(pro_name=pr_name)
    
    # product_info = Product.objects.all()
    context ={
        'category': category_info,
        'product' : product_info,
    }
    return render(request,'home.html',context=context)

def contact(request):
    return render(request,'contact.html')

def Singup(request):
    if request.method == "POST":
        f_name= request.POST.get("fname")
        l_name= request.POST.get("lname")
        email= request.POST.get("email")
        password= request.POST.get("pwd")
        mobile= request.POST.get("mobile")
        gender= request.POST.get("gender")

        c_obj =Registration(
            first_name = f_name,
            last_name = l_name,
            email = email,
            password = make_password(password),
            mobile = mobile,
            gender = gender,

        )
        c_obj.save()
        # return HttpResponse("Registration Successful")
        return redirect('home')

    
    
def Login(request):
    if request.method == "POST":
        email_id = request.POST.get("emailid")
        password = request.POST.get("password")

        
    try:
        fetch_email = Registration.objects.get(email = email_id)
        print(fetch_email)
        print(check_password(password,fetch_email.password))
        if check_password(password,fetch_email.password):
            # return HttpResponse("Login succesfull")
            request.session['name']= fetch_email.first_name
            request.session['customer_id']= fetch_email.id
            return redirect('home')
        
        else:
            return HttpResponse("Wrong Password")
    except:
        return HttpResponse("Email id doesn't exists")
    

def Logout(request):
    request.session.clear()
    return redirect('home')

def cart_detials(request):
    
    try:
        error = None
        ids = list(request.session.get("cart").keys())
        prod_dtls= Product.objects.filter(id__in=ids)
    except:
        error ="Please add Some product"
        prod_dtls = None
    # prod_dtls ="please add product"
    # if request.session.get('cart'):
    # cart_info = list(request.session.get('cart').keys())
    # prod_dtls = Product.objects.filter(id__in = cart_info)
        
    return render(request,'cart.html',{'prod_dtls':prod_dtls})

def checkout(request):
    if  request.method == "POST":
        address= request.POST.get('address')
        mobile = request.POST.get('mobile')

        customer_id = request.session.get('customer_id')
        if not customer_id:
            return HttpResponse("please login")
        cart = request.session.get('cart')
        product =Product.objects.filter(id__in = list(cart))

        for p in product:
            Order_info= Order(
                address =address,
                mobile =mobile,
                price =p.price,
                Product=p,
                quantity= cart.get (str(p.id)),
                customer= Registration(id =customer_id),
            )
            Order_info.save()
        # request.session.cart={}
            request.session['cart']={}
            return redirect('order')
    
def Order_dtls(request):
    order_dtls= Order.objects.all()
    tp = 0
    for t in order_dtls:
        tp =tp + (t.price * t.quantity)
    return render( request,'order.html', {'ord_dtls': order_dtls,'tp':tp})



from .Serialization import RegSerializer
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    queryset =  Registration.objects.all()
    serializer_class =  RegSerializer

        


    



       

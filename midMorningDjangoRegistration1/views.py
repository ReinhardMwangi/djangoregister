from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from .models import Product

def register(request) :
    if  request.method == "POST" :
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('register')
    else:
        form = UserRegistrationForm()

    return render (request, 'register.html', {'form':form})

@login_required
def home (request) :
    return render (request,'home.html')

@login_required
def add_product (request) :
    #check if form submitted has a method post
    if request.method == 'POST' :
        #start receiving data from the form
        p_name = request.POST.get('jina')
        p_quantity = request.POST.get('kiasi')
        p_price = request.POST. get ('bei')

        #finally save data in our table called products
        product = Product(prod_name = p_name, prod_quantity=p_quantity,prod_price=p_price)

        product.save()

        #Redirect back with a success message
        messages.success(request, 'Product Saved Successfully')
        return redirect('add-product')
    return render(request,'addproducts.html')

@login_required
def delete_product(request, id):
    #Fetch the product to be deleted
    product = Product.objects.get(id=id)
    #delete the product
    product.delete()
    #redirect back to products page with a success messages
    messages.success(request, 'Product deleted successfully')
    return redirect('product')

@login_required
def view_products(request) :
    #select all the products to be displayed
    products = Product.objects.all()
    return render (request, 'products.html',{'products' : products})

@login_required
def update_product(request, id):
    #Fetch the product to be updated
    product = Product.objects.get(id=id)
    #Check if the form submitted has a method post
    if request.method =="POST":
        # Receive data from the form
        updated_name = request.POST.get('jina')
        updated_quantity = request.POST.get('kiasi')
        updated_price = request.POST.get('bei')

        # Updated the product with the received updated data
        product.prod_name = updated_name
        product.prod_quantity = updated_quantity
        product.prod_price = updated_price

        #Return the data back to the database and redirect back
        #to products page with a success message
        product.save()
        messages.success(request, 'Product updated successfully ')
        return redirect('product')
    return render(request, 'updateproduct.html', {'product': product})

@login_required
def register_supplier(request):
        #check if form submitted has a method post
    if request.method == 'POST' :
        #start receiving data from the form
        p_name = request.POST.get('jina')
        p_email = request.POST.get('email')
        p_phone = request.POST.get('nambari')
        p_product = request.POST. get ('bidhaa')

        #finally save data in our table called products
        product = Product(prod_name = p_name, prod_email=p_email,prod_phone=p_phone,prod_product=p_product)

        product.save()

        #Redirect back with a success message
        messages.success(request, 'Supplier Saved Successfully')
        return redirect('supplier')
    return render(request, 'supplier.html')



@login_required
def payment(request, id):
    # select the product to be paid
    product = Product.objects.get(id=id)
    return render(request, 'payment.html', {'product': product})

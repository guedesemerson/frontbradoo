from django.shortcuts import render, redirect
from .forms import ProductForm
import requests

def listProduct(request, id):
    form = ProductForm()
    products = requests.get('https://bradooapi.herokuapp.com/api/product/?vendor='+id)
    product = products.json()

    return render(request, 'product/list_product.html',{'product':product, 'form':form, 'vendorid':id})

def newProduct(request, id):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        product = {"name": request.POST['name'], "code": request.POST['code'], "price": request.POST['price'],
                  "vendor": id }
        requests.post('https://bradooapi.herokuapp.com/api/product/', json = product)
        products = requests.get('https://bradooapi.herokuapp.com/api/product/?vendor='+id)
        product = products.json()

        form = ProductForm()
    return render(request, 'product/list_product.html', {'product': product, 'form': form, 'vendorid': id})


def ProductDelete(request, id):
    form = ProductForm()

    vendor = requests.get('https://bradooapi.herokuapp.com/api/product/'+id)
    vendor = vendor.json()
    vendorid = str(vendor['vendor'])

    requests.delete('https://bradooapi.herokuapp.com/api/product/'+id)

    products = requests.get('https://bradooapi.herokuapp.com/api/product/?vendor='+vendorid)
    products = products.json()



    return render(request, 'product/list_product.html', {'product': products, 'form': form, 'vendorid': vendorid})

def updateProduct(request, id):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        vendor = requests.get('https://bradooapi.herokuapp.com/api/product/'+id)
        vendor = vendor.json()

        vendorid = str(vendor['vendor'])

        vendor = {"name": request.POST['name'], "code": request.POST['code'], "price": request.POST['price'],"vendor":vendorid}

        requests.put('https://bradooapi.herokuapp.com/api/product/'+id+'/', data = vendor)

        products = requests.get('https://bradooapi.herokuapp.com/api/product/?vendor='+vendorid)
        products = products.json()

        form = ProductForm()
        return render(request,'product/list_product.html',{'product': products, 'form': form, 'vendorid': vendorid})


    return redirect('vendors')



def formUpdateProduct(request, id):
    response = requests.get('https://bradooapi.herokuapp.com/api/product/'+id)
    response =response.json()


    response = {"name": response['name'], "code": response['code'], "price": response['price']}

    form = ProductForm(response or None)

    return render(request, 'product/form_product.html', {'form': form, 'productid':id})


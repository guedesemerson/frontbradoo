from django.shortcuts import render, redirect
from .forms import VendorForm
import requests

def listVendor(request):

    response = requests.get('https://bradooapi.herokuapp.com/api/vendor/')
    response = response.json()

    return render(request, 'core/main.html',{'vendor':response})

def updateVendor(request, id):
    form = VendorForm(request.POST or None)
    if form.is_valid():
        vendor = {"name": request.POST['name'], "cnpj": request.POST['cnpj'], "city": request.POST['city']}

        result = requests.put('https://bradooapi.herokuapp.com/api/vendor/'+id+'/', data = vendor)
        if result.status_code == 201:
            return redirect('vendors')


    return redirect('vendors')



def formUpdateVendor(request, id):
    response = requests.get('https://bradooapi.herokuapp.com/api/vendor/'+id)
    response =response.json()

    response = {"name": response['name'], "cnpj": response['cnpj'], "city": response['city']}
    vendorid = id
    form = VendorForm(response or None)

    return render(request, 'vendor/form_update.html', {'form': form, 'vendorid':vendorid})



def formNewVendor(request):
    form = VendorForm()
    return render(request, 'vendor/add_vendor.html', {'form': form})

def newVendor(request):
    form = VendorForm(request.POST or None)
    if form.is_valid():
        vendor = {"name":request.POST['name'], "cnpj":request.POST['cnpj'], "city":request.POST['city'], "products":[]}
        result = requests.post('https://bradooapi.herokuapp.com/api/vendor/', json = vendor )
        if result.status_code == 201:
            return redirect('vendors')

    return redirect('formvendor')


def vendorDelete(request, id):
    requests.delete('https://bradooapi.herokuapp.com/api/vendor/'+id+'/')
    return redirect('vendors')


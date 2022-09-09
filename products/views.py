from django.shortcuts import render, redirect
from  django.http import  HttpResponse
from products.models import  Product
# Create your views here.
from products.forms import ProductForm
from django.views.generic.edit import UpdateView, CreateView


def index(request):
    products = Product.objects.all()
    return  render(request, "products/index.html", context={"products":products})



def show(request, id):
    product = Product.objects.get(pk=id)
    # return HttpResponse(product)
    print(product.get_show_url())
    return  render(request, "products/show.html", context={"product":product})



def delete(request, id):
    product = Product.objects.get(pk=id)
    product.delete()
    return redirect("/products")


#
# def createproduct(request):
#     # request may be get request
#     if request.POST:
#         # return HttpResponse("POST request ")
#         # I want to get the data received with the request ?
#         # return HttpResponse(request.POST["name"])
#         product = Product()
#         product.name = request.POST["name"]
#         product.image = request.POST["image"]
#         product.no_of_items = request.POST["no_of_items"]
#         product.description = request.POST["description"]
#         product.save()
#         return redirect('/products')
#
#     myform = ProductForm()
#     return render(request, "products/create.html", context={"form":myform})
#
# #####################################
#
# # ## class based views ---> to edit
#

class UpdateProductView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name ='products/edit.html'
    success_url = "/products"



class CreateProductView(CreateView):
    model = Product
    form_class = ProductForm
    template_name ='products/create.html'
    success_url = "/products"










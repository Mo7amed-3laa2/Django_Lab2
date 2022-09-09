# here I will the urls related to products

from django.urls import path
from products.views import index,show, delete, UpdateProductView, CreateProductView
urlpatterns = [
        path("", index, name="products.index"),          # if usr hit http://127.0.0.1:8000/products/ will go to index.html
        path("<int:id>", show, name= "products.show"),   # will go to show.html
        path("delete/<id>", delete, name ='products.delete'),
        # path("create", createproduct, name='products.create'),
        path("edit/<int:pk>", UpdateProductView.as_view(), name="products.edit"),
        path("create", CreateProductView.as_view(), name="products.create")

]

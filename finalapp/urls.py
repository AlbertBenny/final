from django.urls import path
from . import views


urlpatterns = [



    path('getform/',views.getform,name="getform"),

    path('log/',views.log,name="log"),
    path('logout/',views.out,name="logout"),
    path('shop/',views.shop,name="shop"),

    path('about/',views.about,name="about"),
    path('service/',views.service,name="service"),
    path('click/<int:do>/?',views.click,name="click"),
    path('discription/',views.discrption,name="discription"),
    path('add/<int:did>',views.add,name="add"),
    path('minus/<int:did>',views.minus,name="minus"),
    path('delete/<int:dlt>',views.delete,name="delete"),
    path('home/',views.home,name="home"),
    path('catagory/<int:done>',views.catagory,name="catagory"),
    path('search/',views.search,name="search"),
    path('show_cart/',views.show_cart,name="showcart"),
    path('billing/',views.billing,name="billing"),
    path('demo/',views.demo,name="demo")

]
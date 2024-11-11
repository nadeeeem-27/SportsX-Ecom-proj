from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register_view,name='register'),
    path('football/',views.football,name='football'),
    path('basketball/',views.basketball,name='basketball'),
    path('product/<int:pk>',views.product,name='product'),
    path('allproducts/',views.allproducts,name='allproducts'),
    path('update_info/',views.update_info,name='update_info'),
]
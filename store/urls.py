from django.urls import path
from rest_framework.authtoken import views as authview

from . import views

urlpatterns = [

    #Authentication URL
    path('login', authview.obtain_auth_token),

    #Customer URLs
    path('customer/list', views.CustomerList.as_view()),
    path('customer/search', views.CustomerSearch.as_view()),
    path('customer/add', views.CustomerAdd.as_view()),
    path('customer/<str:id>', views.CustomerSelect.as_view()),

    #Customer Transaction URLs
    path('customer/<str:cid>/transaction/list', views.TransactionList.as_view()),
    path('customer/<str:cid>/transaction/add', views.TransactionAdd.as_view()),
    path('customer/<str:cid>/transaction', views.TransactionSelect.as_view()),

    #Product URLs
    path('product/list', views.ProductList.as_view()),
    path('product/search', views.ProductSearch.as_view()),
    path('product/add', views.ProductAdd.as_view()),
    path('product/<str:code>', views.ProductSelect.as_view()),

    #Product Review URLs
    path('product/<str:code>/review/list', views.ProductReviewList.as_view()),
    path('product/<str:code>/review/add', views.ProductReviewAdd.as_view()),
    path('product/<str:code>/review', views.ProductReviewSelect.as_view()),

    #Game URLs
    path('game/list', views.GameList.as_view()),
    path('game/add', views.GameAdd.as_view()),
    path('game/<str:code>',views.GameSelect.as_view()),

    #DLC URLs
    path('dlc/list', views.DLCList.as_view()),
    path('dlc/add', views.DLCAdd.as_view()),
    path('dlc/<str:code>',views.DLCSelect.as_view()),

    #Bundle URLs
    path('bundle/list', views.BundleList.as_view()),
    path('bundle/add', views.BundleAdd.as_view()),
    path('bundle/<str:code>',views.BundleSelect.as_view()),

    #Promotion URLs
    path('promotion/list', views.PromotionList.as_view()),
    path('promotion/add', views.PromotionAdd.as_view()),
    path('promotion/<str:code>', views.PromotionSelect.as_view()),

    #Employee URLs
    path('employee/list', views.EmployeeList.as_view()),
    path('employee/add', views.EmployeeAdd.as_view()),
    path('employee/<str:code>', views.EmployeeSelect.as_view()),


]
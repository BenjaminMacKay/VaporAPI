from msilib.schema import Class
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from store.apps import *
from store.models import *
from store.serializers import *

for user in User.objects.all():
    Token.objects.get_or_create(user=user)

## CUSTOMER VIEWS ##

class CustomerList(APIView):
    def get(self, request, format=None):
        customers = Customer.objects.all()
        s = CustomerSerializer(customers, many=True)
        return Response (s.data)

class CustomerSearch(APIView):
    def get(self, request, format=None):
        customers = Customer.objects.filter(username__contains = request.data["username"])
        s = CustomerSerializer(customers, many=True)
        return Response (s.data)

class CustomerSelect(APIView):
    def get(self, request, id, format=None):
        customers = Customer.objects.get(customer_id = id)
        s = CustomerSerializer(customers)
        return Response (s.data)

    def put(self, request, id, format=None):
        customer = Customer.objects.get(customer_id = id)
        s = CustomerSerializer(customer, data=request.data, partial=True)
        if s.is_valid():
            s.save()
            return Response (s.data, status=status.HTTP_200_OK)
        else:
            return Response (s.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        customer = Customer.objects.get(customer_id = id)
        customer.delete()
        return Response (status=status.HTTP_204_NO_CONTENT)

class CustomerAdd(APIView):
    def post(self, request, format=None):
        s = CustomerSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response (s.data, status=status.HTTP_201_CREATED)
        else:
            return Response (s.errors, status=status.HTTP_400_BAD_REQUEST)


## PRODUCT VIEWS ##

class ProductList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        s = ProductSerializer(products, many=True)
        return Response (s.data)

class ProductSearch(APIView):
    def get(self, request, format=None):
        products = Product.objects.filter(title__contains = request.data["title"])
        s = ProductSerializer(products, many=True)
        return Response (s.data)

class ProductAdd(APIView):
    def post(self, request, format=None):
        s = ProductSerializer(data=(request.data))
        if s.is_valid():
            s.save()
            return Response (s.data, status=status.HTTP_201_CREATED)
        else:
            return Response (s.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductSelect(APIView):
    def get(self, request, code, format=None):
        products = Product.objects.get(item_code = code)
        s = ProductSerializer(products)
        return Response (s.data)

    def put(self, request, code, format=None):
        product = Product.objects.get(item_code = code)
        s = ProductSerializer(product, data=request.data, partial=True)
        if s.is_valid():
            s.save()
            return Response (s.data, status=status.HTTP_200_OK)
        else:
            return Response (s.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, code, format=None):
        product = Product.objects.get(item_code = code)
        product.delete()
        return Response (status=status.HTTP_204_NO_CONTENT)

class ProductReviewList(APIView):
    def get(self, request, code, format=None):
        reviews = Review.objects.filter(item_code=code)
        s = ReviewSerializer(reviews, many=True)
        return Response (s.data)

class ProductReviewAdd(APIView):
    def post(self, request, code, format=None):
        request.data["item_code"] = code
        s = ReviewSerializer(data=(request.data))
        if s.is_valid():
            s.save()
            return Response (s.data, status=status.HTTP_201_CREATED)
        else:
            return Response (s.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductReviewSelect(APIView):
    def get(self, request, code, format=None):
        review = Review.objects.filter(item_code = code).get(cid=request.data["cid"])
        s = ReviewSerializer(review)
        return Response (s.data)

    def put(self, request, code, format=None):
        review = Review.objects.filter(item_code = code).get(cid=request.data["cid"])
        s = ReviewSerializer(review, data=request.data, partial=True)
        if s.is_valid():
            s.save()
            return Response (s.data, status=status.HTTP_200_OK)
        else:
            return Response (s.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, code, format=None):
        review = Review.objects.filter(item_code = code).get(cid=request.data["cid"])
        review.delete()
        return Response (status=status.HTTP_204_NO_CONTENT)

## GAME VIEWS ##

class GameList(APIView):
    def get(self, request, format=None):
        games = Game.objects.all()
        s = GameSerializer(games, many=True)
        return Response (s.data)

class GameAdd(APIView):
    def post(self, request, format=None):
        s = GameSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response (s.data, status=status.HTTP_201_CREATED)
        else:
            return Response (s.errors, status=status.HTTP_400_BAD_REQUEST)

class GameSelect(APIView):
    def get(self, request, code, format=None):
        game = Game.objects.get(item_code = code)
        s = GameSerializer(game)
        return Response (s.data)

    def put(self, request, code, format=None):
        game = Game.objects.get(item_code = code)
        s = GameSerializer(game, data=request.data, partial=True)
        if s.is_valid():
            s.save()
            return Response (s.data, status=status.HTTP_200_OK)
        else:
            return Response (s.errors, status=status.HTTP_400_BAD_REQUEST)

## DLC VIEWS ##

class DLCList(APIView):
    def get(self, request, format=None):
        dlc = DLC.objects.all()
        s = DLCSerializer(dlc, many=True)
        return Response (s.data)

class DLCAdd(APIView):
    def post(self, request, format=None):
        s = DLCSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response (s.data, status=status.HTTP_201_CREATED)
        else:
            return Response (s.errors, status=status.HTTP_400_BAD_REQUEST)

class DLCSelect(APIView):
    def get(self, request, code, format=None):
        dlc = DLC.objects.get(product_code = code)
        s = DLCSerializer(dlc)
        return Response (s.data)

    def put(self, request, code, format=None):
        dlc = DLC.objects.get(product_code = code)
        s = DLCSerializer(dlc, data=request.data, partial=True)
        if s.is_valid():
            s.save()
            return Response (s.data, status=status.HTTP_200_OK)
        else:
            return Response (s.errors, status=status.HTTP_400_BAD_REQUEST)

## BUNDLE VIEWS ##

class BundleList(APIView):
    def get(self, request, format=None):
        bundle = Bundle.objects.all()
        s = BundleSerializer(bundle, many=True)
        return Response (s.data)

class BundleAdd(APIView):
    def post(self, request, format=None):
        s = BundleSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response (s.data, status=status.HTTP_201_CREATED)
        else:
            return Response (s.errors, status=status.HTTP_400_BAD_REQUEST)

class BundleSelect(APIView):
    def get(self, request, code, format=None):
        bundle = Bundle.objects.get(item_code = code)
        s = BundleSerializer(bundle)
        return Response (s.data)

    def put(self, request, code, format=None):
        bundle = Bundle.objects.get(item_code = code)
        s = BundleSerializer(bundle, data=request.data, partial=True)
        if s.is_valid():
            s.save()
            return Response (s.data, status=status.HTTP_200_OK)
        else:
            return Response (s.errors, status=status.HTTP_400_BAD_REQUEST)

## PROMOTION VIEWS ##

class PromotionList(APIView):
    def get(self, request, format=None):
        promotion = Promotion.objects.all()
        s = PromotionSerializer(promotion, many=True)
        return Response (s.data)

class PromotionAdd(APIView):
    def post(self, request, format=None):
        s = PromotionSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response (s.data, status=status.HTTP_201_CREATED)
        else:
            return Response (s.errors, status=status.HTTP_400_BAD_REQUEST)

class PromotionSelect(APIView):
    def get(self, request, code, format=None):
        promotion = Promotion.objects.get(id = code)
        s = PromotionSerializer(promotion)
        return Response (s.data)

    def put(self, request, code, format=None):
        promotion = Promotion.objects.get(id = code)
        s = PromotionSerializer(promotion, data=request.data, partial=True)
        if s.is_valid():
            s.save()
            return Response (s.data, status=status.HTTP_200_OK)
        else:
            return Response (s.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, code, format=None):
        promotion = Promotion.objects.get(id = code)
        promotion.delete()
        return Response (status=status.HTTP_204_NO_CONTENT)

## EMPLOYEE VIEWS ##

class EmployeeList(APIView):
    def get(self, request, format=None):
        employee = Employee.objects.all()
        s = EmployeeSerializer(employee, many=True)
        return Response (s.data)

class EmployeeAdd(APIView):
    def post(self, request, format=None):
        s = EmployeeSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response (s.data, status=status.HTTP_201_CREATED)
        else:
            return Response (s.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeSelect(APIView):
    def get(self, request, code, format=None):
        employee = Employee.objects.get(id = code)
        s = EmployeeSerializer(employee)
        return Response (s.data)

    def put(self, request, code, format=None):
        employee = Employee.objects.get(id = code)
        s = EmployeeSerializer(employee, data=request.data, partial=True)
        if s.is_valid():
            s.save()
            return Response (s.data, status=status.HTTP_200_OK)
        else:
            return Response (s.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, code, format=None):
        employee = Employee.objects.get(id = code)
        employee.delete()
        return Response (status=status.HTTP_204_NO_CONTENT)

## TRANSACTION VIEWS (To be used under customer)##

class TransactionList(APIView):
    def get(self, request, cid, format=None):
        transactions = Transaction.objects.filter(customer_id=cid)
        s = TransactionSerializer(transactions, many=True)
        return Response (s.data)

class TransactionAdd(APIView):
    def post(self, request, cid, format=None):
        request.data["customer_id"] = cid
        s = TransactionSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response (s.data, status=status.HTTP_201_CREATED)
        else:
            return Response (s.errors, status=status.HTTP_400_BAD_REQUEST)

class TransactionSelect(APIView):

    def delete(self, request, cid, format=None):
        transaction = Transaction.objects.filter(customer_id = cid).get(item_code = request.data["item_code"])
        transaction.delete()
        return Response (status=status.HTTP_204_NO_CONTENT)


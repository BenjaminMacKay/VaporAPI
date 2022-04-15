from rest_framework import serializers
from store.models import *

class CustomerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Customer
		fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = '__all__'

class GameSerializer(serializers.ModelSerializer):
	class Meta:
		model = Game
		fields = '__all__'

class DLCSerializer(serializers.ModelSerializer):
	class Meta:
		model = DLC
		fields = '__all__'

class BundleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Bundle
		fields = '__all__'

class PromotionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Promotion
		fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Employee
		fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Transaction
		fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
	class Meta:
		model = Review
		fields = '__all__'

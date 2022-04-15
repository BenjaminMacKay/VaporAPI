from django.db import models
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)       
    name = models.CharField(max_length=30)
    username = models.CharField(unique=True, max_length=30)
    address = models.TextField()
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'customer'


class DLC(models.Model):
    game_code = models.OneToOneField('Game', models.DO_NOTHING, db_column='game_code', primary_key=True)
    product_code = models.ForeignKey('Product', models.DO_NOTHING, db_column='product_code')
    dlc_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'dlc'
        unique_together = (('game_code', 'product_code'),)


class Employee(models.Model):
    name = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    hours = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'employees'


class Game(models.Model):
    item_code = models.OneToOneField('Product', models.DO_NOTHING, db_column='item_code', primary_key=True)
    developer = models.CharField(max_length=30)
    publisher = models.CharField(max_length=30)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'game'

class Bundle(models.Model):
    item_code = models.OneToOneField('Product', models.DO_NOTHING, db_column='item_code', primary_key=True)
    prod_code1 = models.ForeignKey('Product', models.DO_NOTHING, db_column='prod_code1', related_name='prod1')
    prod_code2 = models.ForeignKey('Product', models.DO_NOTHING, db_column='prod_code2', related_name='prod2')
    products = models.TextField()

    class Meta:
        managed = False
        db_table = 'bundle'

class Product(models.Model):
    item_code = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'product'


class Promotion(models.Model):
    item_code = models.ForeignKey(Product, models.DO_NOTHING, db_column='item_code')
    discount = models.DecimalField(max_digits=10, decimal_places=0)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'promotion'


class Review(models.Model):
    item_code = models.OneToOneField(Game, models.DO_NOTHING, db_column='item_code')
    review = models.TextField()
    cid = models.OneToOneField(Customer, models.DO_NOTHING, db_column='cid', primary_key=True)

    class Meta:
        managed = False
        db_table = 'review'
        unique_together = (('item_code', 'cid'),)


class Transaction(models.Model):
    item_code = models.ForeignKey(Product, models.DO_NOTHING, db_column='item_code')
    customer_id = models.OneToOneField(Customer, models.DO_NOTHING, db_column='customer_id', primary_key=True)
    payment_method = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'transaction'
        unique_together = (('item_code', 'customer_id'),)
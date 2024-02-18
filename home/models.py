from django.db import models

class A(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# حالا دوتا مدل دیگر میخواهیم ایجاد کنیم که فیلدهای بالا را دارند به اضافه چند فیلد دیگر که از روش ابسترکت استفاده میکنیم
# که باید کلاس بالا را تبدیل به ابسترکت کلاس کنیم و کلاس بی و سی ارث بری میکنند از کلاس آ 
    class Meta:#الان کلاس آ تبدیل به یک ابسترکت کلاس میشود
        abstract = True

class B(A): #بجای اینکه از مدل دات مودل فرم ارث بری کند میگوئیم از کلاس آ ارث بری کن
    family = models.CharField(max_length=50)
    # الان سه تا فیلد بالایی را دارد و همچنین سلف دات نیم را با اینکه نمینویسیم
    #حتی میتوانیم کلاس بی را هم ابسترکت کلاس کنیم و  در کلاس های دیگر استفاده کنیم 
    #اگر فیلدی از کلاس آ را هم نخواهیم میتوانیم اوررایت کنیم مثلا نام برابر با نان یا مثلا ریترن کن فامیلی را

class C(A):
    phone = models.IntegerField()

# **************************************
#ارثبری چند جدولی
class Place(models.Model):#براری مکان ها
    address = models.CharField(max_length=50)

class Cinema(Place):
    name = models.CharField(max_length=50)

class Restorant(Place):
    name = models.CharField(max_length=50)

# *****************************************

# مدل های میانی 
class Player(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):#اگر بیشتر از یک مقدار به فانکشن بدهیم خطا میدهد که برای همین
        #  از آرگز استفاده میکنیم و اگر مقدار دوم دیکشنری باشد کیورد آرگز بکار میاید
        if self.name == 'jack':#اگر جک بود نام ذخیره نکن
            pass
        else:#در غیر اینصورت ذخیره کن
            super().save(*args, **kwargs)#برای اوررایت سوپر را صدا میزنیم

class Team(models.Model):
    name = models.CharField(max_length=50)
    player = models.ManyToManyField(Player, through='Extra')#هربار که از رابطه چند به چند استفاده میکنیم خود جنگو یک مدل میانی میسازد برای ما و ما الان اوررایت میکنیم مدل سوم جنگو را
    def __str__(self):
       return self.name

class Extra(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    goal = models.IntegerField()
    number = models.IntegerField()

# ********************************************************************
# برای استفاده از ایجکس
from django.contrib.auth.models import User
class Product(models.Model):
    name = models.CharField(max_length=50)
    favorite = models.ManyToManyField(User, blank=True, related_name='fa_user')

    def __str__(self):
        return self.name

# ********************************************************************
   
   
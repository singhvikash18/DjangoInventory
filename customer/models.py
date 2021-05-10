from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

MY_CHOICES = (('item_key1', 'Item title 1.1'),
              ('item_key2', 'Item title 1.2'),
              ('item_key3', 'Item title 1.3'))

      

Prefence =(('1','Taxable'),
           ('2','Tax Exempt'))  

placeSupply = (("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry"))   

Money =(('USA','USD'),('India','Indian-Rupee'),('European-Union','Euro'),('UAE','Dirham'),('6','Yuan'))    

ListChoice= (("Goods","Goods"),("Service","Service"))
UnitChoice = (("Dozen","Dozen"),("Box","Box"),("Kilogram","kilogram"),("Pieces","Pieces"),("Unit","Unit"),("Meters","Meters"),("Pairs","Pairs"))
Manufracturer_List =(("abc","ABC"),("Xyz","XYZ"))  
Brand_List = (("etc","etc"),(" "," "))

class Emplyoee(models.Model):
    company_name = models.CharField(max_length=50,default='any name of the company')
    fullname = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    phone = PhoneNumberField(blank=True)
    address = models.CharField(max_length=100,default='SOME STRING')
    website = models.CharField(max_length=30,default='website name')

    
    GST_Treatment = models.CharField(max_length=50,choices=MY_CHOICES,default='item_key1')
    Tax_preference = models.CharField(max_length=20,choices=Prefence,default='1')
    Place_of_supply = models.CharField( max_length=50,choices=placeSupply,default='Assam')
    Currency = models.CharField( max_length=50,choices=Money,default='India')

    remarks = models.TextField(max_length=300)
    created = models.DateTimeField(auto_now_add=True, blank=True)

class ItemGroup(models.Model):

    Item_image =models.FileField( upload_to=None,)
    Item_list = models.CharField(max_length=10,choices= ListChoice,default='Goods')
    Item_name = models.CharField(max_length=30)
    Unit =models.CharField(max_length=20,choices=UnitChoice,default="Box")
    Manufracturer = models.CharField(max_length=20,choices=Manufracturer_List,default="abc")
    Brand = models.CharField( max_length=50,choices=Brand_List ,default=" ")
    Tax_preference = models.CharField(max_length=20,choices=Prefence,default='1')
    Discription = models.TextField(max_length=100)






    
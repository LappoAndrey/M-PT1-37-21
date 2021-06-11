from django.db import models
from django.db import connection


class DRUGNAMES(models.Model):

    ID = models.AutoField(primary_key=True)
    DRUGNAME = models.CharField(max_length=350)
    FORM = models.CharField(max_length=350, blank=True)
    CONTAIN = models.CharField(max_length=350, blank=True)
    NUMBER = models.IntegerField(blank=True)
    IDCOUNTRY = models.ForeignKey('COUNTRIES', on_delete=models.CASCADE)
    IDPRODUCER = models.ForeignKey('PRODUCERS', on_delete=models.CASCADE)
    IDCLASS = models.ForeignKey('VIDAL', on_delete=models.CASCADE)
    ISDEAD = models.IntegerField(blank=True)
    GRPJOUR = models.IntegerField(blank=True)
    NUMLIKETHISALL = models.IntegerField(blank=True)
    KEYWORDSTRING = models.CharField(max_length=350, blank=True)

    def __str__(self):
        return f'{self.DRUGNAME}  {self.FORM}  {self.CONTAIN}  {self.NUMBER}'


class FILES(models.Model):
    
   
    fileName = models.CharField(max_length=350, blank=True)
    fileData = models.BinaryField(blank=True)

    def __str__(self):
        return f'{self.fileName}  {self.fileData} '
   


class COUNTRIES(models.Model):
    
    ID = models.AutoField(primary_key=True)
    COUNTRYNAME = models.CharField(max_length=350, blank=True)
    NATIVECOUNTRY = models.CharField(max_length=350, blank=True)

    def __str__(self):
        return f'{self.COUNTRYNAME}'

class KEYWORDS(models.Model):
    
    ID = models.AutoField(primary_key=True)
    KEYWORDNAME = models.CharField(max_length=350, blank=True)
    
    def __str__(self):
        return f'{self.KEYWORDNAME}'

class MAIN(models.Model):
    

    IDCOLOR = models.IntegerField(blank=True)
    IDDRUGNAME = models.ForeignKey('DRUGNAMES', on_delete=models.CASCADE)
    IDSELLER = models.ForeignKey('SELLERS', on_delete=models.CASCADE)
    IDMONEYTYPE = models.IntegerField(blank=True)
    IDPRICEMASK = models.IntegerField(blank=True)
    PRICE = models.IntegerField(blank=True)
    VPRICE = models.IntegerField(blank=True)
    BPRICE = models.IntegerField(blank=True)
    IDEXPDATE = models.IntegerField(blank=True)
    NDS = models.IntegerField(blank=True)
    CDATE = models.DateTimeField(blank=True)

    def __str__(self):
        return f' {self.IDCOLOR}  {self.IDSELLER}  {self.IDMONEYTYPE} {self.PRICE} {self.VPRICE} {self.BPRICE}'



class PARAMETERS(models.Model):
    
    
    PARAMETER = models.CharField(max_length=350, blank=True)
    PARAMETERVALUE = models.CharField(max_length=350, blank=True)

    def __str__(self):
        return f'{self.PARAMETER} {self.PARAMETERVALUE}'


class PRODUCERS(models.Model):
    
    ID = models.AutoField(primary_key=True)
    PRODUCERNAME = models.CharField(max_length=350, blank=True)
    NATIVEPRODUCER = models.CharField(max_length=350, blank=True)
    
    def __str__(self):
        return f'{self.PRODUCERNAME} {self.NATIVEPRODUCER}'

class VIDAL(models.Model):
    
    ID = models.AutoField(primary_key=True)
    INTNAME = models.CharField(max_length=350, blank=True)
    CLINGROUP = models.CharField(max_length=350, blank=True)

    def __str__(self):
        return f'{self.INTNAME} {self.CLINGROUP}'

class SELLERS(models.Model):
    
    ID = models.AutoField(primary_key=True)
    SELLERNAME = models.CharField(max_length=350)
    ADDR = models.CharField(max_length=350, blank=True)
    PHONE = models.CharField(max_length=350, blank=True)
    REGION = models.IntegerField(blank=True)
    PAYCOND = models.IntegerField(blank=True)
    COMMENT = models.IntegerField(blank=True)
    EMAIL = models.EmailField(blank=True)
    LICENSE = models.IntegerField(blank=True)
    FORMOPL = models.IntegerField(blank=True)
    NATIVESELLER = models.IntegerField(blank=True)
    POSINPRICE = models.CharField(max_length=350, blank=True)
    POSINPRICEALL = models.CharField(max_length=350)
    CDATE = models.DateTimeField(blank=True)
    NATBANK = models.CharField(max_length=350, blank=True)
    ESHOP_SITE = models.CharField(max_length=350,blank=True)    # if not null == css - grey and white
    ESHOP_INFO = models.CharField(max_length=350,blank=True)
    USDCOURSE = models.IntegerField(blank=True)
    RURCOURSE = models.IntegerField(blank=True)
    hasDelivery = models.IntegerField(blank=True)
    baseContactId = models.IntegerField(blank=True)
    

    def __str__(self):
        return f'{self.SELLERNAME}  {self.ADDR}  {self.PHONE} {self.REGION}'


class USERS(models.Model):

    login = models.CharField(max_length=100, blank=False)
    password = models.CharField(max_length=100, blank=False)
    email =models.EmailField(blank=False)
    idfirm = models.ForeignKey('FIRMS', on_delete=models.CASCADE)
    mac = models.CharField(max_length=100, blank=False)
    ipCame = models.CharField(max_length=100, blank=False)
    dtCameLats = models.DateTimeField(blank=True)
    ipCheck = models.CharField(max_length=100, blank=False)
    dtCheck = models.DateTimeField(blank=True)
    date_from = models.DateTimeField(blank=True)
    date_to = models.DateTimeField(blank=True)
    srcfile = models.CharField(max_length=100, blank=False)
    typebd = models.IntegerField(blank=True)
    

    def __str__(self):
        return f'{self.login}  {self.password}  {self.idfirm} {self.ipCame}'



class FIRMS(models.Model):
    
    name = models.CharField(max_length=200, blank=False)

    

    def __str__(self):
        return f'{self.name} '




# class Post(models.Model):

#     POST_TYPES = [('C', 'Commercial'), ('A', 'Author'), ('P', 'Public Licinse')]
    
#     title = models.CharField(max_length=100, blank=False)
#     subtitle = models.CharField(max_length=100)
#     content = models.TextField(blank=False)
#     post_type = models.CharField(max_length=1, blank=False, choices=POST_TYPES)
#     issued = models.DateTimeField()
#     image = models.ImageField(upload_to='uploads')

#     author = models.ForeignKey('Author', on_delete=models.CASCADE)

#     class Meta:
#         permissions = (('can_post', 'Can add post'), ('can_manage_post', 'Can manage post'))

#     def __str__(self):
#         return self.title

    

# class Author(models.Model):

#     first_name = models.CharField(max_length=100, blank=False)
#     last_name = models.CharField(max_length=100, blank=False)
#     username = models.CharField(max_length=100, blank=False)
#     avatar = models.ImageField(upload_to='uploads')

#     def __str__(self):
#         return f'{self.first_name} {self.last_name}'
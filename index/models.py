from django.db import models

# Create your models here.
class products(models.Model):
    title=models.CharField(max_length=100,blank=False)
    image=models.ImageField(upload_to='product/',blank=False)
    name=models.CharField(max_length=100,blank=False)
    price=models.CharField(max_length=100,blank=False)
    risk=models.CharField(max_length=100,blank=False,default='$15.00')

    def __str__(self):
        return self.name

class rec(models.Model):
    title=models.CharField(max_length=100,blank=False)
    image=models.ImageField(upload_to='blog/',blank=False)
    dis=models.TextField(max_length=300,blank=False)
    date=models.CharField(max_length=100,blank=False)

    def __str__(self):
        return self.title

class pics(models.Model):
    title=models.CharField(max_length=100,blank=False)
    image1=models.ImageField(upload_to='blog/',blank=False)
    name1=models.CharField(max_length=100,blank=False)
    discription1=models.TextField(max_length=300,blank=False)
    image2=models.ImageField(upload_to='blog/',blank=False)
    name2=models.CharField(max_length=100,blank=False)
    discription2=models.TextField(max_length=300,blank=False)
    image3=models.ImageField(upload_to='blog/',blank=False)
    name3=models.CharField(max_length=100,blank=False)
    discription3=models.TextField(max_length=300,blank=False)
    image4=models.ImageField(upload_to='blog/',blank=False)
    name4=models.CharField(max_length=100,blank=False)
    discription4=models.TextField(max_length=300,blank=False)
    date=models.CharField(max_length=100,blank=False)
    def __str__(self):
        return self.title

class gusto(models.Model):
    title=models.CharField(max_length=100,blank=False)
    image=models.ImageField(upload_to='recentpost/',blank=False)
    name=models.CharField(max_length=100,blank=False)
    dis=models.TextField(max_length=200,blank=False)

    def __str__(self):
        return self.title

class ment(models.Model):
    title=models.CharField(max_length=100,blank=False,default='latest1')
    image=models.ImageField(upload_to='latest/',blank=False)
    name=models.CharField(max_length=100,blank=False)
    dis=models.TextField(max_length=200,blank=False)

    def __str__(self):
        return self.title


class recent(models.Model):
    title=models.CharField(max_length=100,blank=False,default='recent1')
    name=models.CharField(max_length=100,blank=False,default='Lorem ipsum dolor sit amsdf')
    image=models.ImageField(upload_to='blogpost/',blank=False)
    dis=models.TextField(max_length=300,blank=False)

    def __str__(self):
        return self.title    


class contactforms(models.Model):
    name=models.CharField(max_length=100,blank=False)
    email=models.EmailField(max_length=100)
    subject=models.CharField(max_length=100)
    message=models.TextField(max_length=300)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


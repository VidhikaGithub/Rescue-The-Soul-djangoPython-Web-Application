from django.db import models

# Create your models here.


class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name+" "+self.email+" "+self.password

class contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=150)
    message=models.CharField(max_length=250)

    def __str__(self):
        return self.name+" "+self.email+" "+self.subject+" "+self.message

class donatethings(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    address=models.CharField(max_length=250)
    country=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=20)
    message=models.CharField(max_length=250)

    def __str__(self):
        return self.firstname+" "+self.lastname+" "+self.address+" "+self.country
        +" "+self.state+" "+self.city+" "+self.phonw+" "+self.message

class sharethoughts(models.Model):
    sharetext=models.CharField(max_length=250)
    sharefile=models.FileField(upload_to='share_experience')

    def __str__(self):
        return self.sharetext+" "+self.sharefile

class pet(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    address=models.CharField(max_length=250)
    country=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=20)
    message=models.CharField(max_length=250)

    def __str__(self):
        return self.firstname+" "+self.lastname+" "+self.address+" "+self.country
        +" "+self.state+" "+self.city+" "+self.phone+" "+self.message

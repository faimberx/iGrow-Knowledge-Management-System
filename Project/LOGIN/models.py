from django.db import models, migrations
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.syndication.views import Feed

class Person(models.Model):
    Email = models.CharField(max_length=150)
    Password = models.CharField(max_length=150)
    Username = models.CharField(max_length=150)
    Name = models.CharField(max_length=150)
    DateOfBirth = models.CharField(max_length=150)
    Age = models.IntegerField ()
    District = models.CharField(max_length=150)
    State = models.CharField(max_length=150)
    Occupation = models.CharField(max_length=150)
    About = models.CharField(max_length=150)
    Gender = models.CharField(max_length=1)
    MaritalStatus = models.CharField(max_length=150)

    def save(self):
        super().save()

def user_form(sender, instance, created, **kwargs):
    if created:
        Person.objects.create(user=instance)
        instance.Person.save()

class Feed(models.Model):
    class Meta:
        db_table = 'Feed'
    Title = models.CharField(max_length=255, blank=True)
    Message = models.CharField(max_length=255, blank=True)
    Photo = models.ImageField(upload_to ='images/')
    Video = models.FileField(upload_to='uploads/', null=True)
    Graph = models.FileField(upload_to='uploads/')

    def showvideo(request):

        lastvideo = video.objects.last()
        videofile = lastvideo.videofile
    
        form = SharingForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()

        context= {'videofile': videofile, 'form': form}

        return render(request, 'LOGIN/sharing.html', context)
    #def __str__(self):
       # return self.Message + ": " + str(self.videofile)

class Group(models.Model):
    class Meta:
        db_table = 'Group'
    Name = models.CharField(max_length=150)
    About = models.CharField(max_length=1000)
    Media = models.FileField(upload_to='uploads/',default="")

class Member(models.Model):
    class Meta:
        db_table = 'Member'
    Name = models.CharField(max_length=150)
    Study = models.CharField(max_length=1000)
    Lives = models.CharField(max_length=1000)
    

class Booking(models.Model):
    class Meta:
        db_table = 'Booking'
    Name = models.CharField(max_length=150)
    ProgrammeName = models.CharField(max_length=150,default="")
    Date = models.DateField()
    Session = models.CharField(max_length=150)

class Workshop(models.Model):
    class Meta:
        db_table = 'Workshop'
    ProgrammeName = models.CharField(max_length=150,default="")
    Description=models.CharField(max_length=150,default="")
    Date = models.DateField()
    Session = models.CharField(max_length=150)

class SensorData(models.Model):
    class Meta:
        db_table = 'SensorData'    
    Detail = models.CharField(max_length=255)
    Name = models.CharField(max_length=150)

class Plants(models.Model):
    class Meta:
        db_table = 'Plants'
    Pictures = models.ImageField(upload_to='uploads/')
    Species = models.CharField(max_length=150)
    Types = models.CharField(max_length=150)

class Comment(models.Model):
    class Meta:
        db_table = 'Comment'    
    Message = models.CharField(max_length=255)
    Pictures = models.ImageField(upload_to='uploads/')
    Video = models.FileField(upload_to='uploads/')

class Users(models.Model):
    username = models.CharField(max_length=10, unique=True) #AI190201
    password = models.CharField(max_length=30) #ninja saga
    name = models.CharField(max_length=100) #FAIZ BIN AB. HAMID
    age = models.IntegerField() #22
    ranking = models.FloatField() #2.5

    def upload_photo(self, filename):
        path = 'LOGIN/photo/{}'.format(filename)
        return path

    photo = models.ImageField(upload_to=upload_photo, null=True, blank=True)

    def upload_file(self, filename):
        path = 'LOGIN/file/{}'.format(filename)
        return path

    resume = models.ImageField(upload_to=upload_file, null=True, blank=True)

    def __str__(self):
        return f"{self.username} - {self.password}"
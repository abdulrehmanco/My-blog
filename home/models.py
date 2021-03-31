from django.db import models
from Bloging.utils import unique_slug_generator
from django.db.models.signals import pre_save
from PIL import Image
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.


class Rabtaguzari(models.Model):

    name = models.CharField(max_length=122, null=True, blank=True)
    email = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=50, null=True)
    desc = models.TextField(default="default")

    def __str__(self):
        return self.name


class Subjects(models.Model):
    title = models.CharField(max_length=120)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class blogpost(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, null=True)
    image = models.ImageField(null="true", blank="true", upload_to="media/images")
     
    
    #def save(self, *args, **kwargs):
        #super().save(*args, **kwargs)
        #img = Image.open(self.image.path)

        #if img.height >50 or img.width >50:
            #output_size = (50,50)
            #img.thumbnail(output_size)
            #img.save(self.image.path)



    author = models.CharField(max_length=50, null=True)
    body = models.TextField()
    slug = models.SlugField(max_length=130, blank=True, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.title
    
    

def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(slug_generator, sender=blogpost)

class blogcomment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    post = models.ForeignKey(blogpost, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)
    def __str__(self):
        return self.comment[0:13] + "..." + "by" + " " + self.user.username

from django.db import models
from tinymce.models import HTMLField
# # Create your models here.
# def upload_location(instance, filename):
#     # ArbitraryModel = instance.__class__
#     # new_id = Post.objects.order_by("id").last().id + 1
#     return ('%s/%s') % (instance.id, filename)


class Comment(models.Model):
    author_name = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    content = models.TextField()
    website = models.URLField(max_length=200)
    news_id = models.ForeignKey('News', related_name='comments_set', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author_name}-{self.news_id}'

class News(models.Model):
    title = models.CharField(max_length=254)
    content = HTMLField()
    posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        db_table = 'News'

    def __str__(self):
        return f'{self.title}'

class Service(models.Model):
    name = models.CharField(max_length=254)
    short_description = HTMLField()
    is_top = models.BooleanField()
    content = HTMLField(blank=True, null=True)

    def __str__(self):
        return self.name

class ServicePicture(models.Model):
    service = models.ForeignKey('Service', related_name='services', on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='ServicePic/',
        width_field= 'width_field',
        height_field = 'height_field',
        blank=True, null=True
        )
    width_field = models.IntegerField(default = 0)
    height_field = models.IntegerField(default = 0)

    def __str__(self):
        return str(self.id)

class Review(models.Model):
    user_name = models.CharField(max_length=254)
    image = models.ImageField(
        upload_to='ReviewsPic/',
        width_field= 'width_field',
        height_field = 'height_field',
        blank=True, null=True
        )
    width_field = models.IntegerField(default = 0)
    height_field = models.IntegerField(default = 0)
    content = HTMLField()
    date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.user_name

class HospitalInfo(models.Model):
    name = models.CharField(max_length=255)
    countent = HTMLField()
    year = models.PositiveSmallIntegerField(blank=True, null=True)
    num_staffs = models.PositiveSmallIntegerField(blank=True, null=True)
    num_awards = models.PositiveSmallIntegerField(blank=True, null=True)
    num_clients = models.PositiveSmallIntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class Contact(models.Model):
    email = models.EmailField(max_length=254)
    long=models.TextField()
    lat = models.TextField()
    address = models.CharField(max_length = 254)

    def __str__(self):
        return str(self.email)


class Phone(models.Model):
    phone = models.CharField(max_length=255)

    def __str__(self):
        return str(self.phone)


class OpeningHour(models.Model):
    WEEKDAYS = [
        (1, "Monday"),
        (2, "Tuesday"),
        (3, "Wednesday"),
        (4, "Thursday"),
        (5, "Friday"),
        (6, "Saturday"),
        (7, "Sunday"),
    ]
    weekday = models.IntegerField(
        choices=WEEKDAYS,
        unique=True
    )
    from_hour = models.TimeField()
    to_hour = models.TimeField()

    def __str__(self):
        return str(self.weekday)
    

class Message(models.Model):
    name = models.CharField(max_length=255)
    theme = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=254)
    content = models.TextField()

    def __str__(self):
        return str(self.email)

class Doctor(models.Model):
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True, default=None)
    last_name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    bio = models.TextField()
    image = models.ImageField(
        upload_to='Doctors/',
        width_field= 'width_field',
        height_field = 'height_field',
        blank=True, null=True
        )
    width_field = models.IntegerField(default = 0)
    height_field = models.IntegerField(default = 0)
    
    def __str__(self):
        return f'{self.first_name}-{self.last_name}'

class Follower(models.Model):
    emails = models.EmailField( max_length=254)

    def __str__(self):
        return str(self.emails)
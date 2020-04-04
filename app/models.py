from django.db import models
from tinymce.models import HTMLField
from django.core.validators import ValidationError
from django.db.models.signals import pre_save
from django.utils.text import slugify


def validate_name(value):
    if any(char.isdigit() for char in str(value)):
        raise ValidationError(
            'Name contains number, please avoid it'
        )


class Comment(models.Model):
    author_name = models.CharField(max_length=254, validators=[validate_name])
    email = models.EmailField(max_length=254)
    content = models.TextField()
    website = models.URLField(max_length=200)
    news_id = models.ForeignKey('News', related_name='comments_set', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author_name}-{self.news_id}'



class News(models.Model):
    title = models.CharField(max_length=254)
    content = HTMLField()
    slug = models.SlugField(max_length=254, blank=True, unique=True, allow_unicode=True)
    posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name_plural = "News"

    def __str__(self):
        return f'{self.title}'



def create_slug(instance,new_slug=None):
    slug = slugify(instance.title,allow_unicode=True)
    ClassName = instance.__class__
    if new_slug is not None:
        slug = new_slug
    qs = ClassName.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_news_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_news_receiver, sender=News)




class Service(models.Model):
    name = models.CharField(max_length=254, unique=True)
    category = models.ForeignKey('ServiceCategory', related_name='services',
                                 on_delete=models.SET_NULL, null=True)
    is_top = models.BooleanField()
    breif_description = models.TextField(null=True, default=None, blank=True)
    content = HTMLField(blank=True, null=True)
    slug = models.SlugField(max_length=254, unique=True, allow_unicode=True)
    def __str__(self):
        return self.name


class ServiceCategory(models.Model):
    name = models.CharField(max_length=255,unique=True)
    image = image = models.ImageField(
        upload_to='ServiceCategory/',
        width_field= 'width_field',
        height_field = 'height_field',
        blank=True, null=True
        )
    width_field = models.IntegerField(default = 0, blank=True)
    height_field = models.IntegerField(default = 0, blank=True)

    class Meta:
        verbose_name_plural = "ServiceCategories"

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
    author_name = models.CharField(max_length=254, validators=[validate_name])
    image = models.ImageField(
        upload_to='ReviewsPic/',
        width_field= 'width_field',
        height_field = 'height_field',
        blank=True, null=True
        )
    width_field = models.IntegerField(default = 0)
    height_field = models.IntegerField(default = 0)
    content = models.TextField()
    date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.author_name


class HospitalInfo(models.Model):
    name = models.CharField(max_length=255)
    countent = HTMLField()
    year = models.PositiveSmallIntegerField(blank=True, null=True)
    num_staffs = models.PositiveSmallIntegerField(blank=True, null=True)
    num_awards = models.PositiveSmallIntegerField(blank=True, null=True)
    num_clients = models.PositiveSmallIntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "HospitalInfo"
    
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
    phone = models.CharField(max_length=255, unique = True)

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
    name = models.CharField(max_length=255,  validators=[validate_name])
    theme = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15, blank=True, null=True, default = None)
    content = models.TextField()

    def __str__(self):
        return str(self.email)


class Doctor(models.Model):
    first_name = models.CharField(max_length=255,  validators=[validate_name])
    middle_name = models.CharField(max_length=255, blank=True, null=True, default=None,  validators=[validate_name])
    last_name = models.CharField(max_length=255,  validators=[validate_name])
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
    emails = models.EmailField(max_length=254, unique=True)

    def __str__(self):
        return str(self.emails)
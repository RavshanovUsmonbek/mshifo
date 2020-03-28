from django.db import models

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


class News(models.Model):
    title = models.CharField(max_length=254)
    content = models.TextField()
    comment_count = models.IntegerField()
    posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        db_table = 'News'

class Service(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField(blank=True, null=True)
    is_top = models.BooleanField()
    short_desc = models.TextField()

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
    content = models.TextField()
    date = models.DateTimeField(auto_now=False, auto_now_add=True)

class About(models.Model):
    countent = models.TextField()
    address = models.CharField(max_length = 254)
    email = models.EmailField(max_length=254)
    estab_date = models.DateField(auto_now=False, auto_now_add=False)
    long=models.TextField()
    lat = models.TextField()


class Message(models.Model):
    name = models.CharField(max_length=255)
    theme = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=254)
    content = models.TextField()


class Doctor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    experience = models.PositiveSmallIntegerField(blank=True, null=True)
    bio = models.TextField()
    image = models.ImageField(
        upload_to='Doctors/',
        width_field= 'width_field',
        height_field = 'height_field',
        blank=True, null=True
        )
    width_field = models.IntegerField(default = 0)
    height_field = models.IntegerField(default = 0)
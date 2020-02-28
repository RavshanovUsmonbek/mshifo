from django.db import models

# Create your models here.
def upload_location(instance, filename):
    # ArbitraryModel = instance.__class__
    # new_id = Post.objects.order_by("id").last().id + 1
    return ('%s/%s/%s') % (instance.__class__,instance.id, filename)

class Menu(models.Model):
    length = 1
    menu_types = [
        ('F','footer'),
        ('T','topper'),
    ]
    type_of_menu= models.CharField(max_length=length, choices=menu_types)
    name = models.CharField(max_length=255)

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
        verbose_name = 'News'

class Service(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()
    picture = models.ImageField(upload_to=upload_location, height_field=None, width_field=None, max_length=None)
    image = models.ImageField(
        upload_to=upload_location,
        width_field= 'width_field',
        height_field = 'height_field',
        blank=True, null=True
        )
    width_field = models.IntegerField(default = 0)
    height_field = models.IntegerField(default = 0)

class Review(models.Model):
    user_name = models.CharField(max_length=254)
    image = models.ImageField(
        upload_to=upload_location,
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

class Equipments(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()
    image = models.ImageField(
        upload_to=upload_location,
        width_field= 'width_field',
        height_field = 'height_field',
        blank=True, null=True
        )
    width_field = models.IntegerField(default = 0)
    height_field = models.IntegerField(default = 0)

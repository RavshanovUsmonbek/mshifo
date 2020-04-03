from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    StringRelatedField,
    HyperlinkedRelatedField,
    )

from app.models import (
    Doctor, 
    HospitalInfo, 
    Comment, 
    News, 
    Message, 
    Service, 
    ServicePicture, 
    Contact, 
    Phone,
    OpeningHour,
    Follower,
    Review,
    ServiceCategory,
)



class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = ['author_name','image','content','date',]

class FollowerSerializer(ModelSerializer):
    class Meta:
        model = Follower
        fields = '__all__'

class DoctorSerializer(ModelSerializer):    
    class Meta:
        model = Doctor
        fields = [
            'first_name',
            'middle_name',
            'last_name',
            'specialty',
            'bio',
            'image',
            ]


class NewsSerializer(ModelSerializer):
    comments = SerializerMethodField()
    comment_count = SerializerMethodField()
    class Meta:
        model = News
        fields = [
            'title',
            'slug',
            'content',
            'comment_count',
            'posted_on',
            'comments',
        ]
    
    def get_comments(self, obj):
        c_qs = Comment.objects.filter(news_id=obj)
        comments = CommentSerializer(c_qs, many=True).data
        return comments or None
    
    def get_comment_count(self, obj):
        c_qs = Comment.objects.filter(news_id=obj).count()
        return c_qs


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['author_name','email','content','website','news_id',]


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = ['email','long', 'lat', 'address',]

class PhoneSerializer(ModelSerializer):
    class Meta:
        model = Phone
        fields = ['phone',]


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = ['name','theme','email','phone','content',]


class ServiceListSerializer(ModelSerializer):
    category = StringRelatedField()
    url = HyperlinkedIdentityField(
        view_name='app-api:service-detail',
        lookup_field='slug',
    )
    class Meta:
        model = Service
        fields = [
            'url',
            'name', 
            'slug',
            'category', 
            'is_top', 
            ]
    

class ServiceDetailSerializer(ModelSerializer):
    pictures = SerializerMethodField()
    category = StringRelatedField()
    class Meta:
        model = Service
        fields = [
            'name', 
            'slug',
            'category', 
            'is_top', 
            'breif_description',
            'content',
            'pictures',
            ]
    
    def get_pictures(self, obj):
        try:
            p_qs = ServicePicture.objects.filter(service = obj)
            service_pic = ServicePictureSerializer(p_qs, many=True).data
            return service_pic or None
        except:
            return None

        
class ServicePictureSerializer(ModelSerializer):
    class Meta:
        model = ServicePicture
        fields = [
            'service',
            'image',
        ]


class ServiceCategorySerializer(ModelSerializer):
    class Meta:
        model=ServiceCategory
        fields=['name','image',]

class OpenningHoursSerializer(ModelSerializer):
    class Meta:
        model = OpeningHour
        fields = [
            'weekday',
            'from_hour', 
            'to_hour',
        ]


class HospitalInfoSerializer(ModelSerializer):
    phones = SerializerMethodField()
    contacts = SerializerMethodField()
    class Meta:
        model = HospitalInfo
        fields = [
            'name',
            'countent',
            'year',
            'num_staffs',
            'num_awards',
            'num_clients',
            'phones',
            'contacts',
        ]

    def get_phones(self, obj):
        ph_qs = Phone.objects.all()
        phones = PhoneSerializer(ph_qs, many=True).data
        return phones or None

    def get_contacts(self, obj):
        c_qs = Contact.objects.all()
        contacts = ContactSerializer(c_qs, many=True).data
        return contacts or None

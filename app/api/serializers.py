from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField
    )
from app.models import Doctor, HospitalInfo
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
)

class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'



class FollowerSerializer(ModelSerializer):
    class Meta:
        model = Follower
        fields = '__all__'

class DoctorSerializer(ModelSerializer):    
    class Meta:
        model = Doctor
        fields = '__all__'

class NewsSerializer(ModelSerializer):
    comments = SerializerMethodField()
    comment_count = SerializerMethodField()
    class Meta:
        model = News
        fields = [
            'title',
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
        fields = '__all__'

class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class PhoneSerializer(ModelSerializer):
    class Meta:
        model = Phone
        fields = '__all__'

class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class ServiceSerializer(ModelSerializer):
    pictures = SerializerMethodField()
    class Meta:
        model = Service
        fields = [
            'name', 
            'short_description', 
            'is_top', 
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
        fields = '__all__'


class OpenningHoursSerializer(ModelSerializer):
    class Meta:
        model = OpeningHour
        fields = '__all__'


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

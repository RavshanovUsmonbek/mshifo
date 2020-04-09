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




class DoctorDetailSerializer(ModelSerializer):    
    class Meta:
        model = Doctor
        fields = [
            'id'
            'first_name',
            'middle_name',
            'last_name',
            'specialty',
            'bio',
            'image',
            ]


class DoctorListSerializer(ModelSerializer):    
    class Meta:
        model = Doctor
        fields = [
            'id'
            'first_name',
            'middle_name',
            'last_name',
            ]


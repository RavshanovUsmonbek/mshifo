from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView, 
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    ListCreateAPIView
    )

from .serializers import(
        DoctorSerializer,
        HospitalInfoSerializer,
        NewsSerializer,
        CommentSerializer,
        ContactSerializer,
        PhoneSerializer,
        MessageSerializer,
        ServiceSerializer,
        ServicePictureSerializer,
        OpenningHoursSerializer,
        HospitalInfoSerializer,
        FollowerSerializer,
        ReviewSerializer
     )

from rest_framework.permissions import IsAdminUser, AllowAny
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
    Review,
    Follower,
)


class DoctorListAPIView(ListAPIView):
    lookup_field = 'pk'
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [AllowAny]


class HospitalInfoListAPIView(ListAPIView):
    lookup_field = 'pk'
    queryset = HospitalInfo.objects.all()
    serializer_class = HospitalInfoSerializer
    permission_classes = [AllowAny]


class CommentListAPIView(ListCreateAPIView):
    lookup_field = 'pk'
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]


class NewsListAPIView(ListAPIView):
    lookup_field = 'pk'
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [AllowAny]

class MessageListAPIView(ListAPIView):
    lookup_field = 'pk'
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [AllowAny]

class MessageCreateAPIView(CreateAPIView):
    lookup_field = 'pk'
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [AllowAny]

class ContactListAPIView(ListAPIView):
    lookup_field = 'pk'
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]

class PhoneListAPIView(ListAPIView):
    lookup_field = 'pk'
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
    permission_classes = [AllowAny]


class ServiceListAPIView(ListAPIView):
    lookup_field = 'pk'
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [AllowAny]


class ServicePicListAPIView(ListAPIView):
    lookup_field = 'pk'
    queryset = ServicePicture.objects.all()
    serializer_class = ServicePictureSerializer
    permission_classes = [AllowAny]

class OpenningHoursListAPIView(ListAPIView):
    lookup_field = 'pk'
    queryset = OpeningHour.objects.all()
    serializer_class = OpenningHoursSerializer
    permission_classes = [AllowAny]


class FollowerListAPIView(ListAPIView):
    lookup_field = 'pk'
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
    permission_classes = [AllowAny]


class FollowerCreateAPIView(CreateAPIView):
    lookup_field = 'pk'
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
    permission_classes = [AllowAny]


class ReviewListAPIView(ListAPIView):
    lookup_field = 'pk'
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [AllowAny]
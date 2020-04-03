from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView, 
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    ListCreateAPIView,
    )

from .serializers import(
        DoctorSerializer,
        HospitalInfoSerializer,
        NewsSerializer,
        CommentSerializer,
        ContactSerializer,
        PhoneSerializer,
        MessageSerializer,
        ServiceListSerializer,
        ServicePictureSerializer,
        OpenningHoursSerializer,
        HospitalInfoSerializer,
        FollowerSerializer,
        ReviewSerializer,
        ServiceDetailSerializer,
        ServiceCategorySerializer,
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
    ServiceCategory,
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


class ServiceListAPIView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceListSerializer
    permission_classes = [AllowAny]


class ServiceDetailAPIView(RetrieveAPIView):
    lookup_field = 'slug'
    queryset = Service.objects.all()
    serializer_class = ServiceDetailSerializer
    permission_classes = [AllowAny]


class ServiceCategoryListAPIView(ListAPIView):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer
    permission_classes = [AllowAny]
    


class OpenningHoursListAPIView(ListAPIView):
    lookup_field = 'pk'
    queryset = OpeningHour.objects.all()
    serializer_class = OpenningHoursSerializer
    permission_classes = [AllowAny]


class FollowerCreateAPIView(CreateAPIView):
    lookup_field = 'pk'
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
    permission_classes = [AllowAny,]


class ReviewListAPIView(ListAPIView):
    lookup_field = 'pk'
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [AllowAny,]
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView, 
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
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
        CategorySerializer,
        HospitalInfoCreateSerializer,
        NewsCreateSerializer,
        CommentCreateSerializer,
        MessageCreateSerializer,
        ContactCreateSerializer,
        ServiceCreateSerializer,
        CategoryCreateSerializer,
        FollowerCreateSerializer,
        ReviewCreateSerializer,
        PhoneCreateSerializer,
        PhoneSerializer,
        ServicePicCreateSerializer,
        ServicePicSerializer,
        
     )

from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
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

#------------------------------ Doctors-------------------------------------
#---------------------------------------------------------------------------
class DoctorListAPIView(ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [AllowAny]


class DoctorCreateAPIView(CreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated,]


class DoctorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated,]


#------------------------------ HospitalInfo -------------------------------------
#---------------------------------------------------------------------------------
class HospitalInfoListAPIView(ListAPIView):
    queryset = HospitalInfo.objects.all()
    serializer_class = HospitalInfoSerializer
    permission_classes = [AllowAny]


class HospitalInfoCreateAPIView(CreateAPIView):
    queryset = HospitalInfo.objects.all()
    serializer_class = HospitalInfoCreateSerializer
    permission_classes = [IsAuthenticated,]


class HospitalInfoRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = HospitalInfo.objects.all()
    serializer_class = HospitalInfoCreateSerializer
    permission_classes = [IsAuthenticated,]


#------------------------------ Comment -------------------------------------
#---------------------------------------------------------------------------------
class CommentListAPIView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = [IsAuthenticated,]


class CommentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = [IsAuthenticated,]



#------------------------------ News -------------------------------------
#---------------------------------------------------------------------------------
class NewsListAPIView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [AllowAny]


class NewsCreateAPIView(CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsCreateSerializer
    permission_classes = [IsAuthenticated,]


class NewsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsCreateSerializer
    permission_classes = [IsAuthenticated,]


class NewsDetailAPIView(RetrieveAPIView):
    lookup_field = 'slug'
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [AllowAny]



#------------------------------ Message -------------------------------------
#---------------------------------------------------------------------------------
class MessageCreateAPIView(CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageCreateSerializer
    permission_classes = [IsAuthenticated,]


class MessageListAPIView(ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [AllowAny]


class MessageRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    queryset = Message.objects.all()
    serializer_class = MessageCreateSerializer
    permission_classes = [IsAuthenticated,]


#------------------------------ Contact -------------------------------------
#---------------------------------------------------------------------------------
class ContactListAPIView(ListAPIView):
    lookup_field = 'pk'
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]


class ContactCreateAPIView(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactCreateSerializer
    permission_classes = [IsAuthenticated,]


class ContactRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    queryset = Contact.objects.all()
    serializer_class = ContactCreateSerializer
    permission_classes = [IsAuthenticated,]


#------------------------------ Service -------------------------------------
#---------------------------------------------------------------------------------
class ServiceListAPIView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceListSerializer
    permission_classes = [AllowAny]


class ServiceDetailAPIView(RetrieveAPIView):
    lookup_field = 'slug'
    queryset = Service.objects.all()
    serializer_class = ServiceDetailSerializer
    permission_classes = [AllowAny]


class ServiceCreateAPIView(CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceCreateSerializer
    permission_classes = [IsAuthenticated,]


class ServiceRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    queryset = Service.objects.all()
    serializer_class = ServiceCreateSerializer
    permission_classes = [IsAuthenticated,]



#------------------------------ Category -------------------------------------
#---------------------------------------------------------------------------------
class CategoryListAPIView(ListAPIView):
    queryset = ServiceCategory.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


class CategoryCreateAPIView(CreateAPIView):
    queryset = ServiceCategory.objects.all()
    serializer_class = CategoryCreateSerializer
    permission_classes = [IsAuthenticated,]


class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    queryset = ServiceCategory.objects.all()
    serializer_class = CategoryCreateSerializer
    permission_classes = [IsAuthenticated,]



#------------------------------ OpenningHours -------------------------------------
#---------------------------------------------------------------------------------
class OpenningHoursListAPIView(ListAPIView):
    queryset = OpeningHour.objects.all()
    serializer_class = OpenningHoursSerializer
    permission_classes = [AllowAny]


class OpenningHoursCreateAPIView(CreateAPIView):
    queryset = OpeningHour.objects.all()
    serializer_class = OpenningHoursSerializer
    permission_classes = [IsAuthenticated,]


class OpenningHoursRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    queryset = OpeningHour.objects.all()
    serializer_class = OpenningHoursSerializer
    permission_classes = [IsAuthenticated,]

#------------------------------ Follower -------------------------------------
#---------------------------------------------------------------------------------
class FollowerCreateAPIView(CreateAPIView):
    queryset = Follower.objects.all()
    serializer_class = FollowerCreateSerializer
    permission_classes = [IsAuthenticated,]

class FollowerListAPIView(ListAPIView):
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
    permission_classes = [AllowAny,]

class FollowerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    queryset = Follower.objects.all()
    serializer_class = FollowerCreateSerializer
    permission_classes = [IsAuthenticated,]

#------------------------------ Review -------------------------------------
#---------------------------------------------------------------------------------
class ReviewListAPIView(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [AllowAny,]


class ReviewCreateAPIView(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated,]


class ReviewRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated,]


#------------------------------ ServicePic -------------------------------------
#---------------------------------------------------------------------------------
class ServicePicListAPIView(ListAPIView):
    queryset = ServicePicture.objects.all()
    serializer_class = ServicePicSerializer
    permission_classes = [AllowAny,]


class ServicePicCreateAPIView(CreateAPIView):
    queryset = ServicePicture.objects.all()
    serializer_class = ServicePicCreateSerializer
    permission_classes = [IsAuthenticated,]


class ServicePicRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    queryset = ServicePicture.objects.all()
    serializer_class = ServicePicCreateSerializer
    permission_classes = [IsAuthenticated,]

#------------------------------ Phone -------------------------------------
#---------------------------------------------------------------------------------
class PhoneListAPIView(ListAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
    permission_classes = [AllowAny,]


class PhoneCreateAPIView(CreateAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneCreateSerializer
    permission_classes = [IsAuthenticated,]


class PhoneRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    queryset = Phone.objects.all()
    serializer_class = PhoneCreateSerializer
    permission_classes = [IsAuthenticated,]
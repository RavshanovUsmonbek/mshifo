from django.urls import path, include
from . import views

urlpatterns = [
    path('comment/list-create/',views.CommentListAPIView.as_view() ,name = 'api-comment-list'),

    path('contact/list/',views.ContactListAPIView.as_view() ,name = 'api-contact-list'),
    path('doctor/list/',views.DoctorListAPIView.as_view() ,name = 'api-doctor-list'),
    path('hospital_info/list/',views.HospitalInfoListAPIView.as_view() ,name = 'api-hosp_info-list'),
    path('open_hours/list/',views.OpenningHoursListAPIView.as_view() ,name = 'api-open_hours-list'),
   
    path('message/list/',views.MessageListAPIView.as_view() ,name = 'api-message-list'),
    path('message/create/',views.MessageCreateAPIView.as_view() ,name = 'api-message-create'),

    path('news/list/',views.NewsListAPIView.as_view() ,name = 'api-news-list'),
    path('phone/list/',views.PhoneListAPIView.as_view() ,name = 'api-phone-list'),
    path('service/list/',views.ServiceListAPIView.as_view() ,name = 'api-service-list'),
    path('service_pic/list/',views.ServicePicListAPIView.as_view() ,name = 'api-service_pic-list'),
    
    path('follower/list/',views.FollowerListAPIView.as_view() ,name = 'api-follower-list'),
    path('follower/create/',views.FollowerCreateAPIView.as_view() ,name = 'api-follower-create'),
    

    path('review/list/',views.ReviewListAPIView.as_view() ,name = 'api-review-list'),


    
    
]

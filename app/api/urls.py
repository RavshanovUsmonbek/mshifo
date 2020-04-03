from django.urls import path, include
from . import views

app_name='app-api'

urlpatterns = [
    path('comment/list-create/',views.CommentListAPIView.as_view() ,name = 'comment-list'),

    path('contact/list/',views.ContactListAPIView.as_view() ,name = 'contact-list'),
    path('doctor/list/',views.DoctorListAPIView.as_view() ,name = 'doctor-list'),
    path('hospital_info/list/',views.HospitalInfoListAPIView.as_view() ,name = 'hosp_info-list'),
    path('open_hours/list/',views.OpenningHoursListAPIView.as_view() ,name = 'open_hours-list'),
   
    path('message/create/',views.MessageCreateAPIView.as_view() ,name = 'message-create'),

    path('news/list/',views.NewsListAPIView.as_view() ,name = 'news-list'),
    path('news/<str:slug>/',views.NewsDetailAPIView.as_view() ,name = 'news-detail'),
 
    path('service/list/',views.ServiceListAPIView.as_view() ,name = 'service-list'),
    path('service/<str:slug>/',views.ServiceDetailAPIView.as_view() ,name = 'service-detail'),
    
    path('service_category/list/',views.ServiceCategoryListAPIView.as_view() ,name = 'service_category-list'),

    path('follower/create/',views.FollowerCreateAPIView.as_view() ,name = 'follower-create'),
    

    path('review/list/',views.ReviewListAPIView.as_view() ,name = 'review-list'),


    
    
]

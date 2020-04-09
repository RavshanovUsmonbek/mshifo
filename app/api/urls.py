from django.urls import path, include
from . import views

app_name='app-api'

urlpatterns = [
    path('comment/list-create/',views.CommentListAPIView.as_view() ,name = 'comment-list-create'),
    path('comment/create/',views.CommentCreateAPIView.as_view() ,name = 'comment-create'),
    path('comment/<int:pk>/change/',views.CommentRetrieveUpdateDestroyAPIView.as_view() ,name = 'comment-change'),

    path('contact/list/',views.ContactListAPIView.as_view() ,name = 'contact-list'),
    path('contact/create/',views.ContactCreateAPIView.as_view() ,name = 'contact-create'),
    path('contact/<int:pk>/change/',views.ContactRetrieveUpdateDestroyAPIView.as_view() ,name = 'contact-change'),
    
    path('doctor/list/',views.DoctorListAPIView.as_view() ,name = 'doctor-list'),
    path('doctor/create/',views.DoctorCreateAPIView.as_view() ,name = 'doctor-create'),
    path('doctor/<int:pk>/change/',views.DoctorRetrieveUpdateDestroyAPIView.as_view() ,name = 'doctor-change'),
    
    path('hospital_info/list/',views.HospitalInfoListAPIView.as_view() ,name = 'hosp_info-list'),
    path('hospital_info/create/',views.HospitalInfoCreateAPIView.as_view() ,name = 'hosp_info-create'),
    path('hospital_info/<int:pk>/change/',views.HospitalInfoRetrieveUpdateDestroyAPIView.as_view() ,name = 'hosp_info-change'),
    
    path('open_hours/list/',views.OpenningHoursListAPIView.as_view() ,name = 'open_hours-list'), 
    path('open_hours/create/',views.OpenningHoursCreateAPIView.as_view() ,name = 'open_hours-create'), 
    path('open_hours/<int:pk>/change/',views.OpenningHoursRetrieveUpdateDestroyAPIView.as_view() ,name = 'open_hours-change'), 
    
    path('message/create/',views.MessageCreateAPIView.as_view() ,name = 'message-create'),
    path('message/list/',views.MessageListAPIView.as_view() ,name = 'message-list'),
    path('message/<int:pk>/change/',views.MessageRetrieveUpdateDestroyAPIView.as_view() ,name = 'message-change'),
   
    path('news/list/',views.NewsListAPIView.as_view() ,name = 'news-list'),
    path('news/<str:slug>/',views.NewsDetailAPIView.as_view() ,name = 'news-detail'),
    path('news/create/',views.NewsCreateAPIView.as_view() ,name = 'news-create'),
    path('news/<int:pk>/change/',views.NewsRetrieveUpdateDestroyAPIView.as_view() ,name = 'news-change'),
 
    path('service/list/',views.ServiceListAPIView.as_view() ,name = 'service-list'),
    path('service/create/',views.ServiceCreateAPIView.as_view() ,name = 'service-create'),
    path('service/<str:slug>/',views.ServiceDetailAPIView.as_view() ,name = 'service-detail'),
    path('service/<int:pk>/change/',views.ServiceRetrieveUpdateDestroyAPIView.as_view() ,name = 'service-change'),
    
    path('service_category/list/',views.CategoryListAPIView.as_view() ,name = 'category-list'),
    path('service_category/create/',views.CategoryCreateAPIView.as_view() ,name = 'category-create'),
    path('service_category/<int:pk>/change/',views.CategoryRetrieveUpdateDestroyAPIView.as_view() ,name = 'category-change'),

    path('follower/create/',views.FollowerCreateAPIView.as_view() ,name = 'follower-create'),
    path('follower/list/',views.FollowerListAPIView.as_view() ,name = 'follower-list'),
    path('follower/<int:pk>/change/',views.FollowerRetrieveUpdateDestroyAPIView.as_view() ,name = 'follower-change'),

    path('review/list/',views.ReviewListAPIView.as_view() ,name = 'review-list'),
    path('review/create/',views.ReviewCreateAPIView.as_view() ,name = 'review-create'),
    path('review/<int:pk>/change/',views.ReviewRetrieveUpdateDestroyAPIView.as_view() ,name = 'review-change'),

    path('phone/list/',views.PhoneListAPIView.as_view() ,name = 'phone-list'),
    path('phone/create/',views.PhoneCreateAPIView.as_view() ,name = 'phone-create'),
    path('phone/<int:pk>/change/',views.PhoneRetrieveUpdateDestroyAPIView.as_view() ,name = 'phone-change'),

    path('service_pic/list/',views.ServicePicListAPIView.as_view() ,name = 'service_pic-list'),
    path('service_pic/create/',views.ServicePicCreateAPIView.as_view() ,name = 'service_pic-create'),
    path('service_pic/<int:pk>/change/',views.ServicePicRetrieveUpdateDestroyAPIView.as_view() ,name = 'service_pic-change'),

    
]

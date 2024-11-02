from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'onlinecourse'

urlpatterns = [
    # Home page with a course list view
    path('', views.CourseListView.as_view(), name='index'),
    
    # User registration, login, and logout views
    path('registration/', views.registration_request, name='registration'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    
    # Course detail page
    path('course/<int:pk>/', views.CourseDetailView.as_view(), name='course_details'),
    
    # Enroll in a course
    path('course/<int:course_id>/enroll/', views.enroll, name='enroll'),
    
    # Submit view for creating an exam submission record for a course enrollment
    path('course/<int:course_id>/submit/', views.submit, name='submit'),
    
    # Show exam result view
    path('course/<int:course_id>/submission/<int:submission_id>/result/', views.show_exam_result, name='exam_result'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

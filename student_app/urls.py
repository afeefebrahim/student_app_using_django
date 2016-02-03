from django.conf.urls import patterns, url
from student_app import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^add_details/', views.add_details, name='add_details'),
        url(r'^register/', views.register, name='register'),
        url(r'^login/', views.user_login, name='login'),
        url(r'^logout/',views.user_logout, name='logout'),    
        url('^delete_new/(?P<id>\d+)/$', views.delete_new, name='delete_new')   
        )
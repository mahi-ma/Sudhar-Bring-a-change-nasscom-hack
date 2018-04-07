from django.conf.urls import url
from . import views

app_name = 'change'

urlpatterns = [
    url(r'^$', views.start_page, name='start_page'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),
    url(r'^home/$', views.home_page, name='home_page'),
    url(r'^complaints/$', views.complaint_list, name='complaint_list'),
    url(r'^complaint/(?P<pk>[0-9]+)/$', views.complaint_details, name='complaint_details'),
    url(r'^complaint/new/$', views.complaint_new, name='complaint_new'),


]

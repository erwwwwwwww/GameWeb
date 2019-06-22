from django.conf.urls import url
from . import views

app_name = 'article'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^game/(?P<pk>[0-9]+)/$', views.gameDetail, name='gamedetail'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.postDetail, name='postdetial'),
    url(r'^gamecategory/$', views.gamecategory, name='gamecategory'),
    url(r'postcategory/$', views.postcategory, name='postcategory'),
    url(r'contact/$', views.contact, name='contact'),
    url(r'^register/$', views.userRegister, name='register'),
    url(r'^login/$', views.userLogin, name='login'),

]

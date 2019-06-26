from django.conf.urls import url
from . import views

app_name = 'article'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^game/(?P<pk>[0-9]+)/$', views.gameDetail, name='gamedetail'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.postDetail, name='postdetial'),
    url(r'^gamecategory/$', views.GameCategoryView.as_view(), name='gamecategory'),
    url(r'postcategory/$', views.PostCategoryView.as_view(), name='postcategory'),
    url(r'contact/$', views.contact, name='contact'),
    url(r'^register/$', views.userRegister, name='register'),
    url(r'^login/$', views.userLogin, name='login'),
    url(r'^userLogout/$', views.userLogout, name='logout'),
    url(r'^userinfo/$', views.userInfo, name='userinfo')

]

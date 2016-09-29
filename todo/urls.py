from django.conf.urls import url

from . import views

app_name ='todo'
urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^done/$', views.done, name='done'),
    url(r'^(?P<option>[a-zA-Z]+)/sdone/$',views.sDone,name='sDone'),
    url(r'^(?P<option>[a-zA-Z]+)/daylist/$',views.dayList,name='dayList'),
]
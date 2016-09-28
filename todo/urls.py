from django.conf.urls import url

from . import views

app_name ='todo'
urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^(?P<option>[a-zA-Z]+)/daylist/$',views.dayList,name='dayList'),
    url(r'^(?P<option>[a-zA-Z]+)/(?P<item_id_list>[0-9]+)/done/$',views.done,name='done'),
]
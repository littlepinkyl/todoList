from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Todoitem
from django.urls import reverse
from django.utils import timezone
# from django.template import loader
import datetime
from django.shortcuts import render, get_object_or_404


#import datetime
#start_date = datetime.date(2005, 1, 1)
#end_date = datetime.date(2005, 3, 31)
#Entry.objects.filter(pub_date__range=(start_date, end_date))


#Entry.objects.filter(pub_date__date=datetime.date(2005, 1, 1))
#Entry.objects.filter(pub_date__date__gt=datetime.date(2005, 1, 1))

#get today's datetime
#import datetime
#now_time = datetime.datetime.now()
#now_time.day/month/year

#get monday's day
#monday = now_time+datetime.timedelta(days= -datetime.datetime.weekday(now_time))
#get this sunday's day
#sunday = monday+datetime.timedelta(days=6)

nav_conf = [{'option': 0,
             'code': 'today',
             'text': 'today',
             'selected': False},
            {'option': 1,
             'code': 'tomorrow',
             'text': 'tomorrow',
             'selected': False},
            {'option': 7,
             'code': 'thisWeek',
             'text': 'this week',
             'selected': False},
            {'option': 14,
             'code': 'nextWeek',
             'text': 'next week',
             'seelcted': False},
            {'option': -1,
             'code': 'remain',
             'text': 'remain',
             'selected': False},
            {'option': 999,
             'code': 'all',
             'text': 'all',
             'selected': False}
            ]


# Create your views here.
def index(request):
    for i in nav_conf:
        i['selected']=False
    todo_list=Todoitem.objects.order_by('deadline_time')
    context = {
        'todo_list': todo_list,
        'nav_conf': nav_conf,
    }
    return render(request,'todo/index.html',context)

def dayList(request,option):
    for i in nav_conf:
        i['selected']=False
    #0,1,7,14,-1
    now_time = datetime.datetime.now()
    #nav_conf = [[0,'today','today',False],[1,'tomorrow','tomorrow',False],[7,'thisWeek','this week',False],[14,'nextWeek','next week',False],[-1,'remain','remain',False]]
    if option == 'today':
        todo_list=Todoitem.objects.filter(deadline_time__date=datetime.date(now_time.year,now_time.month,now_time.day)).order_by('deadline_time')
        for i in nav_conf:
            if i['code'] == option:
                i['selected']=True
                break

    elif option == 'tomorrow':
        tomorrow_time=now_time + datetime.timedelta(days=1)
        todo_list = Todoitem.objects.filter(deadline_time__date=datetime.date(tomorrow_time.year,tomorrow_time.month,tomorrow_time.day)).order_by('deadline_time')
        for i in nav_conf:
            if i['code'] == option:
                i['selected']=True
                break

    elif option == 'remain':
        todo_list = Todoitem.objects.filter(isDone__exact=False).order_by('deadline_time')
        for i in nav_conf:
            if i['code'] == option:
                i['selected']=True
                break
    elif option == 'all':
        todo_list = Todoitem.objects.order_by('deadline_time').order_by('deadline_time')
        for i in nav_conf:
            if i['code'] == option:
                i['selected']=True

    else :
        monday = now_time + datetime.timedelta(days=-datetime.datetime.weekday(now_time))
        monday_date = datetime.datetime.date(monday)
        sunday = monday + datetime.timedelta(days=6)
        sunday_date = datetime.datetime.date(sunday)
        if option == 'thisWeek':
            todo_list= Todoitem.objects.filter(deadline_time__range=(monday_date,sunday_date)).order_by('deadline_time')
            for i in nav_conf:
                if i['code'] == option:
                    i['selected']= True
                    break
        elif option == 'nextWeek':
            next_monday=sunday + datetime.timedelta(days=1)
            next_sunday= next_monday + datetime.timedelta(days=6)
            next_monday_date = datetime.datetime.date(next_monday)
            next_sunday_date = datetime.datetime.date(next_sunday)
            todo_list= Todoitem.objects.filter(deadline_time__range=(next_monday_date,next_sunday_date)).order_by('deadline_time')
            for i in nav_conf:
                if i['code'] == option:
                    i['selected']= True
                    break

    context = {
        'todo_list': todo_list,
        'nav_conf':nav_conf,
        'option':option
    }
    return render(request,'todo/daylist.html',context)

def done(request):
    item_id_list =  request.POST.getlist("todo_selected_list")
    for item_id in item_id_list:
        item = get_object_or_404(Todoitem,pk=item_id)
        item.doIt()
        item.save()
    #reverse first parameters if t odo:index it will be ok
    return HttpResponseRedirect(reverse('todo:index'))


def sDone(request,option):
    item_id_list =  request.POST.getlist("todo_selected_list")
    for item_id in item_id_list:
        item = get_object_or_404(Todoitem,pk=item_id)
        item.doIt()
        item.save()


    return HttpResponseRedirect(reverse('todo:dayList',args=(option,)))





#filter(created_time___date=datetime.date(year,month,day)
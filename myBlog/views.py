from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
import datetime as dt
# Create your views here.
def hello(request):
    return HttpResponse('Hello world')

def currentDatetime(request):
    now = dt.datetime.now()
    return render_to_response('time.html', {'currenttime':now})
    # t = get_template('time.html')
    # c = Context({'currenttime':now})
    # html = t.render(c)
    # return HttpResponse(html)

def timeAhead(request, ahead):
    try:
        offset = int(ahead)
    except ValueError:
        raise Http404()
    newdt = dt.datetime.now()+dt.timedelta(hours=offset)
    # t = get_template('time.html')
    # c = Context({'offset':offset,'newdt':newdt})
    # html = t.render(c)
    # return HttpResponse(html)
    return render_to_response('plustime.html',{'offset':offset,'newdt':newdt})

def showreq(request):
    ua = request.META.get('HTTP_USER_AGENT', 'UNKnown')
    path = request.path
    referrer = request.META.get('HTTP_REFERER', 'Not Exsit')
    ra = request.META.get('REMOTE_ADDR', 'UNKnown')
    reqmeta = request.META;

    return render_to_response('showreq.html',{'reqmeta':reqmeta,
            'ua':ua, 'path':path,'referrer':referrer,'ra':ra})

def searchform(request):
    if 'q' in request.GET:
        message = 'You have searched for %s' % request.GET['q']
    else:
        message = 'Nothing input'
    return HttpResponse(message)#render_to_response('searchform.html')
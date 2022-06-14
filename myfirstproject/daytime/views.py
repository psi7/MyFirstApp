from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
import datetime
from datetime import datetime
# Create your views her

def index(request):
    current_datetime = datetime.today()
    #weekday=current_datetime.weekday()
    weekday=datetime.today().weekday()
    context= {"name":3,"weekend":weekday}
    #html = "<html><body><b>Current Date and Time Value:</b> %s</body></html>" % current_datetime
    return render(request,'showtime/index.html',context)##return html file
    ##return HttpResponse(html)
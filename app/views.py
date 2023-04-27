from django.shortcuts import render
import filters
import datetime
# Create your views here.
def built_in_filter(request):
    dt=datetime.datetime.now()
    d={'FO':'HOW aRe YoU?','dt':dt,'v':3}
    return render(request,'B_filter.html',d)
from django.shortcuts import render
from django.http import HttpResponse
from .models import SitePropertis
from staicsitecontent.models import *
# Create your views here.

def home(request):
    cc = Category.objects.all()
    SiteTitle = SitePropertis.objects.get(
        property_name="site_title"
    )
    IndexPageTitle = SitePropertis.objects.get(
        property_name="index_page_title"
    )
    IndexPageSubTitle = SitePropertis.objects.get(
        property_name="index_page_subtitle"
    )
    data = {
            'SiteTitle' : SiteTitle.property_data,
            'IndexPageTitle' : IndexPageTitle.property_data,
            'IndexPageSubTitle' : IndexPageSubTitle.property_data,
            'cat' : cc
    }
    return render(request, "mainpage/index.html", context=data)
'''
def home(request):
    centers_list = Center.objects.all()
    SiteTitle = SitePropertis.objects.get(
        property_name="site_title"
    )
    IndexPageTitle = SitePropertis.objects.get(
        property_name="index_page_title"
    )
    IndexPageSubTitle = SitePropertis.objects.get(
        property_name="index_page_subtitle"
    )
    data = {
            'SiteTitle' : SiteTitle.property_data,
            'IndexPageTitle' : IndexPageTitle.property_data,
            'IndexPageSubTitle' : IndexPageSubTitle.property_data,
            'cat' : centers_list
    }
    return render(request, "mainpage/index.html", context=data)
'''
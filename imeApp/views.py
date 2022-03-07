from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.
def main(request):
    companys = Company.objects.all()
    analytics = Analytics.objects.all()
    context = {
        'companys' : companys,
        'analytics' : analytics,
    }
    return render(request, 'main.html', context)
    
# 디테일 연결
def detail(request, id):
    detail_data = get_object_or_404(Company, pk=id)
    context = {
        'term' : detail_data.term,
        'meaning' : detail_data.meaning,
    }
    return render(request, 'main_detail.html', context)

def analytics(request, id):
    detail_data = get_object_or_404(Analytics, pk=id)
    context = {
        'term' : detail_data.term,
        'meaning' : detail_data.meaning,
    }
    return render(request, 'Analytics.html', context)
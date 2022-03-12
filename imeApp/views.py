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
        'keyword' : detail_data.keyword,
    }
    return render(request, 'main_detail.html', context)

# 카테고리별 연결
def analytic(request):
    analytics = Analytics.objects.all()
    context = {
        'analytics' : analytics,
    }
    return render(request, 'analy_main.html', context)
def analytics(request, id):
    detail_data = get_object_or_404(Analytics, pk=id)
    context = {
        'term' : detail_data.term,
        'meaning' : detail_data.meaning,
    }
    return render(request, 'Analytics.html', context)

# 카테고리별 연결
def myAnthropometry(request):
    anthropometrys = Anthropometry.objects.all()
    context = {
        'anthropometrys' : anthropometrys,
    }
    return render(request, 'Anthro_main.html', context)

def myAnthropometrys(request, id):
    detail_data = get_object_or_404(Anthropometry, pk=id)
    context = {
        'term' : detail_data.term,
        'meaning' : detail_data.meaning,
    }
    return render(request, 'Anthro.html', context)
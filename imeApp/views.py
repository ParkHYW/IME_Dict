from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.
def main(request):
    companys = Company.objects.all()
    context = {
        'companys' : companys,
        'analytics' : analytics,

    }
    return render(request, 'main.html',context)
# 디테일 연결
def detail(request, id):
    detail_data = get_object_or_404(Company, pk=id)
    context = {
        'term' : detail_data.term,
        'meaning' : detail_data.meaning,
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

# 카테고리별 연결
def myComputer(request):
    Computers = Computer.objects.all()
    context = {
        'Computers' : Computers,
    }
    return render(request, 'computer_main.html', context)
def myComputers(request, id):
    detail_data = get_object_or_404(Computer, pk=id)
    context = {
        'term' : detail_data.term,
        'meaning' : detail_data.meaning,
    }
    return render(request, 'Computers.html', context)

    # 카테고리별 연결
def myCost(request):
    Costs = Cost.objects.all()
    context = {
        'Costs' : Costs,
    }
    return render(request, 'Cost_main.html', context)
def myCosts(request, id):
    detail_data = get_object_or_404(Cost, pk=id)
    context = {
        'term' : detail_data.term,
        'meaning' : detail_data.meaning,
    }
    return render(request, 'Costs.html', context)

    # 카테고리별 연결
def myDistribution(request):
    Distributions = Distribution.objects.all()
    context = {
        'Distributions' : Distributions,
    }
    return render(request, 'Distribution_main.html', context)
def myDistributions(request, id):
    detail_data = get_object_or_404(Distribution, pk=id)
    context = {
        'term' : detail_data.term,
        'meaning' : detail_data.meaning,
    }
    return render(request, 'Distributions.html', context)

# 카테고리별 연결
def myEmployee(request):
    Employees = Employee.objects.all()
    context = {
        'Employees' : Employees,
    }
    return render(request, 'Employee_main.html', context)
def myEmployees(request, id):
    detail_data = get_object_or_404(Employee, pk=id)
    context = {
        'term' : detail_data.term,
        'meaning' : detail_data.meaning,
    }
    return render(request, 'Employees.html', context)

# 카테고리별 연결
def myEngineering(request):
    Engineerings = Engineering.objects.all()
    context = {
        'Engineerings' : Engineerings,
    }
    return render(request, 'Engineering_main.html', context)
def myEngineerings(request, id):
    detail_data = get_object_or_404(Engineering, pk=id)
    context = {
        'term' : detail_data.term,
        'meaning' : detail_data.meaning,
    }
    return render(request, 'Engineerings.html', context)

# 카테고리별 연결
def myFacility(request):
    Facilitys = Facility.objects.all()
    context = {
        'Facilitys' : Facilitys,
    }
    return render(request, 'Facility_main.html', context)
def myFacilitys(request, id):
    detail_data = get_object_or_404(Facility, pk=id)
    context = {
        'term' : detail_data.term,
        'meaning' : detail_data.meaning,
    }
    return render(request, 'Facilitys.html', context)

# 카테고리별 연결
def myHuman(request):
    Humans = Human.objects.all()
    context = {
        'Humans' : Humans,
    }
    return render(request, 'Human_main.html', context)
def myHumans(request, id):
    detail_data = get_object_or_404(Human, pk=id)
    context = {
        'term' : detail_data.term,
        'meaning' : detail_data.meaning,
    }
    return render(request, 'Humans.html', context)

# 카테고리별 연결
def myManagement(request):
    Managements = Management.objects.all()
    context = {
        'Managements' : Managements,
    }
    return render(request, 'Management_main.html', context)
def myManagements(request, id):
    detail_data = get_object_or_404(Management, pk=id)
    context = {
        'term' : detail_data.term,
        'meaning' : detail_data.meaning,
    }
    return render(request, 'Managements.html', context)

# 카테고리별 연결
def myManufacturing(request):
    Manufacturings = Manufacturing.objects.all()
    context = {
        'Manufacturings' : Manufacturings,
    }
    return render(request, 'Manufacturing_main.html', context)
def myManufacturings(request, id):
    detail_data = get_object_or_404(Manufacturing, pk=id)
    context = {
        'term' : detail_data.term,
        'meaning' : detail_data.meaning,
    }
    return render(request, 'Manufacturings.html', context)

# 카테고리별 연결
def myMaterial(request):
    Materials = new_Materials.objects.all()
    context = {
        'Materials' : Materials,
    }
    return render(request, 'Material_main.html', context)
def myMaterials(request, id):
    detail_data = get_object_or_404(new_Materials, pk=id)
    context = {
        'term' : detail_data.term,
        'meaning' : detail_data.meaning,
    }
    return render(request, 'Materials.html', context)

# 카테고리별 연결
def myOccupational(request):
    Occupationals = Occupational.objects.all()
    context = {
        'Occupationals' : Occupationals,
    }
    return render(request, 'Occupational_main.html', context)
def myOccupationals(request, id):
    detail_data = get_object_or_404(Occupational, pk=id)
    context = {
        'term' : detail_data.term,
        'meaning' : detail_data.meaning,
    }
    return render(request, 'Occupationals.html', context)

# 카테고리별 연결
def myOperation(request):
    Operations = new_Operation.objects.all()
    context = {
        'Operations' : Operations,
    }
    return render(request, 'Operation_main.html', context)
def myOperations(request, id):
    detail_data = get_object_or_404(new_Operation, pk=id)
    context = {
        'term' : detail_data.term,
        'meaning' : detail_data.meaning,
    }
    return render(request, 'Operations.html', context)

# 카테고리별 연결
def myOrganization(request):
    Organizations = Organization.objects.all()
    context = {
        'Organizations' : Organizations,
    }
    return render(request, 'Organization_main.html', context)
def myOrganizations(request, id):
    detail_data = get_object_or_404(Organization, pk=id)
    context = {
        'term' : detail_data.term,
        'meaning' : detail_data.meaning,
    }
    return render(request, 'Organizations.html', context)

# 카테고리별 연결
def myQuality(request):
    Qualitys = Quality.objects.all()
    context = {
        'Qualitys' : Qualitys,
    }
    return render(request, 'Quality_main.html', context)
def myQualitys(request, id):
    detail_data = get_object_or_404(Quality, pk=id)
    context = {
        'term' : detail_data.term,
        'meaning' : detail_data.meaning,
    }
    return render(request, 'Qualitys.html', context)

# 카테고리별 연결
def myWork(request):
    Works = Work.objects.all()
    context = {
        'Works' : Works,
    }
    return render(request, 'Work_main.html', context)
def myWorks(request, id):
    detail_data = get_object_or_404(Work, pk=id)
    context = {
        'term' : detail_data.term,
        'meaning' : detail_data.meaning,
    }
    return render(request, 'Works.html', context)
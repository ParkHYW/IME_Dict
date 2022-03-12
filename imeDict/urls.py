"""imeDict URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from imeApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name="main"),
    path('detail/<int:id>/', detail, name="detail"),
    path('analytics', analytic, name="analytic"), # analytics
    path('analytics/<int:id>/', analytics, name="analytics"), #
    path('Anthropometry', myAnthropometry, name="Anthropometry"), # Anthropometry
    path('Anthropometrys/<int:id>/', myAnthropometrys, name="Anthropometrys"), #
    path('Computer', myComputer, name="Computer"), # Computer
    path('Computers/<int:id>/', myComputers, name="Computers"), #
    path('Cost', myCost, name="Cost"), # Cost
    path('Costs/<int:id>/', myCosts, name="Costs"), #
    path('Distribution', myDistribution, name="Distribution"), # Distribution
    path('Distributions/<int:id>/', myDistributions, name="Distributions"), #
    path('Employee', myEmployee, name="Employee"), # Employee
    path('Employees/<int:id>/', myEmployees, name="Employees"), 
    path('Engineering', myEngineering, name="Engineering"), # Engineering
    path('Engineerings/<int:id>/', myEngineerings, name="Engineerings"), #
    path('Facility', myFacility, name="Facility"), # Facility
    path('Facilitys/<int:id>/', myFacilitys, name="Facilitys"), #
    path('Human', myHuman, name="Human"), # Human
    path('Humans/<int:id>/', myHumans, name="Humans"), #
    path('Management', myManagement, name="Management"), # Management
    path('Managements/<int:id>/', myManagements, name="Managements"), #
    path('Manufacturing', myManufacturing, name="Manufacturing"), # Manufacturing
    path('Manufacturings/<int:id>/', myManufacturings, name="Manufacturings"), #
    path('Material', myMaterial, name="Material"), # Material
    path('Materials/<int:id>/', myMaterials, name="Materials"), #
    path('Occupational', myOccupational, name="Occupational"), # Occupational
    path('Occupationals/<int:id>/', myOccupationals, name="Occupationals"), #
    path('Operation', myOperation, name="Operation"), # Operation
    path('Operations/<int:id>/', myOperations, name="Operations"), #
    path('Organization', myOrganization, name="Organization"), # Organization
    path('Organizations/<int:id>/', myOrganizations, name="Organizations"), #
    path('Quality', myQuality, name="Quality"), # Quality
    path('Qualitys/<int:id>/', myQualitys, name="Qualitys"), #
    path('Work', myWork, name="Work"), # Work
    path('Works/<int:id>/', myWorks, name="Works"), #
]
urlpatterns += \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
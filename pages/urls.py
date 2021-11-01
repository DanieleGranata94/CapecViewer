"""URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from . import views

from pages.views import (

    home_view,

    )


urlpatterns = [

    path('', views.home_view, name='home'),
	url(r'^MetaSelection', views.MetaSelection_view, name='MetaSelection'),
	url(r'^ResultsWizard', views.ResultsWizard_view, name='ResultsWizard'),
	url(r'^StandardSelection', views.StandardSelection_view, name='StandardSelection'),
    url(r'^home', views.home_view, name='home'),
	url(r'^id', views.id_view, name='id'),
    url(r'^parent', views.parent_view, name='parent'),
	url(r'^name', views.name_view, name='name'),
	url(r'^query', views.query_view, name='query'),
	path('details/<int:id>/', views.details_view, name='details'),
	
	url(r'^DomainsOfAttack', views.DomainsOfAttack_view, name='DomainsOfAttack'),
	url(r'^MechanismsOfAttack', views.MechanismsOfAttack_view, name='MechanismsOfAttack'),
	url(r'^MobileDevicePatterns', views.MobileDevicePatterns_view, name='MobileDevicePatterns'),
	url(r'^DeprecatedEntries', views.DeprecatedEntries_view, name='DeprecatedEntries'),
	url(r'^MetaAbstractions', views.MetaAbstractions_view, name='MetaAbstractions'),
	url(r'^StandardAbstractions', views.StandardAbstractions_view, name='StandardAbstractions'),
	url(r'^DetailedAbstractions', views.DetailedAbstractions_view, name='DetailedAbstractions'),
	url(r'^wizard', views.wizard_view, name='wizard'),







]
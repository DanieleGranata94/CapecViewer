from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render, get_object_or_404

#import delle classi
from data.models import *


def home_view(request):

    return render(request, "pages/home.html")

def query_view(request):

    return render(request, "pages/query.html")

def wizard_view(request):

    return render(request, "pages/wizard.html")




def details_view(request, id):

    q = DomainsOfAttack.objects.filter(id=id)
    #print(q)
    context = {
        'object': q
    }

    return render(request, "pages/details.html", context)

#selezione delle views
def DomainsOfAttack_view(request):

    obj = DomainsOfAttack.objects.all()
    context = {
        'object': obj
    }

    return render(request, "pages/list.html", context)

def MechanismsOfAttack_view(request):

    obj = MechanismsOfAttack.objects.all()
    context = {
        'object': obj
    }

    return render(request, "pages/list.html", context)

def DeprecatedEntries_view(request):

    obj = DeprecatedEntries.objects.all()
    context = {
        'object': obj
    }

    return render(request, "pages/list.html", context)

def MobileDevicePatterns_view(request):

    obj = MobileDevicePatterns.objects.all()
    context = {
        'object': obj
    }

    return render(request, "pages/list.html", context)

def MetaAbstractions_view(request):

    obj = MetaAbstractions.objects.all()
    context = {
        'object': obj
    }

    return render(request, "pages/list.html", context)

def MetaSelection_view(request):

    obj = MetaAbstractions.objects.all()
    filteredobj=set()
    #delete DEPRECATED threats
    for e in obj:
        if(not(e.name.startswith("DEPRECATED"))):
            filteredobj.add(e)

    context = {
        'object': filteredobj
    }
    return render(request, "pages/MetaSelection.html", context)

@csrf_exempt
def StandardSelection_view(request):

    context={}
    childrens=set()
    if request.method == 'POST':
        list_selected_ids = request.POST.getlist('checkboxSelection')
        print(list_selected_ids)

        for e in list_selected_ids:
            query_set_result=(DomainsOfAttack.objects.filter(relatedattackpatterns__contains="::NATURE:ChildOf:CAPEC ID:"+e+"::"))
            for e in query_set_result:
                childrens.add(e)

        context = {
            'meta' : list_selected_ids,
            'object': childrens
        }

    return render(request, "pages/StandardSelection.html", context)

@csrf_exempt
def ResultsWizard_view(request):

    context={}
    resultSet=set()
    if request.method == 'POST':
        list_selected_ids = request.POST.getlist('checkboxSelection')
        for e in list_selected_ids:
            query_set_result=(DomainsOfAttack.objects.filter(relatedattackpatterns__contains="::NATURE:ChildOf:CAPEC ID:"+str(e)+"::"))
            for el in query_set_result:
                query_set_result2=(DomainsOfAttack.objects.filter(relatedattackpatterns__contains="::NATURE:ChildOf:CAPEC ID:"+str(el.id)+"::"))
                resultSet.add(el)
                #for standard childOf standard
                for elm in query_set_result2:
                    resultSet.add(elm)

        context = {
            'standard' : list_selected_ids,
            'object': resultSet
        }

    return render(request, "pages/ResultsWizard.html", context)



def searchDetails(id,resultSet):
    print(resultSet)
    query_set_result=(DomainsOfAttack.objects.filter(relatedattackpatterns__contains="::NATURE:ChildOf:CAPEC ID:"+str(id)+"::"))
    for e in query_set_result:
        resultSet.add(e)
        print(str(id)+" "+str(e.id))
        return searchDetails(e.id,resultSet)





def StandardAbstractions_view(request):

    obj = StandardAbstractions.objects.all()
    context = {
        'object': obj
    }

    return render(request, "pages/list.html", context)

def DetailedAbstractions_view(request):

    obj = DetailedAbstractions.objects.all()
    context = {
        'object': obj
    }

    return render(request, "pages/list.html", context)


#query id
@csrf_exempt
def id_view(request):

    idval = "null"
    idval = request.POST.get("id_query")

    obj = DomainsOfAttack.objects.filter(id=idval)

    if obj.exists():
        context = {
           'object': obj
        }
        return render(request, "pages/id_results.html", context)
    else:
        return render(request, "pages/id_results.html", {})


#query ParentOf
@csrf_exempt
def parent_view(request):

    idval = "null"
    idval = request.POST.get("id_query")

    obj = DomainsOfAttack.objects.filter(relatedattackpatterns__contains=":" + idval + "::")

    if obj.exists():
        context = {
           'object': obj
        }
        return render(request, "pages/parent_results.html", context)
    else:
        return render(request, "pages/parent_results.html", {})


#query name
@csrf_exempt
def name_view(request):

    name = " "
    name = request.POST.get("name")

    obj = DomainsOfAttack.objects.filter(name__icontains=name)

    if obj.exists():
        context = {
           'object': obj
        }
        return render(request, "pages/name_results.html", context)
    else:
        return render(request, "pages/name_results.html", {})
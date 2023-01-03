
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from .models import RateSearch
from .forms import RateSearchForm

def activity(request):

    if "user_name" in request.session:
        print("ユーザー名："+request.session["user_name"])

    context = {}
    return render(request,"illuviumsite/activity.html",context)

def augments(request):
    context = {}
    return render(request,"illuviumsite/augments.html",context)

def map_crymzonwaste(request):
    context = {}
    return render(request,"illuviumsite/map_crymzonwaste.html",context)

def capturerate(request):

    context             = {}
    if request.method == 'POST':
        form = RateSearchForm(request.POST)
        print(form.is_valid())
        print(form)

        if form.is_valid():
            form.save()
    else:
        pass
        #context["userFrom"]   = RateSearch.objects.all()

        #選択肢のデータを手に入れる(都道府県文字列のリストを作る。リストの内包表記)
        #context["IlluvialTier"]  = [ p[0] for p in RateSearch.IlluvialTier.field.choices ]
        #context["IlluvialStage"]  = [ p[0] for p in RateSearch.IlluvialStage.field.choices ]
        #return render(request,"illuviumsite/capturerate.html",context)

    #context["IlluvialTier"]  = [ p[0] for p in RateSearch.IlluvialTier.field.choices ]
    #context["IlluvialStage"]  = [ p[0] for p in RateSearch.IlluvialStage.field.choices ]
    context["rateSearch"]   = RateSearch.objects.all()
 
    #detail.htmlへデータを渡す
    return render(request, 'illuviumsite/capturerate.html',context)



def patchnote(request):
    context = {}
    return render(request,"illuviumsite/patchnote.html",context)

def resources(request):
    context = {}
    return render(request,"illuviumsite/resources.html",context)

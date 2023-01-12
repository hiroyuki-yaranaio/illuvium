
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
    print('capturerate')
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
    data = RateSearch.objects.all()
    t0s=[0,0,0,0,0,0]
    t1s=[0,0,0,0,0,0]
    t2s=[0,0,0,0,0,0]
    t3s=[0,0,0,0,0,0]
    t4s=[0,0,0,0,0,0]
    t5s=[0,0,0,0,0,0]

    t0f=[0,0,0,0,0,0]
    t1f=[0,0,0,0,0,0]
    t2f=[0,0,0,0,0,0]
    t3f=[0,0,0,0,0,0]
    t4f=[0,0,0,0,0,0]
    t5f=[0,0,0,0,0,0]

    for d in data:
        if d.IlluvialTier == 0:
            if d.Captured == 1:
                t0s[d.ShardTier] += 1
            else:
                t0f[d.ShardTier] += 1
        elif d.IlluvialTier == 1:
            if d.Captured == 1:
                t1s[d.ShardTier] += 1
            else:
                t1f[d.ShardTier] += 1
        elif d.IlluvialTier == 2:
            if d.Captured == 1:
                t2s[d.ShardTier] += 1
            else:
                t2f[d.ShardTier] += 1
        elif d.IlluvialTier == 3:
            if d.Captured == 1:
                t3s[d.ShardTier] += 1
            else:
                t3f[d.ShardTier] += 1
        elif d.IlluvialTier == 4:
            if d.Captured == 1:
                t4s[d.ShardTier] += 1
            else:
                t4f[d.ShardTier] += 1
        elif d.IlluvialTier == 5:
            if d.Captured == 1:
                t5s[d.ShardTier] += 1
            else:
                t5f[d.ShardTier] += 1
    print(t0s,t0f)
    print(t1s,t1f)
    print(t2s,t2f)
    print(t3s,t3f)
    print(t4s,t4f)
    print(t5s,t5f)

    context['ratet0s0'] = 0
    context['ratet1s1'] = 0
    context['ratet2s2'] = 0
    context['ratet3s3'] = 0
    context['ratet4s4'] = 0

    try:
        context['ratet0s0'] = round(t0s[0]/(t0s[0]+t0f[0])*100,1)
        context['ratet1s1'] = round(t1s[1]/(t1s[1]+t1f[1])*100,1)
        context['ratet2s2'] = round(t2s[2]/(t2s[2]+t2f[2])*100,1)
        context['ratet3s3'] = round(t2s[3]/(t2s[3]+t2f[3])*100,1)
        context['ratet4s4'] = round(t2s[4]/(t2s[4]+t2f[4])*100,1)
    except Exception as e:
        print(e)



        
    #context["rateSearch"]   = RateSearch.objects.all()
 
    #detail.htmlへデータを渡す
    return render(request, 'illuviumsite/capturerate.html',context)



def patchnote(request):
    context = {}
    return render(request,"illuviumsite/patchnote.html",context)

def resources(request):
    context = {}
    return render(request,"illuviumsite/resources.html",context)

def google(request):
    context = {}
    return render(request,"illuviumsite/google425ab4421bc49419.html",context)



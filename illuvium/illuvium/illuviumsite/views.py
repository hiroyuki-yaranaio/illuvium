
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

def leaderboard(request):
    context = {}
    return render(request,"illuviumsite/leaderboard.html",context)


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
    t0s1s=[0,0,0,0,0,0]
    t1s1s=[0,0,0,0,0,0]
    t2s1s=[0,0,0,0,0,0]
    t3s1s=[0,0,0,0,0,0]
    t4s1s=[0,0,0,0,0,0]
    t5s1s=[0,0,0,0,0,0]

    t0s1f=[0,0,0,0,0,0]
    t1s1f=[0,0,0,0,0,0]
    t2s1f=[0,0,0,0,0,0]
    t3s1f=[0,0,0,0,0,0]
    t4s1f=[0,0,0,0,0,0]
    t5s1f=[0,0,0,0,0,0]

    for d in data:
        if d.IlluvialTier == 0:
            if d.Captured == 1:
                t0s1s[d.ShardTier] += 1
            else:
                t0s1f[d.ShardTier] += 1
        elif d.IlluvialTier == 1:
            if d.Captured == 1:
                t1s1s[d.ShardTier] += 1
            else:
                t1s1f[d.ShardTier] += 1
        elif d.IlluvialTier == 2:
            if d.Captured == 1:
                t2s1s[d.ShardTier] += 1
            else:
                t2s1f[d.ShardTier] += 1
        elif d.IlluvialTier == 3:
            if d.Captured == 1:
                t3s1s[d.ShardTier] += 1
            else:
                t3s1f[d.ShardTier] += 1
        elif d.IlluvialTier == 4:
            if d.Captured == 1:
                t4s1s[d.ShardTier] += 1
            else:
                t4s1f[d.ShardTier] += 1
        elif d.IlluvialTier == 5:
            if d.Captured == 1:
                t5s1s[d.ShardTier] += 1
            else:
                t5s1f[d.ShardTier] += 1
    print("T0S1",t0s1s,t0s1f)
    print("T1S1",t1s1s,t1s1f)
    print("T2S1",t2s1s,t2s1f)
    print("T3S1",t3s1s,t3s1f)
    print("T4S1",t4s1s,t4s1f)
    print("T5S1",t5s1s,t5s1f)

    context['ratet0s0'] = 0
    context['ratet1s1'] = 0
    context['ratet2s1'] = 0
    context['ratet2s2'] = 0
    context['ratet3s2'] = 0
    context['ratet3s3'] = 0
    context['ratet4s3'] = 0
    context['ratet4s4'] = 0
    context['ratet5s4'] = 0
    context['ratet5s5'] = 0

    try:
        context['ratet0s1'] = round(t0s1s[0]/(t0s1s[0]+t0s1f[0])*100,1)
    except Exception as e:
        print(e)
    try:
        context['ratet1s1'] = round(t1s1s[1]/(t1s1s[1]+t1s1f[1])*100,1)
    except Exception as e:
        print(e)
    try:
        context['ratet2s1'] = round(t2s1s[1]/(t2s1s[1]+t2s1f[1])*100,1)
    except Exception as e:
        print(e)
    try:
        context['ratet2s2'] = round(t2s1s[2]/(t2s1s[2]+t2s1s[2])*100,1)
    except Exception as e:
        print(e)
    try:
        context['ratet3s2'] = round(t3s1s[2]/(t3s1s[2]+t3s1f[2])*100,1)
    except Exception as e:
        print(e)
    try:
        context['ratet3s3'] = round(t3s1s[3]/(t3s1s[3]+t3s1f[3])*100,1)
    except Exception as e:
        print(e)
    try:
        context['ratet4s3'] = round(t4s1s[3]/(t4s1s[3]+t4s1f[3])*100,1)
    except Exception as e:
        print(e)
    try:
        context['ratet4s4'] = round(t4s1s[4]/(t4s1s[4]+t4s1f[4])*100,1)
    except Exception as e:
        print(e)
    try:
        context['ratet5s4'] = round(t5s1s[4]/(t5s1s[4]+t5s1f[4])*100,1)
    except Exception as e:
        print(e)
    try:
        context['ratet5s5'] = round(t5s1s[5]/(t5s1s[5]+t5s1f[5])*100,1)
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




# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from . forms import UserForm
from pprint import pprint

def signup(request):
    context = {}
    return render(request,"login/signup.html",context)

# 新規登録フォームHTMLへ返す
def showCreateUserForm(request):

    if request.method == 'POST':
        form = UserForm(request.POST)
        print(form.is_valid())
        print(form)

        if form.is_valid():
            form.save()
    else:
        form = UserForm()
        
    # context = {
    #     'form' : form,
    #     'AccountData': models.Account.objects.all(),
    # }
    # return render(request, 'index.html', context)


    #フォームを変数にセット
    #form = UserForm()

    context = {
        'userForm':form,
    }
 
    #detail.htmlへデータを渡す
    return render(request, 'login/signup.html',context)

# 新規登録フォームHTMLへ返す
def signup(request):

    if request.method == 'POST':
        form = UserForm(request.POST)
        print(form.is_valid())
        print(form)

        if form.is_valid():
            form.save()
            request.session['user_name'] = request.POST["Name"]
            print("登録しました")
            # セッションを削除したい場合
            # del request.session['セッション名']
    else:
        form = UserForm()

    #フォームを変数にセット
    form = UserForm()

    context = {
        'userForm':form,
    }
 
    #detail.htmlへデータを渡す
    return render(request, 'login/signup.html',context)

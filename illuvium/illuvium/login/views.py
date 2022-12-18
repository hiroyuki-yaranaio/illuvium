
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from . forms import UserForm

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
def showUsers(request):
    #フォームを変数にセット
    form = UserForm()

    context = {
        'userForm':form,
    }
 
    #detail.htmlへデータを渡す
    return render(request, 'login/signup_complete.html',context)
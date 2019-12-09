from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from .forms import AuthenticationForm, UserCreationForm

def signup(request):
    # 요청을 보낸 사용자가 인증이 되어 있지 않으면 -> 회원가입
    if not request.user.is_authenticated: # is_authenticated -> 로그인
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                auth_login(request, user) 
                return redirect('codi:codi')
        else: # GET
            form = UserCreationForm()
        context = {'form' : form}
        return render(request, 'accounts/signup.html', context)
    else:
        return redirect('accounts/signup.html')   
    
def login(request):
    if request.user.is_authenticated:
        return redirect('codi:codi')
    else:
        if request.method == 'POST':
            form = AuthenticationForm(request, request.POST)
            if form.is_valid(): # 검증
                # 인증을 한 후, save가 아니라 get_user 
                # 누군지 가져오기
                user = form.get_user()
                # user 인증되면 팔찌를 채워
                auth_login(request, user)
                # -> 이 상태에서는 회원가입 페이지로 이동하지 못 함
                # return redirect('codi:codi')
                return redirect('codi:codi')
        else: # GET
            form = AuthenticationForm()
        context = {'form' : form}
        return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('codi:codi')
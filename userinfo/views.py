from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate

from .forms import SignUpForm, ProfileForm

from .models import Profile

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request,'userinfo/profile.html')
    else:
        form = SignUpForm()
    return render(request,'userinfo/signup.html',{'form':form})

def profile_create(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile_detail')
    else:
        form = ProfileForm()
        return render(request,'userinfo/profile-create.html',{'form':form})

def profile_detail(request):
    try:
        profile=Profile.objects.get(user=request.user)
        context={'profile':profile}
    except:
        context={'errmsg':'You have no profile'}
    return render(request,'userinfo/profile-detail.html',context)

def profile_edit(request):
    profile=Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('/registration_app/profile_details/')
    else:
        form = ProfileForm(instance=profile)
        return render(request,'userinfo/edit_profile.html',{'form':form})
# Create your views here.

from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Profile, CustomUsers
from member.models import Post

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.is_active=False
            user.save()
            profile = Profile()
            profile.user = user
            image = request.FILES.get("image")
            if image:
                profile.image = image
            else:
                image = 'default.jpg'
                profile.image = image
            profile.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:        
        form = UserRegisterForm()        
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    profile = Profile.objects.get(user=CustomUsers.objects.get(username = request.user.username))
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, 
                                   request.FILES,
                                   instance=profile)
        if u_form.is_valid() and p_form.is_valid ():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')                          
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=profile)    

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)   



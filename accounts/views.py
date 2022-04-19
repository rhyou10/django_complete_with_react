from pipes import Template
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required 
from django.views.generic import TemplateView, UpdateView
from .models import Profile
from .forms import ProfileFrom

# @login_required
# def profile(request):
#     return render(request, 'accounts/profile.html')
# Create your views here.


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'
    
profile = ProfileView.as_view()

# class ProfileUpdateView(LoginRequiredMixin, UpdateView):
#     model = Profile
#     form_class =  ProfileFrom

# profile_edit =ProfileUpdateView.as_view()

@login_required
def profile_edit(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = None

    if request.method =='POST':
        form = ProfileFrom(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    else:
        form = ProfileFrom(instance=profile)
    return render(request, 'accounts/profile_form.html',{
        'form':form,
    })


def signup(request):
    pass

def logout(request):
    pass
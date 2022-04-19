from urllib import response
from django.contrib.auth import get_user_model, login as auth_login
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required 
from django.views.generic import TemplateView, UpdateView, CreateView
from .models import Profile
from .forms import ProfileFrom
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings


User = get_user_model()
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

class SignUpView(CreateView):
    model = User
    form_class=UserCreationForm
    success_url=settings.LOGIN_REDIRECT_URL
    template_name = 'accounts/sign_up.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object #방금 가입한 유저를 가지고온다
        auth_login(self.request, user) # 회원가입 즉시 로그인했다.
        return  response


signup = SignUpView.as_view()

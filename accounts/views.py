from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, authenticate, login, logout
from .forms import LoginForm, RegistrationForm

User = get_user_model()


class HomeView(TemplateView):
    template_name = "home.html"


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = LoginForm
    succes_url = '/'


class UserRegistrationView(CreateView):
    model = User
    template_name = 'accounts/signup.html'
    form_class = RegistrationForm
    success_url = '/login/'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            try:
                user = form.save()
                
                user.save()
                return HttpResponseRedirect("/login/")
            except Exception as e:
                print(e)
                pass
        
        else:
            return self.form_invalid(form)


def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required(login_url='/login/')
def profile(request):
    context = {
        'segment': 'profile',
    }
    return render(request, 'accounts/profile.html', context)
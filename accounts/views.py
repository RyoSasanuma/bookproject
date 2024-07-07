from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy('list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user, backend='accounts.backends.EmailAuthBackend')
        messages.add_message(self.request, messages.SUCCESS, "会員登録に成功しました。")
        self.object = user
        return HttpResponseRedirect(self.get_success_url())
    
    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "会員登録に失敗しました。")
        return super().form_invalid(form)
    
def logout_view(request):
    logout(request)
    return redirect('login')    

"""
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('top')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})
"""
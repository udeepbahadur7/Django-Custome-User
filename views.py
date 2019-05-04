from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from user.forms import CustomUserCreationForm
from django.contrib import messages
from django.views import generic

# def register(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}!')
#             return redirect('login')
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'registration/signup.html', {'form': form})


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url=reverse_lazy('login')
    template_name = 'registration/signup.html'



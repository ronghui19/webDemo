from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import Group
import json

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import CreateUserForm, ContactModelForm
from .models import Client
from .decorators import unauthenticated_user

# Create your views here.
def homePage(request):
    context = {}
    return render(request, 'accounts/home.html', context)

@unauthenticated_user
def signinPage(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Usernamer or password is incorrect')

    context = {}
    return render(request, 'accounts/signin.html', context) 

@unauthenticated_user
def signupPage(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid:
            user = form.save()
            username = form.cleaned_data['username']

            group = Group.objects.get(name='customer')
            user.groups.add(group)

            Client.objects.create(
                user=user,
                name=user.username,
            )

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/signup.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

# def contactPage(request):
#     form = ContactModelForm()
#     if request.method == "POST":
#         form = ContactModelForm(request.POST)
#         if form.is_valid():
#             human = True
#             form.save()
#             return JsonResponse({
#                 'message': 'success'
#             })
#     return render(request, 'accounts/contact.html', {'form': form})
class contactPage(CreateView):
    template_name = 'accounts/contact.html'
    form_class = ContactModelForm

    def form_invalid(self, form):
        if self.request.is_ajax():
            to_json_response = dict()
            to_json_response['status'] = 0
            to_json_response['form_errors'] = form.errors

            to_json_response['new_cptch_key'] = CaptchaStore.generate_key()
            to_json_response['new_cptch_image'] = captcha_image_url(to_json_response['new_cptch_key'])

            return HttpResponse(json.dumps(to_json_response), content_type='application/json')

    def form_valid(self, form):
        form.save()
        if self.request.is_ajax():
            to_json_response = dict()
            to_json_response['status'] = 1

            to_json_response['new_cptch_key'] = CaptchaStore.generate_key()
            to_json_response['new_cptch_image'] = captcha_image_url(to_json_response['new_cptch_key'])

            return HttpResponse(json.dumps(to_json_response), content_type='application/json')


def aboutPage(request):
    context = {}
    return render(request, 'accounts/about.html', context)
from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User


from django.contrib import messages

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect 
from .forms import RegisterForm, ProfileForm, LoginForm
from .models import Profile


# Create your views here.



def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'Login successful!')
                    return redirect('dashboard:dashboard')  # Redirect to a home page after login
                else:
                    messages.error(request, 'Account is disabled.')
                    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
            else:
                messages.error(request, 'Invalid login credentials.')
                return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        # If the form is not valid or login failed, stay on the sign-in page
        return redirect('signin')  # Redirect to the sign-in page itself if there's an error

    # If it's a GET request, just render the sign-in page
    return render(request, 'signin.html')


def signup (request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password1']
            try:
                user = User.objects.get(username-username)
                messages.success(request, 'Your profile aleardy exists!')
                return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

            except:
                profile =  profile_form.save(commit=False)
                profile.user = user
                profile.save()
                messages.success(request, 'Your profile was create & login successful!')
                #authenticate checks if credentials exists in db
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        if 'next' in request.POST:
                            return redirect(request.POST.get('next'))
                        else:
                            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

                    else:
                        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
                        
                else:
                    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
                
        else:
            print(user_form.errors)
            print(profile_form.errors)
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = RegisterForm()
        profile_form = ProfileForm()
    context = {
      'user_form':user_form,
      'profile_form':profile_form,
    }

    return render(request, 'signup.html', context)



    






def reset(request):
    return render(request, 'reset_password.html')

def forgot(request):
    return render(request , 'forgot_password.html')
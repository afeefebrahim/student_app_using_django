from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from student_app.models import student
from student_app.forms import UserForm,UserProfileForm,studentForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
 
# Create your views here.


def index(request):
    category_list = student.objects.all()
    context_dict = {'categories': category_list}
    return render(request, 'student_app/index.html', context_dict)

def delete_new(request,id):
   u = student.objects.get(pk=id).delete()
   return redirect(index)

def add_details(request):
    if request.method == 'POST':
        form = studentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = studentForm()
        return render(request, 'student_app/add_details.html', {'form': form})

    
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            print profile
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request,
            'student_app/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/student_app/add_details')
            else:
                return HttpResponse("Your student_app account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'student_app/login.html', {})
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/student_app/')
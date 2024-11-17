from django.shortcuts import render, redirect
from tasklogin.models import Login
from tasklogin.forms import LoginForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# Create your views here.

def add(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                return HttpResponse("There was an error saving the form data.")
    else:
        form = LoginForm()  # This line should be outside the if-else

    return render(request, 'index.html', {'form': form})  # Ensure 'index.html' exists

def show(request):
    logins = Login.objects.all()
    return render(request, "show.html", {'loginss': logins})

def edit(request, PhoneNo):
    logins = Login.objects.get(PhoneNo=PhoneNo)
    return render(request, "edit.html", {'logins': logins})

def update(request, PhoneNo):
    logins = get_object_or_404(Login, PhoneNo=PhoneNo)
    
    if request.method == 'POST':
        form = LoginForm(request.POST, instance=logins)
        if form.is_valid():
            form.save()
            return redirect("/show")
    else:
        form = LoginForm(instance=logins)
        
    return render(request, 'edit.html', {'logins': logins})

def destroy(request, PhoneNo):
    # logins = Login.objects.get(PhoneNo=PhoneNo)
    # logins.delete()
    # return redirect("/show")
    logins = get_object_or_404(Login, PhoneNo=PhoneNo)
    logins.delete()
    return redirect("/show")

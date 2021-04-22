from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm, BuildingForm, BuildingTenantForm
from .models import Building, BuildingTenant, Profile
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

def ownersignup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  
            user.profile.name = form.cleaned_data.get('name')
            user.profile.phone = form.cleaned_data.get('phone')
            user.profile.next_of_kin = form.cleaned_data.get('next_of_kin')
            user.profile.is_owner = True
            user.save()
            
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/owner-signup.html', {'form': form})


def tenantsignup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  
            user.profile.name = form.cleaned_data.get('name')
            user.profile.phone = form.cleaned_data.get('phone')
            user.profile.next_of_kin = form.cleaned_data.get('next_of_kin')
            user.profile.is_tenant = True
            user.save()
            
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/tenant-signup.html', {'form': form})

@login_required
def index(request):
    buildings = Building.objects.filter(owner=request.user)
    tenants = Profile.objects.filter(is_tenant=True)

    context = {
        "buildings" : buildings,
        "tenants" : tenants,
    }
    return render(request, 'index.html', context)

@login_required
def create_building(request):
    if request.method == "POST":
        form = BuildingForm(request.POST)

        if form.is_valid():
            building = form.save(commit=False)
            building.owner = request.user
            building.save()

        return redirect('home')

    else:
        form = BuildingForm()

    context = {
        "form" : form
    }

    return render(request, 'create-building.html', context)

@login_required
def building_tenants(request, building_id):
    building_tenants = BuildingTenant.objects.filter(id=building_id)
    print(building_tenants)
  
    context = {
        "building_tenants" : building_tenants
    }
  
    return render(request, "buildingtenants.html", context)


@login_required
def edit_building(request, id):
    obj = get_object_or_404(Building, id = id)
  
    form = BuildingForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect("home")
  
    context = {
        "form" : form
    }
  
    return render(request, "edit-building.html", context)

@login_required
def edit_building_tenants(request, id):
    obj = get_object_or_404(BuildingTenant, id = id)
  
    form = BuildingTenantForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect("home")
    
    context = {
        "form" : form
    }
  
    return render(request, "edit-building-tenants.html", context)


def add_tenant(request):
    if request.method == "POST":
        form = BuildingTenantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    
    else:
        form = BuildingTenantForm()

    context = {
        "form" : form
    }
    return render(request, "add-tenant.html", context)
from django.shortcuts import render, redirect
from .models import AddProperty
from userinfo.models import Profile
from .forms import AddProperyForm

# Create your views here.

def property_create(request):
	profile = Profile.objects.get(user=request.user)
	if request.method == "POST":
		form = AddProperyForm(request.POST, request.FILES)
		if form.is_valid():
			propery = form.save(commit=False)
			propery.profile = profile
			propery.save()
			return redirect('property_detail', id=propery.id)
	else:
		form = AddProperyForm()
		return render(request, 'property/property-create.html',{'form': form})

def property_detail(request, id=None):
	propery = AddProperty.objects.get(id=id)
	context = {
		'propery': propery,
	}

	return render(request, 'property/property-detail', context)

def property_edit(request, id=None):
	propery = AddProperty.objects.get(id=id)
	if request.method == "POST":
		form = AddProperyForm(request.POST, request.FILES, instance=propery)
		if form.is_valid():
			propery = form.save(commit=False)
			propery.save()
			return redirect('property_detail', id=propery.id)
	else:
		form = AddProperyForm(instance=propery)
		return render(request, 'property/property-edit.html',{'form': form})
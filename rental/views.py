from django.shortcuts import render
from property.models import AddProperty


def home(request):
	propery = AddProperty.objects.all()[:3]
	context = {
		'propery': propery,
	}
	template = 'home.html'
	return render(request, template, context)

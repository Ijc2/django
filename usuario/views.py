from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from .models import Usuario
from .models import Proyecto

""""
def usuario_model_list_view(request):
	

	qs = Usuario.objects.all()
	print(qs)
	template="blog/list-view.html"
	context={
		"objects_list":qs
	}
	return render(request,template, context)"""
def list_usuario(request):

		usuario =Usuario.objects.all()
		template="list_usuario.html"
		context={"usuario":usuario}
		return render(request, template,context)

def list_proyecto(request):

		proyecto =Proyecto.objects.all()
		template="list_proyectos.html"
		context={"proyecto":proyecto}
		return render(request, template,context)

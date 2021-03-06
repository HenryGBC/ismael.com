from django.shortcuts import render_to_response,get_object_or_404, render
from django.template.context import RequestContext
from .models import Plato, Ingrediente, Tipo, Menu, Email
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required


def recetas(request, slugTipo):
	tipo = get_object_or_404(Tipo,slug_tipo=slugTipo)
	platos = Plato.objects.filter(tipo=tipo)
	tipos = Tipo.objects.all()
	template = "mostrartodos.html"
	return render(request, template, locals())

def detalles(request, slug_view):
	plato = get_object_or_404(Plato,slug=slug_view)
	tipos = Tipo.objects.all()
	tipo = get_object_or_404(Tipo,nombre=plato.tipo)
	slug_tipo = tipo.slug_tipo
	template = "detalles.html"
	ingredientes = plato.ingredientes.all()
	return render(request,template,locals())

def emails(request):
	email_index = request.GET['email']
	email = Email(email=email_index)
	email.save()

def menu(request):
	menu = get_object_or_404(Menu, pk=1)
	plato = get_object_or_404(Plato, nombre=menu.plato)
	template = "menu.html"
	return render(request,template,locals())

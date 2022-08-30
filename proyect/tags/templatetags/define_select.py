import os
from pathlib import Path
from typing import Any
from django import template
from subprocess import getoutput

register = template.Library()

@register.simple_tag
def name(request):
  return request.GET.get('Name', '')

@register.simple_tag
def type(request):
  return request.GET.get('Tipo', '')

@register.simple_tag
def permits(request):
  return request.GET.get('Permisos', '')

@register.simple_tag
def showpermits(request, Ruta):
  rutashow = ''
  rutasplit = Ruta.split('-')
  for rut in rutasplit:
    rutashow = os.path.join(rutashow, rut)

  if request.GET.get('Name', '')!='':
    comando = "ls -ld %s" % os.path.join(rutashow, request.GET.get('Name', ''))
    return list(getoutput(comando)[1:11])

@register.simple_tag
def owner(request, Ruta):
  rutashow = ''
  rutasplit = Ruta.split('-')
  for rut in rutasplit:
    rutashow = os.path.join(rutashow, rut)

  if request.GET.get('Name', '')!='':
    comando = "ls -ld %s" % os.path.join(rutashow, request.GET.get('Name', ''))
    return getoutput(comando).split()[2]
 
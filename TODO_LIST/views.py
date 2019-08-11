from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import elements
# Create your views here.
def todot(request):
    allel=elements.objects.all()
    return render(request, 'todo.html',
                  {'all_items':allel})
def addit(request):
    nt = elements(content = request.POST['content'])
    nt.save()
    return HttpResponseRedirect('/todo/')
def delit(request, inti):
    i=elements.objects.get(id=inti)
    i.delete()
    return HttpResponseRedirect('/todo/')
from django.shortcuts import render

from django.http import HttpResponse
from .models import * 
from .forms import *

def list(request):
    PisteList=Piste.objects.all()
    JoueurList=Joueur.objects.all()
    EnqueteMap={}
    for enquete in Enquete.objects.all(): 
        m=EnqueteMap.get((enquete.joueur,enquete.piste),[])
        value = enquete.niveau
        if enquete.type is not 'E': 
            value = value + '(' + enquete.type + ')'
        m.append(value)
        EnqueteMap[(enquete.joueur,enquete.piste)]=m

    context = {"joueur_list" : JoueurList,"piste_list": PisteList,"enquete_list" : EnqueteMap}
    return render(request,'list.html', context)

def enquete(request):
    if request.method == "POST":
        form = EnqueteForm(request.POST)
        if form.is_valid():
            enquete = form.save(commit=False)
            enquete.dice = int(form.cleaned_data['dice'])
            enquete.status(int(form.cleaned_data['points']))
            enquete.interception()
            if not enquete.intercepted:
                enquete.save()
            context = { "enquete" : enquete }
            return render(request, 'enquete_status.html', context)
    else: 
        form = EnqueteForm()
        return render(request, 'form.html', {'form': form})

def interception(request):
    if request.method == "POST":
        form = InterceptionForm(request.POST)
        if form.is_valid():
            interception = form.save(commit=False)
            interception.target = Joueur.objects.get(id = int(form.cleaned_data['target']))
            interception.status()
            interception.save()
            context = { "interception" : interception }
            return render(request, 'interception_status.html', context)
    else: 
        form = InterceptionForm()
        return render(request, 'form.html', {'form': form})

def copie(request):
    if request.method == "POST":
        form = CopieForm(request.POST)
        if form.is_valid():
            copie = form.save(commit=False)
            copie.target = Joueur.objects.get(id = int(form.cleaned_data['target']))
            copie.action()
            copie.save()
            context = { "copie" : copie }
            return render(request, 'copie_status.html', context)
    else: 
        form = CopieForm()
        return render(request, 'form.html', {'form': form})



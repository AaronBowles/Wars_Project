from django.shortcuts import render, redirect
from django.http import JsonResponse

from .forms import WarForm, BattleForm
from .models import War, Battle
# Create your views here.

def war_list(request):
    wars = War.objects.all()
    return render(request, 'wars/war_list.html', {'wars': wars})

def war_detail(request, pk):
    war = War.objects.get(id = pk)
    return render(request, 'wars/war_detail.html', {'war': war})

def war_create(request):
    if request.method == 'POST':
        form = WarForm(request.POST)
        if form.is_valid():
            war = form.save()
            return redirect('war_detail', pk = war.pk)
    else:
        form = WarForm()
    return render(request, 'wars/war_form.html', {'form': form})


def war_edit(request, pk):
    war = War.objects.get(pk = pk)
    if request.method == 'POST':
        form = WarForm(request.POST, instance = war)
        if form.is_valid():
            war = form.save()
            return redirect('war_detail', pk = war.pk)
    else:
        form = WarForm(instance = war)
    return render(request, 'wars/war_form.html', {'form': form})

def war_delete(request, pk):
    War.objects.get(id=pk).delete()
    return redirect('war_list')

def battle_list(request):
    battles = Battle.objects.all()
    return render(request, 'wars/battle_list.html', {'battles': battles})

def battle_detail(request, pk):
    battle = Battle.objects.get(id = pk)
    return render(request, 'wars/battle_detail.html', {'battle': battle})

def battle_create(request):
    if request.method == 'POST':
        form = BattleForm(request.POST)
        if form.is_valid():
            battle = form.save()
            return redirect('battle_detail', pk = battle.pk)
    else:
        form = BattleForm()
    return render(request, 'wars/battle_form.html', {'form': form})


def battle_edit(request, pk):
    battle = Battle.objects.get(pk = pk)
    if request.method == 'POST':
        form = BattleForm(request.POST, instance = battle)
        if form.is_valid():
            battle = form.save()
            return redirect('battle_detail', pk = battle.pk)
    else:
        form = BattleForm(instance = battle)
    return render(request, 'wars/battle_form.html', {'form': form})

def battle_delete(request, pk):
    Battle.objects.get(id=pk).delete()
    return redirect('battle_list')


# class WarList(generics.ListCreateAPIView):
#     queryset = War.objects.all()
#     serializer_class = WarSerializer

# class WarDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = War.objects.all()
#     serializer_class = WarSerializer
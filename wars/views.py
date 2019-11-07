from django.shortcuts import render, redirect
from django.http import JsonResponse

from .forms import WarForm
from .models import War
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

# class WarList(generics.ListCreateAPIView):
#     queryset = War.objects.all()
#     serializer_class = WarSerializer

# class WarDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = War.objects.all()
#     serializer_class = WarSerializer
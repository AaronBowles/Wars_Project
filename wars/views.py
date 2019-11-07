from django.shortcuts import render, redirect
from django.http import JsonResponse

from .forms import WarForm
from .models import War
# Create your views here.

def war_list(request):
    wars = War.objects.all()
    return render(request, 'wars/war_list.html', {'wars': wars})

def war_detail(request, pk):
    war = War.objects.get(id=pk)
    return render(request, 'wars/war_detail.html', {'war': war})

def war_create(request):
    if request.method = 'POST':
        form = WarForm(request.POST)
        if form.is_valid():
            artist = form.save()
            return redirect('war_detail', pk=war.pk)
    else:
        from = WarForm()
    return render(request, 'war/war_form.html', {'form': form})






# class WarList(generics.ListCreateAPIView):
#     queryset = War.objects.all()
#     serializer_class = WarSerializer

# class WarDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = War.objects.all()
#     serializer_class = WarSerializer
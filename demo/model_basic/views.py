from django.shortcuts import render, redirect, get_object_or_404

from .forms import PersonForm
from .models import Person


# Create your views here.

def list_person(request):
    persons = Person.objects.all().order_by('first_name')
    context = {
        'person_list': persons
    }
    return render(request, 'model_basic/list.html', context)


def create_person(request):
    form = PersonForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('model:list')
    else:
        context = {'form': form}
        return render(request, 'model_basic/person_form.html', context)


def update_person(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonForm(request.POST or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('model:list')
    else:
        context = {'form': form}
        return render(request, 'model_basic/person_form.html', context)


def save_person(request, pk=None):
    if pk is None:
        form = PersonForm(request.POST or None)
    else:
        person = get_object_or_404(Person, pk=pk)
        form = PersonForm(request.POST or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('model:list')
    else:
        context = {'form': form}
        return render(request, 'model_basic/person_form.html', context)


def delete_person(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        person.delete()
        return redirect('model:list')
    else:
        context = {'person': person}
        return render(request, 'model_basic/delete_form.html', context)

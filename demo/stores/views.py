from django.shortcuts import render, get_object_or_404
from django.views import generic

from .forms import StoreForm
from .models import Store


# Create your views here.
class IndexViewStore(generic.ListView):
    template_name = "stores/store/index.html"
    model = Store
    context_object_name = 'list_store'

    def get_queryset(self):
        return Store.objects.order_by('create_date')


class DetailViewStore(generic.DetailView):
    template_name = "stores/store/detail.html"
    model = Store


def edit(request, store_id):
    store = get_object_or_404(Store, pk=store_id)
    context = {
        'store': store
    }
    return render(request, 'stores/store/detail.html', context)


def update(request):
    if request.method == 'POST':
        data = request.POST['store']
    else:
        form = StoreForm()
        content = {
            'form': form
        }
    return render(request, 'stores/store/detail.html', content)

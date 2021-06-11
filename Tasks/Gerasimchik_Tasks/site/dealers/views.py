from .models import Dealer
from catalog.models import Brand
from .forms import AddDealer
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin


class DealersBrandView(ListView):
    model = Brand
    template_name = 'dealer_brands.html'


class DealersListView(ListView):
    model = Dealer
    template_name = 'dealers_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dealers_list'] = Dealer.objects.filter(brand__slug=self.kwargs['slug'])
        return context


class DealerDetailView(DetailView):
    model = Dealer
    template_name = 'dealer.html'


@method_decorator(permission_required('dealers.add_dealer'), name='dispatch')
class AddDealer(LoginRequiredMixin, CreateView):
    form_class = AddDealer
    template_name = 'add_dealer.html'
    success_url = '/dealers/'

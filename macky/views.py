from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView, DetailView
from .models import rasa, macka



class IndexView(ListView):
    model = rasa
    template_name = 'macky/index.html'
    context_object_name = 'rasa'
    paginate_by = 6

class CatsView(ListView):
    template_name = 'macky/cats.html'
    paginate_by = 6

    def get_queryset(self):
        self.rasa_r = get_object_or_404(rasa, meno_rasy=self.kwargs['meno_rasy'])
        return macka.objects.filter(typ_rasy=self.rasa_r)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['urcita_rasa'] = self.rasa_r
        return context

class Detail_Cats_View(DetailView):
    model = macka
    template_name = 'macky/detail.html'
    context_object_name = 'cats'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(macka, id=id_)
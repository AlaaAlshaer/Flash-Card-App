import random
from typing import Any
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Card
from django.urls import reverse_lazy
from .form import CardCheckForm

# Create your views here.
class CardListView(ListView):
    model= Card
    queryset= Card.objects.all().order_by("box","-created_at")
    context_object_name = "card_list"


class BoxView(CardListView):
    template_name = "card/box.html"
    form_class = CardCheckForm


    def get_queryset(self):
        return Card.objects.filter(box=self.kwargs["box_num"])
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["box_number"] = self.kwargs["box_num"]

        if self.object_list:
            context["check_card"] = random.choice(self.object_list)
        return context
    
     
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        form = self.form_class(request.POST)
        if form.is_valid():
            card = get_object_or_404(Card, id=form.cleaned_data["card_id"])
            card.move(form.cleaned_data["solved"])
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    

class CreateCardView(SuccessMessageMixin, CreateView):
    model = Card
    fields = ["question", "answer", "box"]
    success_url = reverse_lazy("card:card-create")
    context_object_name = "card"

    success_message = "card add successfully"


class UpdateCardView(SuccessMessageMixin, UpdateView):
    model = Card
    fields = ["question", "answer", "box"]
    success_url = reverse_lazy("card:card-list")
    context_object_name = "card"
    success_message = "card update successfully"

class DeleteCardView(SuccessMessageMixin, DeleteView):
    model = Card
    context_object_name = "card"
    success_url = reverse_lazy("card:card-list")
    success_message = "card delete successfully"

    
                

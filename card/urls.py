from django.urls import path
from .views import CardListView, BoxView , CreateCardView , UpdateCardView, DeleteCardView

app_name = "card"

# define app's urls
urlpatterns = [
    path("", CardListView.as_view(), name="card-list"),
    path("box/<int:box_num>", BoxView.as_view(), name="box"),
    path("new", CreateCardView.as_view(), name="card-create"),
    path("update/<int:pk>", UpdateCardView.as_view(), name="card-update"),
    path("delete/<int:pk>", DeleteCardView.as_view(), name="card-delete"),
]

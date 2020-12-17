from django.urls import path

from . import views
from macky.views import IndexView, CatsView, Detail_Cats_View


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<meno_rasy>', CatsView.as_view(), name='cats'),
    path('macka/<int:id>', Detail_Cats_View.as_view(), name='detail'),
]
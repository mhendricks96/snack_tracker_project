from django.urls import path
from django.urls.resolvers import URLPattern
from .views import SnackListView, HomeView, SnackDetailView

urlpatterns=[
    path('', HomeView.as_view(), name='home'),
    path('snacks/', SnackListView.as_view(), name='snack_list'),
    path('<int:pk>', SnackDetailView.as_view(), name='snack_detail')
]
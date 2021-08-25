from django.urls import path
from django.urls.resolvers import URLPattern
from .views import HomeView, SnackListView

urlpatterns=[
    path('', HomeView.as_view(), name='home'),
    path('snack_list', SnackListView.as_view(), name='snack_list'),
]
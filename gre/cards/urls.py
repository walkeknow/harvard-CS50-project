from django.urls import path
from . import views

app_name = 'cards'

urlpatterns = [
    # cards/
    path('', views.index, name='index'),

    # cards/id/
    path('<int:word_id>/', views.detail, name='detail'),
]

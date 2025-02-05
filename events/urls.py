from django.urls import path
from .views import events_list, create_event, update_event, delete_event

urlpatterns = [
    path('', events_list, name='event_list'),
    path('create/', create_event, name='create_event'),
    path('update/<int:event_id>/', update_event, name='update_event'),
    path('delete/<int:event_id>/', delete_event, name='delete_event'),
]


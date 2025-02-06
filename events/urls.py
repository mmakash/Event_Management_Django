from django.urls import path
from .views import events_list, create_event, update_event, delete_event, category_list, category_create, category_update, category_delete, participant_list, participant_create, participant_update, participant_delete

urlpatterns = [
    path('', events_list, name='event_list'),
    path('create/', create_event, name='create_event'),
    path('update/<int:event_id>/', update_event, name='update_event'),
    path('delete/<int:event_id>/', delete_event, name='delete_event'),

    path('categories/', category_list, name='category_list'),
    path('categories/create/', category_create, name='category_create'),
    path('categories/update/<int:category_id>/', category_update, name='category_update'),
    path('categories/delete/<int:category_id>/', category_delete, name='category_delete'),

    path('participants/', participant_list, name='participant_list'),
    path('participants/create/', participant_create, name='participant_create'),
    path('participants/update/<int:participant_id>/', participant_update, name='participant_update'),
    path('participants/delete/<int:participant_id>/', participant_delete, name='participant_delete'),
]


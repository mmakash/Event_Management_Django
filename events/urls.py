from django.urls import path
from .views import dashboard, events_list, create_event, update_event, delete_event, category_list, category_create, category_update, category_delete, participant_list, participant_create, participant_update, participant_delete

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('all_events/', events_list, name='all_events'),
    path('create_event/', create_event, name='create_event'),
    path('update_event/<int:event_id>/', update_event, name='update_event'),
    path('delete_event/<int:event_id>/', delete_event, name='delete_event'),

    path('category_list/', category_list, name='category_list'),
    path('create_category/', category_create, name='create_category'),
    path('update_category/<int:category_id>/', category_update, name='category_update'),
    path('delete_category/<int:category_id>/', category_delete, name='category_delete'),

    path('all_participants/', participant_list, name='all_participants'),
    path('create_participant/', participant_create, name='create_participant'),
    path('update_participant/<int:participant_id>/', participant_update, name='participant_update'),
    path('delete_participant/<int:participant_id>/', participant_delete, name='participant_delete'),
]


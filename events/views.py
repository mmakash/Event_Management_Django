from django.shortcuts import render, redirect
from .models import Event, Category, Participant
from .forms import EventForm
from django.contrib import messages
from django.http import Http404

# Create your views here.

# Read Events
def events_list(request):
    events = Event.objects.all()
    return render(request, 'events_list.html', {'events': events})

# Create Event
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event created successfully!')
            print('Event created successfully!')
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'event_form.html', {'form': form})

# Update Event
def update_event(request, event_id):
    try:
        event = Event.objects.get(id=event_id)
    except Event.DoesNotExist:
        raise Http404("Event not found")
    
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated successfully!')
            return redirect('event_list')
    else:
        form = EventForm(instance=event)
    
    return render(request, 'event_form.html', {'form': form})

# Delete Event
def delete_event(request, event_id):
    event = Event.objects.get(id=event_id)
    event.delete()
    messages.success(request, 'Event deleted successfully!')
    return redirect('event_list')


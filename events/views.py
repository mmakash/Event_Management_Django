from django.shortcuts import render, redirect
from .models import Event, Category, Participant
from .forms import EventForm, CategoryForm, ParticipantForm
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

# Read Categories
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})    

# Create Category
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category created successfully!')
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'category_form.html', {'form': form})

# Update Category
def category_update(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category updated successfully!')
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category_form.html', {'form': form})

# Delete Category
def category_delete(request, category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    messages.success(request, 'Category deleted successfully!')
    return redirect('category_list')

# Read Participants
def participant_list(request):
    participants = Participant.objects.all()
    return render(request, 'participant_list.html', {'participants': participants})

# Create Participant
def participant_create(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Participant created successfully!')
            return redirect('participant_list')
    else:
        form = ParticipantForm()
    return render(request, 'participant_form.html', {'form': form})

# Update Participant
def participant_update(request, participant_id):
    participant = Participant.objects.get(id=participant_id)
    if request.method == 'POST':
        form = ParticipantForm(request.POST, instance=participant)
        if form.is_valid():
            form.save()
            messages.success(request, 'Participant updated successfully!')
            return redirect('participant_list')
    else:    
        form = ParticipantForm(instance=participant)
    return render(request, 'participant_form.html', {'form': form})

# Delete Participant    
def participant_delete(request, participant_id):    
    participant = Participant.objects.get(id=participant_id)
    participant.delete()
    messages.success(request, 'Participant deleted successfully!')
    return redirect('participant_list')
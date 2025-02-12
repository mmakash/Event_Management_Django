from django.shortcuts import render, redirect
from .models import Event, Category, Participant
from .forms import EventForm, CategoryForm, ParticipantForm
from django.contrib import messages
from django.http import Http404
from django.db.models import Count
from django.utils.timezone import now
from datetime import date

# Create your views here.
def dashboard(request):
    events = Event.objects.select_related('category').prefetch_related('participants').all()
    total_participants = events.aggregate(total_participants=Count('participants'))['total_participants'] or 0
    total_events = events.count()
    upcomming_events = events.filter(date__gte=now().date()).count()
    past_events = events.filter(date__lt=now().date()).count()
    todays_events = events.filter(date=now().date())
    return render(request, 'dashboard.html',{
        'total_participants': total_participants,
        'total_events': total_events,
        'upcomming_events': upcomming_events,
        'past_events': past_events,
        'todays_events': todays_events
    })

# Read Events
def events_list(request):
    # events = Event.objects.all()
    category_id = request.GET.get('category_id')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    events = Event.objects.select_related('category').prefetch_related('participants').all()

    if category_id:
        events = events.filter(category_id=category_id)

    if start_date and end_date:
        events = events.filter(date__range=[start_date, end_date])

    total_participants = events.aggregate(total_participants=Count('participants'))['total_participants'] or 0

    today = date.today()
    today_events = events.filter(date=today)
    upcoming_events_count = events.filter(date__gt=today).count()
    past_events_count = events.filter(date__lt=today).count()

    # Prepare event data for the template
    event_data = []
    for event in events:
        event_data.append({
            'id': event.id,
            'name': event.name,
            'date': event.date,
            'category': event.category.name if event.category else "Uncategorized",
            'participants': [participant.name for participant in event.participants.all()],
            'participant_count': event.participants.count(),
        })

    return render(request, 'events_list.html', {
        'events': event_data,
        'upcoming_events_count': upcoming_events_count,
        'past_events_count': past_events_count,
        'today_events': today_events,
        'total_participants': total_participants
        })
# Read Event Details
def event_details(request, event_id):
    event = Event.objects.get(id=event_id)
    event_data = {
        'id': event.id,
        'name': event.name,
        'description': event.description,
        'date': event.date,
        'category': event.category.name if event.category else "Uncategorized",
        'participants': [participant.name for participant in event.participants.all()],
        'participant_count': event.participants.count(),
    }
    return render(request, 'event_details.html', {'event': event_data})
# Create Event
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event created successfully!')
            return redirect('create_event') 
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
            return redirect('create_event')
            # return redirect(request, 'event_form.html', {'form': EventForm()})
    else:
        form = EventForm(instance=event)
    return render(request, 'event_form.html', {'form': form})

# Delete Event
def delete_event(request, event_id):
    event = Event.objects.get(id=event_id)
    event.delete()
    messages.success(request, 'Event deleted successfully!')
    return redirect('all_events')

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
            return redirect('create_category')
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
            return redirect('create_category')
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
    try:
        if request.method == 'POST':
            form = ParticipantForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Participant created successfully!')
                return redirect('create_participant')
        else:
            form = ParticipantForm()
        return render(request, 'participant_form.html', {'form': form})
    except Participant.DoesNotExist:
        raise Http404("Participant not found")

# Update Participant
def participant_update(request, participant_id):
    try:
        participant = Participant.objects.get(id=participant_id)
        if request.method == 'POST':
            form = ParticipantForm(request.POST, instance=participant)
            if form.is_valid():
                form.save()
                messages.success(request, 'Participant updated successfully!')
                return redirect('create_participant')
        else:
            form = ParticipantForm(instance=participant)
        return render(request, 'participant_form.html', {'form': form})
    except Participant.DoesNotExist:
        raise Http404("Participant not found")

# Delete Participant    
def participant_delete(request, participant_id):    
    participant = Participant.objects.get(id=participant_id)
    participant.delete()
    messages.success(request, 'Participant deleted successfully!')
    return redirect('all_participants')



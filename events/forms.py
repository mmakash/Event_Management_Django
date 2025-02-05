from django import forms
from .models import Event, Category, Participant

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date', 'time', 'location', 'category']
        widgets = {
            'date' : forms.DateInput(attrs={'type':'date', 'class':'form-control'}),
            'time' : forms.TimeInput(attrs={'type':'time', 'class':'form-control'}),
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'description' : forms.Textarea(attrs={'class':'form-control'}),
            'location' : forms.TextInput(attrs={'class':'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all()
        self.fields['category'].widget.attrs.update({'class':'form-control'})

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'email', 'events']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'events' : forms.SelectMultiple(attrs={'class':'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['events'].queryset = Event.objects.all()
        self.fields['events'].widget.attrs.update({'class':'form-control'})
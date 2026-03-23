from django import forms
from .models import Notes

# Notes Form_______!

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'user', 'content', 'is_completed']




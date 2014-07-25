from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    person_display = forms.CharField(max_length=100, help_text='type Id Card, Name or Surname')

    class Meta:
        model = Project
        fields=('title','person_display', 'author',)

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args,**kwargs)
        self.fields['person_display'].label = "Author"
        self.fields['author'].widget = forms.HiddenInput()

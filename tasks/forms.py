from django import forms

from .models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = [
            "title",
            "description",
            "priority",
            "completed",
        ]

    def clean_title(self):
        title = self.cleaned_data["title"]

        title = title.strip()

        if len(title) < 3:
            raise forms.ValidationError(
                "Task title must contain at least 3 characters."
            )

        return title

    def clean_description(self):
        description = self.cleaned_data.get("description", "")

        description = description.strip()

        if description and len(description) < 5:
            raise forms.ValidationError(
                "Description must contain at least 5 characters."
            )

        return description
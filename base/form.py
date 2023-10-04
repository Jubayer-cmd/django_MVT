from django.forms import ModelForm
from .models import Room


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = [
            "name",
            "description",
            "host",
            "topic",
        ]  # List the fields you want in the form

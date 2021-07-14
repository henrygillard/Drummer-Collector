from django.db.models.base import Model
from django.forms import ModelForm
from .models import Sponsor

class SponsorForm(ModelForm):
    class Meta:
        model = Sponsor
        fields = ["stick_sponsor"]

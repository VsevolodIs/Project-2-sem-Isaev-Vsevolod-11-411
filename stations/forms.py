from django import forms
from .models import StationReview

class StationReviewForm(forms.ModelForm):
    class Meta:
        model = StationReview
        fields = ['rating', 'text']

    def clean_rating(self):
        rating = self.cleaned_data.get('rating')

        if rating is not None and (rating < 1 or rating > 5):
            raise forms.ValidationError("Оценка должна быть от 1 до 5")

        return rating
from django import forms 
from .models import Review

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label='twoje yme', max_length=10, error_messages={
#         'required': 'thys ys required',
#         'max_length': 'max lenf is 10',
#     })
#     review_text = forms.CharField(label='ur feedback', widget=forms.Textarea, max_length=200)
#     rating = forms.IntegerField(label='your rating', min_value=1, max_value=5)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        exclude = ['owner_comment']
        labels = {
            'user_name': 'twoje yme',
            'review_text': 'ur feedback',
            'rating': 'ur rating',
        }

# Register your models here.
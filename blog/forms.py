from django import forms
class ExamForm1(forms.Form):
    # class Meta:

    # widgets = {
    #       'agriculture': forms.TextInput(attrs={'class': 'form-control'}),
    #      }
    agriculture = forms.CharField()
    photography = forms.CharField()
    hotel_management = forms.CharField()
    gaming = forms.CharField()
    commerce = forms.CharField()
    business_management = forms.CharField()
    biology = forms.CharField()
    animation = forms.CharField()
    computer_engineering = forms.CharField()
    journalism = forms.CharField()



from django import forms

class IndexForm(forms.Form):
    name = forms.CharField(max_length=100)
    email =  forms.EmailField()
    subject = forms.CharField()
    message = forms.CharField(widget= forms.Textarea(attrs={
        "rows":7,
        "cols":30
    }) )
from django import forms

class descForm(forms.Form):
	videotitle = forms.CharField(max_length=50,
		widget = forms.TextInput(attrs = {
		'class': 'form-control',
		'placeholder': 'Name',
		'id': 'inputName'
			}))
	videodesc = forms.CharField(
		widget = forms.Textarea(attrs = { 
        'class': 'form-control',
        'rows': '5',
        'id': 'comment',
        'placeholder': 'Comment'
    		}))

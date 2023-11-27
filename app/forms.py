from django import forms

class Front_times_form(forms.Form):
    word = forms.CharField()
    times = forms.IntegerField()
    length = forms.IntegerField()

class Centered_form(forms.Form):
    n1 = forms.IntegerField()
    n2 = forms.IntegerField()
    n3 = forms.IntegerField()
    n4 = forms.IntegerField()
    n5 = forms.IntegerField()
    n6 = forms.IntegerField( required=False )
    n7 = forms.IntegerField( required=False )

class No_teen_sum_form(forms.Form):
    n1 = forms.IntegerField()
    n2 = forms.IntegerField()
    n3 = forms.IntegerField()

class xyz_form(forms.Form):
    word = forms.CharField()
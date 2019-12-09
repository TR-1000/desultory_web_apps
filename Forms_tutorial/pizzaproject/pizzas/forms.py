from django import forms
from .models import Pizza, Size

class PizzaForm(forms.ModelForm):
    # Model form

    # widgets = {'topping1':forms.Textarea, 'size':forms.CheckboxSelectMultiple}
    # size = forms.ModelChoiceField(queryset=Size.objects, empty_label=None, widget=forms.RadioSelect)
    # image = forms.ImageField() # if we wasnt to add image select add request.FILES to view and enctype="multipart/form-data" to form attributes

    class Meta:
        model = Pizza
        fields = ['topping1', 'topping2', 'size']
        labels = {'topping1':'Topping 1','topping2':'Topping 2'} #size choices is now in models

class MultiplePizzaForm(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=6)







# class PizzaForm(forms.Form):
#
#     SIZE_CHOICES = [('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')]
#     TOPPING_CHOICES =[('pep','pepperoni'), ('cheese','Cheese'), ('olives', 'Olives')]
#
#     # topping1 = forms.CharField(label='Topping 1', max_length=100, widget=forms.Textarea)
#     # topping2 = forms.CharField(label='Topping 2', max_length=100, widget=forms.PasswordInput)
#     # toppings = forms.MultipleChoiceField(choices=TOPPING_CHOICES)
#     # toppings = forms.MultipleChoiceField(choices=TOPPING_CHOICES,widget=forms.CheckboxSelectMultiple)
#
#     topping1 = forms.CharField(label='Topping 1', max_length=100)
#     topping2 = forms.CharField(label='Topping 2', max_length=100)
#     size = forms.ChoiceField(label='Size', choices=SIZE_CHOICES)

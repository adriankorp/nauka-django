from django.forms import (
    CharField, DateField, Form, IntegerField, ModelChoiceField, Textarea, SelectDateWidget, DateTimeField
)
from .models import  Category


class PostForm(Form):
    title = CharField(max_length=128)
    category = ModelChoiceField(queryset=Category.objects)
    text = CharField(widget=Textarea, required=False)
    created_at = DateTimeField(widget=SelectDateWidget)

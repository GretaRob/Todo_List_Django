from django.forms import ModelForm
from .models import todo


class createTodo(ModelForm):
    class Meta:
        model = todo
        fields = "__all__"

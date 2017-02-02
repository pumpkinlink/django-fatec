from django import forms
from django.contrib.auth.models import User
from curriculo.models import Aluno
from django.forms.widgets import PasswordInput

class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget=PasswordInput()

    def save(self, *args, **kwargs):
        user = super(UserForm, self).save(*args, **kwargs)
        aluno = Aluno()
        aluno.user = user
        aluno.nome = user.first_name
        import pdb; pdb.set_trace()
        aluno.save()

        return user

    class Meta:
        model = User
        exclude = (
            'last_login', 
            'is_superuser', 
            'user_permissions', 
            'groups', 
            'is_staff', 
            'is_active', 
            'date_joined', 
            )
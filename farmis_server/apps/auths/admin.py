from django.contrib import admin
from django.http import HttpRequest
from django.forms import Form

from .models import CustomUser
from .services.customuser import customuser_create, customuser_delete, customuser_update

# Register your models here.
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):


    def save_model(self, request: HttpRequest, obj: CustomUser, form: Form, change: bool, **kwargs):
        if not change:
            _data = form.cleaned_data
            create_field = ['phone_number', 'password', 'user_type']
            data = {k:v for k, v in _data.items() if k in create_field}
            customuser_create(
                **data
            )
        else:
            data = form.cleaned_data
            customuser_update(customuser=obj, fields=list(data.keys()), data=data)

    def delete_model(self, request: HttpRequest, obj: CustomUser) -> None:
        return customuser_delete(customuser=obj)

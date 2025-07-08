from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from apps.users.models import CustomUser
# Register your models here.

class CustomCreationForm(forms.ModelForm):
    password1=forms.CharField(label="password,",widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )
    class  Meta:
        model=CustomUser
        fields=["email","phone","date_of_birth"]
    def clean_password2(self):
        password1=self.cleaned_data.get("password1")
        password2=self.cleaned_data.get("password2")
        if password1 and password2 and password1!=password2:
            raise ValidationError("password does not matched")
        return password2
    def save(self, commit = True):
        user=super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
             user.save()
        return user
    
class CustomChangeForm(forms.ModelForm):
    # this field is for updating the  user along with all the values
    password=ReadOnlyPasswordHashField()
    class Meta:
        model=CustomUser
        fields=["email","password","date_of_birth","is_active","is_admin"]

class CustomAdmin(BaseUserAdmin):
    form=CustomChangeForm
    add_form=CustomCreationForm
    list_display=["email","phone",
                  
                  "date_of_birth","is_admin"
                  ]
    list_filter=["is_admin"]
    fieldsets = [
    (None, {"fields": ["email", "password"]}),
    ("Personal Info", {"fields": ["date_of_birth", "phone"]}),
    ("Permissions", {"fields": ["is_admin"]}),
]

    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "date_of_birth", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []

admin.site.register(CustomUser,CustomAdmin)
admin.site.unregister(Group)

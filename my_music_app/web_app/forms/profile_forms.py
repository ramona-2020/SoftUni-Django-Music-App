from django import forms

from my_music_app.web_app.models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'user_name': forms.TextInput(
                attrs={
                    'placeholder': 'Username',
                }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email',
            }),
            'age': forms.NumberInput(attrs={
                'placeholder': 'Age',
            })
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class DeleteProfileForm(forms.ModelForm):

    def save(self, commit=True):
        if self.instance:
            if commit:
                self.instance.delete()

        return self.instance

    class Meta:
        model = Profile
        fields = ()

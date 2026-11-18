import json

from django import forms

from .models import SubscriptionModel, CourseModel

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class CourseForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorUploadingWidget(), required=False)
    short_description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = CourseModel
        exclude = ()


class SubscriptionFormStep1(forms.ModelForm):

    date = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        )
    )
    time = forms.TimeField(
        widget=forms.TextInput(
            attrs={'type': 'time'}
        )
    )

    class Meta:
        model = SubscriptionModel
        fields = (
            'date',
            # 'course',
            'time'
        )


class SubscriptionFormStep2(forms.ModelForm):

    class Meta:
        model = SubscriptionModel
        fields = (
            'name',
            'email',
            'phone_number',
        )


class SubscriptionForm(forms.ModelForm):

    class Meta:
        model = SubscriptionModel
        fields = (
            'course',
            'name',
            'email',
            'phone_number',
        )

    def save(self, commit=True):
        instance = super().save(commit=False)

        instance.payment_status = SubscriptionModel.PaymentStatus.PAID
        instance.payment_data = json.dumps(
            {
                'type': 'free'
            }
        )
        instance.datetime = instance.course.date

        if commit:
            instance.save()
        return instance

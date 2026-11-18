from django import forms
from django.conf import settings

from .models import (
    ServiceModel, TeamModel,
    EnquiryModel
)

from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    Layout, Fieldset,
    Submit, Field
)
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class FormRequestMixin:

    def __init__(self, *args, **kwargs):
        try:
            self.request = kwargs.pop("request")
        except KeyError as e:
            if settings.DEBUG:
                print('Request cannot be fetched!')
        super().__init__(*args, **kwargs)


class ServiceForm(forms.ModelForm):

    body = forms.CharField(widget=CKEditorUploadingWidget())
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=False)
    short_description = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = ServiceModel
        exclude = ()


class TeamForm(forms.ModelForm):

    bio = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = TeamModel
        exclude = ()


class EnquiryForm(forms.ModelForm):
    query = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={'rows': 6}
        )
    )

    class Meta:
        model = EnquiryModel
        input_class = "block w-full py-4 rounded-lg shadow-sm border-primary focus:ring focus:ring-primary"
        text_area_class = "block w-full rounded-lg shadow-sm border-primary focus:ring focus:ring-primary"
        exclude = (
            'created_by',
            'updated_by',
            'ip',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field(
                'name',
                css_class=self.Meta.input_class
            ),
            Field(
                'phone_number',
                css_class=self.Meta.input_class
            ),
            Field(
                'email',
                css_class=self.Meta.input_class
            ),
            Field(
                'service',
                css_class=self.Meta.input_class
            ),
            Field(
                'type_of_query',
                css_class=self.Meta.input_class
            ),
            Field(
                'query',
                css_class=self.Meta.text_area_class,
            ),
        )


class SearchForm(forms.Form):
    q = forms.CharField(max_length=50)

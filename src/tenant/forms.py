from django import forms


class TenantedForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super(TenantedForm, self).__init__(*args, **kwargs)

from django import forms

from .models import Listing


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        # 'owner' must be set only by the view (request.user) so it can’t be null/overridden.
        fields = [
            'title',
            'description',
            'price',
            'address',
        ]

    def save(self, commit=True):
        instance = super().save(commit=False)
        # Defensive: never allow owner to be empty when saving from this form.
        if getattr(instance, 'owner_id', None) is None:
            instance.owner_id = None
        if commit:
            instance.save()
        return instance



""" Waste generated in operations """
from django import forms
from django.utils.translation import gettext_lazy as _
from ...base.forms import CustomAverageDataMethodForm


class WasteTreatmentForm(CustomAverageDataMethodForm):
    """Waste treatment method"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["custom_factor_name"].label = _("Waste Treatment")
        self.fields["custom_factor_name"].widget = forms.Select(
            choices=[
                ("landfill", _("Landfill")),
                ("combustion", _("Combustion")),
                ("composting", _("Composting")),
                ("open_loop_recycling", _("Open-loop Recycling")),
                ("closed_loop_recycling", _("Closed-loop Recycling")),
                ("anaerobic_digestion", _("Anaerobic digestion")),
            ]
        )
        self.factor_type = "waste_treatment"


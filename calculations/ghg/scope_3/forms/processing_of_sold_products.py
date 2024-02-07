""" Custom forms for the processing of sold products calculation method """
from django.utils.translation import gettext_lazy as _

from ...base.forms import CustomFactorCalculationMethodForm, PredefinedFactorCalculationMethodForm

class SiteSpecificMethodForm(CustomFactorCalculationMethodForm):
    """Custom Site-specific method form"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["description_user"].widget.attrs["placeholder"] = _("Sold Product / Processor name")
        self.fields["custom_factor_name"].label = _("Process Type")
        self.fields["custom_factor_name"].widget.attrs["placeholder"] = _("Process Type")
        self.factor_type = "processor"


class AverageDataMethodForm(PredefinedFactorCalculationMethodForm):
    """Custom Average data method form"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["description_user"].widget.attrs["placeholder"] = _("Sold Product / Processor name")

    class Meta(PredefinedFactorCalculationMethodForm.Meta):
        pass

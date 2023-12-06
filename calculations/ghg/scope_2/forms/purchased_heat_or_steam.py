""" Scope 2 calculation method for purchased heat and steam. """
from django.utils.translation import gettext_lazy as _
from ...base.forms import SupplierSpecificMethodForm


class EnergySupplierForm(SupplierSpecificMethodForm):
    """Energy supplier form"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["custom_factor_name"].label = _("Supplier name")
        self.factor_type = "heatsteam_supplier"
        self.fields["ghg_unit"].choices = [
            ("kwh", _("kWh")),
        ]

    class Meta(SupplierSpecificMethodForm.Meta):
        pass

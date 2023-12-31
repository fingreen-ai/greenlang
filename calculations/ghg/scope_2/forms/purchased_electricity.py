""" Scope 2 calculation method for purchased electricity. """
from django.utils.translation import gettext_lazy as _
from ...base.forms import SupplierSpecificMethodForm


class EnergySupplierForm(SupplierSpecificMethodForm):
    """Energy supplier form"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["custom_factor_name"].label = _("Factor type/supplier name")
        self.fields["custom_factor_name"].widget.attrs["placeholder"] = _("Factor type/supplier name")

        self.factor_type = "energy_supplier"
        self.fields["ghg_unit"].choices = [
            ("kwh", _("kWh")),
        ]

    class Meta(SupplierSpecificMethodForm.Meta):
        pass

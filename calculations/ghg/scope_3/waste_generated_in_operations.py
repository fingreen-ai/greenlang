""" Waste generated in operations """
from django.utils.translation import gettext_lazy as _
from ..base.base import BaseCalculationMethod
from ..base.forms import SupplierSpecificMethodForm
from .forms.waste_generated_in_operations import WasteTreatmentForm


class WasteTypeMethod(BaseCalculationMethod):
    """Spend-based method"""


class SupplierSpecificMethod(BaseCalculationMethod):
    """Supplier specific method"""

    @property
    def form_class(self):
        """Return form class"""
        return SupplierSpecificMethodForm


class AverageDataMethod(BaseCalculationMethod):
    """Average data method"""

    @property
    def form_class(self):
        """Return form class"""
        return WasteTreatmentForm

""" Scope 2 calculation method for purchased electricity. """
from django.utils.translation import gettext_lazy as _
from ..base.base import BaseCalculationMethod
from .forms.purchased_electricity import EnergySupplierForm


class LocationBasedMethod(BaseCalculationMethod):
    """Location based method"""


class MarketBasedMethod(BaseCalculationMethod):
    """Market based method"""

    @property
    def form_class(self):
        """Return form class"""
        return EnergySupplierForm

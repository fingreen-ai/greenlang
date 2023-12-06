""" Fuel and Energy Related Activities Calculation Method"""
from ..base.base import BaseCalculationMethod
from .forms.fuel_and_energy_related_activities import AutomaticMethodForm

class AutomaticMethod(BaseCalculationMethod):
    """Automatic method"""

    @property
    def form_class(self):
        """Return form class."""
        return AutomaticMethodForm

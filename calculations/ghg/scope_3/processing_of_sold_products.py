""" Implementation of the processing of sold products category of scope 3 GHG emissions."""
from ..base.base import BaseCalculationMethod
from .forms.processing_of_sold_products import AverageDataMethodForm, SiteSpecificMethodForm

class SiteSpecificMethod(BaseCalculationMethod):
    """ Average data method."""

    @property
    def form_class(self):
        """ Return form class to use for this calculation method."""
        return SiteSpecificMethodForm


class AverageDataMethod(BaseCalculationMethod):
    """ Site-specific method."""

    @property
    def form_class(self):
        """ Return form class to use for this calculation method."""
        return AverageDataMethodForm

"""End of life treatment of sold products."""

from ..base.base import BaseCalculationMethod
from .forms.end_of_life_treatment_of_sold_products import (
    EndOfLifeTreatmentForm
)

class SoldProductEndOfLifeTreatment(BaseCalculationMethod):
    """SoldProductEndOfLifeTreatment"""

    @property
    def form_class(self):
        """Return form class"""
        return EndOfLifeTreatmentForm


    def amount(self, collection_item):
        return super().amount(collection_item) * collection_item.widget_data["sold_quantity"]


class SoldProductPackagingEndOfLifeTreatment(SoldProductEndOfLifeTreatment):
    """SoldProductPackagingEndOfLifeTreatment"""

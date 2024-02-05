""" Fuel and Energy Related Activities Calculation Method"""
from django.utils.translation import gettext_lazy as _
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, Hidden

from fingreen_web.models import (
    CollectionItem,
    GhgEmissionFactorValue,
    GhgEmissionSourceComputationMethod,
)


class AutomaticMethodForm(forms.ModelForm):
    """Automatic method form"""

    method = forms.ModelChoiceField(
        queryset=GhgEmissionSourceComputationMethod.objects.all(), required=True
    )

    def __init__(self, *args, **kwargs):
        """Init form"""
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = False

        self.helper.form_show_labels = False

        self.helper.layout = Layout(
            Hidden(
                "method", self.initial["method"].id
            ),  # field used in the view to preset form
            Hidden("collection", self.initial["collection"].id),
            Hidden("item_type", self.initial["item_type"]),
            Hidden("ghg_scope", self.initial["ghg_scope"]),
            Row(
                Column(
                    Submit(
                        "submit",
                        _("Generate from other scopes"),
                        css_class="btn btn-light-primary w-100",
                    ),
                    css_class="col-4",
                ),
            ),
        )

    def save(self, commit=True):
        """Save form"""

        collection = self.cleaned_data["collection"]
        ghg_scope = self.cleaned_data["ghg_scope"]

        stationary_combustion_generic_method = (
            GhgEmissionSourceComputationMethod.objects.get(
                source__slug="stationary-combustion", slug="generic-method"
            )
        )

        mobile_combustion_fuel_method = GhgEmissionSourceComputationMethod.objects.get(
            source__slug="mobile-combustion", slug="fuel-amount-method"
        )

        mobile_combustion_vehicle_method = (
            GhgEmissionSourceComputationMethod.objects.get(
                source__slug="mobile-combustion", slug="vehicle-type-method"
            )
        )

        purchased_electricity_location_method = (
            GhgEmissionSourceComputationMethod.objects.get(
                source__slug="purchased-electricity", slug="location-based-method"
            )
        )

        purchased_heatsteam_location_method = (
            GhgEmissionSourceComputationMethod.objects.get(
                source__slug="purchased-heat-or-steam", slug="location-based-method"
            )
        )

        activities_automatic_method = GhgEmissionSourceComputationMethod.objects.get(
            source__slug="fuel-and-energy-related-activities", slug="automatic-method"
        )

        item = CollectionItem.objects.filter(
            collection=collection,
            ghg_factor__method=activities_automatic_method,
            ghg_scope=ghg_scope,
            item_type="ghg",
        ).delete()

        for item in collection.collectionitem_set.filter(
            ghg_factor__method__in=[
                stationary_combustion_generic_method,
                mobile_combustion_fuel_method,
                mobile_combustion_vehicle_method,
                purchased_electricity_location_method,
                purchased_heatsteam_location_method,
            ]
        ):
            wtt_value = GhgEmissionFactorValue.objects.filter(
                factor__method=activities_automatic_method,
                factor__factor_subtype=item.ghg_factor.factor_subtype,
                factor__factor_type=item.ghg_factor.factor_type,
                factor__name=item.ghg_factor.name,
                unit=item.ghg_unit,
            ).first()

            if wtt_value:
                CollectionItem.objects.create(
                    collection=collection,
                    ghg_scope=activities_automatic_method.source.scope,
                    item_type="ghg",
                    description_user=f"From scope {item.ghg_factor.method.source.scope}\
                          {item.ghg_factor.method}",
                    ghg_factor=wtt_value.factor,
                    value_float=item.value_float,
                    ghg_unit=wtt_value.unit,
                )
            else:
                raise Exception("NO WTT FACTOR") # pylint: disable=[broad-exception-raised]

        return item

    class Meta:
        model = CollectionItem
        fields = [
            "method",
            "collection",
            "ghg_scope",
            "item_type",
        ]

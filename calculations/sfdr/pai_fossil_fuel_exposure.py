""" fossil_fuel_exposure """
import logging

from fingreen_web.models import CollectionItem

logger = logging.getLogger(__name__)


class FossilFuelExposure(): # pylint: disable=[too-few-public-methods]
    """ fossil_fuel_exposure """

    def impact(self, collections, assets, invest_value_tot, period): # pylint: disable=[unused-argument]
        """ Compute carbon_footprint 
        
        Formula ???

        Args:
        - assets
        Returns:
        - share_t
        """
        share_t = 0
        for asset in assets:
            #collection = Collection.objects.get(company=asset.company)
            collection = collections.filter(company=asset.company, collection_type='metrics')[0]
            collection_item_fossil_fuel_active_bool = CollectionItem.objects.get(
                collection=collection, template__name='fossil_fuel_active_bool')
            value = collection_item_fossil_fuel_active_bool.value_boolean

            if value:
                valuation = CollectionItem.objects.get(collection__company=asset.company,
                    item_type='corp_valuation',
                    collection__period_year=period['period_year']).value_pint

                #share_i =(asset.shares_pct / 100) * asset.company.valuation_eur  / invest_value_tot
                share_i = (asset.shares_pct / 100) * valuation  / invest_value_tot
                share_t = share_t + share_i

        share_t = round(share_t * 100, 2)

        return f'{share_t:g}'

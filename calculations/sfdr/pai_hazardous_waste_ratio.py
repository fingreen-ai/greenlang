""" hazardous_waste_ration """
import logging

from fingreen_web.models import CollectionItem

logger = logging.getLogger(__name__)


class HazardousWaste(): #pylint: disable=[invalid-name, too-few-public-methods]
    """ hazardous_waste_ratio """
    
    def impact(self, collections, assets, invest_value_tot, period): # pylint: disable=[unused-argument]
        """ Compute hazardous_waste_ratio 
        
        Formula ???

        Args:
        - assets
        Returns:
        - share_t
        """
        value_t = 0
        weight_t = 0
        for asset in assets:
            #collection = Collection.objects.get(company=asset.company)
            collection = collections.filter(company=asset.company, collection_type='metrics')[0]
            collection_item_waste_hazardous_tonnes = CollectionItem.objects.get(
                collection=collection, template__name='waste_hazardous_tonnes')

            valuation = CollectionItem.objects.get(collection__company=asset.company,
                item_type='corp_valuation',
                collection__period_year=period['period_year']).value_pint

            #weight_i = (asset.shares_pct / 100) * asset.company.valuation_eur
            weight_i = (asset.shares_pct / 100) * valuation
            emissions_i = collection_item_waste_hazardous_tonnes.value_pint
            value_i = 0
            if (emissions_i and weight_i):
                value_i = weight_i * emissions_i / (invest_value_tot / 1000000)

            value_t = value_t + value_i
            weight_t = weight_t + weight_i

        value_t = value_t / weight_t
        value_t = round(value_t, 2)

        return f'{value_t:g}'

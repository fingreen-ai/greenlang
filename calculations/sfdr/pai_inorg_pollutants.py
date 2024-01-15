""" inorg_pollutants """
import logging

from fingreen_web.models import CollectionItem

logger = logging.getLogger(__name__)


class InorganicPollutants(): #pylint: disable=[invalid-name, too-few-public-methods]
    """ inorg_pollutants """

    def impact(self, collections, assets, invest_value_tot, period): # pylint: disable=[unused-argument]
        """ Compute inorg_pollutants 
        
        Formula ???

        Args:
        - assets
        Returns:
        - value_t
        """
        value_t = 0
        weight_t = 0
        for asset in assets:
            #collection = Collection.objects.get(company=asset.company)
            collection = collections.filter(company=asset.company, collection_type='metrics')[0]
            try:
                collection_item_inorg_pollutants_tonnes = CollectionItem.objects.get(
                    collection=collection, template__name='inorg_pollutants_tonnes')
            except: # pylint: disable=[bare-except]
                collection_item_inorg_pollutants_tonnes = None

            if collection_item_inorg_pollutants_tonnes:
                valuation = CollectionItem.objects.get(collection__company=asset.company,
                    item_type='corp_valuation',
                    collection__period_year=period['period_year']).value_pint
                #weight_i = (asset.shares_pct / 100) * asset.company.valuation_eur
                weight_i = (asset.shares_pct / 100) * valuation
                emissions_i = collection_item_inorg_pollutants_tonnes.value_pint
                value_i = 0
                if (emissions_i and weight_i):
                    value_i = weight_i * emissions_i / (invest_value_tot / 1000000)

                value_t = value_t + value_i
                weight_t = weight_t + weight_i

        value_t = value_t / weight_t
        value_t = round(value_t, 2)

        return f'{value_t:g}'

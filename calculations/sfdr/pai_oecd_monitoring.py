""" oecd_monitoring """
import logging

from fingreen_web.models import CollectionItem

logger = logging.getLogger(__name__)


class OecdCompliancePolicies(): # pylint: disable=[too-few-public-methods]
    """ oecd_monitoring """

    def impact(self, collections, assets, invest_value_tot, period): # pylint: disable=[unused-argument]
        """ Compute oecd_monitoring_bool 
        
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
            collection_item_oecd_monitoring_bool = CollectionItem.objects.get(
                collection=collection, template__name='oecd_monitoring_bool')
            value = collection_item_oecd_monitoring_bool.value_boolean

            if value:
                valuation = CollectionItem.objects.get(collection__company=asset.company,
                    item_type='corp_valuation',
                    collection__period_year=period['period_year']).value_pint
                #share_i =(asset.shares_pct / 100) * asset.company.valuation_eur  / invest_value_tot
                share_i = (asset.shares_pct / 100) * valuation  / invest_value_tot
                share_t = share_t + share_i

        share_t = 100 - round(share_t * 100, 2)

        return f'{share_t:g}'

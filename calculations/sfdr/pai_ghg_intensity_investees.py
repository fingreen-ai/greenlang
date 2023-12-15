""" ghg_intensity_investees """
import logging

from fingreen_web.models import CollectionItem

logger = logging.getLogger(__name__)

class GhgIntensityOfInvesteeCompanies(): #pylint: disable=[invalid-name, too-few-public-methods]
    """ ghg_intensity_investees """

    def impact(self, collections, assets, invest_value_tot, period): # pylint: disable=[unused-argument, too-many-locals]
        """ Compute ghg_intensity_investees 
        
        """
        value_t = 0
        for asset in assets:
            # Get spcope 1, 2, 3 ghg emissions
            #collection = Collection.objects.get(company=asset.company)
            collection = collections.filter(company=asset.company, collection_type='metrics')[0]
            collection_items_ghg_1 = CollectionItem.objects.get(collection=collection,
                                                    template__name='ghg_scope_1_tonnes')
            collection_items_ghg_2 = CollectionItem.objects.get(collection=collection,
                                                    template__name='ghg_scope_2_tonnes')
            collection_items_ghg_3 = CollectionItem.objects.get(collection=collection,
                                                    template__name='ghg_scope_3_tonnes')
            if collection_items_ghg_1.value_pint is None:
                collection_items_ghg_1.value_pint = 0
            if collection_items_ghg_2.value_pint is None:
                collection_items_ghg_2.value_pint = 0
            if collection_items_ghg_3.value_pint is None:
                collection_items_ghg_3.value_pint = 0

            ghg_tot = (collection_items_ghg_1.value_pint
                    + collection_items_ghg_2.value_pint
                    + collection_items_ghg_3.value_pint)
            #logger.debug(f'ghg_tot:{ghg_tot}')

            valuation = CollectionItem.objects.get(collection__company=asset.company,
                item_type='corp_valuation', collection__period_year=period['period_year'])

            weight_i = (asset.shares_pct / 100) * valuation.value_pint / invest_value_tot
            #logger.debug(f'weight_i:{weight_i}')

            try:
                # revenue_i = CompanyRevenue.objects.get(company=asset.company,
                #                                        period_year=period['period_year'])
                revenue_i = CollectionItem.objects.get(collection__company=asset.company,
                    item_type='corp_revenue',
                    collection__period_year=period['period_year']).value_pint
            except: # pylint: disable=[bare-except]
                revenue_i = None

            #logger.debug(f'revenue_i:{revenue_i}')

            if revenue_i:
                #value_i = weight_i * ghg_tot / (revenue_i.revenue_eur / 1000000)
                value_i = weight_i * ghg_tot / (revenue_i / 1000000)
                #logger.debug(f'value_i:{value_i}')

                value_t = value_t + value_i

        value_t = round(value_t, 2)
        return f'{value_t:g}'

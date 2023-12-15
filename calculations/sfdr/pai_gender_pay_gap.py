""" gender_pay_gap """
import logging

from fingreen_web.models import CollectionItem

logger = logging.getLogger(__name__)


class GenderPayGap(): # pylint: disable=[too-few-public-methods]
    """ gender_pay_gap """

    def impact(self, collections, assets, invest_value_tot, period): # pylint: disable=[unused-argument]
        """ Compute carbon_footprint 
        
        Formula ???

        Args:
        - assets
        Returns:
        - share_t
        """
        gap_tot = 0
        for asset in assets:
            #collection = Collection.objects.get(company=asset.company)
            collection = collections.filter(company=asset.company, collection_type='metrics')[0]
            collection_item_gender_pay_gap_pct = CollectionItem.objects.get(
                collection=collection, template__name='gender_pay_gap_pct')

            gap_i = 0
            if collection_item_gender_pay_gap_pct.value_float:
                gap_i = collection_item_gender_pay_gap_pct.value_float
            gap_tot = gap_tot + gap_i

        gap_avrg = gap_tot / len(assets)
        gap_avrg = round(gap_avrg, 2)

        return f'{gap_avrg:g}'

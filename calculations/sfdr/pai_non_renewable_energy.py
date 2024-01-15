""" fossil_fuel_exposure """
import logging

from fingreen_web.models import CollectionItem

logger = logging.getLogger(__name__)


class NonRenewableEnergy(): #pylint: disable=[invalid-name, too-few-public-methods]
    """ non_renewable_energy """

    def impact(self, collections, assets, invest_value_tot, period): # pylint: disable=[unused-argument, too-many-locals, too-many-branches]
        """ Compute fossil_fuel_exposure 
        
        Formula ???

        Args:
        - assets
        Returns:
        - share_t
        """
        value_t = 0
        kwh_tot = 0
        for asset in assets:
            # Fetch related collection. TODO could be multiple
            collection = collections.filter(company=asset.company, collection_type='metrics')[0]
            # Fetch metrics value for this collection. TODO could be multiple

            # Legacy energy_consumption_kwh + energy_nonrenewable_pct mode
            mode = None
            try:
                collection_item_energy_nonrenewable_pct = CollectionItem.objects.get(
                    collection=collection, template__name='energy_nonrenewable_pct')
                collection_item_energy_consumption_kwh = CollectionItem.objects.get(
                    collection=collection, template__name='energy_consumption_kwh')
                mode = 'pct'
            except: # pylint: disable=[bare-except]
                pass

            # New templates
            try:
                ci_ec_renewable_kwh = CollectionItem.objects.get(
                    collection=collection, template__name='energy_consumption_renewable_kwh')
                ci_ec_non_renewable_kwh = CollectionItem.objects.get(
                    collection=collection, template__name='energy_consumption_non_renewable_kwh')
                mode = 'new'
            except: # pylint: disable=[bare-except]
                pass

            if mode == 'pct':
                if collection_item_energy_nonrenewable_pct.value_float is None:
                    collection_item_energy_nonrenewable_pct.value_float = 0
                if collection_item_energy_consumption_kwh.value_pint is None:
                    collection_item_energy_consumption_kwh.value_pint = 0

                kw_tot_i = collection_item_energy_consumption_kwh.value_pint

                nonrenewable_pct = collection_item_energy_nonrenewable_pct.value_float

            elif mode == 'new':
                if ci_ec_renewable_kwh.value_pint is None:
                    ci_ec_renewable_kwh.value_pint = 0
                if ci_ec_non_renewable_kwh.value_pint is None:
                    ci_ec_non_renewable_kwh.value_pint = 0

                kw_tot_i = ci_ec_renewable_kwh.value_pint + ci_ec_non_renewable_kwh.value_pint

                nonrenewable_pct = None
                if kw_tot_i > 0:
                    nonrenewable_pct = ci_ec_non_renewable_kwh.value_pint / kw_tot_i * 100

            kwh_tot = kwh_tot + kw_tot_i
            valuation = CollectionItem.objects.get(collection__company=asset.company,
                item_type='corp_valuation',
                collection__period_year=period['period_year']).value_pint
            #logger.debug(f'valuation 1:{valuation}')
            weight_i = (asset.shares_pct / 100) * valuation  / invest_value_tot

            if nonrenewable_pct is not None:
                value_i = weight_i * nonrenewable_pct
            else:
                value_i = 0

            value_t = value_t + value_i

        value_t = round(value_t, 2)

        #logger.debug(f'value_t 1:{value_t}')
        if kwh_tot == 0:
            return None
        return f'{value_t:g}'

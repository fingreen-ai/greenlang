Datasets
========

GHG emission factors
--------------------

For the moment, the GHG emission factors are gathered according to the category in which they are involved. Thus, 
same emission factors can be found in different files.

+-------+--------------------------------+-----------------------------------------------------------------------------------+
| Scope | Category                       | File                                                                              |
+=======+================================+===================================================================================+
| 1     | 1. Stationary combustion       | :download:`csv <./ghg/scope_1/stationary_combustion.csv>`                         |
|       +--------------------------------+-----------------------------------------------------------------------------------+
|       | 2. Mobile combustion           | :download:`csv <./ghg/scope_1/mobile_combustion.csv>`                             |
|       +--------------------------------+-----------------------------------------------------------------------------------+
|       | 3. Fugitive emissions          | :download:`csv <./ghg/scope_1/fugitive_emissions.csv>`                            |
+-------+--------------------------------+-----------------------------------------------------------------------------------+
| 2     | 1. Purchased electricity       | :download:`csv <./ghg/scope_2/purchased_electricity.csv>`                         |
|       +--------------------------------+-----------------------------------------------------------------------------------+
|       | 2. Purchased heat or steam     | :download:`csv <./ghg/scope_2/purchased_heat_or_steam.csv>`                       |
+-------+--------------------------------+-----------------------------------------------------------------------------------+
| 3     | 1. Purchased goods and services| :download:`csv <./ghg/scope_3/purchased_goods_and_services.csv>`                  |
|       +--------------------------------+-----------------------------------------------------------------------------------+
|       | 2. Capital goods               | :download:`csv <./ghg/scope_3/capital_goods.csv>`                                 |
|       +--------------------------------+-----------------------------------------------------------------------------------+
|       | 3. Fuel- and energy-related    | :download:`csv <./ghg/scope_3/upstream_transportation_and_distribution.csv>`      |
|       |    activities                  |                                                                                   |
|       +--------------------------------+-----------------------------------------------------------------------------------+
|       | 4. Upstream transportation and | :download:`csv <./ghg/scope_3/upstream_transportation_and_distribution.csv>`      |
|       |    distribution                |                                                                                   |
|       +--------------------------------+-----------------------------------------------------------------------------------+
|       | 5. Waste generated in          | :download:`csv <./ghg/scope_3/waste_generated_in_operations.csv>`                 |
|       |    operations                  |                                                                                   |
|       +--------------------------------+-----------------------------------------------------------------------------------+
|       | 6. Business travels            | :download:`csv <./ghg/scope_3/business_travels.csv>`                              |
|       +--------------------------------+-----------------------------------------------------------------------------------+
|       | 7. Employee commuting          | :download:`csv <./ghg/scope_3/employee_commuting.csv>`                            |
|       +--------------------------------+-----------------------------------------------------------------------------------+
|       | 8. Upstream leased assets      | :download:`csv <./ghg/scope_3/upstream_leased_assets.csv>`                        |
|       +--------------------------------+-----------------------------------------------------------------------------------+
|       | 9. Downstream transportation   | :download:`csv <./ghg/scope_3/downstream_transportation_and_distribution.csv>`    |
|       |    and distribution            |                                                                                   |
+-------+--------------------------------+-----------------------------------------------------------------------------------+


Combinated emissions factors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Most of the time, the GHG emissions are gathered on public datasets. However, some of them are not available so we have combine different datasets to get the final emission factor.

Scope 3 - Category 7 - Employee commuting
*****************************************

For emissions related to employee commuting and specially for the homeworking

Electricity emission factors related to homeworking, per country
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

General GHG emission factors for electricity consumption are listed by European Commission in the `dataset <http://data.europa.eu/89h/919df040-0252-4e4e-ad82-c054896e1641>`_. However, these factors are not specific to homeworking.

Combining the report `Carbon footprint assessment and reduction <https://www.sqw.co.uk/application/files/7116/4364/4603/Carbon_footprint_report_and_plan_SQW_20-21.pdf>`_ from `SQW <https://www.sqw.co.uk/>`_ 
and the `Homeworking emissions Whitepaper <https://info.eco-act.com/hubfs/0%20-%20Downloads/Homeworking%20emissions%20whitepaper/Homeworking%20Emissions%20Whitepaper%202020.pdf>`_ from `UK Government <https://www.gov.uk/>`_, 
we can get the following emission factors for electricity consumption in the telework sector:

.. table:: CONSTANTS FOR ELECTRICITY
    :align: left

    +--------------------------------------------------------------+--------+
    | Electricity Use of Office Equipment per working hour (Watt)  |140     | 
    +--------------------------------------------------------------+--------+
    | Electricity Use of Lightning  working hour (Watt)            |10      | 
    +--------------------------------------------------------------+--------+
    | Total Electricity Use per working hour (Watt)                |150     | 
    +--------------------------------------------------------------+--------+
    | **Total Electricity Use per  working hour (kW)**             |**0,15**| 
    +--------------------------------------------------------------+--------+

We obtain the total electricity use per working hour as a constant value of 0,15 kW.
This constant is multiplied by the emission factor of the country to get the final emission factor which is reported in the :download:`dataset of this GHG category <./ghg/scope_3/employee_commuting.csv>`

Heating emission factors related to homeworking
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

On the one hand, According to the `Homeworking emissions Whitepaper <https://info.eco-act.com/hubfs/0%20-%20Downloads/Homeworking%20emissions%20whitepaper/Homeworking%20Emissions%20Whitepaper%202020.pdf>`_ from `UK Government <https://www.gov.uk/>`_,
the energy use per working hour for heating is 5kW
On the other hand, according to DEFRA-2022, emission factors for natural gas are  0,23832 kgCO2e per units.
As a result, the emission factor for heating is 1,1916 kgCO2e per working hour.
# [Employee Commuting](#employee-commuting)

### scope

3

### name_fr

Déplacements domicile-travail

### description 

This category includes emissions from the transportation of employees4 between their homes and their worksites. Emissions from employee commuting may arise from: 

- Automobile travel 
- Bus travel 
- Rail travel 
- Air travel 
- Other modes of transportation (e.g., subway, bicycling, walking).  

A reporting company’s scope 3 emissions from employee commuting include the scope 1 and scope 2 emissions of employees and third-party transportation providers.


### description_fr

Cette catégorie comprend les émissions liées au transport des employés4 entre leur domicile et leur lieu de travail. Les émissions liées aux déplacements des employés peuvent provenir de :

- Voyage en voiture
- Voyage en bus
- Voyage en train
- Voyage en avion
- Autres modes de transport (par exemple, métro, vélo, marche).

Les émissions de portée 3 d'une entreprise de déclaration liées aux déplacements des employés comprennent les émissions de portée 1 et de portée 2 des employés et des fournisseurs de transport tiers.


## [Distance-based method](#distance-based-method)

### name_fr

Méthode basée sur la distance

### description

Involves collecting data from employees on commuting patterns (e.g., distance traveled and mode used for commuting) and applying appropriate emission factors for the modes used

**Activity data needed**

Companies should collect data on: Total distance travelled by employees over the reporting period (e.g., passenger-kilometers travelled)

- Mode of transport used for commuting (e.g., train, subway, bus, car, bicycle). 

**Emission factors needed** 

Companies should collect: Emission factors for each mode of transport

**Data collection guidance**

Methods of data collection include: 

- Distance travelled by employees per day, or location of residence and office 
- The number of days per week that employees use different vehicle types (all categories of subway, car, bus, train, bicycle, etc.) 
- Number of commuting days per week and number of weeks worked per year 
- If the company is multinational: employees’ region of residence/work (since transportation emission factors vary by region) 
- Whether there is a significant car-pooling scheme in operation, the proportion of employees using the scheme and the average occupancy per vehicle 
- If applicable, the amount of energy used from teleworking (e.g., kWh of gas, electricity consumed). 

Collecting commuting data from all employees through a survey may not be feasible. Companies may extrapolate from a representative sample of employees to represent the total commuting patterns of all employees. For example, a company with 4,000 employees, who each have different commuting profiles, may extrapolate from a representative sample of, for example, 1,000 employees to approximate the total commuting of all employees

### description_fr

Implique la collecte de données auprès des employés sur les habitudes de déplacement (par exemple, la distance parcourue et le mode utilisé pour les déplacements) et l'application de facteurs d'émission appropriés pour les modes utilisés

**Données d'activité nécessaires**

Les entreprises doivent collecter des données sur : Distance totale parcourue par les employés au cours de la période de déclaration (par exemple, passagers-kilomètres parcourus)

- Mode de transport utilisé pour les déplacements (par exemple, train, métro, bus, voiture, vélo).

**Facteurs d'émission nécessaires**

Les entreprises doivent collecter : Facteurs d'émission pour chaque mode de transport

**Guide de collecte de données**

Les méthodes de collecte de données comprennent :

- Distance parcourue par les employés par jour, ou lieu de résidence et bureau
- Le nombre de jours par semaine que les employés utilisent différents types de véhicules (toutes les catégories de métro, voiture, bus, train, vélo, etc.)
- Nombre de jours de déplacement par semaine et nombre de semaines travaillées par an
- Si l'entreprise est multinationale : région de résidence / travail des employés (les facteurs d'émission de transport variant selon la région)
- S'il existe un programme de covoiturage important en fonctionnement, la proportion d'employés utilisant le programme et l'occupation moyenne par véhicule
- Le cas échéant, la quantité d'énergie utilisée pour le télétravail (par exemple, kWh de gaz, électricité consommée).

La collecte de données de déplacement auprès de tous les employés par le biais d'une enquête peut ne pas être réalisable. Les entreprises peuvent extrapoler à partir d'un échantillon représentatif d'employés pour représenter les habitudes de déplacement totales de tous les employés. Par exemple, une entreprise de 4 000 employés, qui ont chacun des profils de déplacement différents, peut extrapoler à partir d'un échantillon représentatif de, par exemple, 1 000 employés pour approximer le déplacement total de tous les employés

### implem_path

greenlang.calculations.ghg.scope_3.employee_commuting.DistanceBasedMethod


## [Equipment-based method](#equipment-based-method)

### name_fr

Méthode basée sur l'équipement

### description

Emissions from teleworking

### description_fr

Émissions liées au télétravail

### implem_path

greenlang.calculations.ghg.scope_3.employee_commuting.EquipmentBasedMethod

## [Fuel Amount Method](#fuel-amount-method)

### name_fr

Méthode basée sur la consommation de carburant

### description

The "fuel amount" method for calculating emissions is a direct approach that relies on actual fuel consumption data. This method involves calculating emissions, such as CO2, based on the quantity of fuel used by vehicles. To implement this approach effectively, access to detailed records is essential, including fuel consumption logs, gas station data, or vehicle mileage. The precision of this method is particularly high when accurate and specific fuel usage data is available. The "fuel amount" method provides a granular understanding of emissions by directly tying them to real-world fuel consumption.

### description_fr

La méthode basée sur la quantité de carburant pour le calcul des émissions est une approche directe qui repose sur des données réelles de consommation de carburant. Cette méthode consiste à calculer les émissions, telles que le CO2, en fonction de la quantité de carburant utilisée par les véhicules. Pour mettre en œuvre cette approche de manière efficace, l'accès à des dossiers détaillés est essentiel, notamment des journaux de consommation de carburant, des données de stations-service ou des kilométrages des véhicules. La précision de cette méthode est particulièrement élevée lorsque des données de consommation de carburant précises et spécifiques sont disponibles. Celle-ci offre une compréhension granulaire des émissions en les reliant directement à la consommation de carburant du monde réel.

### implem_path

greenlang.calculations.ghg.scope_3.employee_commuting.FuelAmountMethod
# [Waste Generated in Operations](#waste-generated-in-operations)

### scope

3

### name_fr

Déchets générés dans les opérations

### description 

Category 5 includes emissions from third-party disposal and treatment of waste generated in the reporting company’s owned or controlled operations in the reporting year. This category includes emissions from disposal of both solid waste and wastewater.

Only waste treatment in facilities owned or operated by third parties is included in scope 3. Waste treatment at facilities owned or controlled by the reporting company is accounted for in scope 1 and scope 2. Treatment of waste generated in operations is categorized as an upstream scope 3 category because waste management services are purchased by the reporting company. This category includes all future emissions that result from waste generated in the reporting year. Waste treatment activities may include:

- Disposal in a landfill
- Disposal in a landfill with landfill-gas-to-energy (LFGTE) – that is, combustion of landfill gas to generate electricity
- Recovery for recycling
- Incineration
- Composting
- Waste-to-energy (WTE) or energy-from-waste (EfW) – that is, combustion of municipal solid waste (MSW) to generate electricity
- Wastewater treatment.

A reporting company’s scope 3 emissions from waste generated in operations derive from the scope 1 and scope 2 emissions of solid waste and wastewater management companies. Companies may optionally include emissions from transportation of waste in vehicles operated by a third party.

**Calculating emissions from transportation**

Companies may use any one of the following methods to calculate emissions from waste generated in their operations,
but managed by third parties:

- Supplier-specific method, which involves collecting waste-specific scope 1 and scope 2 emissions data directly from waste treatment companies (e.g., for incineration, recovery for recycling)
- Waste-type-specific method, which involves using emission factors for specific waste types and waste treatment methods
- Average-data method, which involves estimating emissions based on total waste going to each disposal method (e.g., landfill) and average emission factors for each disposal method. 

### description_fr

Les entreprises peuvent utiliser l'une des méthodes suivantes pour calculer les émissions provenant des déchets générés dans leurs opérations, mais gérés par des tiers :

- Méthode spécifique au fournisseur, qui consiste à collecter directement des données sur les émissions de la portée 1 et de la portée 2 spécifiques aux déchets auprès des entreprises de traitement des déchets (par exemple, pour l'incinération, la récupération en vue du recyclage).
- Méthode spécifique au type de déchets, qui consiste à utiliser des facteurs d'émission pour des types de déchets spécifiques et des méthodes de traitement des déchets spécifiques.
- Méthode de données moyennes, qui consiste à estimer les émissions en fonction du volume total de déchets envoyés à chaque méthode d'élimination (par exemple, l'enfouissement) et des facteurs d'émission moyens pour chaque méthode d'élimination.


## [Supplier specific method](#supplier-specific-method)

### name_fr

Méthode spécifique au fournisseur

### description

In certain cases, third party waste-treatment companies may be able to provide waste-specific scope 1 and scope 2 emissions data directly to customers (e.g., for incineration, recovery for recycling). 

**Activity data needed, Companies should collect:** 

- Allocated scope 1 and scope 2 emissions of the waste-treatment company (allocated to the waste collected from the reporting company). 

**Emission factors needed, Companies should collect:**
 
- The reporting company collects emissions data from waste treatment companies, so no emission factors are required (the company would have already used emission factors to calculate the emissions).

### description_fr

Dans certains cas, des entreprises de traitement des déchets tierces peuvent fournir directement aux clients des données sur les émissions de la portée 1 et de la portée 2 spécifiques aux déchets (par exemple, pour l'incinération ou la récupération en vue du recyclage).

**Données d'activité requises :**

- Les entreprises devraient collecter les émissions de la portée 1 et de la portée 2 attribuées à l'entreprise de traitement des déchets (attribuées aux déchets collectés auprès de l'entreprise déclarante).

**Facteurs d'émission nécessaires :**

- Si la méthode spécifique au fournisseur est utilisée, l'entreprise déclarante collecte des données d'émissions auprès des entreprises de traitement des déchets, donc aucun facteur d'émission n'est requis (l'entreprise aurait déjà utilisé des facteurs d'émission pour calculer les émissions).


### implem_path

ghg.calculation.scope_3.waste_generated_in_operations.SupplierSpecificMethod


## [Average-data method](#average-data-method)

### name_fr

Méthode des données moyennes

### description

Companies using the average-data method should collect data based on the total waste diversion rates from the reporting organization. This is often preferable where the type of waste produced is unknown. However, this method has a higher degree of uncertainty than the waste-type-specific method. 

**Activity data needed, Companies should collect:** 

- Total mass of waste generated in operations, 
- Proportion of this waste being treated by different methods (e.g., percent landfilled, incinerated, recycled). Because many waste operators charge for waste by disposal method, this data may be collected from utility bills. The information may also be stored on internal IT systems. 

**Emission factors needed, Companies should collect:**

- Average waste treatment specific emission factors based on all waste disposal types. The emission factors should include end-of-life processes only.


### description_fr

Les entreprises qui utilisent la méthode de données moyennes devraient collecter des données basées sur les taux de diversion totale des déchets de l'organisation déclarante. Cette méthode est souvent préférable lorsque le type de déchets produit est inconnu. Cependant, cette méthode présente un degré d'incertitude plus élevé que la méthode spécifique au type de déchets.

**Données d'activité requises :**

Les entreprises devraient collecter les données suivantes :

- La masse totale de déchets générée dans leurs opérations.
- La proportion de ces déchets traitée par différentes méthodes (par exemple, pourcentage d'enfouissement, d'incinération, de recyclage). Comme de nombreuses entreprises de traitement des déchets facturent en fonction de la méthode d'élimination des déchets, ces données peuvent être collectées à partir des factures de services publics. Les informations peuvent également être stockées dans les systèmes informatiques internes.

**Facteurs d'émission nécessaires :**

- Les entreprises devraient collecter des facteurs d'émission spécifiques à la méthode de traitement des déchets basés sur tous les types d'élimination des déchets. Les facteurs d'émission devraient inclure uniquement les processus en fin de vie.


### implem_path

ghg.calculation.scope_3.waste_generated_in_operations.AverageDataMethod


## [Waste type method](#waste-type-method)

### name_fr

Méthode par type de déchets

### description

Emissions from waste depend on the type of waste being disposed of, and the waste diversion method. Therefore, companies should try to differentiate waste based on its type (e.g., cardboard, food-waste, wastewater) and the waste treatment method (e.g., incinerated, landfilled, recycled, wastewater). 

**Activity data needed, Companies should collect:** 

- Waste produced (e.g., tonne/ cubic meter) and type of waste generated in operations,
- For each waste type, specific waste treatment method applied (e.g., landfilled, incinerated, recycled). Because many waste operators charge for waste disposal by the method used, disposal methods may be identified on utility bills. The information may also be stored on internal IT systems. Companies with leased facilities may have difficulty obtaining primary data.

**Emission factors needed, Companies should collect:**

- Waste type-specific and waste treatment-specific emission factors. The emission factors should include end-of-life processes only. Emission factors may include emissions from transportation of waste. 


### description_fr

Les émissions provenant des déchets dépendent du type de déchets qui est éliminé et de la méthode de diversion des déchets. Par conséquent, les entreprises devraient essayer de différencier les déchets en fonction de leur type (par exemple, carton, déchets alimentaires, eaux usées) et de la méthode de traitement des déchets (par exemple, incinération, enfouissement, recyclage, traitement des eaux usées).

**Données d'activité requises :**

Les entreprises devraient collecter les données suivantes :

- Les déchets produits (par exemple, en tonnes ou en mètres cubes) et le type de déchets générés dans leurs opérations.
- Pour chaque type de déchets, la méthode de traitement spécifique des déchets appliquée (par exemple, enfouissement, incinération, recyclage). Comme de nombreuses entreprises de traitement des déchets facturent en fonction de la méthode d'élimination des déchets, les méthodes d'élimination peuvent être identifiées sur les factures de services publics. Les informations peuvent également être stockées dans les systèmes informatiques internes. Les entreprises ayant des installations louées peuvent rencontrer des difficultés pour obtenir des données primaires.

**Facteurs d'émission nécessaires :**

- Les entreprises devraient collecter des facteurs d'émission spécifiques au type de déchets et à la méthode de traitement des déchets. Les facteurs d'émission devraient inclure uniquement les processus en fin de vie. Les facteurs d'émission peuvent également inclure les émissions liées au transport des déchets.

### implem_path

ghg.calculation.scope_3.waste_generated_in_operations.WasteTypeMethod
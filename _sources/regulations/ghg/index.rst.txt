.. important:: Document format:

    - Each document is a markdown file (.md)
    - Each document has a title, which is the first line of the file, prefixed with a hash (#). This title is a in fact a link to the document with category name as text and category slugified name as target.
    - Second level headings (##) are used to define calculation methods. The method name is used as text and the method slugified name is used as target.
    - Whether for the category or its calculation methods, attributes are a third level heading (###) with attribute name as text and attribute value as paragraph below. 

Scope 1
~~~~~~~

.. toctree::
    :maxdepth: 1

    scope_1/01_Stationary Combustion.md
    scope_1/02_Mobile Combustion.md
    scope_1/03_Fugitive Emissions.md

Scope 2
~~~~~~~

.. toctree::
    :maxdepth: 1

    scope_2/01_Purchased Electricity.md
    scope_2/02_Purchased Heat and Steam.md

Scope 3
~~~~~~~

.. toctree::
    :maxdepth: 1

    scope_3/01_Purchased Goods and Services.md
    scope_3/02_Capital Goods.md
    scope_3/03_Fuel and Energy Related Activities.md
    scope_3/04_Upstream Transportation and Distribution.md
    scope_3/05_Waste Generated in Operations.md
    scope_3/06_Business Travels.md
    scope_3/07_Employee Commuting.md
    scope_3/08_Upstream Leased Assets.md
    scope_3/09_Downstream Transportation and Distribution.md
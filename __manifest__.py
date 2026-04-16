{
    'name': 'Champs IBATIX',
    'version': '19.0.1.0.0',
    'category': 'Customizations',
    'summary': 'Champs personnalisés IBATIX sur produits, clients et devis',
    'author': 'ibatix',
    'depends': ['sale', 'product', 'contacts', 'objets_ibatix'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_views.xml',
        'views/partner_views.xml',
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}

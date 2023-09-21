{
    'name': "Boton de Pago del Banco de Venezuela",
    'category': 'eCommerce',
    'summary': 'Pagos por Banco de Venezuela',
    'author': "Luis Millan",
    'depends': [
        'payment'
    ],
    'data': [
        'views/payment_views.xml',
        'views/payment_authorize_templates.xml',
        'data/payment_acquirer_data.xml'
    ],
    'installable': True,
}
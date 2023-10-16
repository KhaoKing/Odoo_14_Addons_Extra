# -*- coding: utf-8 -*-
{
    'name': "Salesperson Restriction",
    'summary': """
        Seller restriction. You cannot see other clients if they are not yours.""",
    'author': "Leonardo Khaoim",
    'version': '1.0',
    'depends': ['base', 'sale'],
    'data': [
        'security/sale_security.xml',
        'views/views_restriction_sale.xml'
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}

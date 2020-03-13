# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Transfers',
    'version': '1.0',
    'summary': 'Module for Money Transfer',
    'category': 'Extra Tools',
    'description':
    """
Transifex integration
=====================
This module will add a link to the Transifex project in the translation view.
The purpose of this module is to speed up translations of the main modules.

To work, Odoo uses Transifex configuration files `.tx/config` to detec the
project source. Custom modules will not be translated (as not published on
the main Transifex project).

The language the user tries to translate must be activated on the Transifex
project.
        """,
    'data': [
	'transfers.xml',
        
    ],
    'depends': [],
    'installable':True,
    'application':True,
    'auto_install':False,
}

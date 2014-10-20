# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Alexandre Fayolle
#    Copyright 2012 Camptocamp SA
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{'name': 'Picking dispatch',
 'version': '1.2.3',
 'author': 'Camptocamp',
 'maintainer': 'Camptocamp',
 'category': 'Products',
 'complexity': "normal",  # easy, normal, expert
 'depends': ['stock',
             'base',
             'report_webkit',
             'base_headers_webkit',
             ],
 'description': """Dispatch pickings to employees working in warehouses
 """,
 'website': 'http://www.camptocamp.com/',
 'init_xml': [],
 'update_xml': ['picking_dispatch_view.xml',
                'picking_dispatch_sequence.xml',
                'wizard/create_dispatch_view.xml',
                'wizard/dispatch_assign_picker_view.xml',
                'wizard/dispatch_start_view.xml',
                'wizard/check_assign_all_view.xml',
                'report.xml',
                'cron_data.xml',
                'security/ir.model.access.csv',
                'security/security.xml',
                # 'picking_dispatch_workflow.xml',
                ],
 'demo_xml': [],
 'tests': [],
 'installable': False,
 'auto_install': False,
 'license': 'AGPL-3',
 'application': False
 }
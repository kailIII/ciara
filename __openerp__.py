# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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
# Generated by the OpenERP plugin for Dia !
{
        "name" : "fundo_zamorano",
        "version" : "0.6",
        "author" : "Ahida Briceño / Victor Davila",
        "website" : "http://ciara.com.ve",
        "category" : "Unknown",
        "description": """ Versión Numero 5 del modulo de Fundos Zamoranos  """,
        "depends" : ['base'],
        "init_xml" : [ ],
        "demo_xml" : [ ],
        "update_xml" : [
         'security/fundo_zamorano.xml', 
         'data/redi.xml', 
         'data/estados.xml',
         'data/municipios.xml',
         'data/parroquias.xml',
         'fundo_zamorano_view.xml',
         'organizacion4/organizacion4_view.xml',
         'ejecucion_fisica1/ejecucion_fisica1_view.xml',
         'usuarios/usuarios_view.xml',
         'asociados2/asociados2_view.xml',
         'security/per_admin_fundo/ir.model.access.csv',
         'security/per_coor_ana/ir.model.access.csv',
         'security/per_coor_dir/ir.model.access.csv',
         'security/per_coor_sup_tec/ir.model.access.csv',
         'security/per_coor_tec/ir.model.access.csv',
         'security/filtro_tree.xml',
         'wizard/ejecucion_fisica_wizard.xml',
         'report/ejecucion_fisica_report.xml',
        ],
        "installable": True
}

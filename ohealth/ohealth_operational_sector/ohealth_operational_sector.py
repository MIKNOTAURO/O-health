# -*- coding: utf-8 -*-
#/#############################################################################
#
#    HITSF
#    
#    Special Credit and Thanks to Thymbra Latinoamericana S.A.
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
#/#############################################################################
from osv import osv
from osv import fields


class OHealthOperationalSector(osv.Model):
    _name = 'ohealth.operational_sector'

    _columns = {
        'info': fields.text(string='Extra Information'),
        'operational_area_id': fields.many2one('ohealth.operational_area',
                                               string='Operational Area', ),
        'name': fields.char(size=256, string='Op. Sector', required=True, 
                            help='Region included in an operational area'),
    }
    _sql_constraints = [
        ('name_uniq', 'UNIQUE(name)', 'Name must be unique!'),
    ]
OHealthOperationalSector()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

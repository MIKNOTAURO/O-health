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


class OHealthSpecialty(osv.Model):
    _name = 'ohealth.specialty'

    _columns = {
        'code': fields.char(size=256, string='Code'),
        'name': fields.char(size=256, string='Specialty', required=True,
                            translate=True),
    }
    _sql_constraints = [
        ('name_uniq', 'UNIQUE(name)', 'Name must be unique!'),
    ]
OHealthSpecialty()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

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


class OHealthDiseaseGene(osv.osv):

    _name = 'ohealth.disease.gene'
    _description = 'Disease Genes'

    _columns = {
        'name': fields.char('Official Symbol', size=256, required=True),
        'gene_id': fields.char('Gene ID', size=256),
        'long_name': fields.char('Official Long Name', size=256, required=True),
        'location': fields.char('Location', size=256, required=True, help="Locus of the chromosome"),
        'chromosome': fields.char('Affected Chromosome', size=256, required=True),
        'info': fields.text(string='Information'),
        'dominance' : fields.selection([
                    ('d', 'dominant'),
                    ('r', 'recessive'),
                    ], 'Dominance', select=True)

    }

OHealthDiseaseGene()



class PatientGeneticRisk(osv.Model):
    
    _name = 'ohealth.patient.genetic.risk'
    _description = 'Patient Genetic Risks'
    _columns = {
            'patient_id' : fields.many2one('ohealth.patient', 'Patient', select=True),
            'disease_gene' : fields.many2one('ohealth.disease.gene', 'Disease Gene', required=True),
                }
PatientGeneticRisk()


class FamilyDiseases(osv.Model):
    
    _name = 'ohealth.patient.family.diseases'
    _description = 'Family Diseases'
    _columns = {
    'patient_id' : fields.many2one('ohealth.patient', 'Patient', select=True),
    'name' : fields.many2one('ohealth.pathology', 'Disease', required=True),
    'xory' : fields.selection([
            ('m', 'Maternal'),
            ('f', 'Paternal'),
            ], 'Maternal or Paternal', select=True),
    'relative' : fields.selection([
            ('mother', 'Mother'),
            ('father', 'Father'),
            ('brother', 'Brother'),
            ('sister', 'Sister'),
            ('aunt', 'Aunt'),
            ('uncle', 'Uncle'),
            ('nephew', 'Nephew'),
            ('niece', 'Niece'),
            ('grandfather', 'Grandfather'),
            ('grandmother', 'Grandmother'),
            ('cousin', 'Cousin'),
            ], 'Relative',
            help="First degree = siblings, mother and father; second degree = "
            "Uncles, nephews and Nieces; third degree = Grandparents and cousins",
            required=True),
            }

FamilyDiseases()

class ohealthPatient(osv.Model):
    'Add to the Medical patient_data class (ohealth.patient) the genetic ' \
    'and family risks'
    _inherit='ohealth.patient'
    _columns = {
            'genetic_risks' : fields.one2many('ohealth.patient.genetic.risk', 'patient_id', 'Genetic Risks'),
            'family_history' : fields.one2many('ohealth.patient.family.diseases', 'patient_id', 'Family History'),
                }

ohealthPatient()


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

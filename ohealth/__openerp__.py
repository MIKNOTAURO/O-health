##############################################################################
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>). All Rights Reserved
#    OHealth, HMS Opensource Solution
##############################################################################

##############################################################################
#    This project is mantained by O-Health Team:
#    
#
##############################################################################
#    It is a collaborative effort between several companies that want to join
#    efforts in have a proposal solid and strong in the Health Care environment
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
{

    'name': 'OHealth : Free Health and Hospital Information System',
    'version': '1.0',
    'author': "O-Health Team",
    'category': 'Generic Modules/Others',
    'depends': ['base', 'sale', 'purchase', 'account', 'product'],
    'application': True,
    'description': """

About OHealth
---------------

OHealth is a multi-user, highly scalable, centralized Electronic
Medical Record (EMR) and Hospital Information System for openERP.

OHealth provides a free universal Health and Hospital Information System,
so doctors and institutions all over the world,
specially in developing countries will benefit from a centralized,
high quality, secure and scalable system.

OHealth at a glance:

    * Strong focus in family medicine and Primary Health Care
    
    * Major interest in Socio-economics (housing conditions, substance abuse,
    education...)
    
    * Diseases and Medical procedures standards (like ICD-10 / ICD-10-PCS ...)
    
    * Patient Genetic and Hereditary risks : Over 4200 genes related to
    diseases (NCBI / Genecards)
    
    * Epidemiological and other statistical reports
    
    * 100% paperless patient examination and history taking
    
    * Patient Administration 
    (creation, evaluations / consultations, history ... )
    
    * Doctor Administration
    
    * Lab Administration
    
    * Medicine / Drugs information (vademécum)
    
    * Medical stock and supply chain management
    
    * Hospital Financial Administration
    
    * Designed with industry standards in mind
    
    * Open Source : Licensed under AGPL
    
""",
    "website": "http://launchpad.net/ohealth",
    "licence": "AGPL v3",
    "data": [
        'sequence/ohealth_sequence.xml',
        'ohealth_secondary_condition/ohealth_secondary_condition_view.xml',
        'ohealth_pathology_category/ohealth_pathology_category_view.xml',
        'ohealth_signs_and_symptoms/ohealth_signs_and_symptoms_view.xml',
        'product_product/product_product_view.xml',
        'ohealth_physician/ohealth_physician_view.xml',
        'ohealth_directions/ohealth_directions_view.xml',
        'ohealth_insurance/ohealth_insurance_view.xml',
        'res_partner/res_partner_view.xml',
        'ohealth_pathology/ohealth_pathology_view.xml',
        'ohealth_operational_area/ohealth_operational_area_view.xml',
        'ohealth_ethnicity/ohealth_ethnicity_view.xml',
        'ohealth_operational_sector/ohealth_operational_sector_view.xml',
        'ohealth_prescription_order/ohealth_prescription_order_view.xml',
        'ohealth_medicament_category/ohealth_medicament_category_view.xml',
        'ohealth_insurance_plan/ohealth_insurance_plan_view.xml',
        'ohealth_diagnostic_hypothesis/'
        'ohealth_diagnostic_hypothesis_view.xml',
        'ohealth_procedure/ohealth_procedure_view.xml',
        'ohealth_medication_template/ohealth_medication_template_view.xml',
        'ohealth_vaccination/ohealth_vaccination_view.xml',
        'ohealth_medication_dosage/ohealth_medication_dosage_view.xml',
        'ohealth_family_member/ohealth_family_member_view.xml',
        'ohealth_hospital_ward/ohealth_hospital_ward_view.xml',
        'ohealth_hospital_or/ohealth_hospital_or_view.xml',
        'ohealth_drug_form/ohealth_drug_form_view.xml',
        'ohealth_patient_medication/ohealth_patient_medication_view.xml',
        'ohealth_patient_evaluation/ohealth_patient_evaluation_view.xml',
        'ohealth_hospital_building/ohealth_hospital_building_view.xml',
        'ohealth_patient/ohealth_patient_view.xml',
        'ohealth_prescription_line/ohealth_prescription_line_view.xml',
        'ohealth_patient_disease/ohealth_patient_disease_view.xml',
        'ohealth_drug_route/ohealth_drug_route_view.xml',
        'ohealth_hospital_unit/ohealth_hospital_unit_view.xml',
        'ohealth_appointment/ohealth_appointment_view.xml',
        'ohealth_specialty/ohealth_specialty_view.xml',
        'ohealth_family/ohealth_family_view.xml',
        'ohealth_hospital_bed/ohealth_hospital_bed_view.xml',
        'ohealth_occupation/ohealth_occupation_view.xml',
        'ohealth_disease_group_members/'
        'ohealth_disease_group_members_view.xml',
        'ohealth_medicament/ohealth_medicament_view.xml',
        'ohealth_pathology_group/ohealth_pathology_group_view.xml',
        'ohealth_gynecology_and_obstetrics/ohealth_gynecology_and_obstetrics_view.xml',
        'ohealth_lifestyle/ohealth_lifestyle_view.xml',
        'ohealth_lifestyle/data/recreational_drugs.xml',
        'ohealth_genetics/ohealth_disease_gene_view.xml',
        'ohealth_genetics/data/disease_genes.xml',
        'ohealth_hospital_profile/ohealth_hospital_profile_view.xml',
        'security/ir.model.access.csv',
        'ohealth_menu.xml',
    ],
    "demo": [

    ],
    'test':[
            'test/physician.yml',
            'test/patient.yml',
            'test/partners.yml',
            'test/insurance_plan.yml',
            'test/insurance.yml',
            'test/physician_speciality.yml'
    ],
    'css': [

    ],
    'js': [

    ],
    'qweb': [

    ],
    "active": False
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

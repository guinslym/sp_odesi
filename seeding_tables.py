from peewee import *
from datetime import datetime

from odesi_tables import *

GROUPS = ['ALBERTA', 'ALGOMA', 'BROCK', 'CALGARY', 'CAMBRIAN', 'CARLETON',
       'CONCORDIA', 'FANSHAWE', 'FRASER', 'GUELPH', 'HEC', 'HOSPITALS',
       'KPU', 'LAKEHEAD', 'LAURENTIAN', 'LAURIER', 'LAVAL', 'MACEWAN',
       'MANITOBA', 'MCGILL', 'MCMASTER', 'MONTREAL', 'NIPISSING', 'OCAD',
       'OTTAWA', 'PUBLISHER', 'QUEENS', 'REGINA', 'RMC', 'RYERSON',
       'SHERBROOKE', 'SHERIDAN', 'STATCAN', 'TORONTO', 'TRENT', 'TRU',
       'UNBC', 'UOIT', 'UQAC', 'UQAM', 'USASK', 'WATERLOO', 'WESTERN',
       'WINDSOR', 'WINNIPEG', 'YORK', 'ZZ-UNKNOWN']

#result = df.sample(20)[['Survey \ School', 'Survey ID', 'Collection'] ].to_dict('records')
SURVEYS = [{'Survey \\ School': 'Enquête sur la population active, novembre 1980 [Canada]', 'Survey ID': '71M0001XCB_F_1980_novembre', 'Collection': 'DLI'}, {'Survey \\ School': "Federal2006ExitPolldataNOSOHO'[0]", 'Survey ID': "Federal2006ExitPolldataNOSOHO'[0]", 'Collection': 'UNASSIGNED'}, {'Survey \\ School': 'Canadian Gallup Poll, March 1978, #410', 'Survey ID': 'cipo_410_E_1978-03', 'Collection': 'CGP'}, {'Survey \\ School': 'Enquête sur la population active, juillet 2009 [Canada] [Remanié Recensement 2011]', 'Survey ID': 'epa-71M0001XCB-F-juillet-2009-remanie-2011', 'Collection': 'DLI'}, {'Survey \\ School': 'Health Statistics at a Glance, 1999 [Canada] [B2020]', 'Survey ID': 'hlthind_82F0075_E_1999', 'Collection': 'DLI_AGGREGATE'}, {'Survey \\ School': "Enquête sur l'adhésion syndicale, 1984, [Canada]", 'Survey ID': 'easy_71M0004_F_1984', 'Collection': 'DLI'}, {'Survey \\ School': 'Labour Force Survey, May 2006 [Canada] [Rebased, 2011 Census of Population]', 'Survey ID': 'LFS-71M0001-E-2006-May-Rebased2011', 'Collection': 'DLI'}, {'Survey \\ School': 'Canadian Gallup Poll, April 1988, #532_1', 'Survey ID': 'cipo_532_1_E_1988-04', 'Collection': 'CGP'}, {'Survey \\ School': 'CR9306A [CROP Political Survey 1993-06A]', 'Survey ID': 'cora-cr1993-E-1993-06A', 'Collection': 'CORA'}, {'Survey \\ School': 'Enquête sur la population active, avril 1987 [Canada] [Remanié Recensement 2006]', 'Survey ID': 'epa-71M0001XCB-F-avril-1987-remanie-2006', 'Collection': 'DLI'}, {'Survey \\ School': 'Absence from Work Survey, 1988 [Canada]', 'Survey ID': 'aws_75M0007_E_1988', 'Collection': 'DLI'}, {'Survey \\ School': 'Enquête sur la population active, janvier 1997 [Canada] [Remanié Recensement 2006]', 'Survey ID': 'epa-71M0001XCB-F-1997-janvier-remanie-2006', 'Collection': 'DLI'}, {'Survey \\ School': '1981 Census of Population [Canada] Public Use Microdata File (PUMF): Individual  File', 'Survey ID': 'pumf_95M00_E_1981_individual', 'Collection': 'DLI'}, {'Survey \\ School': 'International Travel Survey, 2009: Canadian Resident Trips Abroad', 'Survey ID': 'its_66M00010_E_2009Q1-Q4_ca', 'Collection': 'DLI'}, {'Survey \\ School': 'Ontario College Applicant Survey, 2004 [Canada]', 'Survey ID': 'cmsf_ocas_E_2004', 'Collection': 'CMSF'}, {'Survey \\ School': 'Fichier de conversion des codes postaux [Canada], août 2015', 'Survey ID': 'FCCP-92154G-F-2015-aout', 'Collection': 'DLI'}, {'Survey \\ School': 'Survey of Labour and Income Dynamics, 2009 [Canada]: Key File', 'Survey ID': 'slid_75M0010XCB_E_2009ke', 'Collection': 'DLI'}, {'Survey \\ School': 'Canadian Gallup Poll, July 1971, #348', 'Survey ID': 'cipo_348_E_1971-07', 'Collection': 'CGP'}, {'Survey \\ School': 'Canadian Community Health Survey, 2011-2012: Annual Component', 'Survey ID': 'cchs-82M0013-E-2011-2012-Annual-component', 'Collection': 'DLI'}, {'Survey \\ School': 'National Population Health Survey, 1996-97 [Canada]: General File', 'Survey ID': 'nphs_82M0009_E_1996_general-file', 'Collection': 'DLI'}]

COLLECTIONS = ['DLI', 'OTHER_GOV', 'UNASSIGNED', 'CORA',
       'CGP', 'ARG', 'DLI_AGGREGATE', 'LEGER', 'GUELPH', 'ISSP', 'CHM',
       'CRIC', 'CIO', 'COMMON', 'FREE', 'TESTCOLL', 'OTHER_RESEARCHER',
       'CPRN', 'ISO', 'DAVID', 'FORUM', 'ICPSR','UPDATE']

def seed_collections():
    for col in COLLECTIONS:
        Collections.create(collection_name=col).save()

def seed_groups():
    for school in GROUPS:
        Groups.create(school_name=school, coll_ids="Unknown").save()

def seed_surveys():
    for survey in SURVEYS:
        Surveys.create(
            survey_id=survey.get("Survey ID"), 
            dash_survey_id="Unknown"
            collection_id=4,
            survey_name=survey.get('Survey \\ School')).save()

if __name__ == '__main__':
    seed_collections()
    seed_groups()
    seed_surveys()

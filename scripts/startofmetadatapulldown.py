#this function should be added to ag_data_access when complete
def get_new_survey_metadata(barcode):
    sql = """
    select akb.barcode as sample_name,
        akb.barcode as ANONYMIZED_NAME,
        akb.sample_date as collection_date,
        'y' as "public",
        0 as depth,
        'American Gut Project ' || akb.site_sampled || ' sample' as
            DESCRIPTION,
        akb.sample_time,
        0 as altitude,
        'y' as assigned_from_geo,
        'American Gut Project' as TITLE,
        case akb.site_sampled
            when 'Please select...' then 'unknown'
            else akb.site_sampled
        end as site_sampled,
        md5(md5(cast(ahs.ag_login_id as varchar(100)) || ahs.participant_name))
            as host_subject_id,
        case akb.site_sampled
            when 'Stool' then '408170'
            when 'Mouth' then '447426'
            when 'Right hand' then '539655'
            when 'Left hand' then '539655'
            when 'Forehead' then '539655'
            when 'Nares' then '1115523'
            when 'Hair' then '646099'
            when 'Tears' then '646099'
            when 'Ear wax' then '646099'
            when 'Nasal mucus' then '1115523'
            when 'Vaginal mucus' then '646099'
            when 'Please select...' then 'unknown'
            else akb.site_sampled
        end as TAXON_ID,
        '9606' host_taxid,
        case akb.site_sampled
            when 'Stool' then 'human gut metagenome'
            when 'Mouth' then 'human oral metagenome'
            when 'Right hand' then 'human skin metagenome'
            when 'Left hand' then 'human skin metagenome'
            when 'Forehead' then 'human skin metagenome'
            when 'Nares' then 'upper respiratory tract metagenome'
            when 'Hair' then 'human metagenome'
            when 'Tears' then 'human metagenome'
            when 'Ear wax' then 'human metagenome'
            when 'Vaginal mucus' then 'human metagenome'
            when 'Please select...' then 'unknown'
            else akb.site_sampled
        end as common_name,
        'human' as host_common_name,
        case akb.site_sampled
            when 'Stool' then 'UBERON:feces'
            when 'Mouth' then 'UBERON:oral cavity'
            when 'Right hand' then 'UBERON:skin'
            when 'Left hand' then 'UBERON:skin'
            when 'Forehead' then 'UBERON:skin'
            when 'Nares' then 'UBERON:nose'
            when 'Hair' then 'UBERON:hair'
            when 'Tears' then 'UBERON:eye'
            when 'Ear wax' then 'UBERON:ear'
            when 'Nasal mucus' then 'UBERON:nose'
            when 'Vaginal mucus' then 'UBERON:vagina'
            when 'Please select...' then 'unknown'
            else akb.site_sampled
        end as body_habitat,
        case akb.site_sampled
            when 'Stool' then 'UBERON:feces'
            when 'Mouth' then 'UBERON:tongue'
            when 'Right hand' then 'UBERON:hand'
            when 'Left hand' then 'UBERON:hand'
            when 'Forehead' then 'UBERON:skin'
            when 'Nares' then 'UBERON:nostril'
            when 'Hair' then 'UBERON:hair follicle'
            when 'Tears' then 'UBERON:secretion'
            when 'Ear wax' then 'UBERON:ear canal'
            when 'Nasal mucus' then 'UBERON:nostril'
            when 'Vaginal mucus' then 'UBERON:mucosa of vagina'
            when 'Please select...' then 'unknown'
            else akb.site_sampled
        end as body_site,
        case akb.site_sampled
            when 'Stool' then 'UBERON:feces'
            when 'Mouth' then 'UBERON:saliva'
            when 'Right hand' then 'UBERON:sebum'
            when 'Left hand' then 'UBERON:sebum'
            when 'Forehead' then 'UBERON:sebum'
            when 'Nares' then 'UBERON:mucus'
            when 'Hair' then 'UBERON:sebum'
            when 'Tears' then 'UBERON:tear'
            when 'Ear wax' then 'UBERON:cerumen'
            when 'Nasal mucus' then 'UBERON:mucus'
            when 'Vaginal mucus' then 'UBERON:mucus'
            when 'Please select...' then 'unknown'
            else akb.site_sampled
        end as body_product,
        case akb.site_sampled
            when 'Stool' then 'ENVO:urban biome'
            when 'Mouth' then 'ENVO:urban biome'
            when 'Right hand' then 'ENVO:urban biome'
            when 'Left hand' then 'ENVO:urban biome'
            when 'Forehead' then 'ENVO:urban biome'
            when 'Nares' then 'ENVO:urban biome'
            when 'Hair' then 'ENVO:urban biome'
            when 'Tears' then 'ENVO:urban biome'
            when 'Ear wax' then 'ENVO:urban biome'
            when 'Nasal mucus' then 'ENVO:urban biome'
            when 'Vaginal mucus' then 'ENVO:urban biome'
            when 'Please select...' then 'unknown'
            else akb.site_sampled
        end as env_biome,
        case akb.site_sampled
            when 'Stool' then 'ENVO:human-associated habitat'
            when 'Mouth' then 'ENVO:human-associated habitat'
            when 'Right hand' then 'ENVO:human-associated habitat'
            when 'Left hand' then 'ENVO:human-associated habitat'
            when 'Forehead' then 'ENVO:human-associated habitat'
            when 'Nares' then 'ENVO:human-associated habitat'
            when 'Hair' then 'ENVO:human-associated habitat'
            when 'Tears' then 'ENVO:human-associated habitat'
            when 'Ear wax' then 'ENVO:human-associated habitat'
            when 'Nasal mucus' then 'ENVO:human-associated habitat'
            when 'Vaginal mucus' then 'ENVO:human-associated habitat'
            when 'Please select...' then 'unknown'
            else akb.site_sampled
        end as env_feature,
        case akb.site_sampled
            when 'Stool' then 'ENVO:feces'
            when 'Mouth' then 'ENVO:saliva'
            when 'Right hand' then 'ENVO:sebum'
            when 'Left hand' then 'ENVO:sebum'
            when 'Forehead' then 'ENVO:sebum'
            when 'Nares' then 'ENVO:mucus'
            when 'Hair' then 'ENVO:sebum'
            when 'Tears' then 'ENVO:tears'
            when 'Ear wax' then 'ENVO:cerumen'
            when 'Nasal mucus' then 'ENVO:mucus'
            when 'Vaginal mucus' then 'ENVO:mucus'
            when 'Please select...' then 'unknown'
            else akb.site_sampled
        end as env_matter,
        case
            when coalesce(city::text, '') = '' then 'unknown'
            else lower(city)
        end as city,
        case
            when coalesce(state::text, '') = '' then 'unknown'
            else upper(state)
        end as state,
        case
            when coalesce(zip::text, '') = '' then 'unknown'
            when zip ~ '^\d*$' and length(zip) < 5 then lpad(zip, 5, '0')
            else zip
        end as zip,
        case
        lower(country) is null then 'unknown'
            when lower(country) = 'united states' then
                'GAZ:United States of America'
            when lower(country) = 'united states of america' then
                'GAZ:United States of America'
            when lower(country) = 'us' then 'GAZ:United States of America'
            when lower(country) = 'usa' then 'GAZ:United States of America'
            when lower(country) = 'u.s.a' then 'GAZ:United States of America'
            when lower(country) = 'u.s.' then 'GAZ:United States of America'
            when lower(country) = 'canada' then 'GAZ:Canada'
            when lower(country) = 'canadian' then 'GAZ:Canada'
            when lower(country) = 'ca' then 'GAZ:Canada'
            when lower(country) = 'australia' then 'GAZ:Australia'
            when lower(country) = 'au' then 'GAZ:Australia'
            when lower(country) = 'united kingdom' then 'GAZ:United Kingdom'
            when lower(country) = 'belgium' then 'GAZ:Belgium'
            when lower(country) = 'gb' then 'GAZ:Great Britain'
            when lower(country) = 'korea, republic of' then 'GAZ:South Korea'
            when lower(country) = 'nl' then 'GAZ:Netherlands'
            when lower(country) = 'netherlands' then 'GAZ:Netherlands'
            when lower(country) = 'spain' then 'GAZ:Spain'
            when lower(country) = 'es' then 'GAZ:Spain'
            when lower(country) = 'norway' then 'GAZ:Norway'
            when lower(country) = 'germany' then 'GAZ:Germany'
            when lower(country) = 'de' then 'GAZ:Germany'
            when lower(country) = 'china' then 'GAZ:China'
            when lower(country) = 'singapore' then 'GAZ:Singapore'
            when lower(country) = 'new zealand' then 'GAZ:New Zealand'
            when lower(country) = 'france' then 'GAZ:France'
            when lower(country) = 'fr' then 'GAZ:France'
            when lower(country) = 'ch' then 'GAZ:Switzerland'
            when lower(country) = 'switzerland' then 'GAZ:Switzerland'
            when lower(country) = 'denmark' then 'GAZ:Denmark'
            when lower(country) = 'scotland' then 'GAZ:Scotland'
            when lower(country) = 'united arab emirates' then
                'GAZ:United Arab Emirates'
            when lower(country) = 'ireland' then 'GAZ:Ireland'
            when lower(country) = 'thailand' then 'GAZ:Thailand'
            else 'unknown'
        end as country,
        case
            when coalesce(al.latitude::text, '') = '' then 'unknown'
            else cast(al.latitude as varchar(100))
        end as latitude,
        case
            when coalesce(al.longitude::text, '') = '' then 'unknown'
            else cast(al.longitude as varchar(100))
        end as longitude,
        case
            when coalesce(al.elevation::text, '') = '' then 'unknown'
            else cast(al.elevation as varchar(100))
        end as elevation,
        'years' as age_unit,
        akb.survey_id
        from    ag_login al
        inner join ag_kit ak
        on al.ag_login_id = ak.ag_login_id
        inner join ag_kit_barcodes akb
        on ak.ag_kit_id = akb.ag_kit_id
        where
        (akb.site_sampled IS NOT NULL AND akb.site_sampled::text <> '')
        akb.site_sampled != 'Please Select...'
        (akb.sample_date IS NOT NULL AND akb.sample_date::text <> '')
        akb.barcode = %s;
    """
    cursor = self.get_cursor()
    cursor.execute(sql, [barcode])
    col_names = [x[0] for x in cursor.description]
    results = [dict(zip(col_names, row)) for row in cursor.fetchall()]
    cursor.close()
    survey_id = results[0]['survey_id']
    sql = """select survey_question_id as sqi, response from survey_answers
             as sa
             where survey_id = %s"""
    cursor = self.get_cursor()
    cursor.execute(sql, [survey_id])
    col_names = [x[0] for x in cursor.description]
    results2 = [dict(zip(col_names, row)) for row in cursor.fetchall()]
    returnable = {}
    for row in results2:
        if row['sqi'] == 1:
            returnable['DIET_TYPE'] = row['sa']
        elif row['sqi'] == 2:
            returnable['MULTIVITAMIN'] = row['sa']
        elif row['sqi'] == 7:
            returnable['LACTOSE'] = row['sa']
        elif row['sqi'] == 8:
            returnable['GLUTEN'] = row['sa']
        elif row['sqi'] == 13:
            returnable['DRINKING_WATER_SOURCE'] = row['sa']
        elif row['sqi'] == 15:
            returnable['CURRENT_RESIDENCE_DURATION'] = row['sa']   
        elif row['sqi'] == 20:
            returnable['DOG'] = row['sa']
        elif row['sqi'] == 21:
            returnable['CAT'] = row['sa']
        elif row['sqi'] == 22:
            returnable['dominant_hand'] = row['sa']
        elif row['sqi'] == 24:
            returnable['EXERCISE_FREQUENCY'] = row['sa']
        elif row['sqi'] == 25:
            returnable['EXERCISE_LOCATION'] = row['sa']
        elif row['sqi'] == 26:
            returnable['NAILS'] = row['sa']
        elif row['sqi'] == 27:
            returnable['POOL_FREQUENCY'] = row['sa']
        elif row['sqi'] == 29:
            returnable['ALCOHOL_FREQUENCY'] = row['sa']
        elif row['sqi'] == 32:
            returnable['FLOSSING_FREQUENCY'] = row['sa']
        elif row['sqi'] == 33:
            returnable['COSMETICS_FREQUENCY'] = row['sa']
        elif row['sqi'] == 34:
            returnable['DEODORANT_USE'] = row['sa']
        elif row['sqi'] == 40:
            returnable['FLU_VACCINE_DATE'] = row['sa']
        elif row['sqi'] == 41:
            returnable['contraceptive'] = row['sa']
        elif row['sqi'] == 42:
            returnable['PREGNANT'] = row['sa']
        elif row['sqi'] == 45:
            returnable['APPENDIX_REMOVED'] = row['sa']
        elif row['sqi'] == 46:
            returnable['CHICKENPOX'] = row['sa']
        elif row['sqi'] == 47:
            returnable['ACNE_MEDICATION'] = row['sa']
        elif row['sqi'] == 48:
            returnable['ACNE_MEDICATION_OTC'] = row['sa']
        elif row['sqi'] == 50:
            returnable['CSECTION'] = row['sa']
        elif row['sqi'] == 82:
            returnable['DIABETES'] = row['sa']
        elif row['sqi'] == 92:
            returnable['MIGRAINE'] = row['sa']
        elif row['sqi'] == 98:
            returnable['PREGNANT_DUE_DATE'] = row['sa']
        elif row['sqi'] == 111:
            returnable['birth_month'] = row['sa']
        elif row['sqi'] == 112:
            returnable['birth_year'] = row['sa']

 
####
# after all the fields are in returnable dictonary create birth date by combining
# birth month and birth year
# merge returnable and resutls to get the complete metadata dictionary. 


#these are the fields form the old metadata pulldown
        case 
            when coalesce(ANTIBIOTIC_CONDITION::text, '') = '' then 'unknown'
            else REPLACE(REPLACE(REPLACE(ANTIBIOTIC_CONDITION, CHR(10), ''), CHR(13), ''), CHR(9), '')
        end as ANTIBIOTIC_CONDITION, 
        case 
            when coalesce(ANTIBIOTIC_SELECT::text, '') = '' then 'unknown'
            else REPLACE(REPLACE(REPLACE(ANTIBIOTIC_SELECT, CHR(10), ''), CHR(13), ''), CHR(9), '')
        end as ANTIBIOTIC_SELECT, 
      
        case 
            when coalesce(BIRTH_DATE::text, '') = '' then 'unknown'
            else regexp_replace(replace(replace(replace(birth_date, CHR(10), ''), CHR(13), ''), CHR(9), ''), '([[:digit:]]{2})/([[:digit:]]{2})/([[:digit:]]{4})', E'\\1/\\3')
        end as BIRTH_DATE,  
        case 
            when coalesce(COMMUNAL_DINING::text, '') = '' then 'unknown'
            when REPLACE(REPLACE(REPLACE(COMMUNAL_DINING, CHR(10), ''), CHR(13), ''), CHR(9), '') = 'on' then 'yes'
            else REPLACE(REPLACE(REPLACE(COMMUNAL_DINING, CHR(10), ''), CHR(13), ''), CHR(9), '')
        end as COMMUNAL_DINING, 
        case 
            when coalesce(CONDITIONS_MEDICATION::text, '') = '' then 'unknown'
            else lower(REPLACE(REPLACE(REPLACE(CONDITIONS_MEDICATION, CHR(10), ''), CHR(13), ''), CHR(9), ''))
        end as CONDITIONS_MEDICATION, 
        

        case
            when 
            (
                SELECT  term
                from    controlled_vocab_values
                where   vocab_value_id = cast(ahs.COUNTRY_OF_BIRTH as bigint)
            ) is null then 'unknown'
            else
            (
                SELECT  term
                from    controlled_vocab_values
                where   vocab_value_id = cast(ahs.COUNTRY_OF_BIRTH as bigint)
            )
        end as COUNTRY_OF_BIRTH,
        case
            when coalesce(DECEASED_PARENT::text, '') = '' then 'unknown'
            else REPLACE(REPLACE(REPLACE(DECEASED_PARENT, CHR(10), ''), CHR(13), ''), CHR(9), '') 
        end as DECEASED_PARENT, 
        case
            when coalesce(DIABETES_DIAGNOSE_DATE::text, '') = '' then 'unknown'
            else REPLACE(REPLACE(REPLACE(DIABETES_DIAGNOSE_DATE, CHR(10), ''), CHR(13), ''), CHR(9), '') 
        end as DIABETES_DIAGNOSE_DATE, 
        case
            when coalesce(DIABETES_MEDICATION::text, '') = '' then 'unknown'
            when REPLACE(REPLACE(REPLACE(DIABETES_MEDICATION, CHR(10), ''), CHR(13), ''), CHR(9), '') = 'on' then 'yes'
            else REPLACE(REPLACE(REPLACE(DIABETES_MEDICATION, CHR(10), ''), CHR(13), ''), CHR(9), '')
        end as DIABETES_MEDICATION,    
        case 
            when coalesce(FIBER_GRAMS::text, '') = '' then 'unknown'
            when cast(REPLACE(REPLACE(REPLACE(FIBER_GRAMS, CHR(10), ''), CHR(13), ''), CHR(9), '') as double precision) between 1 and 1000 then
                cast(REPLACE(REPLACE(REPLACE(FIBER_GRAMS, CHR(10), ''), CHR(13), ''), CHR(9), '') as varchar(100))
            else 'unknown'
        end as FIBER_GRAMS,
        case 
            when coalesce(FOODALLERGIES_OTHER::text, '') = '' then 'unknown'
            when FOODALLERGIES_OTHER = 'on' then 'yes'
            else FOODALLERGIES_OTHER
        end as FOODALLERGIES_OTHER, 
        case
            when coalesce(FOODALLERGIES_OTHER_TEXT::text, '') = '' then 'unknown'
            else REPLACE(REPLACE(REPLACE(FOODALLERGIES_OTHER_TEXT, CHR(10), ''), CHR(13), ''), CHR(9), '') 
        end as FOODALLERGIES_OTHER_TEXT, 
        case
            when coalesce(FOODALLERGIES_PEANUTS::text, '') = '' then 'unknown'
            when FOODALLERGIES_PEANUTS = 'on' then 'yes'
            else FOODALLERGIES_PEANUTS
        end as FOODALLERGIES_PEANUTS,
        case
            when coalesce(FOODALLERGIES_SHELLFISH::text, '') = '' then 'unknown'
            when FOODALLERGIES_SHELLFISH = 'on' then 'yes'
            else FOODALLERGIES_SHELLFISH
        end as FOODALLERGIES_SHELLFISH, 
        case
            when coalesce(FOODALLERGIES_TREENUTS::text, '') = '' then 'unknown'
            when FOODALLERGIES_TREENUTS = 'on' then 'yes'
            else FOODALLERGIES_TREENUTS
        end as FOODALLERGIES_TREENUTS, 
        case
            when coalesce(FRAT::text, '') = '' then 'unknown'
            when FRAT = 'on' then 'yes'
            else FRAT
        end as FRAT, 
        case
            when coalesce(GENDER::text, '') = '' then 'unknown'
            else lower(REPLACE(REPLACE(REPLACE(GENDER, CHR(10), ''), CHR(13), ''), CHR(9), ''))
        end as sex,
        case
            when coalesce(HEIGHT_IN::text, '') = '' then 'unknown'
            when cast(REPLACE(REPLACE(REPLACE(HEIGHT_IN, CHR(10), ''), CHR(13), ''), CHR(9), '') as double precision) between 10 and 106 then
                cast(cast(REPLACE(REPLACE(REPLACE(HEIGHT_IN, CHR(10), ''), CHR(13), ''), CHR(9), '') as double precision) as varchar(100))
            else 'unknown'
        end as HEIGHT_IN,
        case
            when coalesce(HEIGHT_CM::text, '') = '' then 'unknown'
            when cast(REPLACE(REPLACE(REPLACE(HEIGHT_CM, CHR(10), ''), CHR(13), ''), CHR(9), '') as double precision) between 25 and 270 then
                cast(cast(REPLACE(REPLACE(REPLACE(HEIGHT_CM, CHR(10), ''), CHR(13), ''), CHR(9), '') as double precision) as varchar(100))
            else 'unknown'
        end as height_or_length,
        case
            when coalesce(IBD::text, '') = '' then 'unknown'
            else REPLACE(REPLACE(REPLACE(IBD, CHR(10), ''), CHR(13), ''), CHR(9), '') 
        end as IBD,
        case
            when coalesce(LAST_TRAVEL::text, '') = '' then 'unknown'
            else REPLACE(REPLACE(REPLACE(LAST_TRAVEL, CHR(10), ''), CHR(13), ''), CHR(9), '') 
        end as LAST_TRAVEL, 
        case
            when coalesce(LIVINGWITH::text, '') = '' then 'unknown'
            else REPLACE(REPLACE(REPLACE(LIVINGWITH, CHR(10), ''), CHR(13), ''), CHR(9), '') 
        end as LIVINGWITH, 
        case
            when coalesce(MAINFACTOR_OTHER_1::text, '') = '' then 'unknown'
            else REPLACE(REPLACE(REPLACE(MAINFACTOR_OTHER_1, CHR(10), ''), CHR(13), ''), CHR(9), '') 
        end as MAINFACTOR_OTHER_1, 
        case
            when coalesce(MAINFACTOR_OTHER_2::text, '') = '' then 'unknown'
            else REPLACE(REPLACE(REPLACE(MAINFACTOR_OTHER_2, CHR(10), ''), CHR(13), ''), CHR(9), '') 
        end as MAINFACTOR_OTHER_2, 
        case
            when coalesce(MAINFACTOR_OTHER_3::text, '') = '' then 'unknown'
            else REPLACE(REPLACE(REPLACE(MAINFACTOR_OTHER_3, CHR(10), ''), CHR(13), ''), CHR(9), '') 
        end as MAINFACTOR_OTHER_3,
        case
            when coalesce(MIGRAINEMEDS::text, '') = '' then 'unknown'
            when MIGRAINEMEDS = 'on' then 'yes'
            else MIGRAINEMEDS
        end as MIGRAINEMEDS, 
        case
            when coalesce(MIGRAINE_AGGRAVATION::text, '') = '' then 'unknown'
            when MIGRAINE_AGGRAVATION = 'on' then 'yes'
            else MIGRAINE_AGGRAVATION
        end as MIGRAINE_AGGRAVATION, 
        case 
            when coalesce(MIGRAINE_AURA::text, '') = '' then 'unknown'
            when MIGRAINE_AURA = 'on' then 'yes'
            else MIGRAINE_AURA
        end as MIGRAINE_AURA, 
        case
            when coalesce(MIGRAINE_FACTOR_1::text, '') = '' then 'unknown'
            else REPLACE(REPLACE(REPLACE(MIGRAINE_FACTOR_1, CHR(10), ''), CHR(13), ''), CHR(9), '') 
        end as MIGRAINE_FACTOR_1, 
        case
            when coalesce(MIGRAINE_FACTOR_2::text, '') = '' then 'unknown'
            else REPLACE(REPLACE(REPLACE(MIGRAINE_FACTOR_2, CHR(10), ''), CHR(13), ''), CHR(9), '') 
        end as MIGRAINE_FACTOR_2, 
        case
            when coalesce(MIGRAINE_FACTOR_3::text, '') = '' then 'unknown'
            else REPLACE(REPLACE(REPLACE(MIGRAINE_FACTOR_3, CHR(10), ''), CHR(13), ''), CHR(9), '') 
        end as MIGRAINE_FACTOR_3, 
        case
            when coalesce(MIGRAINE_FREQUENCY::text, '') = '' then 'unknown'
            else REPLACE(REPLACE(REPLACE(MIGRAINE_FREQUENCY, CHR(10), ''), CHR(13), ''), CHR(9), '') 
        end as MIGRAINE_FREQUENCY, 
        case
            when coalesce(MIGRAINE_NAUSEA::text, '') = '' then 'unknown'
            when MIGRAINE_NAUSEA = 'on' then 'yes'
            else MIGRAINE_NAUSEA
        end as MIGRAINE_NAUSEA, 
        case 
            when coalesce(MIGRAINE_PAIN::text, '') = '' then 'unknown'
            when MIGRAINE_PAIN = 'on' then 'yes'
            else MIGRAINE_PAIN
        end as MIGRAINE_PAIN, 
        case
            when coalesce(MIGRAINE_PHONOPHOBIA::text, '') = '' then 'unknown'
            when MIGRAINE_PHONOPHOBIA = 'on' then 'yes'
            else MIGRAINE_PHONOPHOBIA
        end as MIGRAINE_PHONOPHOBIA, 
        case
            when coalesce(MIGRAINE_PHOTOPHOBIA::text, '') = '' then 'unknown'
            when MIGRAINE_PHOTOPHOBIA = 'on' then 'yes'
            else MIGRAINE_PHOTOPHOBIA
        end as MIGRAINE_PHOTOPHOBIA, 
        case
            when coalesce(MIGRAINE_RELATIVES::text, '') = '' then 'unknown'
            when MIGRAINE_RELATIVES = 'on' then 'yes'
            else MIGRAINE_RELATIVES
        end as MIGRAINE_RELATIVES,
####stopped here 
        case
            when coalesce(NAILS::text, '') = '' then 'unknown'
            else lower(NAILS)
        end as NAILS, 
        case
            when coalesce(NONFOODALLERGIES_BEESTINGS::text, '') = '' then 'unknown'
            when NONFOODALLERGIES_BEESTINGS = 'on' then 'yes'
            else NONFOODALLERGIES_BEESTINGS
        end as NONFOODALLERGIES_BEESTINGS, 
        case
            when coalesce(NONFOODALLERGIES_DANDER::text, '') = '' then 'unknown'
            when NONFOODALLERGIES_DANDER = 'on' then 'yes'
            else NONFOODALLERGIES_DANDER
        end as NONFOODALLERGIES_DANDER, 
        case
            when coalesce(NONFOODALLERGIES_DRUG::text, '') = '' then 'unknown'
            when NONFOODALLERGIES_DRUG = 'on' then 'yes'
            else NONFOODALLERGIES_DRUG
        end as NONFOODALLERGIES_DRUG, 
        case
            when coalesce(NONFOODALLERGIES_NO::text, '') = '' then 'unknown'
            when NONFOODALLERGIES_NO = 'on' then 'yes'
            else NONFOODALLERGIES_NO
        end as NONFOODALLERGIES_NO, 
        case
            when coalesce(NONFOODALLERGIES_POISONIVY::text, '') = '' then 'unknown'
            when NONFOODALLERGIES_POISONIVY = 'on' then 'yes'
            else NONFOODALLERGIES_POISONIVY
        end as NONFOODALLERGIES_POISONIVY, 
        case
            when coalesce(NONFOODALLERGIES_SUN::text, '') = '' then 'unknown'
            when NONFOODALLERGIES_SUN = 'on' then 'yes'
            else NONFOODALLERGIES_SUN
        end as NONFOODALLERGIES_SUN, 
        case
            when coalesce(PERCENTAGE_FROM_CARBS::text, '') = '' then 'unknown'
            else REPLACE(REPLACE(REPLACE(PERCENTAGE_FROM_CARBS, CHR(10), ''), CHR(13), ''), CHR(9), '') 
        end as PERCENTAGE_FROM_CARBS, 
        case
            when coalesce(PKU::text, '') = '' then 'unknown'
            else lower(REPLACE(REPLACE(REPLACE(PKU, CHR(10), ''), CHR(13), ''), CHR(9), '')) 
        end as PKU, 
        case
            when coalesce(PRIMARY_CARB::text, '') = '' then 'unknown'
            else REPLACE(REPLACE(REPLACE(PRIMARY_CARB, CHR(10), ''), CHR(13), ''), CHR(9), '') 
        end as PRIMARY_CARB, 
        case
            when coalesce(PRIMARY_VEGETABLE::text, '') = '' then 'unknown'
            else REPLACE(REPLACE(REPLACE(PRIMARY_VEGETABLE, CHR(10), ''), CHR(13), ''), CHR(9), '') 
        end as PRIMARY_VEGETABLE, 
        case
            when coalesce(RACE::text, '') = '' then 'unknown'
            else REPLACE(REPLACE(REPLACE(RACE, CHR(10), ''), CHR(13), ''), CHR(9), '') 
        end as RACE, 
        case
            when coalesce(RACE_OTHER::text, '') = '' then 'unknown'
            else REPLACE(REPLACE(REPLACE(RACE_OTHER, CHR(10), ''), CHR(13), ''), CHR(9), '') 
        end as RACE_OTHER, 
        case
            when coalesce(ROOMMATES::text, '') = '' then 'unknown'
            else REPLACE(REPLACE(REPLACE(ROOMMATES, CHR(10), ''), CHR(13), ''), CHR(9), '') 
        end as ROOMMATES, 
        case
            when coalesce(SEASONAL_ALLERGIES::text, '') = '' then 'unknown'
            else lower(REPLACE(REPLACE(REPLACE(SEASONAL_ALLERGIES, CHR(10), ''), CHR(13), ''), CHR(9), '')) 
        end as SEASONAL_ALLERGIES, 
        case
            when coalesce(SHARED_HOUSING::text, '') = '' then 'unknown'
            else lower(REPLACE(REPLACE(REPLACE(SHARED_HOUSING, CHR(10), ''), CHR(13), ''), CHR(9), '')) 
        end as SHARED_HOUSING, 
        case
            when coalesce(SKIN_CONDITION::text, '') = '' then 'unknown'
            else REPLACE(REPLACE(REPLACE(SKIN_CONDITION, CHR(10), ''), CHR(13), ''), CHR(9), '') 
        end as SKIN_CONDITION, 
        case 
            when coalesce(SLEEP_DURATION::text, '') = '' then 'unknown'
            else REPLACE(REPLACE(REPLACE(SLEEP_DURATION, CHR(10), ''), CHR(13), ''), CHR(9), '') 
        end as SLEEP_DURATION, 
        case
            when coalesce(SMOKING_FREQUENCY::text, '') = '' then 'unknown'
            else REPLACE(REPLACE(REPLACE(SMOKING_FREQUENCY, CHR(10), ''), CHR(13), ''), CHR(9), '') 
        end as SMOKING_FREQUENCY, 
        case
            when coalesce(SOFTENER::text, '') = '' then 'unknown'
            else lower(REPLACE(REPLACE(REPLACE(SOFTENER, CHR(10), ''), CHR(13), ''), CHR(9), '')) 
        end as SOFTENER, 
        case
            when coalesce(SPECIAL_RESTRICTIONS::text, '') = '' then 'unknown'
            else lower(REPLACE(REPLACE(REPLACE(SPECIAL_RESTRICTIONS, CHR(10), ''), CHR(13), ''), CHR(9), '')) 
        end as SPECIAL_RESTRICTIONS, 
        case
            when coalesce(SUPPLEMENTS::text, '') = '' then 'unknown'
            else lower(REPLACE(REPLACE(REPLACE(SUPPLEMENTS, CHR(10), ''), CHR(13), ''), CHR(9), '')) 
        end as SUPPLEMENTS, 
        case
            when coalesce(TANNING_BEDS::text, '') = '' then 'unknown'
            else REPLACE(REPLACE(REPLACE(TANNING_BEDS, CHR(10), ''), CHR(13), ''), CHR(9), '') 
        end as TANNING_BEDS, 
        case
            when coalesce(TANNING_SPRAYS::text, '') = '' then 'unknown'
            else REPLACE(REPLACE(REPLACE(TANNING_SPRAYS, CHR(10), ''), CHR(13), ''), CHR(9), '') 
        end as TANNING_SPRAYS, 
        case
            when coalesce(TEETHBRUSHING_FREQUENCY::text, '') = '' then 'unknown'
            else REPLACE(REPLACE(REPLACE(TEETHBRUSHING_FREQUENCY, CHR(10), ''), CHR(13), ''), CHR(9), '') 
        end as TEETHBRUSHING_FREQUENCY, 
        case
            when coalesce(TONSILS_REMOVED::text, '') = '' then 'unknown'
            else lower(REPLACE(REPLACE(REPLACE(TONSILS_REMOVED, CHR(10), ''), CHR(13), ''), CHR(9), '')) 
        end as TONSILS_REMOVED, 
        case
            when coalesce(TYPES_OF_PLANTS::text, '') = '' then 'unknown'
            else REPLACE(REPLACE(REPLACE(TYPES_OF_PLANTS, CHR(10), ''), CHR(13), ''), CHR(9), '') 
        end as TYPES_OF_PLANTS, 
        case
            when coalesce(WEIGHT_CHANGE::text, '') = '' then 'unknown'
            else REPLACE(REPLACE(REPLACE(WEIGHT_CHANGE, CHR(10), ''), CHR(13), ''), CHR(9), '') 
        end as WEIGHT_CHANGE, 
        case
            when coalesce(WEIGHT_KG::text, '') = '' then 'unknown'
            when cast(REPLACE(REPLACE(REPLACE(WEIGHT_KG, CHR(10), ''), CHR(13), ''), CHR(9), '') as double precision) between 1 and 227 then
                cast(REPLACE(REPLACE(REPLACE(WEIGHT_KG, CHR(10), ''), CHR(13), ''), CHR(9), '') as varchar(100))
            else 'unknown'
        end as tot_mass,
        case
            when coalesce(WEIGHT_LBS::text, '') = '' then 'unknown'
            when cast(REPLACE(REPLACE(REPLACE(WEIGHT_LBS, CHR(10), ''), CHR(13), ''), CHR(9), '') as double precision) between 1 and 500 then
                cast(REPLACE(REPLACE(REPLACE(WEIGHT_LBS, CHR(10), ''), CHR(13), ''), CHR(9), '') as varchar(100))
            else 'unknown'
        end as WEIGHT_LBS,
        case
            when cast(weight_lbs as numeric) > 0 and cast(height_in as numeric) > 0 then
            case 
                when (cast(weight_lbs as numeric) / ((cast(height_in as numeric) * cast(height_in as numeric)))) * 703 between 5 and 100 
                    then cast((cast(weight_lbs as numeric) / ((cast(height_in as numeric) * cast(height_in as numeric)))) * 703 as varchar(100))
                else 'unknown'
            end
            else 'unknown'
        end as BMI,
        case
            when 
            (
                SELECT  string_agg(item_value, ',' order by item_name)
                from    ag_survey_multiples
                where   ag_login_id = al.ag_login_id
                        and participant_name = akb.participant_name
                        and item_name like 'antibiotic_med_%'
            ) is null then 'unknown'
            else 
            (
                SELECT  string_agg(item_value, ',' order by item_name)
                from    ag_survey_multiples
                where   ag_login_id = al.ag_login_id
                        and participant_name = akb.participant_name
                        and item_name like 'antibiotic_med_%'
            )
        end as antibiotic_meds,
        case
            when 
            (
                SELECT  string_agg(item_value, ',' order by item_name)
                from    ag_survey_multiples
                where   ag_login_id = al.ag_login_id
                        and participant_name = akb.participant_name
                        and item_name like 'diabetes_medications_%'
            ) is null then 'unknown'
            else
            (
                SELECT  string_agg(item_value, ',' order by item_name)
                from    ag_survey_multiples
                where   ag_login_id = al.ag_login_id
                        and participant_name = akb.participant_name
                        and item_name like 'diabetes_medications_%'
            )
        end as diabetes_medications,
        case
            when 
            (
                SELECT  string_agg(item_value, ',' order by item_name)
                from    ag_survey_multiples
                where   ag_login_id = al.ag_login_id
                        and participant_name = akb.participant_name
                        and item_name like 'dietrestrictions_%'
            ) is null then 'unknown'
            else
            (
                SELECT  string_agg(item_value, ',' order by item_name)
                from    ag_survey_multiples
                where   ag_login_id = al.ag_login_id
                        and participant_name = akb.participant_name
                        and item_name like 'dietrestrictions_%'
            )
        end as diet_restrictions,
        case
            when 
            (
                SELECT  string_agg(item_value, ',' order by item_name)
                from    ag_survey_multiples
                where   ag_login_id = al.ag_login_id
                        and participant_name = akb.participant_name
                        and item_name like 'general_meds_%'
            ) is null then 'unknown'
            else
            (
                SELECT  string_agg(item_value, ',' order by item_name)
                from    ag_survey_multiples
                where   ag_login_id = al.ag_login_id
                        and participant_name = akb.participant_name
                        and item_name like 'general_meds_%'
            )
        end as general_meds,
        case
            when 
            (
                SELECT  string_agg(item_value, ',' order by item_name)
                from    ag_survey_multiples
                where   ag_login_id = al.ag_login_id
                        and participant_name = akb.participant_name
                        and item_name like 'migraine_medication_%'
            ) is null then 'unknown'
            else
            (
                SELECT  string_agg(item_value, ',' order by item_name)
                from    ag_survey_multiples
                where   ag_login_id = al.ag_login_id
                        and participant_name = akb.participant_name
                        and item_name like 'migraine_medication_%'
            )
        end as migraine_medications,
        case
            when 
            (
                SELECT  string_agg(item_value, ',' order by item_name)
                from    ag_survey_multiples
                where   ag_login_id = al.ag_login_id
                        and participant_name = akb.participant_name
                        and item_name like 'pet_%'
            ) is null then 'unknown'
            else
            (
                SELECT  string_agg(item_value, ',' order by item_name)
                from    ag_survey_multiples
                where   ag_login_id = al.ag_login_id
                        and participant_name = akb.participant_name
                        and item_name like 'pet_%'
            )
        end as pets,
        case
            when
            (
                SELECT  string_agg(item_value, ',' order by item_name)
                from    ag_survey_multiples
                where   ag_login_id = al.ag_login_id
                        and participant_name = akb.participant_name
                        and item_name like 'pet_contact_%'
            ) is null then 'unknown'
            else
            (
                SELECT  string_agg(item_value, ',' order by item_name)
                from    ag_survey_multiples
                where   ag_login_id = al.ag_login_id
                        and participant_name = akb.participant_name
                        and item_name like 'pet_contact_%'
            )
        end as pet_contact,
        case
            when
            (
                SELECT  string_agg(item_value, ',' order by item_name)
                from    ag_survey_multiples
                where   ag_login_id = al.ag_login_id
                        and participant_name = akb.participant_name
                        and item_name like 'pet_location_%'
            ) is null then 'unknown'
            else
            (
                SELECT  string_agg(item_value, ',' order by item_name)
                from    ag_survey_multiples
                where   ag_login_id = al.ag_login_id
                        and participant_name = akb.participant_name
                        and item_name like 'pet_location_%'
            )
        end as pet_locations,
        case
            when 
            (
                SELECT  string_agg(item_value, ',' order by item_name)
                from    ag_survey_multiples
                where   ag_login_id = al.ag_login_id
                        and participant_name = akb.participant_name
                        and item_name like 'relation_%'
            ) is null then 'unknown'
            else
            (
                SELECT  string_agg(item_value, ',' order by item_name)
                from    ag_survey_multiples
                where   ag_login_id = al.ag_login_id
                        and participant_name = akb.participant_name
                        and item_name like 'relation_%'
            )
        end as relations,
        case
            when
            (
                SELECT  string_agg(item_value, ',' order by item_name)
                from    ag_survey_multiples
                where   ag_login_id = al.ag_login_id
                        and participant_name = akb.participant_name
                        and item_name like 'supplements_fields_%'
            ) is null then 'unknown'
            else
            (
                SELECT  string_agg(item_value, ',' order by item_name)
                from    ag_survey_multiples
                where   ag_login_id = al.ag_login_id
                        and participant_name = akb.participant_name
                        and item_name like 'supplements_fields_%'
            )
        end as supplements_fields,
        (
            cast(REPLACE(REPLACE(REPLACE(CARBOHYDRATE_PER, CHR(10), ''), CHR(13), ''), CHR(9), '') as integer) +
            cast(REPLACE(REPLACE(REPLACE(PROTEIN_PER, CHR(10), ''), CHR(13), ''), CHR(9), '') as integer) +
            cast(REPLACE(REPLACE(REPLACE(FAT_PER, CHR(10), ''), CHR(13), ''), CHR(9), '') as integer)
        ) as macronutrient_pct_total,
        
        
        
        case
            when 
            (
                SELECT  string_agg(item_value, ',' order by item_name)
                from    ag_survey_multiples
                where   ag_login_id = al.ag_login_id
                        and participant_name = akb.participant_name
                        and lower(item_name) like 'antibiotic_med_%'
                        and 
                        (
                            lower(item_value) like '%moxifloxacin%'
                            or lower(item_value) like '%avelox%'
                            or lower(item_value) like '%ciprofloxacin%'
                            or lower(item_value) like '%cipro%'
                        )
            ) is null then 'no'
            else 'yes'
        end as Quinoline,
        case
            when 
            (
                SELECT  string_agg(item_value, ',' order by item_name)
                from    ag_survey_multiples
                where   ag_login_id = al.ag_login_id
                        and participant_name = akb.participant_name
                        and lower(item_name) like 'antibiotic_med_%'
                        and 
                        (
                            lower(item_value) like '%metronidazole%'
                            or lower(item_value) like '%flagyl%'
                            or lower(item_value) like '%secnidazole%'
                            or lower(item_value) like '%tinidazole%'
                            or lower(item_value) like '%tindamax%'
                        )
            ) is null then 'no'
            else 'yes'
        end as Nitromidazole,
        case
            when 
            (
                SELECT  string_agg(item_value, ',' order by item_name)
                from    ag_survey_multiples
                where   ag_login_id = al.ag_login_id
                        and participant_name = akb.participant_name
                        and lower(item_name) like 'antibiotic_med_%'
                        and 
                        (
                            lower(item_value) like '%amoxicillin%'
                            or lower(item_value) like '%penicillin%'
                            or lower(item_value) like '%augmentin%'
                            or lower(item_value) like '%methicillin%'
                        )
            ) is null then 'no'
            else 'yes'
        end as Penicillin,
        case
            when 
            (
                SELECT  string_agg(item_value, ',' order by item_name)
                from    ag_survey_multiples
                where   ag_login_id = al.ag_login_id
                        and participant_name = akb.participant_name
                        and lower(item_name) like 'antibiotic_med_%'
                        and 
                        (
                            lower(item_value) like '%sulfamethoxazole%'
                            or lower(item_value) like '%bactrim%'
                            or lower(item_value) like '%septra%'
                        )
            ) is null then 'no'
            else 'yes'
        end as Sulfa_Drug,
        case
            when 
            (
                SELECT  string_agg(item_value, ',' order by item_name)
                from    ag_survey_multiples
                where   ag_login_id = al.ag_login_id
                        and participant_name = akb.participant_name
                        and lower(item_name) like 'antibiotic_med_%'
                        and 
                        (
                            lower(item_value) like '%cefuroxime axetil%'
                            or lower(item_value) like '%ceftin%'
                            or lower(item_value) like '%cefalexin%'
                            or lower(item_value) like '%keflex%'
                            or lower(item_value) like '%ceftriaxone%'
                            or lower(item_value) like '%recophin%'
                            or lower(item_value) like '%levofloxacin%'
                            or lower(item_value) like '%levaquin%'
                            or lower(item_value) like '%cefdinir%'
                            or lower(item_value) like '%omnicef%'
                            or lower(item_value) like '%cefotaxime%'
                        )
            ) is null then 'no'
            else 'yes'
        end as Cephalosporin






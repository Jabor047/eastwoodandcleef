SELECT
  person_id, provider_id,
  MIN(procedure_dat) OVER(PARTITION BY provider_id, person_id) AS firstVisit
FROM
  `bigquery-public-data.cms_synthetic_patient_data_omop.procedure_occurrence`
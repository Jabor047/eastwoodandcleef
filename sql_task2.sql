SELECT
  person_id,
  provider_id,
  DATE_DIFF(procedure_dat, LAG(procedure_dat) OVER(PARTITION BY person_id, provider_id ORDER BY procedure_dat), DAY) AS consecutive_visits
FROM
  `bigquery-public-data.cms_synthetic_patient_data_omop.procedure_occurrence`
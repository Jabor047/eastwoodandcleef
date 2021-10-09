SELECT
  provider_id,
  COUNT(visit_occurrence_id) AS number_of_visit
FROM
  `bigquery-public-data.cms_synthetic_patient_data_omop.procedure_occurrence`
GROUP BY
  person_id,
  provider_id
ORDER BY
  number_of_visit DESC
LIMIT
  3;
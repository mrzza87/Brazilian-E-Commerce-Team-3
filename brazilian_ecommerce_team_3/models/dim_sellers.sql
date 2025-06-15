SELECT
  seller_id,
  seller_zip_code_prefix,
  seller_city,
  seller_state
FROM {{ source('BET_Team3', 'sellers') }}

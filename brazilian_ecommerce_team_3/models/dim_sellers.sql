SELECT
  seller_id,
  seller_city,
  seller_state
FROM {{ source('BET_Team3', 'sellers') }}
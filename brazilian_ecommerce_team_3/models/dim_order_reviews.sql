SELECT
  *
FROM (
  SELECT *,
    ROW_NUMBER() OVER (PARTITION BY review_id ORDER BY review_creation_date DESC) as row_num
  FROM {{ source('BET_Team3', 'order_reviews') }}
)
WHERE row_num = 1

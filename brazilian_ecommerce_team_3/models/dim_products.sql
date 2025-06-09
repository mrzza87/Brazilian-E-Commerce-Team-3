-- models/dim_product.sql
SELECT
  product_id,
  product_category_name
FROM {{ source('BET_Team3', 'products_corrected') }}
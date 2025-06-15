SELECT
    product_id,
    product_category_name,
    product_name_length,
    product_description_length,
    product_photos_qty
FROM {{ source('BET_Team3', 'products_corrected') }}

SELECT
    customer_id,
    customer_unique_id,
    customer_zip_code_prefix,  -- ✅ add this line
    customer_city,
    customer_state
FROM {{ source('BET_Team3', 'customers') }}

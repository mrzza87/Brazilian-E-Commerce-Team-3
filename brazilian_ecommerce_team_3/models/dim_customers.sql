-- models/dim_customer.sql
SELECT
  customer_id,
  customer_unique_id,
  customer_city,
  customer_state
FROM {{ source('BET_Team3', 'customers') }}

-- This model selects the customer_id, customer_unique_id, customer_city, and customer_state
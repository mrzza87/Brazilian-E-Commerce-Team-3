SELECT
  order_id,
  payment_type,
  payment_installments
FROM {{ source('BET_Team3', 'order_payments') }}

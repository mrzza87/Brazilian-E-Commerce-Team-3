WITH order_items AS (
    SELECT * FROM {{ source('BET_Team3', 'order_items_corrected') }}
),

orders AS (
    SELECT * FROM {{ source('BET_Team3', 'orders_corrected') }}
),

products AS (
    SELECT * FROM {{ source('BET_Team3', 'products_corrected') }}
),

sellers AS (
    SELECT * FROM {{ source('BET_Team3', 'sellers') }}
),

payments AS (
    SELECT * FROM {{ source('BET_Team3', 'order_payments') }}
),

reviews AS (
    SELECT * FROM {{ source('BET_Team3', 'order_reviews') }}
),

joined_data AS (
    SELECT
        o.order_id,
        o.order_item_id,
        ord.customer_id,
        o.product_id,
        p.product_category_name,
        s.seller_id,
        s.seller_city,
        s.seller_state,
        ord.order_status,
        ord.order_purchase_timestamp,
        ord.order_approved_at,
        ord.order_delivered_carrier_date,
        ord.order_delivered_customer_date,
        ord.order_estimated_delivery_date,
        o.price,
        o.freight_value,
        pay.payment_type,
        pay.payment_value,
        pay.payment_sequential,
        r.review_score,
        ROW_NUMBER() OVER (
            PARTITION BY o.order_id, o.order_item_id
            ORDER BY ord.order_purchase_timestamp DESC
        ) AS row_num
    FROM order_items o
    JOIN orders         ord ON o.order_id = ord.order_id
    JOIN products       p   ON o.product_id = p.product_id
    JOIN sellers        s   ON o.seller_id = s.seller_id
    LEFT JOIN payments  pay ON pay.order_id = o.order_id
    LEFT JOIN reviews   r   ON r.order_id = o.order_id
)

SELECT *
FROM joined_data
WHERE row_num = 1


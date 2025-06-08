with order_items as (
    select * from {{ source('BET_Team3', 'order_items') }}
),

orders as (
    select * from {{ source('BET_Team3', 'orders') }}
),

products as (
    select * from {{ source('BET_Team3', 'products') }}
),

sellers as (
    select * from {{ source('BET_Team3', 'sellers') }}
),

payments as (
    select * from {{ source('BET_Team3', 'order_payments') }}
),

reviews as (
    select * from {{ source('BET_Team3', 'order_reviews') }}
),

final as (
    select
        o.order_id,
        oi.order_item_id,
        o.customer_id,
        oi.product_id,
        p.product_category_name,
        oi.seller_id,
        s.seller_city,
        s.seller_state,
        o.order_status,
        o.order_purchase_timestamp,
        o.order_approved_at,
        o.order_delivered_carrier_date,
        o.order_delivered_customer_date,
        o.order_estimated_delivery_date,
        oi.price,
        oi.freight_value,
        pay.payment_type,
        pay.payment_value,
        r.review_score
    from order_items oi
    join orders o on o.order_id = oi.order_id
    join products p on p.product_id = oi.product_id
    join sellers s on s.seller_id = oi.seller_id
    left join payments pay on pay.order_id = o.order_id
    left join reviews r on r.order_id = o.order_id
)

select * from final

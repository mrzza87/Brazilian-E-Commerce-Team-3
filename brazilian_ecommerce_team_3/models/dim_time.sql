with times as (

    -- Generate distinct timestamp columns from orders
    select distinct
        order_purchase_timestamp as time
    from {{ source('BET_Team3', 'orders') }}

    union distinct

    select distinct
        order_approved_at as time
    from {{ source('BET_Team3', 'orders') }}

    union distinct

    select distinct
        order_delivered_carrier_date as time
    from {{ source('BET_Team3', 'orders') }}

    union distinct

    select distinct
        order_delivered_customer_date as time
    from {{ source('BET_Team3', 'orders') }}

    union distinct

    select distinct
        order_estimated_delivery_date as time
    from {{ source('BET_Team3', 'orders') }}

),

final as (
    select
        time as time_id,
        extract(hour from time) as hour,
        extract(minute from time) as minute,
        format_time('%H:%M', time) as time_hhmm
    from times
    where time is not null
)

select * from final


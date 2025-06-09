with times as (
    select distinct cast(order_purchase_timestamp as timestamp) as time
    from {{ source('BET_Team3', 'orders') }}
    union distinct
    select distinct cast(order_approved_at as timestamp) as time
    from {{ source('BET_Team3', 'orders') }}
    union distinct
    select distinct cast(order_delivered_carrier_date as timestamp) as time
    from {{ source('BET_Team3', 'orders') }}
    union distinct
    select distinct cast(order_delivered_customer_date as timestamp) as time
    from {{ source('BET_Team3', 'orders') }}
    union distinct
    select distinct cast(order_estimated_delivery_date as timestamp) as time
    from {{ source('BET_Team3', 'orders') }}
),
final as (
    select
        time as time_id,
        extract(hour from time) as hour,
        extract(minute from time) as minute,
        format_time('%H:%M', cast(time as TIME)) as time_hhmm
    from times
    where time is not null
)
select * from final



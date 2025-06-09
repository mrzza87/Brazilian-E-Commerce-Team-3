with raw_dates as (
    select distinct
        date(order_purchase_timestamp) as date_id
    from {{ source('BET_Team3', 'orders_corrected') }}
),

final as (
    select
        date_id,
        extract(year from date_id) as year,
        extract(month from date_id) as month,
        extract(day from date_id) as day,
        format_date('%A', date_id) as day_name,
        format_date('%B', date_id) as month_name
    from raw_dates
)

select * from final

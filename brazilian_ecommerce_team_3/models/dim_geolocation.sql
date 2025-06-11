with raw_geo as (
  select distinct
    geolocation_zip_code_prefix,
    geolocation_lat,
    geolocation_lng,
    geolocation_city,
    geolocation_state
  from {{ source('BET_Team3', 'geolocation_version1') }}
)

select * from raw_geo

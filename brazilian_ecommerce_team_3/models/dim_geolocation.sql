-- models/dim_geolocation.sql

WITH raw_geo AS (
  SELECT DISTINCT
    geolocation_zip_code_prefix,
    geolocation_lat,
    geolocation_lng,
    LOWER(TRIM(geolocation_city)) AS geolocation_city,
    UPPER(TRIM(geolocation_state)) AS geolocation_state
  FROM {{ source('BET_Team3', 'geolocation_version1') }}
),

with_surrogate AS (
  SELECT
    ROW_NUMBER() OVER () AS surrogate_key,
    *
  FROM raw_geo
)

SELECT * FROM with_surrogate


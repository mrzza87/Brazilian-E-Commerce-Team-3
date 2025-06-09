-- models/dim_order_reviews.sql

WITH base AS (
    SELECT
        review_id,
        order_id,
        CONCAT(order_id, '_', review_id) AS order_id_review_id,
        review_score,
        review_comment_title,
        review_comment_message,
        review_creation_date,
        review_answer_timestamp
    FROM {{ source('BET_Team3', 'order_reviews') }}
)

SELECT *
FROM base

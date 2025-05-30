# 📖 Data Dictionary - Brazilian E-Commerce (Olist)

This document explains the tables and columns used in our e-commerce data warehouse.

---

## 🧍‍♀️ `customers`
- `customer_id`: Unique ID of a customer (used in orders)
- `customer_unique_id`: ID for the actual person (can appear multiple times)
- `customer_zip_code_prefix`: First 5 digits of the ZIP code
- `customer_city`: Customer’s city
- `customer_state`: State abbreviation (e.g. SP, RJ)

---

## 📦 `orders`
- `order_id`: Unique ID for each order
- `customer_id`: Links to customers table
- `order_status`: Status (delivered, shipped, canceled...)
- `order_purchase_timestamp`: Purchase date
- `order_approved_at`: Approval timestamp
- `order_delivered_carrier_date`: Sent to delivery
- `order_delivered_customer_date`: Delivered to customer
- `order_estimated_delivery_date`: Expected delivery

---

## 🛍 `order_items`
- `order_id`: Order ID
- `order_item_id`: Item sequence in the order
- `product_id`: Product sold
- `seller_id`: Seller of the item
- `shipping_limit_date`: Shipping deadline
- `price`: Item price
- `freight_value`: Shipping fee

---

## 💳 `order_payments`
- `order_id`: Order ID
- `payment_sequential`: Payment sequence (for split payments)
- `payment_type`: Method (credit card, boleto, etc.)
- `payment_installments`: Number of installments
- `payment_value`: Amount paid

---

## 📝 `order_reviews`
- `review_id`: Unique review ID
- `order_id`: Order reviewed
- `review_score`: Rating (1–5)
- `review_comment_title`: Title of the comment
- `review_comment_message`: Full review message
- `review_creation_date`: Date review was written
- `review_answer_timestamp`: When Olist responded

---

## 🎁 `products`
- `product_id`: Unique product ID
- `product_category_name`: Category in Portuguese
- `product_name_length`, `product_description_length`: Character counts
- `product_photos_qty`: Number of photos
- `product_weight_g`, `product_length_cm`, `product_height_cm`, `product_width_cm`: Dimensions

---

## 🧑‍💼 `sellers`
- `seller_id`: Unique ID of the seller
- `seller_zip_code_prefix`: First 5 digits of seller ZIP
- `seller_city`: Seller city
- `seller_state`: Seller state

---

## 🌍 `geolocation`
- `geolocation_zip_code_prefix`: First 5 digits of ZIP
- `geolocation_lat`, `geolocation_lng`: Latitude & longitude
- `geolocation_city`, `geolocation_state`: Region info

---

## 🌐 `product_category_name_translation`
- `product_category_name`: Category in Portuguese
- `product_category_name_english`: English translation

---

📝 Maintained by Team 3  
🚀 Generated after successful ingestion using `load_to_sql.py`

# 📖 Data Dictionary - Brazilian E-Commerce (Olist)

This document explains the tables and columns used in our e-commerce data warehouse.

---

## 🧍‍♀️ `customers`
- `customer_id`: Unique ID of a customer (used in orders)(GX: Not null, Unique)
- `customer_unique_id`: ID for the actual person (can appear multiple times)(GX: Not null)
- `customer_zip_code_prefix`: First 5 digits of the ZIP code(GX: 5-digits, "regex": "^\\d{5}$")
- `customer_city`: Customer’s city (GX: Exist)
- `customer_state`: State abbreviation (e.g. SP, RJ)(GX: Exist)

---

## 📦 `orders`
- `order_id`: Unique ID for each order (GX: Not null, Unique)
- `customer_id`: Links to customers table (GX: Not null)
- `order_status`: Status (delivered, shipped, canceled...)(GX: Must be one in set)
- `order_purchase_timestamp`: Purchase date (GX: Timestamp format)
- `order_approved_at`: Approval timestamp (GX: Timestamp  format)
- `order_delivered_carrier_date`: Sent to delivery (GX: Timestamp  format)
- `order_delivered_customer_date`: Delivered to customer (GX: Timestamp  format)
- `order_estimated_delivery_date`: Expected delivery (GX: Timestamp  format)

order_status
approved           2
canceled         625
created            5
delivered      96478
invoiced         314
processing       301
shipped         1107
unavailable      609

---

## 🛍 `order_items`
- `order_id`: Order ID (GX: Not null)
- `order_item_id`: Item sequence in the order (GX: Not null, 1-30; max: 21)
- `product_id`: Product sold (GX: Not null)
- `seller_id`: Seller of the item (GX: Not null)
- `shipping_limit_date`: Shipping deadline (GX: Timestamp  format)
- `price`: Item price (GX: 0-10000; max: 6735)
- `freight_value`: Shipping fee (GX: 0-1000; max:409.68)

---

## 💳 `order_payments`
- `order_id`: Order ID (GX: Not null)
- `payment_sequential`: Payment sequence (for split payments)(GX:1-48; max:29)
- `payment_type`: Method (credit card, boleto, etc.)(GX: Must be one of boleto, credit_card, debit_card, voucher, not_defined)
- `payment_installments`: Number of installments (GX: 0-48; max:24)
- `payment_value`: Amount paid (GX: 0-20000; max: 13664.08)

payment_type
boleto         19784
credit_card    76795
debit_card      1529
not_defined        3
voucher         5775

---

## 📝 `order_reviews`
- `review_id`: Unique review ID (GX: Not null)
- `order_id`: Order reviewed (GX: Not null)
- `order_id_review_id`: Order reviewed (GX: Not null, Unique)
- `review_score`: Rating (1–5)(GX: 1-5; max: 5)
- `review_comment_title`: Title of the comment (GX: Exist)
- `review_comment_message`: Full review message (GX: Exist)
- `review_creation_date`: Date review was written (GX: Timestamp format)
- `review_answer_timestamp`: When Olist responded (GX: Timestamp format)

---

## 🎁 `products`
- `product_id`: Unique product ID (GX: Not Null, Unique)
- `product_category_name`: Category in Portuguese (GX: Not Null)
- `product_name_length`: Character counts (GX: 0-100; max: 76)
- `product_description_length`: Character counts (GX: 0-4000; max: 3992)
- `product_photos_qty`: Number of photos (GX: 0-25; max: 20)
- `product_weight_g` : Dimensions (GX: 0-50000; max: 40425)
- `product_length_cm`: Dimensions (GX: 0-200; max: 105)
- `product_height_cm`: Dimensions (GX: 0-200; max: 105)
- `product_width_cm`: Dimensions (GX: 0-200; max: 118)

---

## 🧑‍💼 `sellers`
- `seller_id`: Unique ID of the seller (GX: Not null, Unique)
- `seller_zip_code_prefix`: First 5 digits of seller ZIP (GX: 5 digits)
- `seller_city`: Seller city (GX: Exist)
- `seller_state`: Seller state (GX: Exist)

---

## 🌍 `geolocation`
- `geolocation_zip_code_prefix`: First 5 digits of ZIP (GX: 5 digits)
- `geolocation_lat` : Latitude (GX: Exist)
- `geolocation_lng`:  Longitude (GX: Exist)
- `geolocation_city` : Region info (GX: Exist)
- `geolocation_state`: Region info (GX: Exist)

---

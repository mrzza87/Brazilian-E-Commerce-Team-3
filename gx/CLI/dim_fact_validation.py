from gx_olist_validation import run_checkpoint

# %%
tgt = 'dim_customers'
mod_name = "gxe_01_olist_dim_customers_suite"
func_name = "build_expectations_gxe_01_olist_dim_customers_suite"
run_checkpoint(tgt, mod_name, func_name)

# %%
tgt = 'dim_date'
mod_name = "gxe_02_olist_dim_date_suite"
func_name = "build_expectations_gxe_02_olist_dim_date_suite"
run_checkpoint(tgt, mod_name, func_name)

# %%
tgt = 'dim_time'
mod_name = "gxe_03_olist_dim_time_suite"
func_name = "build_expectations_gxe_03_olist_dim_time_suite"
run_checkpoint(tgt, mod_name, func_name)

# %%
tgt = 'dim_payments'
mod_name = "gxe_04_olist_dim_payments_suite"
func_name = "build_expectations_gxe_04_olist_dim_payments_suite"
run_checkpoint(tgt, mod_name, func_name)

# %%
tgt = 'dim_order_reviews'
mod_name = "gxe_05_olist_dim_order_reviews_suite"
func_name = "build_expectations_gxe_05_olist_dim_order_reviews_suite"
run_checkpoint(tgt, mod_name, func_name)

# %%
tgt = 'dim_products'
mod_name = "gxe_06_olist_dim_products_suite"
func_name = "build_expectations_gxe_06_olist_dim_products_suite"
run_checkpoint(tgt, mod_name, func_name)

# %%
tgt = 'dim_sellers'
mod_name = "gxe_07_olist_dim_sellers_suite"
func_name = "build_expectations_gxe_07_olist_dim_sellers_suite"
run_checkpoint(tgt, mod_name, func_name)

# %%
tgt = 'dim_geolocation'
mod_name = "gxe_08_olist_dim_geolocation_suite"
func_name = "build_expectations_gxe_08_olist_dim_geolocation_suite"
run_checkpoint(tgt, mod_name, func_name)

# %%
tgt = 'fact_sales_corrected'
mod_name = "gxe_09_olist_fact_sales_suite"
func_name = "build_expectations_gxe_09_olist_fact_sales_suite"
run_checkpoint(tgt, mod_name, func_name)

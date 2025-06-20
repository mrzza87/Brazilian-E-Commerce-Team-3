import sys
import os

# Add parent directory to sys.path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)

from gx_olist_validation import run_checkpoint

def main():

    # %%
    tgt = 'customers'
    mod_name = "gxe_01_olist_customers_suite"
    func_name = "build_expectations_gxe_01_olist_customers_suite"
    run_checkpoint(tgt, mod_name, func_name)

    # %%
    tgt = 'orders_corrected'
    mod_name = "gxe_02_olist_orders_suite"
    func_name = "build_expectations_gxe_02_olist_orders_suite"
    run_checkpoint(tgt, mod_name, func_name)

    # %%
    tgt = 'order_items_corrected'
    mod_name = "gxe_03_olist_order_items_suite"
    func_name = "build_expectations_gxe_03_olist_order_items_suite"
    run_checkpoint(tgt, mod_name, func_name)

    # %%
    tgt = 'order_payments'
    mod_name = "gxe_04_olist_order_payments_suite"
    func_name = "build_expectations_gxe_04_olist_order_payments_suite"
    run_checkpoint(tgt, mod_name, func_name)

    # %%
    tgt = 'order_reviews'
    mod_name = "gxe_05_olist_order_reviews_suite"
    func_name = "build_expectations_gxe_05_olist_order_reviews_suite"
    run_checkpoint(tgt, mod_name, func_name)

    # %%
    tgt = 'products_corrected'
    mod_name = "gxe_06_olist_products_suite"
    func_name = "build_expectations_gxe_06_olist_products_suite"
    run_checkpoint(tgt, mod_name, func_name)

    # %%
    tgt = 'sellers'
    mod_name = "gxe_07_olist_sellers_suite"
    func_name = "build_expectations_gxe_07_olist_sellers_suite"
    run_checkpoint(tgt, mod_name, func_name)

    # %%
    tgt = 'dim_geolocation' # materialised dim table.  geolocation_version1 failed due to 4-char zip code
    mod_name = "gxe_08_olist_geolocation_suite"
    func_name = "build_expectations_gxe_08_olist_geolocation_suite"
    run_checkpoint(tgt, mod_name, func_name)

if __name__ == "__main__":
    main()
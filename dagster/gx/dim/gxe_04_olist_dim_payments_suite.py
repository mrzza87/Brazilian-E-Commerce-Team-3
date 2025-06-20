# File Name: gxe_04_olist_dim_payments_suite.py
# Creation Date/Time: 2025-06-16 11:20:19.703562

# Usage:
#        from gx_exp_gxe_04_olist_dim_payments_suite import build_expectations_gxe_04_olist_dim_payments_suite
#        suite = build_expectations_gxe_04_olist_dim_payments_suite(suite)

import great_expectations as gx

def build_expectations_gxe_04_olist_dim_payments_suite(suite):
  exp = gx.expectations.ExpectColumnValuesToNotBeNull(column="order_id")
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToBeInSet(column="payment_type", value_set=['boleto','canceled','credit_card', 'debit_card', 'voucher', 'not_defined'], mostly="0.9")
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnValuesToBeBetween(column="payment_installments", min_value=0, max_value=48)
  suite.add_expectation(exp)
  return suite
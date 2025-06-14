# File Name: gxe_08_olist_geolocation_suite.py
# Creation Date/Time: 2025-06-14 17:18:48.009976

# Usage:
#        from gx_exp_gxe_08_olist_geolocation_suite import build_expectations_gxe_08_olist_geolocation_suite
#        suite = build_expectations_gxe_08_olist_geolocation_suite(suite)

import great_expectations as gx

def build_expectations_gxe_08_olist_geolocation_suite(suite):
  exp = gx.expectations.ExpectColumnValuesToMatchRegex(column="geolocation_zip_code_prefix", regex="^\\d{5}$")
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnToExist(column="geolocation_lat")
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnToExist(column="geolocation_lng")
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnToExist(column="geolocation_city")
  suite.add_expectation(exp)
  exp = gx.expectations.ExpectColumnToExist(column="geolocation_state")
  suite.add_expectation(exp)
  return suite
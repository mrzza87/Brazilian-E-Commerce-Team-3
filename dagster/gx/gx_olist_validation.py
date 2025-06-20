# %%
import great_expectations as gx

# %%
def dd_site_config(context, site_name):
    # Define a Data Docs site configuration dictionary
    base_directory = "uncommitted/data_docs/local_site/"  # this is the default path (relative to the root folder of the Data Context) but can be changed as required
    site_config = {
        "class_name": "SiteBuilder",
        "site_index_builder": {"class_name": "DefaultSiteIndexBuilder"},
        "store_backend": {
            "class_name": "TupleFilesystemStoreBackend",
            "base_directory": base_directory,
        },
    }


    if site_name not in context.get_site_names():
        context.add_data_docs_site(site_name=site_name, site_config=site_config)
    return context

# %%
def get_data_source(context, data_source_name):
    my_BQ_connection_string="bigquery://brazilian-e-commerce-team-3/BET_Team3"

    # Add BigQuery datasource (Fluent style)
    data_source = context.data_sources.add_or_update_sql(
        name=data_source_name,
        connection_string=my_BQ_connection_string
    )
    return data_source

# %%
def get_data_asset(data_source, tgt, asset_name):
    database_table_name = tgt
    table_data_asset = data_source.add_table_asset(
        table_name=database_table_name, name=asset_name
    )

    # Get the Data Asset from the Data Source
    data_asset = data_source.get_asset(asset_name)
    return data_asset

# %%
def get_full_table_batch(data_asset, batch_definition_name):
    full_table_batch_definition = data_asset.add_batch_definition_whole_table(
        name=batch_definition_name
    )
    full_table_batch = full_table_batch_definition.get_batch()
    return full_table_batch

# %%
import importlib

def get_exp_suite(context, exp_suite_name, mod_name, func_name):
    exp_suite = gx.ExpectationSuite(name=exp_suite_name)
    exp_suite = context.suites.add_or_update(exp_suite)

    #from gxe_01_olist_customers_suite import build_expectations_gxe_01_olist_customers_suite
    # exp_suite = build_expectations_01_olist_customers_suite(exp_suite)

    module = importlib.import_module(mod_name)
    func = getattr(module, func_name)
    exp_suite = func(exp_suite)
    return exp_suite

# %%
def get_batch_defintion(context, data_source_name, asset_name, batch_definition_name):
    batch_definition = (
        context.data_sources.get(data_source_name)
        .get_asset(asset_name)
        .get_batch_definition(batch_definition_name)
    )
    return batch_definition

# %%
def get_validation_definitions(context, validation_definition_name, batch_definition, exp_suite):
    validation_definition = gx.ValidationDefinition(
        data=batch_definition, suite=exp_suite, name=validation_definition_name
    )
    validation_definition = context.validation_definitions.add_or_update(validation_definition)
    validation_definitions = [
        context.validation_definitions.get(validation_definition_name)
    ]
    return validation_definitions

# %%
def get_checkpoint(context, checkpoint_name, site_name, validation_definitions):
    actions = [
        gx.checkpoint.actions.UpdateDataDocsAction(
            name="update_olist_site", site_names=[site_name]       
        )
    ]
    checkpoint = context.checkpoints.add_or_update(
        gx.Checkpoint(
            name=checkpoint_name,
            validation_definitions=validation_definitions,
            actions=actions,
        )
    )
    return checkpoint

# %%
def run_checkpoint(tgt, mod_name, func_name):
    print("Processing Checkpoint for:", tgt)
    context = gx.get_context(mode="file")

    # Add the Data Docs configuration to the Data Context
    site_name = "olist_data_docs_site"
    context = dd_site_config(context, site_name)

    #data_source_name = "BQ_olist_customer_datasource"
    data_source_name = "BQ_olist_" + tgt + "_datasource"
    data_source = get_data_source(context, data_source_name)

    # asset_name = "olist_customers_asset"
    asset_name = "olist_" + tgt + "_asset"
    data_asset = get_data_asset(data_source, tgt, asset_name)

    # batch_definition_name = "olist_customers_batch_def_name"
    batch_definition_name = "olist_" + tgt + "_batch_def_name"
    full_table_batch = get_full_table_batch(data_asset, batch_definition_name)
    full_table_batch.head()

    #exp_suite_name = "olist_customers_suite"
    exp_suite_name = "olist_" + tgt + "_suite"
    exp_suite = get_exp_suite(context, exp_suite_name, mod_name, func_name)

    batch_definition = get_batch_defintion(context, data_source_name, asset_name, batch_definition_name)

    # validation_definition_name = "BQ_customers_validation_definition"
    validation_definition_name = "BQ_" + tgt + "_validation_definition"
    validation_definitions = get_validation_definitions(context, validation_definition_name, batch_definition, exp_suite)

    #checkpoint_name = "olist_customers_checkpoint"
    checkpoint_name = "olist_" + tgt + "_checkpoint"
    checkpoint = get_checkpoint(context, checkpoint_name, site_name, validation_definitions)

    result = checkpoint.run()
    context.open_data_docs()


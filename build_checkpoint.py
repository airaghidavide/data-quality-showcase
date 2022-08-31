import great_expectations as ge
from ruamel import yaml
from great_expectations.data_context.types.resource_identifiers import ValidationResultIdentifier
from great_expectations.core.batch import RuntimeBatchRequest
from fake_data_generator import gen_fake_data
import elm_settings as qs

if __name__ == "__main__":

    n_rows=100

    q = qs.qaSett()

    #generate fake data to validate
    df_fake = gen_fake_data(n_rows)

    #get a data context
    ctx= ge.get_context()
    
    batch_request = RuntimeBatchRequest(
        datasource_name="example_datasource",
        data_connector_name="default_runtime_data_connector_name",
        data_asset_name="my_test",  # This can be anything that identifies this data_asset for you
        runtime_parameters={"batch_data": df_fake},  # df is your dataframe
        batch_identifiers={"default_identifier_name": "default_identifier"},
    )
    
    ctx.create_expectation_suite(expectation_suite_name="check_suite", overwrite_existing=True)
    validator = ctx.get_validator(batch_request=batch_request, expectation_suite_name="check_suite")

    # set of a validations we want to apply to the dataset
 
    validator.expect_column_values_to_be_unique(column="id_cliente")
    validator.expect_column_values_to_be_in_set(
          column = "tipo_carta", 
          value_set = ["PPSTD","PPEVO","PPDIG"]
    )   
    validator.expect_column_to_exist('data_transazione')

    validator.expect_column_values_to_be_between(column='importo',min_value=0,max_value=900)

    validator.expect_table_row_count_to_equal(n_rows-4)

    validator.expect_column_value_lengths_to_equal('secure_code',3)

    # save expectations
    validator.save_expectation_suite(discard_failed_expectations=False)

    # create checkpoint
    q.add_checkpoint(ctx)
import great_expectations as ge
from ruamel import yaml
import pandas as pd
from fake_data_generator import gen_fake_data

if __name__ == "__main__":

    n_rows=100

    #generate fake data to validate
    df_to_eval = gen_fake_data(n_rows)

    #get a data context
    ctx= ge.get_context()

    results = ctx.run_checkpoint(
                                checkpoint_name="checkpoint_data_quality_1",
                                batch_request={
                                                "runtime_parameters": {"batch_data": df_to_eval},
                                                "batch_identifiers": {
                                                            "default_identifier_name": "default_identifier"},
                                                },
                                )
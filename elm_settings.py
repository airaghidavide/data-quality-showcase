import great_expectations as ge
from ruamel import yaml
from great_expectations.data_context.types.resource_identifiers import ValidationResultIdentifier
from great_expectations.core.batch import RuntimeBatchRequest


class qaSett:

    def add_data_source(context):

        datasource_config = {
        "name": "example_datasource",
        "class_name": "Datasource",
        "module_name": "great_expectations.datasource",
        "execution_engine": {
        "module_name": "great_expectations.execution_engine",
        "class_name": "PandasExecutionEngine",
     },
        "data_connectors": {
            "default_runtime_data_connector_name": {
                "class_name": "RuntimeDataConnector",
                "module_name": "great_expectations.datasource.data_connector",
                "batch_identifiers": ["default_identifier_name"],
            },
        },
    }
        context.test_yaml_config(yaml.dump(datasource_config))
        context.add_datasource(**datasource_config)

    def add_checkpoint(context):

        checkpoint_config = {
        "name": "checkpoint_data_quality_1",
        "config_version": 1,
        "class_name": "SimpleCheckpoint",
        "validations": [
            {
                "batch_request": {
                    "datasource_name": "example_datasource",
                    "data_connector_name": "default_runtime_data_connector_name",
                    "data_asset_name": "my_test",
                },
                "expectation_suite_name": "check_suite",
            }
        ],
    }

        context.add_checkpoint(**checkpoint_config)
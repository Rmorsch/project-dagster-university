# src/dagster_and_dbt/defs/assets/dbt.py
import dagster as dg
from dagster_dbt import dbt_assets, DbtCliResource, DagsterDbtTranslator
from dagster import AssetKey

from dagster_and_dbt.defs.project import dbt_project

class CustomizedDagsterDbtTranslator(DagsterDbtTranslator):
    def get_asset_key

@dbt_assets(
    manifest=dbt_project.manifest_path,
)
def dbt_analytics(context: dg.AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()

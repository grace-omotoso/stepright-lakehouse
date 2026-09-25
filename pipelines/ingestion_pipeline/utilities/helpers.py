"""
Shared utilities for step right ingestion pipeline
"""

from pyspark.sql import SparkSession

def get_catalog() -> str:
    """
        Retures the target catalog for this pipeline run
    """

    spark = SparkSession.getActiveSession()
    return spark.conf.get("stepright.catalog", "dev")

def get_landing_path(subfolder: str) -> str:
    """
        Builds a path into this projects landing volume for a give source subfolder.
    """
    return f"/Volumes/{get_catalog()}/stepright/landing/{subfolder}"
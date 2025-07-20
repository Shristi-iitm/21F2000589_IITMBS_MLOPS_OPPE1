# feature_repo/definitions.py
from datetime import timedelta
from feast import Entity, FeatureView, FileSource, ValueType

# Define an entity for our stocks
stock = Entity(
    name="stock_id",
    value_type=ValueType.STRING,
    description="Stock ticker symbol"
)

# Define the source of our feature data (the parquet files we created)
v0_feature_source = FileSource(
    path="data/processed/v0_data.parquet",
    timestamp_field="timestamp",   # ✅ updated from 'date' to 'timestamp'
)

v1_feature_source = FileSource(
    path="data/processed/v1_data.parquet",
    timestamp_field="timestamp",   # ✅ updated from 'date' to 'timestamp'
)

# Define a feature view for our engineered features
stock_features_v0 = FeatureView(
    name="stock_features_v0",
    entities=["stock_id"],
    ttl=timedelta(days=0),
    features=[
        ("rolling_avg_10", ValueType.FLOAT),
        ("volume_sum_10", ValueType.FLOAT),
        ("target", ValueType.INT64),  # Including target here for simplicity
    ],
    online=False,
    source=v0_feature_source,
    tags={},
)

stock_features_v1 = FeatureView(
    name="stock_features_v1",
    entities=["stock_id"],
    ttl=timedelta(days=0),
    features=[
        ("rolling_avg_10", ValueType.FLOAT),
        ("volume_sum_10", ValueType.FLOAT),
        ("target", ValueType.INT64),
    ],
    online=False,
    source=v1_feature_source,
    tags={},
)

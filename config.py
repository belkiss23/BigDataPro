"""
Configuration file for IMDB Analysis and Wikipedia Stream Processing
"""

# IMDB Data URLs
IMDB_BASE_URL = "https://datasets.imdbws.com/"
IMDB_DATASETS = {
    "name_basics": "name.basics.tsv.gz",
    "title_akas": "title.akas.tsv.gz",
    "title_basics": "title.basics.tsv.gz",
    "title_crew": "title.crew.tsv.gz",
    "title_episode": "title.episode.tsv.gz",
    "title_principals": "title.principals.tsv.gz",
    "title_ratings": "title.ratings.tsv.gz"
}

# Data directories
DATA_DIR = "data"
IMDB_DIR = f"{DATA_DIR}/imdb"
WIKI_STREAM_DIR = f"{DATA_DIR}/wiki_stream"

# Spark configuration
SPARK_CONFIG = {
    "spark.sql.adaptive.enabled": "true",
    "spark.sql.adaptive.coalescePartitions.enabled": "true",
    "spark.serializer": "org.apache.spark.serializer.KryoSerializer"
}

# Wikipedia EventStreams configuration
WIKI_STREAM_URL = "https://stream.wikimedia.org/v2/stream/recentchange"
WIKI_CHECKPOINT_LOCATION = f"{WIKI_STREAM_DIR}/checkpoints"

# Streaming configuration
STREAMING_BATCH_INTERVAL = "10 seconds"
STREAMING_TRIGGER_INTERVAL = "10 seconds"

# Alert configuration
ALERT_KEYWORDS = ["vandalism", "deletion", "block", "revert", "protection"]



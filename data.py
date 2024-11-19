import pandas as pd
import numpy as np

# Number of sample configurations
num_samples = 30000

# Generate sample configuration IDs
config_ids = range(1, num_samples + 1)

# Generate random knob settings (e.g., memory and caching settings)
knob_data_df = pd.DataFrame({
    "config_id": config_ids,
    "buffer_pool_size": np.random.randint(256, 8192, num_samples),      # in MB
    "cache_size": np.random.randint(64, 2048, num_samples),             # in MB
    "log_file_size": np.random.randint(64, 512, num_samples),           # in MB
    "thread_concurrency": np.random.randint(1, 32, num_samples),        # thread count
    "query_cache_size": np.random.randint(0, 1024, num_samples)         # in MB
})

# Generate random runtime metrics (e.g., read/write counts, lock waits)
metrics_data_df = pd.DataFrame({
    "metric_pages_read": np.random.randint(10000, 50000, num_samples),
    "metric_pages_written": np.random.randint(10000, 50000, num_samples),
    "metric_cache_hits": np.random.randint(5000, 20000, num_samples),
    "metric_cache_misses": np.random.randint(1000, 5000, num_samples),
    "metric_lock_wait_time": np.random.uniform(0.1, 5.0, num_samples)  # in seconds
})

# Generate random performance metrics (e.g., latency in milliseconds)
performance_data_df = pd.DataFrame({
    "performance_latency_99th_percentile": np.random.uniform(100, 2000, num_samples)  # in ms
})

# Combine all DataFrames into a single DataFrame
df = pd.concat([knob_data_df, metrics_data_df, performance_data_df], axis=1)

# Save the DataFrame to a CSV file
df.to_csv('dbms_tuning_data.csv', index=False)
print("Sample DBMS tuning data saved to 'dbms_tuning_data.csv'")

# Convert data sections into numpy arrays for downstream compatibility
knob_data = knob_data_df.to_numpy()
metrics_data = metrics_data_df.to_numpy()
performance_metric = performance_data_df["performance_latency_99th_percentile"].to_numpy()

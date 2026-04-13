# Pydantic Settings for all environment configuration

# Step 1: Define Settings class using pydantic BaseSettings
# Step 2: AWS settings — region, Bedrock model ID, RDS host/port/db/user/password
# Step 3: Auth settings — JWT secret, algorithm, token expiry
# Step 4: Kafka settings — bootstrap servers, topic names
# Step 5: pgvector settings — embedding dimensions, similarity threshold
# Step 6: App settings — debug mode, log level, environment (dev/prod)
# Step 7: Implement get_settings() singleton using lru_cache

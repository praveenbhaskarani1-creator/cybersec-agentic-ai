# PostgreSQL + pgvector Connection Pool (Aurora RDS)

# Step 1: Load DB config from config.py (host, port, db, user, password)
# Step 2: Create SQLAlchemy async engine with connection pooling
# Step 3: Enable pgvector extension on first connect (CREATE EXTENSION IF NOT EXISTS vector)
# Step 4: Implement get_db() — async session generator for dependency injection
# Step 5: Implement DatabaseManager singleton with health_check() method
# Step 6: Handle connection retries on startup (ECS Fargate cold start)

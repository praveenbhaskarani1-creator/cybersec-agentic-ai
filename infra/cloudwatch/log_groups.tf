# Terraform — CloudWatch Log Groups

# Step 1: Create log group for ECS Fargate FastAPI container: /ecs/cybersec-api
# Step 2: Create log group for Streamlit EC2: /ec2/cybersec-streamlit
# Step 3: Create log group for ingestion workers: /workers/cybersec-ingestion
# Step 4: Set retention policy (e.g. 30 days for dev, 365 days for prod)
# Step 5: Create CloudWatch alarms:
#         - High error rate on /ask endpoint
#         - HIL queue depth > N (too many pending approvals)
#         - Ingestion lag (Kafka consumer lag > threshold)
# Step 6: Configure SNS topic for alarm notifications to SOC team

import faker
import random
from datetime import datetime



def generate_descriptions(filename, n=1000000):
    # combination of actions, subjection, context, technonologies 

    actions = [
        "Automated", "Distributed", "Legacy", "Containerized", "Cloud-native",
        "Serverless", "Encrypted", "Optimized", "Synchronized", "Parallelized",
        "Validated", "Aggregated", "Replicated", "Virtualized", "Consolidated",
        "Federated", "Decentralized", "Anonymized", "Normalized", "Scalable",
        "Isolated", "Provisioned", "Orchestrated", "Instrumented", "Monitored",
        "Refactored", "Versioned", "Hardened", "Audited", "Streamlined",
        "Automated", "Elastic", "Resilient", "Redundant", "Stateless",
        "Stateful", "Reactive", "Asynchronous", "Event-driven", "Decoupled",
        "Hierarchical", "Categorized", "Serialized", "Compressed", "Encapsulated",
        "Standardized", "Centralized", "Governed", "Fragmented", "Synthesized"
    ]
    subjects = [
        "ETL Pipeline", "Data Warehouse", "Microservice", "API Gateway", "Auth Module",
        "Load Balancer", "Metadata Store", "Blob Storage", "Query Engine", "Stream Processor",
        "Feature Store", "Semantic Layer", "Compute Cluster", "Workflow Engine", "Data Lake",
        "Ingestion Job", "Discovery Service", "Security Sandbox", "Event Hub", "Logic Controller",
        "Message Broker", "Key-Value Store", "Search Index", "Cache Layer", "Relational Proxy",
        "Validation Engine", "Migration Script", "Logging Daemon", "Metrics Collector", "Identity Provider",
        "Rule Engine", "File System", "Backup Vault", "Edge Gateway", "Virtual Network",
        "Application Mesh", "Batch Processor", "In-Memory DB", "Document Store", "Graph Node",
        "Transaction Coordinator", "Schema Registry", "Protocol Buffer", "Web Socket", "Worker Node",
        "Task Scheduler", "Notification Hub", "Encryption Module", "Access Controller", "State Machine"
    ]

    contexts = [
        "for Financial Audit", "supporting Real-time Analytics", "within the Compliance Layer", 
        "handling User Telemetry", "managed via Kubernetes", "deployed in AWS-East", 
        "serving Edge Nodes", "integrating Legacy Mainframes", "optimizing Resource Allocation", 
        "tracking Multi-cloud Assets", "facilitating Cross-border Trade", "monitoring System Health", 
        "powering Predictive Models", "during Disaster Recovery", "for Stakeholder Reporting", 
        "within Zero-Trust Network", "handling Sensitive PII", "scaling Background Tasks", 
        "processing Batch Exports", "mapping Customer Journeys", "enforcing Data Privacy",
        "securing Internal Endpoints", "analyzing Market Trends", "reducing Latency Overhead",
        "governing Metadata Standards", "within DevOps Pipelines", "handling High-Traffic Spikes",
        "supporting Mobile Clients", "bridging Hybrid Environments", "during Seasonal Peak",
        "for Inventory Management", "tracking Logistical Flows", "securing IoT Streams",
        "managing Subscription Lifecycles", "optimizing Database Queries", "facilitating Global Search",
        "within Sandbox Environments", "supporting Legacy Integration", "validating API Requests",
        "processing Credit Scores", "monitoring Network Traffic", "handling Error Logs",
        "calculating Risk Profiles", "matching User Profiles", "detecting Fraud Patterns",
        "balancing Server Loads", "storing User Preferences", "indexing Web Content",
        "serving Static Assets", "authenticating Remote Workers"
    ]

    technologies = [
        "using Python/PySpark", "via GraphQL", "backed by Redis", "running on Snowflake", 
        "with Kafka streams", "using OAuth2.0", "leveraging AI-driven indexing", 
        "integrated with Databricks", "via gRPC calls", "using Terraform HCL", 
        "backed by MongoDB Atlas", "running on Azure Functions", "via RESTful Webhooks", 
        "using dbt core", "with ElasticSearch", "leveraging Docker Compose", 
        "using Prometheus metrics", "via Jenkins Pipeline", "backed by PostgreSQL", 
        "using AWS Lambda", "with RabbitMQ", "running on Google BigQuery",
        "leveraging Apache Flink", "using Rust binaries", "via Apollo Server",
        "backed by Cassandra", "using Kubernetes CRDs", "with Helm Charts",
        "running on EC2", "leveraging OpenTelemetry", "using SQL Server",
        "via SOAP requests", "with Spark Streaming", "using Go routines",
        "backed by DynamoDB", "running on Heroku", "via Cloudflare Workers",
        "leveraging Vector Search", "using Scikit-learn", "with TensorFlow",
        "running on On-Prem Servers", "via Private Link", "using Bitbucket Pipelines",
        "backed by MariaDB", "using Nginx", "with Istio Service Mesh",
        "leveraging PyTorch", "using Node.js", "via Fast API", "backed by SQLite"
    ]

    descriptions = set()
    
    print(f"Generating {n} unique descriptions...")
    with open(filename, "w", encoding="utf-8") as f:

        while len(descriptions) < n:
            # Construct a randomized sentence
            desc = (
                f"{random.choice(actions)} {random.choice(subjects)} "
                f"{random.choice(contexts)} {random.choice(technologies)} "
            )
            

            if desc not in descriptions:
                descriptions.add(desc)
                f.write(desc + "\n")
            
            # Progress tracker
            if len(descriptions) % 200000 == 0:
                print(f"Progress: {len(descriptions)}/1000000")


def generate_names(filename, n=1000000):
    # Combination of prefix, mid_words, and suffixes
    prefixes = [
        "Global", "Nexus", "Hyper", "Alpha", "Omega", "Cloud", "Data", "Smart", "Swift", "Core",
        "Azure", "Vertex", "Iron", "Sonic", "Ultra", "Prime", "Meta", "Quantum", "Apex", "Flux",
        "Nova", "Zion", "Titan", "Orbit", "Aura", "Zenith", "Polar", "Solar", "Logic", "Vector",
        "Cyber", "Active", "Deep", "Rapid", "Infinite", "Delta", "Sigma", "Origin", "Eon", "Vortex",
        "Shield", "Matrix", "Aero", "Neon", "Static", "Dynamic", "Fusion", "Macro", "Micro", "Atomic"
    ]

    mid_words = [
        "Stream", "Sync", "Link", "Flow", "Pulse", "Forge", "Grid", "Scale", "Point", "Base",
        "View", "Sight", "Path", "Node", "Bolt", "Web", "Net", "Zone", "Frame", "Work",
        "Shift", "Layer", "Trace", "Scan", "Graph", "Wire", "Key", "Map", "Melt", "Bond",
        "Dash", "Blast", "Track", "Drive", "Edge", "Core", "Burst", "Snap", "Split", "Join",
        "Peak", "Ridge", "Span", "Mark", "Step", "Wave", "Slide", "Sort", "Filter", "Route"
    ]     
    
    suffixes = [
        "Analytics", "Engine", "Portal", "Suite", "Manager", "Hub", "Lab", "System", "Interface", "Gateway",
        "Vault", "Bridge", "Stack", "Fabric", "Service", "Client", "Node", "Center", "Store", "Library",
        "Module", "Plugin", "Anchor", "Pilot", "Beacon", "Relay", "Unit", "Cell", "Source", "Flow",
        "Tool", "Kit", "Panel", "Console", "Desk", "Room", "Vault", "Shell", "Kernel", "Core",
        "Proxy", "Agent", "Bot", "Sense", "Vision", "Scope", "Metrics", "Log", "Registry", "Deploy"
    ]

    app_names = set()
    print(f"Generating {n} unique app names...")

    with open(filename, "w", encoding="utf-8") as f:
        while len(app_names) < n:
            # Structure: Prefix + Mid + Suffix + Random ID
            # Example: GlobalSyncPortal_8842
            name = (
                f"{random.choice(prefixes)} "
                f"{random.choice(mid_words)} "
                f"{random.choice(suffixes)}"
            )
            if name not in app_names:
                app_names.add(name)
                f.write(name + "\n")
            
            # Progress tracker
            if len(app_names) % 200000 == 0:
                print(f"Progress: {len(app_names)}/1000000")


if __name__ == "__main__":
    # Generate the descriptions and app name
    desc_results = generate_descriptions('desc.txt',1000000)
    app_results = generate_names('app.txt',100000)

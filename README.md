# Elasticsearch Logging Middleware

# Usecase:

- All requests to Elasticsearch service must go through the provided endpoints

# Endpoints

## /api/query POST

### body:

- {  
  "client_id":"atomberg",
  "index":"atomberg",
  "type":"details"
  "question":"What are store timings?",
  "category":"general_queries",
  "return_fields": ["answers", "pname", "questiontop"]
  }

## /api/logs GET

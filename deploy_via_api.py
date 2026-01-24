#!/usr/bin/env python3
"""Deploy to Railway via API"""
import requests
import json
import os
import subprocess

# Railway API endpoint
API_URL = "https://backboard.railway.com/graphql/v2"

# Project and service IDs
PROJECT_ID = "e1c962f8-9338-4d73-8f72-3874c2ce5ffe"
SERVICE_ID = "5daaa389-bec4-4283-84da-9f54f1be51fa"
TOKEN = "c5206d1b-e582-422a-a0dc-19eb07e35288"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

# Create deployment from local source
print("Creating deployment from local source...")

# First, let's try to get service info
query = """
query getService {
  service(id: "%s") {
    id
    name
    project {
      id
      name
    }
  }
}
""" % SERVICE_ID

response = requests.post(
    API_URL,
    headers=headers,
    json={"query": query}
)

print(f"Service info response: {response.status_code}")
print(response.text)

# Try to trigger a deployment
mutation = """
mutation {
  serviceInstanceRedeploy(
    environmentId: "production"
    serviceId: "%s"
  )
}
""" % SERVICE_ID

response = requests.post(
    API_URL,
    headers=headers,
    json={"query": mutation}
)

print(f"\\nDeploy response: {response.status_code}")
print(response.text)

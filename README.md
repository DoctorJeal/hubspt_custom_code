# HubSpot Custom Code Actions for CRM Automation

A collection of reusable custom code snippets for HubSpot workflows, designed to extend automation capabilities beyond standard workflow actions.

This repository focuses on practical, production-ready examples using HubSpot’s API with secure authentication via private app tokens.

---

## 🚀 Overview

HubSpot custom code actions allow you to run Node.js or Python within workflows. This repository provides ready-to-use snippets for common use cases such as:

- CRM object search and filtering  
- Record counting and aggregation  
- Sequential numbering and ID generation  
- Data transformation within workflows  
- API-based enrichment and updates  

All examples follow best practices for:
- Secure token handling using environment variables  
- Efficient API usage  
- Clear, maintainable structure  

---

## 🔐 Authentication

All code examples assume the use of a **HubSpot private app token** stored as a secret in the custom code action.

Secrets are accessed via environment variables:

### Python
```python
import os
from hubspot import HubSpot

client = HubSpot(access_token=os.environ['YOUR_SECRET_NAME'])

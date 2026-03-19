"""
Example HubSpot Custom Code Action: Custom Object Record Count with Offset

This script demonstrates how to retrieve the total number of records for a 
HubSpot custom object and return an incremented value. It is intended for use 
within a HubSpot workflow custom code action.

Typical use case:
- Generate a sequential number based on the current number of records
- Apply an offset to control the starting point of the sequence

Important:
- This example uses a custom object. You MUST update the `object_type` value 
  (e.g. "2-2149023") to match your own HubSpot custom object ID.
- A private app token must be added as a secret in the workflow and referenced 
  via `os.environ`. In this example, the secret name is 'Sequential_Numbering' 
  and should be updated if your secret uses a different name.

Key behaviour:
- Performs a search request with `limit=1` to efficiently retrieve only the 
  total record count (no need to fetch all records)
- Uses the `total` property from the API response
- Applies a numeric offset (+671 in this example) to control numbering

Returns:
- total_count (int): The adjusted total number of records, returned to the 
  workflow via `outputFields`

Notes:
- Ensure your private app has the required permissions to read the custom object
- The offset value can be modified depending on your numbering requirements
"""

import os
from hubspot import HubSpot
from hubspot.crm.objects import PublicObjectSearchRequest, ApiException

def main(event):
    try:
        client = HubSpot(access_token=os.environ['Sequential_Numbering'])

        public_object_search_request = PublicObjectSearchRequest(
            limit=1,
            after=0
        )

        api_response = client.crm.objects.search_api.do_search(
            object_type="2-2149023",
            public_object_search_request=public_object_search_request
        )

        total_count = api_response.total
        total_count = int(total_count) + 671 #offset for where you want to start the numbering.

        return {
            "outputFields": {
                "total_count": total_count
            }
        }

    except ApiException as e:
        print(f"Exception when calling search_api->do_search: {e}")
        raise e

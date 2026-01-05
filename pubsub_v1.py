from google.cloud import pubsub_v1
from google.oauth2 import service_account

# Option 1: Automatic authentication via environment variable
client = pubsub_v1.PublisherClient()

# Option 2: Explicit credentials
credentials = service_account.Credentials.from_service_account_file(
    '/path/to/service-account-key.json'
)
client = pubsub_v1.PublisherClient(credentials=credentials)

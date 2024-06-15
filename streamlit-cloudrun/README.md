# streamlit-cloudrun

Streamlit App を Cloud Run にデプロイするサンプル

## Quickstart

### Deploy

```bash
poetry export -f requirements.txt -o requirements.txt
gcloud run deploy --allow-unauthenticated --source . --region asia-northeast1 streamlit-tutotial
```

## Tips

### About Logging

- [Logging client libraries  |  Google Cloud](https://cloud.google.com/logging/docs/reference/libraries#client-libraries-install-python)
- [Python client library  |  Google Cloud](https://cloud.google.com/python/docs/reference/logging/latest/std-lib-integration)

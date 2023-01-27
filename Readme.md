gcloud config set project PROJECT_ID

gcloud builds submit --tag gcr.io/twilio-361201/twilio .

gcloud run deploy --image gcr.io/twilio-361201/twilio --platform managed --allow-unauthenticated --memory=512M --cpu=1 --concurrency=80 --timeout=300 --max-instances=2
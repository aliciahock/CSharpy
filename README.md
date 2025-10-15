How to publish to google cloud

https://cloud.google.com/?hl=en

Create a project

IAM & Admin/Service Accounts/Create a Service account

Grant the Cloud Run Admin role to the Cloud Build service account:

In the Cloud Console, go to the Cloud Build Settings page:

Open the Settings page

Locate the row with the Cloud Run Admin role and set its Status to ENABLED.

Enable Container Analysis API

Enable Gemini API

gcloud init

gcloud run deploy --source .

Service name (programming):
Please specify a region:
 [9] asia-southeast1

How to run in local PC:

pip install -r requirements.txt

flask run

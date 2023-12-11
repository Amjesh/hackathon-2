from src.utils.temp_db import temp_data
from src.config.logger import Logger
from src.utils.webhook import call_webhook_with_error

logger = Logger()


# Function to filter CVs based on job description
def filter_cvs(job_description, drive, folder_id, threshold=0.5):
    job_tokens = preprocess_text(job_description)
    filtered_cvs = []

    # Retrieve files from Google Drive folder
    file_list = drive.ListFile(
        {'q': f"'{folder_id}' in parents and trashed=false"}).GetList()

    for file in file_list:
        # Download the CV file
        cv_file = drive.CreateFile({'id': file['id']})
        cv_content = StringIO(cv_file.GetContentString())

        # Extract text from the CV
        cv_text = extract_text_from_pdf(cv_content)

        # Tokenize and preprocess the CV text
        cv_tokens = preprocess_text(cv_text)

        # Calculate Jaccard similarity between job description and CV
        similarity_score = calculate_jaccard_similarity(job_tokens, cv_tokens)

        # Check if the similarity score is above the threshold
        if similarity_score > threshold:
            # Append information about the CV to the filtered CVs list
            filtered_cvs.append({
                'Rank': len(filtered_cvs) + 1,
                'Name': file['title'],
                'CV link': file['alternateLink'],
                # Add logic to extract experience information
                'Experience': 'Example Experience',
                'Education': 'Example Education',  # Add logic to extract education information
                'Highlights': 'Example Highlights',  # Add logic to extract highlights
                'Don\'t Meet Criteria': 'Example Criteria',  # Add logic to check criteria
                'Score': similarity_score
            })

    # Sort the filtered CVs based on similarity scores in descending order
    filtered_cvs = sorted(filtered_cvs, key=lambda x: x['Score'], reverse=True)

    return filtered_cvs


# This is the base_agent function. This function is called when the agent is executed.
# You can also use the temp_data variable to store data that you want to use in other methods.
# You can use the call_webhook_with_success and call_webhook_with_error methods to call the webhook.
# You can use the logger variable to log your data.
# For return the response you can use see config/agent.json file output section.
def base_agent(payload):
    try:
        logger.info("base_agent() called with ", payload)
        inputs = payload.get("inputs")
        job_description = inputs.get("job_description")
        pdf_cv_paths = inputs.get("pdf_cv_paths")
        threshold = 0.7

       # Authenticate with Google Drive
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()

        # Create GoogleDrive instance
        drive = GoogleDrive(gauth)

        # Replace 'YOUR_FOLDER_ID' with the actual folder ID in your Google Drive
        folder_id = 'YOUR_FOLDER_ID'

        # Filter CVs based on the job description
        result = filter_cvs(job_description, drive, folder_id)
        resp = {
            "name": "greeting",
            "type": "shortText",
            "data": result
        }

        return resp
    except Exception as e:
        logger.error('Getting Error in base_agent:', e)
        raise call_webhook_with_error(str(e), 500)

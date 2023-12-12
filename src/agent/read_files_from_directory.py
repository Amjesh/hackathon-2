import os
import re
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from oauth2client.service_account import ServiceAccountCredentials
import docx2txt
import fitz  # PyMuPDF
import json

drive = None

def authenticate_drive():
    try:
        global drive
        service_account_json = 'src/config/hackathon-407906-e75ff1af6a9a.json'

        # Create ServiceAccountCredentials using the JSON file
        credentials = ServiceAccountCredentials.from_json_keyfile_name(service_account_json, ['https://www.googleapis.com/auth/drive'])

        # Authenticate PyDrive with the credentials
        gauth = GoogleAuth()
        gauth.credentials = credentials

        # Save the credentials to a file for future use
        gauth.SaveCredentialsFile("src/config/client_secret_70946552265-gn7bf32qnmehltpqka5ucer2kbo41vs0.apps.googleusercontent.com.json")

        drive = GoogleDrive(gauth)
        return drive
    except Exception as e:
        print(e)

def fetch_cvs(drive):
    # Rest of the function remains the same
    cv_folder_id = '12eumdvdfurRZ-gPsk1ct65zly5734_qw'
    cv_files = drive.ListFile({'q': f"'{cv_folder_id}' in parents and trashed=false"}).GetList()
    print(cv_files)
    return cv_files

def download_file(drive, file_id, file_name):
    # Download a file from Google Drive and save it locally
    file = drive.CreateFile({'id': file_id})
    file.GetContentFile(file_name)

def extract_information_from_cv(cv_text):
    try:
        # Placeholder values for extracted information
        experience = re.search(r'(experience|work\s*experience).*?(\n\n|\n\*|\n\s*\d+\.)', cv_text, re.IGNORECASE | re.DOTALL)
        projects = re.search(r'(projects|personal\s*projects).*?(\n\n|\n\*|\n\s*\d+\.)', cv_text, re.IGNORECASE | re.DOTALL)
        skills = re.search(r'(skills).*?(\n\n|\n\*|\n\s*\d+\.)', cv_text, re.IGNORECASE | re.DOTALL)

        return {
            "experience": experience.group(0).strip() if experience else "",
            "projects": projects.group(0).strip() if projects else "",
            "skills": skills.group(0).strip() if skills else ""
        }
    except Exception as e:
        print(e)

def process_cvs_and_store_json(drive, cv_files):
    try:
        data = []
        existing_data = []
        if os.path.exists('cv_data.json'):
            with open('cv_data.json', 'r') as existing_file:
                existing_data = json.load(existing_file)

        for cv_file in cv_files:
            file_id = cv_file['id']
            file_name = cv_file['title']

            if file_name.lower().endswith('.json') or any(item["file_name"] == file_name for item in existing_data):
                continue

            # Download the file locally
            download_file(drive, file_id, file_name)

            # Process the downloaded file
            if file_name.endswith('.docx'):
                cv_text = docx2txt.process(file_name)
            elif file_name.endswith('.pdf'):
                cv_text = extract_text_from_pdf(file_name)
            else:
                # Handle other file types if needed
                cv_text = ""

            # Extract information from the CV text
            cv_info = extract_information_from_cv(cv_text)

            data.append({
                "file_name": file_name,
                "cv_info": cv_info
            })

            # Remove the downloaded file (optional)
            os.remove(file_name)

        # Store the data in a JSON file
        final_data = existing_data + data
        with open('src/config/cv_data.json', 'w') as json_file:
            json.dump(final_data, json_file, indent=2)
    except Exception as e:
        print(e)

def extract_text_from_pdf(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page_number in range(doc.page_count):
            page = doc[page_number]
            text += page.get_text()

        return text
    except Exception as e:
        print(e)
import json
import os
import sys

import yaml
from dotenv import load_dotenv

load_dotenv()


SETTINGS_PATH = os.path.join("settings.yaml")
MYCREDS_PATH = os.path.join("_mycreds.txt")
SECRETS_PATH = os.path.join("client_secrets.json")


# create yaml file
if not os.path.exists(SETTINGS_PATH):
    settings_yaml = {
        "client_config_backend": "settings",
        "client_config": {
            "client_id": "9637341109347.apps.googleusercontent.com",
            "client_secret": "psDskOoWr1P602PXRTHi",
        },
        "save_credentials": True,
        "save_credentials_backend": "file",
        "save_credentials_file": "credentials.json",
        "get_refresh_token": True,
        "oauth_scope": [
            "https://www.googleapis.com/auth/drive",
            "https://accounts.google.com/o/oauth2/auth",
        ],
    }

    # Generate configuration file for pyydrive authentication
    with open(os.path.join(SETTINGS_PATH), "w") as f:
        yaml.dump(settings_yaml, f, default_flow_style=False)

    print("The settings.yaml file has been created!")

# Create client_secrets.json in downloader_app directory
if not os.path.exists(SECRETS_PATH):
    credentials_info = {
        "web": {
            "client_id": os.getenv("CLIENTE_ID"),
            "project_id": os.getenv("PROJETO_ID"),
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_secret": os.getenv("CLIENTE_SECRETS"),
            "redirect_uris": ["http://localhost:8090/", "http://localhost:8080/",],
            "javascript_origins": ["http://localhost:8080", "http://localhost:8090",],
        }
    }

    with open(os.path.join(SECRETS_PATH), "w") as f:
        json.dump(credentials_info, f)
        print("The client_secrets.json file has been created!")

# Create mycreds in downloader_app directory
if not os.path.exists(MYCREDS_PATH):
    mycreds_info = {
        "access_token": os.getenv("ACESSO_TOKEN"),
        "client_id": os.getenv("CLIENTE_ID"),
        "client_secret": os.getenv("CLIENTE_SECRETS"),
        "refresh_token": os.getenv("REFRESCA_TOKEN"),
        "token_expiry": "2020-12-31T23:36:20Z",
        "token_uri": "https://oauth2.googleapis.com/token",
        "user_agent": "null",
        "revoke_uri": "https://oauth2.googleapis.com/revoke",
        "id_token": "null",
        "id_token_jwt": "null",
        "token_response": {
            "access_token": os.getenv("ACESSO_TOKEN"),
            # "expires_in": 3599,
            "scope": "https://www.googleapis.com/auth/drive",
            "token_type": "Bearer",
        },
        "scopes": ["https://www.googleapis.com/auth/drive"],
        "token_info_uri": "https://oauth2.googleapis.com/tokeninfo",
        "invalid": False,
        "_class": "OAuth2Credentials",
        "_module": "oauth2client.client",
    }
    with open(os.path.join(MYCREDS_PATH), "w") as f:

        class to_str(dict):
            def __str__(self):
                return json.dumps(self)

        mycreds_str = to_str(mycreds_info)
        f.write(str(mycreds_str))
        f.close()
        print("The mycreds.txt file has been created!")

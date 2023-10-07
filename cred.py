from google.oauth2 import service_account
import config


def get_cred():
    return service_account.Credentials.from_service_account_file(config.SERVICE_ACCOUNT_FILE, scopes=config.SCOPES)

import os

class Config:
    # Flask secret key for session management
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'

    # Azure SQL Database
    SQL_SERVER   = os.environ.get('SQL_SERVER')   or 'cms.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'cms'
    SQL_USER_NAME= os.environ.get('SQL_USER_NAME')or 'cmsadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'CMS4dmin'

    # Azure Blob Storage
    BLOB_ACCOUNT           = os.environ.get('BLOB_ACCOUNT')           or 'images11'
    BLOB_CONTAINER         = os.environ.get('BLOB_CONTAINER')         or 'images'
    BLOB_STORAGE_KEY       = os.environ.get('BLOB_STORAGE_KEY')       or '<YOUR_BLOB_STORAGE_KEY>'
    BLOB_CONNECTION_STRING = os.environ.get('BLOB_CONNECTION_STRING') or (
        'DefaultEndpointsProtocol=https;AccountName=images11;'
        'AccountKey=<YOUR_BLOB_STORAGE_KEY>;'
        'EndpointSuffix=core.windows.net'
    )

    # Microsoft Entra ID / OAuth2
    CLIENT_ID     = os.environ.get('CLIENT_ID')     or '1660e7a3-74ae-4945-aea0-5bd962871c33'
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET') or '<YOUR_CLIENT_SECRET>'
    AUTHORITY     = 'https://login.microsoftonline.com/common'
    REDIRECT_PATH = '/getAToken'
    SCOPE         = ['User.Read']

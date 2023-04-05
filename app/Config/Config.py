from dotenv import load_dotenv
import os 


class Config():
    def __init__(self):
        load_dotenv()

        self.API_TOKEN = os.getenv('API_TOKEN')

        self.AIRTABLE_API_KEY=\
                os.getenv('AIRTABLE_API_KEY')
        self.AIRTABLE_BASE_ID=\
                os.getenv('AIRTABLE_BASE_ID')
        self.AIRTABLE_STATES_TABLE_ID=\
                os.getenv('AIRTABLE_STATES_TABLE_ID')
        self.AIRTABLE_STATES_TABLE_VIEW_ID=\
                os.getenv('AIRTABLE_STATES_TABLE_VIEW_ID')
        self.AIRTABLE_TRANSITIONS_TABLE_ID=\
                os.getenv('AIRTABLE_TRANSITIONS_TABLE_ID')
        self.AIRTABLE_TRANSITION_TABLE_VIEW_ID=\
                os.getenv('AIRTABLE_TRANSITION_TABLE_VIEW_ID')
        self.AIRTABLE_FORMS_TABLE_ID=\
                os.getenv('AIRTABLE_FORMS_TABLE_ID')
        self.AIRTABLE_FORMS_TABLE_VIEW_ID=\
                os.getenv('AIRTABLE_FORMS_TABLE_VIEW_ID') 
        self.AIRTABLE_CONFIG_TABLE_ID=\
                os.getenv('AIRTABLE_CONFIG_TABLE_ID')
        self.AIRTABLE_CONFIG_TABLE_VIEW_ID=\
                os.getenv('AIRTABLE_CONFIG_TABLE_VIEW_ID')

        self.MAXDMG_DOCGEN_TEMPLATES_DIR=\
                os.getenv('MAXDMG_DOCGEN_TEMPLATES_DIR')
        self.MAXDMG_DOCGEN_TMP_DIR=\
                os.getenv('MAXDMG_DOCGEN_TMP_DIR')

        self.WEBHOOK = False
        WEBHOOK_HOST = os.getenv('WEBHOOK_HOST', '')

        if len(WEBHOOK_HOST) > 0:
            WEBHOOK_PORT = os.getenv('WEBHOOK_PORT', '')
            if len(WEBHOOK_PORT) == 0:
                WEBHOOK_PORT = '443'

            if not hasattr(self, 'WEBHOOK_ID'):
                import random
                import string
                self.WEBHOOK_ID = ''.join(random.choice(string.ascii_lowercase) 
                                      for i in range(20))            

            self.WEBHOOK_PATH = f"/webhook/{self.WEBHOOK_ID}"
            self.WEBHOOK_URL  = f"{WEBHOOK_HOST}:{WEBHOOK_PORT}{self.WEBHOOK_PATH}"

            self.WEBAPP_HOST  = os.getenv('WEBAPP_HOST', '')
            self.WEBAPP_PORT  = os.getenv('WEBAPP_PORT', '')

            self.WEBHOOK_SSL_CERT_PATH  = os.getenv('WEBHOOK_SSL_CERT_PATH')
            self.WEBHOOK_SSL_PRIV_PATH  = os.getenv('WEBHOOK_SSL_PRIV_PATH')
            print(self.WEBHOOK_URL)

            self.WEBHOOK = True

        self.LOG_DIR        = os.getenv('LOG_DIR')
        self.LOG_FILE       = os.getenv('LOG_FILE')
        self.LOG_FILE_SIZE  = int(os.getenv('LOG_FILE_SIZE'))
        self.LOG_MAX_FILES  = int(os.getenv('LOG_MAX_FILES'))

        self.STATS_DB_NAME  = \
            os.getenv('POSTGRES_DB')
        self.STATS_DB_PASS  = \
            os.getenv('TGFE_STATS_ADMIN_PASS')


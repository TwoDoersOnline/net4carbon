#%%
from pygsheets import authorize as api
import panel as pn
from core.carbon import Sensor


pn.extension(sizing_mode='stretch_width', template='bootstrap')

bootstrap = pn.template.BootstrapTemplate(title='Net4-CO2')









pn.Row(
    pn.Card(time_now)
    pn.Card(historic)
)

# %%
from google_auth_oauthlib.flow import InstalledAppFlow
SCOPE = ['https://www.googleapis.com/auth/spreadsheets']
flow = InstalledAppFlow.from_client_secrets_file('client_secrets.json', SCOPE)
cred = flow.run_local_server(port=0)


API_KEY='AIzaSyAIlL33GPcc3Niw3kEA6EbOW9cVWR9Z93o'
key=API_KEY
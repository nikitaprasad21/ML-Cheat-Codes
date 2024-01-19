3 Dataset url
acme_url = "https://raw.githubusercontent.com/JovianML/opendatasets/master/data/medical-charges.csv"
# Importing url retrieve method from urllib.request 
from urllib.request import urlretrieve

urlretrieve(acme_url, "acme_dataset.csv")
('acme_dataset.csv', <http.client.HTTPMessage at 0x217c6eeb850>)
# Now creating a Pandas dataframe using the downloaded file
import pandas as pd

acme_data = pd.read_csv("acme_dataset.csv")
acme_data

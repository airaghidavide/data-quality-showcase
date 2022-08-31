from faker.providers import DynamicProvider
from faker import Faker
import random
import pandas as pd
import datetime as dt

def gen_fake_data(sz):

   fake = Faker()

   tipo_carta_provider = DynamicProvider(
     provider_name="tipo_carta",
     elements=["PPSTD", "PPEVO", "PPDIG"]
   )

   fake.add_provider(tipo_carta_provider)

   my_data = []
  
   for i in range(0, sz): 
        my_data.append( [
                           random.randint(0,500),
                           fake.tipo_carta(),
                           fake.credit_card_provider(),
                           fake.credit_card_security_code(),
                           fake.date_between_dates(date_start = dt.date(year=2021, month=5, day=1), date_end = dt.date(year=2022, month=5, day=1)),
                           random.randint(0,2000)
                        ]
       
                       )                    

   df_fake_data = pd.DataFrame(my_data,columns=['id_cliente','tipo_carta','fornitore_carta','secure_code','data_transazione','importo'])
   
   return df_fake_data

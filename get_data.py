import os
import pandas as pd
import sqlalchemy

# Conectando no banco local
str_connection = 'sqlite:///{path}'

Base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Data_dir = os.path.join(Base_dir, 'data')

print('Diretório do projeto:', Base_dir)
print('Diretório dos dados: ', Data_dir)

my_files = []

# Forma 2
files_names = [i for i in os.listdir(Data_dir) if i.endswith('.csv')]

# Abrindo conexão com o banco local
str_connection = str_connection.format(path=os.path.join(Data_dir, 'dataset_final.db'))

for i in files_names:
    df_tmp = pd.read_csv(os.path.join(Data_dir, i))
    db_name = 'fr_' + i.strip('.csv').replace('olist','').replace('_dataset','')
    df_tmp.to_sql(db_name, str_connection)
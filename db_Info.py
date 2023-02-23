# db 정보
import pickle 

db_dict = {'DB_USERNAME' : 'root',
           'DB_PASSWORD' : 'root123',
           'DB_HOST' :'52.78.168.253',
           'DB_PORT' : 59543,
           'DB_DATABASE' : 'cocomong'}

with open('db_dict.pickle','wb') as f :
    pickle.dump(db_dict, f)
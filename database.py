from mongoengine import connect
import config as c


connect('apiSalvador',host=c.CONFIG['url_database'])

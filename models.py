from mongoengine import (Document,EmbeddedDocument)
from mongoengine.fields import (
     StringField,
    PointField
)



class Pontos_Saude(Document):
    meta = {'collection':'pontos_saude' }
    titulo = StringField()
    localizacao = PointField()
    end = StringField()
    tipo = StringField()
    tipo_descricao = StringField()
    ponto_referencia = StringField()
    telefone = StringField()



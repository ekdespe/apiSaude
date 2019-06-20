import graphene
import datetime
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from models import Pontos_Saude as PontosSaudeModel
import database

class Pontos_Saude(MongoengineObjectType):

    class Meta:
        model = PontosSaudeModel
        interfaces = (Node,)




class Query(graphene.ObjectType):
    node = Node.Field()
    pontos_saude = MongoengineConnectionField(Pontos_Saude)
    



    
schema = graphene.Schema(query=Query, types=[Pontos_Saude])

import graphene
from graphql_auth import mutations 
from graphql_auth.schema import UserQuery, MeQuery
from users.models import ExtendUser
from django.contrib.auth.models import User as UserAuth

class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    token_auth = mutations.ObtainJSONWebToken.Field()


    
    


class UserQuery(UserQuery, MeQuery, graphene.ObjectType):
    pass

class UserMutation(AuthMutation, graphene.ObjectType):
    pass



from graphene import Schema
import graphene
from graphene_django import DjangoObjectType

from .models import UserTable


class UserObject(DjangoObjectType):
    class Meta:
        model = UserTable


class Query(graphene.ObjectType):
    user_list = graphene.List(UserObject)

    def resolve_user_list(self, info):
        return UserTable.objects.all()


schema = Schema(query=Query)

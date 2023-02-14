from django.urls import path
from graphene_django.views import GraphQLView
from assignments.schema import schema


urlpatterns = [
    # Only a single URL to access GraphQL
    path("assignments", GraphQLView.as_view(graphiql=True, schema=schema)),
]
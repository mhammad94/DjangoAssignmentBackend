from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from users.schema import schema


urlpatterns = [
    path("auth", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]
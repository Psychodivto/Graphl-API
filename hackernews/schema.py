import graphene
<<<<<<< HEAD
=======
<<<<<<< HEAD
import graphql_jwt

import links.schema
import users.schema


class Query(users.schema.Query, links.schema.Query, graphene.ObjectType):
    pass

class Mutation(users.schema.Mutation, links.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
=======
>>>>>>> master

import links.schema


class Query(links.schema.Query, graphene.ObjectType):
    pass


<<<<<<< HEAD
schema = graphene.Schema(query=Query)
=======
schema = graphene.Schema(query=Query)
>>>>>>> develop
>>>>>>> master

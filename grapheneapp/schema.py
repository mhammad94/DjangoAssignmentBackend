import graphene
from users.schema import UserQuery,UserMutation
from assignments.schema import AssignmentQuery, AssignmentsMutation 
from courses.schema import CoursesMutation, CoursesQuery
from submissions.schema import SubmissionQuery, SubmissionsMutation


class Mutation(UserMutation, AssignmentsMutation, CoursesMutation, SubmissionsMutation):
    pass

class Query(UserQuery, AssignmentQuery, CoursesQuery, SubmissionQuery):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)


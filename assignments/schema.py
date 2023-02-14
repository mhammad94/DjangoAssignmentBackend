import graphene
from graphene_django import DjangoListField, DjangoObjectType
from assignments.models import Assignments
from courses.models import Courses
from users.models import ExtendUser


class AssignmentsType(DjangoObjectType):
    class Meta:
        model = Assignments
        fields =("id", "assignmenttitle", "submitter", "course")

class UserType(DjangoObjectType):
    class Meta:
        model = ExtendUser

class CourseType(DjangoObjectType):
    class Meta:
        model = Courses


class AssignmentQuery(graphene.ObjectType):
    all_assignments = graphene.List(AssignmentsType)
    assignments_by_id = graphene.List(AssignmentsType, id=graphene.Int())
    assignments_by_user = graphene.List(AssignmentsType, userID=graphene.Int())
    assignments_by_course = graphene.List(AssignmentsType, courseID=graphene.Int())


    def resolve_all_assignments(root, info,  **kwargs):
        return Assignments.objects.all()

    def resolve_assignments_by_id(root, info, id):
        return Assignments.objects.filter(id=id)
    
    def resolve_assignments_by_user(root, info, userID):
        return Assignments.objects.filter(submitter=userID)
    
    def resolve_assignments_by_course(root, info, courseID):
        return Assignments.objects.filter(course=courseID)


class CreateAssignment(graphene.Mutation):
    class Arguments:
        assignmenttitle = graphene.String(required=True)
        submitter = graphene.String(required=True)
        course = graphene.String(required=True)
    
    assignment = graphene.Field(AssignmentsType)
    
    @classmethod
    def mutate(cls, root, info, assignmenttitle, submitter, course):
        assignment = Assignments()
        assignment.assignmenttitle = assignmenttitle
        assignment.submitter = submitter
        assignment.course = course
        assignment.save()
        return CreateAssignment(assignment=assignment)


class EditAssignment(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        assignmenttitle = graphene.String(required=True)
        submitter = graphene.String(required=True)
        course = graphene.String(required=True)
    
    assignment = graphene.Field(AssignmentsType)
    
    @classmethod
    def mutate(cls, root, info, assignmenttitle, submitter, course):
        assignment = Assignments.objects.get(id=id)
        assignment.assignmenttitle = assignmenttitle
        assignment.submitter = submitter
        assignment.course = course
        assignment.save()
        return CreateAssignment(assignment=assignment)

class DeleteAssignment(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
    
    assignment = graphene.Field(AssignmentsType)

    @classmethod
    def mutate(cls, root, info, id):
        assignment = Assignments.objects.get(id=id)
        assignment.delete()
        return

class AssignmentsMutation(graphene.ObjectType):
    save_assignment = CreateAssignment.Field()
    edit_assignment = EditAssignment.Field()
    delete_assignment = DeleteAssignment.Field()





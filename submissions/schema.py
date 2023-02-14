import graphene
from graphene_django import DjangoListField, DjangoObjectType
from submissions.models import Submissions
from assignments.models import Assignments
from users.models import ExtendUser

class SubmissionsType(DjangoObjectType):
    class Meta:
        model = Submissions
        fields =("id", "submissiontitle", "submitter", "assignment")

class AssignmentType(DjangoObjectType):
    class Meta:
        model = Assignments

class UserType(DjangoObjectType):
    class Meta:
        model = ExtendUser

class SubmissionQuery(graphene.ObjectType):
    all_submissions = graphene.List(SubmissionsType)
    submission_by_id = graphene.List(SubmissionsType, id=graphene.Int())
    submission_by_assignment = graphene.List(SubmissionsType, assignmentID=graphene.Int())
    submission_by_user = graphene.List(SubmissionsType, userID=graphene.Int())


    def resolve_all_submissions(root, info,  **kwargs):
        return Submissions.objects.all()
        

    def resolve_submission_by_id(root, info, id):
        return Submissions.objects.filter(id=id)
    
    def resolve_submission_by_assignment(root,info,assignmentID):
        return Submissions.objects.filter(assignment=assignmentID)
    
    def resolve_submission_by_user(root, info, userID):
        return Submissions.objects.filter(submitter=userID)

class CreateSubmission(graphene.Mutation):
    class Arguments:
        submissiontitle = graphene.String(required=True)
        submitter = graphene.String(required=True)
        assignment = graphene.String(required=True)
    
    submission = graphene.Field(SubmissionsType)
    
    @classmethod
    def mutate(cls, root, info, submissiontitle, submitter, assignment):
        submission = Submissions()
        submission.submissiontitle = submissiontitle
        submission.submitter = submitter
        submission.assignment = assignment
        submission.save()
        return CreateSubmission(submission=submission)


class EditSubmission(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        submissiontitle = graphene.String(required=True)
        submitter = graphene.String(required=True)
        assignment = graphene.String(required=True)
    
    submission = graphene.Field(SubmissionsType)
    
    @classmethod
    def mutate(cls, root, info, submissiontitle, submitter, assignment,id):
        submission = Submissions.objects.get(id=id)
        submission.submissiontitle = submissiontitle
        submission.submitter = submitter
        submission.assignment = assignment
        submission.save()
        return CreateSubmission(submission=submission)

class DeleteSubmission(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
    
    submission = graphene.Field(SubmissionsType)

    @classmethod
    def mutate(cls, root, info, id):
        submission = Submissions.objects.get(id=id)
        submission.delete()
        return

class SubmissionsMutation(graphene.ObjectType):
    save_submission = CreateSubmission.Field()
    edit_submission = EditSubmission.Field()
    delete_submission = DeleteSubmission.Field()


    
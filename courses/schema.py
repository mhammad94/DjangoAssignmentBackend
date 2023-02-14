import graphene
from graphene_django import DjangoListField, DjangoObjectType
from courses.models import Courses


class CoursesType(DjangoObjectType):
    class Meta:
        model = Courses
        fields = ("id", "coursetitle")



class CoursesQuery(graphene.ObjectType):
    all_courses = graphene.List(CoursesType)
    course_by_id = graphene.List(CoursesType, id=graphene.Int())

    def resolve_all_courses(root, info):
        return Courses.objects.all()
    
    def resolve_course_by_id(root, info, id):
       return Courses.objects.filter(id=id)

class CreateCourse(graphene.Mutation):
    class Arguments:
        course_title = graphene.String(required=True)

    course = graphene.Field(CoursesType)

    @classmethod
    def mutate(cls, root, info, course_title):
        course = Courses()
        course.coursetitle = course_title
        course.save()
        return CreateCourse(course=course)

class EditCourse(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        course_title = graphene.String(required=True)
        
    course = graphene.Field(CoursesType)
    @classmethod
    def mutate(cls, root, info, course_title, id):
        course = Courses.objects.get(id=id)
        course.coursetitle = course_title
        course.save()
        return EditCourse(course=course)

class DeleteCourse(graphene.Mutation):

    class Arguments:
        id = graphene.ID()
    
    course = graphene.Field(CoursesType)

    @classmethod
    def mutate(cls, root, info, id):
        course = Courses.objects.get(id=id)
        course.delete()
        return


class CoursesMutation(graphene.ObjectType):
    save_course = CreateCourse.Field()
    edit_course = EditCourse.Field()
    delete_course = DeleteCourse.Field()


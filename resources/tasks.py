from main import *
from models.taskmodel import Task_model, task_schema, tasks_schema
from flask_jwt_extended import JWTManager,jwt_required,create_access_token,get_jwt_identity

# namespace
ns_tasks = api.namespace("tasks", description="All tasks regarding tasks",)


# models
task_model = api.model(
    "Task", {"title": fields.String(min_length=1), "description": fields.String(min_length=1)}
)



@ns_tasks.route("")
class TasksList(Resource):


    @api.response(200, 'Success')
    @api.doc(security="apikey") #documenting decurity
    @jwt_required
    def get(self):
        """ use this ednpoint to get a list of tasks """
       
      
        return tasks_schema.dump(Task_model.query.filter_by(user_id=get_jwt_identity())), 200



    @api.response(201, 'Success')
    @api.response(400, 'The request was invalid.')
    @api.doc(security="apikey")
    @api.expect(task_model)
    @jwt_required
    def post(self):
        """ use this ednpoint to add new tasks """
        try:
            data = api.payload
            task_to_create = Task_model(
                title=data["title"], description=data["description"],user_id=get_jwt_identity()
            )
            task_to_create.create()
            return task_schema.dump(task_to_create), 201  # created
        except Exception:
            return (
                ({"message": "Check your details and retry again"}),
                400,
            )  # The request was invalid.


@ns_tasks.route("/<int:id>")
class Task(Resource):
    
    @api.response(404, 'Task not found.')
    @api.response(200, 'ok.')

    @api.doc(security="apikey")
    @api.doc(params={'id': 'task id'}) #this add a placeholde to the enter id section in the docmentation
    @jwt_required
    def get(self, id):
        """retrieve a task by it's id"""
        task_to_get = next(
            filter(lambda x: x["id"] == id, tasks_schema.dump(Task_model.query.all())),
            None,
        )
        if task_to_get:
            
            return task_to_get, 200  # ok
        else:
            return ({"message": "Task not found"}), 404  # not found

    @api.expect(task_model)
    @api.doc(security="apikey")
    @api.doc(params={'id': 'An of the task to update'})
    @jwt_required
    def put(self, id):
        """edit a task by it's id"""
        
        data = api.payload
    
        task_to_update = Task_model.query.filter_by(id=id).first()
        
        if task_to_update:
            if u"title" in data:
                task_to_update.title = data["title"]
            if u"description" in data:
                task_to_update.description = data["description"]
            # Task_model.update_task(id=task_to_update.id)
            # print(*task_to_update)
            Task_model.update_task(obj=task_to_update)
            return task_schema.dump(task_to_update), 201  # created

        else:
            return message({"message": "Task not found"}), 404  # not found
    @api.doc(security="apikey")
    @api.doc(params={'id': 'An ID of task to delete'})
    @jwt_required #make sure user is authenticated
    def delete(self, id):
        """use this endpoint to delete a task"""
        # query  tasl_list for that id
        task_to_delete = Task_model.query.filter_by(id=id).first()
        if task_to_delete:
            Task_model.delete_task(id=id)
            return ({"message": "Task deleted"}), 200  # ok
        else:
            return ({"message": "Task not found"}), 404  # not found


from main import db,ma
import datetime

class Task_model(db.Model):
    __tablename__="tasks_table"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def create(self):
        """this method adds to the tasks table"""
        db.session.add(self)
        db.session.commit()

    @classmethod
    def update_task(cls,obj=None):
        """tis method is to update a task"""
        db.session.commit()
        return True

    @classmethod
    def delete_task(cls,id):
        """this method deletes a task"""
        task_to_delete=cls.query.filter_by(id=id)
        if task_to_delete.first():
            task_to_delete.delete()
            db.session.commit()
            return True
        else:
            return False


        
class TaskSchema(ma.Schema):
    class Meta:
        fields = ("id","title","description")


task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)
from marshmallow import Schema, fields


class TaskSchema(Schema):
    id = fields.Str(dump_only=True)
    task_name = fields.Str(required=True)
    list_id = fields.Str(required=True)

class TaskUpdateSchema(Schema):
    task_name = fields.Str()

class ListSchema(Schema):
    id = fields.Str(dump_default=True)
    list_name = fields.Str(required=True)

class UpdateListSchema(Schema):    
    list_name = fields.Str(required=True)    
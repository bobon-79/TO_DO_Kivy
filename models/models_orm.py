"""
This file contains the ORM models for the database.
"""

from __future__ import annotations

from peewee import (
    Model, CharField, TextField, BooleanField, IntegerField, DateTimeField,
    ForeignKeyField, Check, DatabaseProxy
)

db_proxy = DatabaseProxy()  # database proxy object

class BaseModel(Model):
    """
    Base model for all other models.
    """
    class Meta:
        """
        Metaclass for the base model.
        """
        database = db_proxy  # database connection object


class TagModel(BaseModel):
    name = CharField(unique=True, index=True)


    class Meta:
        table_name = "tag"


class TaskModel(BaseModel):
    title = CharField()
    notes = TextField(null=True)

    done = BooleanField(default=False, index=True)
    priority = IntegerField(default=3, constraints=[Check("priority BETWEEN 1 AND 5")], index=True)

    due = DateTimeField(null=True, index=True)
    created = DateTimeField(null=True)
    updated = DateTimeField(null=True)

    class Meta:
        table_name = "task"


class TaskTagModel(BaseModel):
    task = ForeignKeyField(TaskModel, backref="task_tags", on_delete="CASCADE", index=True)
    tag  = ForeignKeyField(TagModel,  backref="tag_tasks",  on_delete="CASCADE", index=True)

    class Meta:
        table_name = "task_tag"
        indexes = (
            (("task", "tag"), True),  # unique index on task and tag
        )

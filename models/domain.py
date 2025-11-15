"""Domain model"""
from __future__ import annotations

from models import dataclass, field
from datetime import datetime, date


@dataclass
class Task:
    """
    Task domain model.\n
    Attributes: id, title, notes, done, priority, due, created, updated.
        id: a unique identifier of the task \n
        title: title of the task \n
        notes: additional notes about the task\n
        done: boolean flag indicating whether the task is done or not\n
        priority: integer value indicating the priority of the task\n
        due: date when the task is due\n
        created: datetime when the task was created\n
        updated: datetime when the task was last updated.\n

    """
    id: int | None
    title: str
    notes: str = field(default_factory=str, repr=False)
    done: bool = field(default_factory=bool, repr=False)
    priority: int = field(default=0, repr=False)
    due: date | None = field(default=None, repr=False)
    created: datetime | None = field(default=None, repr=False)
    updated: datetime | None = field(default=None, repr=False)

    def __post__init(self) -> None:
        self.title = self.title.strip()



@dataclass
class Tag:
    """
    Tag domain model.\n
    Attributes: id, name.
        id: a unique identifier of the tag. \n
        name: name of the tag.\n
        """
    id: int | None
    name: str
    def __post__init(self) -> None:
        self.name = self.name.strip()

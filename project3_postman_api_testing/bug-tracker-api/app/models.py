from datetime import datetime
import random
import uuid

bugs = []

class Bug:
    def __init__(self, created_by, priority, severity, title, description):
        self.bug_id = str(uuid.uuid4())
        self.created_by = created_by
        self.created_on = datetime.utcnow()
        self.updated_on = self.created_on
        self.priority = priority
        self.severity = severity
        self.title = title
        self.description = description
        self.status = "Open"
        self.assigned_to = None
        self.comments = []
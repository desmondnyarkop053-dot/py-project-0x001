School Management CLI

Quick start

Run the interactive CLI (PowerShell):

```powershell
python .\school_manager.py
```

Non-interactive example (use the programmatic API):

```python
from school_manager import SchoolManager
mgr = SchoolManager('data.json')
# create sample data
sid = mgr.add_student('Alice', 14)
tid = mgr.add_teacher('Mr. Smith', 'Math')
cid = mgr.add_course('Algebra', tid)
mgr.enroll(sid, cid)
print(mgr.list_students())
print(mgr.list_courses())
mgr.save()
```

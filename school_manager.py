from dataclasses import dataclass, asdict
import json
from typing import Dict, List, Optional
import os

@dataclass
class Student:
    id: int
    name: str
    age: int

    def to_dict(self):
        return asdict(self)

@dataclass
class Teacher:
    id: int
    name: str
    subject: str

    def to_dict(self):
        return asdict(self)

@dataclass
class Course:
    id: int
    name: str
    teacher_id: Optional[int]
    students: List[int]

    def to_dict(self):
        return asdict(self)

class SchoolManager:
    def __init__(self, filename: str = 'data.json'):
        self.filename = filename
        self.students: Dict[int, Student] = {}
        self.teachers: Dict[int, Teacher] = {}
        self.courses: Dict[int, Course] = {}
        self._next_id = 1
        self.load()

    def _gen_id(self):
        nid = self._next_id
        self._next_id += 1
        return nid

    def add_student(self, name: str, age: int) -> int:
        sid = self._gen_id()
        self.students[sid] = Student(sid, name, age)
        return sid

    def add_teacher(self, name: str, subject: str) -> int:
        tid = self._gen_id()
        self.teachers[tid] = Teacher(tid, name, subject)
        return tid

    def add_course(self, name: str, teacher_id: Optional[int] = None) -> int:
        if teacher_id is not None and teacher_id not in self.teachers:
            raise ValueError('Teacher id not found')
        cid = self._gen_id()
        self.courses[cid] = Course(cid, name, teacher_id, [])
        return cid

    def enroll(self, student_id: int, course_id: int) -> None:
        if student_id not in self.students:
            raise ValueError('Student id not found')
        if course_id not in self.courses:
            raise ValueError('Course id not found')
        course = self.courses[course_id]
        if student_id in course.students:
            return
        course.students.append(student_id)

    def list_students(self) -> List[Dict]:
        return [s.to_dict() for s in self.students.values()]

    def list_teachers(self) -> List[Dict]:
        return [t.to_dict() for t in self.teachers.values()]

    def list_courses(self) -> List[Dict]:
        return [c.to_dict() for c in self.courses.values()]

    def save(self) -> None:
        data = {
            'students': {k: v.to_dict() for k, v in self.students.items()},
            'teachers': {k: v.to_dict() for k, v in self.teachers.items()},
            'courses': {k: v.to_dict() for k, v in self.courses.items()},
            '_next_id': self._next_id,
        }
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)

    def load(self) -> None:
        if not os.path.exists(self.filename):
            return
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except Exception:
            return
        self.students = {int(k): Student(**v) for k, v in data.get('students', {}).items()}
        self.teachers = {int(k): Teacher(**v) for k, v in data.get('teachers', {}).items()}
        self.courses = {int(k): Course(**v) for k, v in data.get('courses', {}).items()}
        self._next_id = data.get('_next_id', max(list(self.students.keys()) + list(self.teachers.keys()) + list(self.courses.keys()) + [0]) + 1)


def _prompt_int(msg: str) -> int:
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print('Please enter a valid integer.')


def run_cli():
    mgr = SchoolManager()
    while True:
        print('\nSchool Management')
        print('1) Add student')
        print('2) Add teacher')
        print('3) Add course')
        print('4) Enroll student in course')
        print('5) List students')
        print('6) List teachers')
        print('7) List courses')
        print('8) Save')
        print('9) Exit')
        choice = input('Choose an option: ').strip()
        if choice == '1':
            name = input('Student name: ').strip()
            age = _prompt_int('Age: ')
            sid = mgr.add_student(name, age)
            print(f'Added student id {sid}')
        elif choice == '2':
            name = input('Teacher name: ').strip()
            subject = input('Subject: ').strip()
            tid = mgr.add_teacher(name, subject)
            print(f'Added teacher id {tid}')
        elif choice == '3':
            name = input('Course name: ').strip()
            tid_input = input('Teacher id (or leave blank): ').strip()
            tid = int(tid_input) if tid_input else None
            try:
                cid = mgr.add_course(name, tid)
                print(f'Added course id {cid}')
            except ValueError as e:
                print('Error:', e)
        elif choice == '4':
            sid = _prompt_int('Student id: ')
            cid = _prompt_int('Course id: ')
            try:
                mgr.enroll(sid, cid)
                print('Enrolled successfully')
            except ValueError as e:
                print('Error:', e)
        elif choice == '5':
            for s in mgr.list_students():
                print(s)
        elif choice == '6':
            for t in mgr.list_teachers():
                print(t)
        elif choice == '7':
            for c in mgr.list_courses():
                print(c)
        elif choice == '8':
            mgr.save()
            print('Saved to', mgr.filename)
        elif choice == '9':
            mgr.save()
            print('Bye')
            break
        else:
            print('Unknown option')


if __name__ == '__main__':
    run_cli()

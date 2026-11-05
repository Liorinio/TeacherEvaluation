import os
from datetime import datetime
from sqlalchemy import DateTime, create_engine, ForeignKey
from sqlalchemy import String, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine = create_engine(os.environ["DATABASE_URL"])
connection = engine.connect()


class Base(DeclarativeBase):
    pass

class Student(Base):
    __tablename__ = "students"

    student_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    student_name: Mapped[str] = mapped_column(String, nullable=False)
    grade_level: Mapped[str] = mapped_column(String, nullable=False)
    enroll_date: Mapped[datetime] = mapped_column(DateTime, nullable=True)


class Subject(Base):
    __tablename__ = "subjects"

    subject_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    subject_name: Mapped[str] = mapped_column(String, nullable=False)


class Exam(Base):
    __tablename__ = "exams"

    exam_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    subject_id: Mapped[int] = mapped_column(Integer, ForeignKey("subjects.subject_id"), nullable=False)
    title: Mapped[str] = mapped_column(String, nullable=False)
    date: Mapped[datetime] = mapped_column(DateTime, nullable=False)

class Grade(Base):
    __tablename__ = "grades"

    student_id: Mapped[int] = mapped_column(Integer, ForeignKey("students.student_id"), nullable=False)
    exam_id: Mapped[int] = mapped_column(Integer, ForeignKey("exams.exam_id"), nullable=False)
    comments: Mapped[int] = mapped_column(String, nullable=False)
    score: Mapped[int] = mapped_column(Integer, nullable=False)
    test_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)

Base.metadata.create_all(engine)

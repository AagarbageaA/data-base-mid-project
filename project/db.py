"""
MongoDB database operations for Course Management System.
Collection: courses
"""

from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from bson import ObjectId
from typing import List, Dict, Optional

# MongoDB connection
client = MongoClient("mongodb://localhost:27017")
db = client["courseDB"]

# Collections
courses = db["courses"]

# Ensure indexes
courses.create_index({ "level.name": 1 })
courses.create_index({ "level.CEFR": 1 })
courses.create_index({ "series": 1 })
courses.create_index({ "name.full": "text", "summary": "text" })

def add_course(course_id: int, full_name: str, short_name: str, summary: str,
               cat_id: int, cat_name: str, cat_path: str, cat_path_names: str, top_cat: str,
               level_id: str, level_name: str, cefr: str, series: str):
    """Add a new course."""
    doc = {
        "_id": course_id,
        "name": {
            "full": full_name,
            "short": short_name
        },
        "summary": summary,
        "category": {
            "id": cat_id,
            "name": cat_name,
            "path": cat_path,
            "path_names": cat_path_names,
            "top_category": top_cat
        },
        "level": {
            "id": level_id,
            "name": level_name,
            "CEFR": cefr
        },
        "series": series,
        "created_at": {"$date": "auto"},
        "updated_at": {"$date": "auto"}
    }
    try:
        result = courses.insert_one(doc)
        return str(result.inserted_id)
    except DuplicateKeyError:
        raise ValueError(f"Course with ID {course_id} already exists")

def get_course(course_id: int):
    """Get a course by ID."""
    return courses.find_one({"_id": course_id})

def get_all_courses():
    """Get all courses."""
    return list(courses.find())

def update_course(course_id: int, updates: dict):
    """Update a course."""
    updates["updated_at"] = {"$date": "auto"}
    result = courses.update_one({"_id": course_id}, {"$set": updates})
    return result.modified_count > 0

def delete_course(course_id: int):
    """Delete a course."""
    result = courses.delete_one({"_id": course_id})
    return result.deleted_count > 0

def filter_courses(level_name: str = None, cefr: str = None, series: str = None):
    """Filter courses by level, CEFR, or series."""
    query = {}
    if level_name and level_name != '':
        query["level.name"] = level_name
    if cefr and cefr != '':
        query["level.CEFR"] = cefr
    if series and series != '':
        query["series"] = series
    return list(courses.find(query))

def search_courses(search_text: str):
    """Fuzzy search by course name or summary using regex for Chinese text support."""
    return list(courses.find({
        "$or": [
            {"name.full": {"$regex": search_text, "$options": "i"}},
            {"summary": {"$regex": search_text, "$options": "i"}}
        ]
    }))

def get_distinct_values(field: str):
    """Get distinct values for a field."""
    return courses.distinct(field)
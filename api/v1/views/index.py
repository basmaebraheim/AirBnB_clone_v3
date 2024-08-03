#!/usr/bin/python3
"""start flask api"""

from api.v1.views import app_views
from flask import jsonify
from models import storage


classes = {"Amenity": "Amenity", "BaseModel": "BaseModel", "City": "City",
           "Place": "Place", "Review": "Review", "State": "State", "User": "User"}


@app_views.route('/status', strict_slashes=False)
def status():
    """return status"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def stats():
    """retrieves the number of each objects by type"""
    stats_counts = {}
    for key, value in classes.items():
        stats_counts[key] = storage.count(value)
    return jsonify(stats_counts)


if __name__ == "__main__":
    pass

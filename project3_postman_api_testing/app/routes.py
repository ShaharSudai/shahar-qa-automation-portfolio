from flask import Flask, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import app
from models import bugs, Bug
from datetime import datetime, timedelta
import random

request_counter = 0

def _get_bug_dict(bug):
    bug_info = {
        'bug_id': bug.bug_id,
        'created_by': bug.created_by,
        'created_on': bug.created_on.strftime('%Y-%m-%d %H:%M:%S'),
        'updated_on': bug.updated_on.strftime('%Y-%m-%d %H:%M:%S'),
        'priority': bug.priority,
        'severity': bug.severity,
        'title': bug.title,
        'description': bug.description
    }

    return bug_info

@app.route('/', methods=['GET'])
def welcome():
    return "Welcome to the Bug Tracking API"

@app.route('/bugs', methods=['GET'])
def get_bugs():

    bug_list = []

    for bug in bugs:
        bug_list.append(_get_bug_dict(bug))

    return jsonify(bug_list), 200

@app.route('/bugs/<string:bug_id>', methods=['GET'])
def get_bug(bug_id):
    bug = next((b for b in bugs if b.bug_id == bug_id), None)

    if bug:
        return jsonify(_get_bug_dict(bug)), 200
    else:
        return jsonify({'error': 'Bug not found'}), 404

@app.route('/bugs', methods=['POST'])
@jwt_required()
def create_bug():
    data = request.json

    new_bug = Bug(
        data['created_by'],
        data['priority'],
        data['severity'],
        data['title'],
        data['description']
    )
    bugs.append(new_bug)

    return jsonify(_get_bug_dict(new_bug)), 201

@app.route('/bugs/<string:bug_id>', methods=['PUT'])
@jwt_required()
def update_bug(bug_id):
    bug = next((b for b in bugs if b.bug_id == bug_id), None)
    if not bug:
        return jsonify({'error': 'Bug not found'}), 404

    data = request.json
    bug.created_by = data.get('created_by', bug.created_by)
    bug.priority = data.get('priority', bug.priority)
    bug.severity = data.get('severity', bug.severity)
    bug.title = data.get('title', bug.title)
    bug.description = data.get('description', bug.description)
    bug.updated_on = datetime.utcnow()

    return jsonify(_get_bug_dict(bug)), 200

@app.route('/bugs/<string:bug_id>', methods=['DELETE'])
@jwt_required()
def delete_bug(bug_id):
    bug = next((b for b in bugs if b.bug_id == bug_id), None)
    if not bug:
        return jsonify({'error': 'Bug not found'}), 404

    deleted_bug_id = bug.bug_id
    bugs.remove(bug)

    deleted_bug = {
        'message': 'Bug deleted',
        'bug_id': deleted_bug_id
    }

    return jsonify(deleted_bug), 200

@app.route('/bugs/<string:bug_id>/status', methods=['PUT'])
@jwt_required()
def update_status(bug_id):
    bug = next((b for b in bugs if b.bug_id == bug_id), None)
    if not bug:
        return jsonify({"error": "Bug not found"}), 404

    data = request.get_json()
    new_status = data.get("status")
    valid_statuses = ["Open", "In Progress", "Resolved", "Closed"]

    if new_status not in valid_statuses:
        return jsonify({"error": "Invalid status"}), 400

    bug.status = new_status
    bug.updated_on = datetime.utcnow()
    return jsonify({"message": f"Status updated to {new_status}"}), 200


@app.route('/bugs/<string:bug_id>/comment', methods=['POST'])
@jwt_required()
def add_comment(bug_id):
    bug = next((b for b in bugs if b.bug_id == bug_id), None)
    if not bug:
        return jsonify({"error": "Bug not found"}), 404

    data = request.get_json()
    comment = data.get("comment")
    if not comment:
        return jsonify({"error": "Missing comment"}), 400

    user = get_jwt_identity()["user"]
    bug.comments.append({"author": user, "comment": comment, "time": datetime.utcnow().isoformat()})
    bug.updated_on = datetime.utcnow()
    return jsonify({"message": "Comment added"}), 201
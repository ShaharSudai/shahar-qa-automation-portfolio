# Bug Tracker API – Postman Test Suite

This project is part of **Shahar Sudai’s QA Automation Portfolio**.  
It demonstrates REST API testing using **Postman** for a functional **Bug Tracking API** built with Flask.

The API supports CRUD operations, business logic (status flow, comments), and Swagger documentation.  
The purpose of this collection is to validate both **functional** and **negative** scenarios in a clear, reproducible way.

---

## Overview

**Technology Stack:**
- Python + Flask (backend)
- Flasgger (Swagger UI)
- Postman (manual & automated API validation)

**Main Features:**
- Full CRUD functionality for bugs
- Commenting and status flow (Open → In Progress → Resolved → Closed)
- Field validation and error handling
- Detailed Swagger documentation for all endpoints

---

## Test Scenarios

### **Sanity**
1. **Server Running**  
   - Validates that the server responds with status `200` and message `"API is live"`.

---

### **Bugs CRUD**
2. **Create Bug – Valid Data**  
   - Sends a valid JSON body to create a new bug.  
   - Expects `201 Created` and verifies `bug_id` and `title`.  
   - Stores the created ID for subsequent tests.

3. **Get All Bugs**  
   - Verifies that a list of bugs is returned (`status 200`).  
   - Checks that the count matches the expected number and that the created bug exists.

4. **Get Bug by ID**  
   - Retrieves a specific bug using `{{bug_id}}`.  
   - Validates title, severity, and comments array.  
   - Tests invalid ID → expects `404 Not Found`.

5. **Update Bug**  
   - Updates bug fields (`title`, `priority`, etc.).  
   - Verifies the updated values persist in the next GET request.  
   - Attempts to update non-existing bug → expects `404`.

6. **Delete Bug**  
   - Deletes a bug and expects `"Bug deleted"` with `200`.  
   - Tries deleting the same bug again → expects `404`.

---

### **Business Logic**
7. **Update Status Flow**  
   - Changes bug status through stages (`Open → In Progress → Resolved → Closed`).  
   - Verifies `"Status updated to..."` response each time.  
   - Invalid status value → expects `400 Bad Request`.

8. **Add Comments**  
   - Adds multiple comments to an existing bug.  
   - Validates `201 Created` and ensures comments are saved.  
   - Missing comment field → expects `400`.

9. **Filter Bugs by Status**  
   - Sends `GET /bugs?status=Resolved`.  
   - Verifies only resolved bugs are returned.

---

### **Negative Tests**
10. **Create Bug – Missing Title**  
    - Omits `title` from body.  
    - Expects `400 Bad Request` with `"Missing required field: title"`.

11. **Create Bug – Missing Description**  
    - Omits `description` from body.  
    - Expects `400 Bad Request` with `"Missing required field: description"`.

12. **Add Comment – Missing comment field**  
    - Sends JSON without `comment`.  
    - Expects `400` and `"Missing comment"` message.

13. **Update Non-Existing Bug**  
    - Attempts to update a random ID → expects `404`.

14. **Delete Non-Existing Bug**  
    - Attempts to delete a bug that doesn’t exist → expects `404`.

---

### **Validation Tests**
15. **Bug Has Exactly 2 Comments**  
    - Fetches a bug known to have two comments.  
    - Asserts that `comments.length === 2`.  
    - Optionally verifies comment author names.

16. **Response Time Validation**  
    - Ensures each request completes in under `1000ms`.

17. **Response Schema Validation** *(optional)*  
    - Validates JSON structure for required fields (e.g., `bug_id`, `title`, `severity`, `status`).

---

## How to Run Tests

1. Make sure the Flask app is running:
   ```bash
   python app/app.py

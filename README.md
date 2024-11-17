Testing the Endpoints

Use Postman, curl, or a similar tool to test the endpoints:

    GET /api/users/: Fetch all users.

    
    POST /api/users/create/: Create a new user.
    {
        "username": "testuser",
        "password": "password123",
        "active": true
    }

    GET /api/users/<id>/: Fetch a user by ID.

    PUT /api/users/update/<id>/: Update a user by ID.
    
    DELETE /api/users/delete/<id>/: Delete a user by ID.

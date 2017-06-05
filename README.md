## Listing team members

Request Method: GET

URL: http://127.0.0.1:8000/users/

## Adding a team member

Request Method: POST

URL: http://127.0.0.1:8000/users/

{
    "first_name": "John",
    "last_name": "Smith",
    "email": "john@abc.com",
    "phone": "6462662840",
    "role": "regular"
}

## Editing a team member
Request Method: PATCH

URL: http://127.0.0.1:8000/users/2/

{
    "id": 2,
    "email": "john@xyz.com"

}

## Deleting a team member
Request Method: DELETE

URL: http://127.0.0.1:8000/users/<user_id>/

URL Example: http://127.0.0.1:8000/users/2/

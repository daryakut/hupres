from app import UserSignupResponse, user_signup, UserSignupRequest

from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_read_item():
    item_id = 1
    response = client.get(f"/items/{item_id}")

    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "name": "Item Name"}


class UserTester:

    def signup(self, email_address: str) -> UserSignupResponse:
        return user_signup(UserSignupRequest(email_address=email_address))

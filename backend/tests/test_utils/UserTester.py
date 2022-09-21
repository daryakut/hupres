from __future__ import annotations

from app import user_signup, UserSignupRequest

from quiz_algorithm.models import User


# client = TestClient(app)
#
# def test_read_item():
#     item_id = 1
#     response = client.get(f"/items/{item_id}")
#
#     assert response.status_code == 200
#     assert response.json() == {"item_id": 1, "name": "Item Name"}


class UserTester:
    user: User

    def __init__(self, user: User):
        self.user = user

    @staticmethod
    async def signup(email_address: str = "georgii@hupres.com") -> UserTester:
        response = await user_signup(UserSignupRequest(email_address=email_address))
        return UserTester(response.user)

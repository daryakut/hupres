from __future__ import annotations

from quiz_algorithm.models import User
from tests.users.google_oauth import get_test_google_oauth_service
from tests.users.sessions import get_test_session_data_provider
from users.users_api import google_auth, get_current_user_response


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
    # async def signup(email_address: str = "georgii@hupres.com") -> UserTester:
    async def login_with_google(email_address: str = "georgii@hupres.com"):
        get_test_google_oauth_service().email_address_to_return = email_address
        response = await google_auth(None)
        user_token = response['user_token']
        get_test_session_data_provider().update_current_session(user_token)
        print('response', response)
        response = await get_current_user_response()
        #
        # response = await user_signup(UserSignupRequest(email_address=email_address))
        return UserTester(response.user)

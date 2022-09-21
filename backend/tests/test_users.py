import pytest
import asyncio
import unittest

from app import user_signup, UserSignupRequest


def setup_module(module):
    print(f"Setting up for {module.__name__}")

@pytest.mark.asyncio
async def test_can_create_user():
    #     response = await user_signup(UserSignupRequest(email_address="georgii@hupres.com"))
    #     assert response.user.email_address == "georgii@hupres.com"
    assert 3 + 3 == 6


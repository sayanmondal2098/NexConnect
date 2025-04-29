
import sys 
import os
from dotenv import load_dotenv
# Get the absolute path to the root directory (one level up from current file)
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(root_dir)


from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
import httpx
from fastapi import Request
from sqlalchemy.orm import Session
from core.database import get_db
from models.github_token import GitHubToken
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# GitHub OAuth credentials
GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")
GITHUB_API_URL = "https://api.github.com/user"
GITHUB_AUTH_URL = "https://github.com/login/oauth/authorize"
GITHUB_TOKEN_URL = "https://github.com/login/oauth/access_token"

github_router = APIRouter()

# Step 1: Redirect to GitHub for authentication
@github_router.get("/")
async def github_login():
    print("Redirecting to GitHub for authentication...")
    print(f"GITHUB_CLIENT_ID: {GITHUB_CLIENT_ID}")
    print(f"GITHUB_AUTH_URL: {GITHUB_AUTH_URL}")
    redirect_uri = f"http://localhost:8000/auth/github/callback"
    github_url = f"{GITHUB_AUTH_URL}?client_id={GITHUB_CLIENT_ID}&redirect_uri={redirect_uri}"
    print(f"Redirecting to: {github_url}")
    return RedirectResponse(github_url)


# Step 2: GitHub redirects back to our app with a code
@github_router.get("/callback")
async def github_callback(code: str, db: Session = Depends(get_db)):
    """
    Handle the callback from GitHub after the user grants permissions.
    The GitHub service sends a code, which we exchange for an access token.
    """
    # Step 3: Exchange the code for an access token
    async with httpx.AsyncClient() as client:
        response = await client.post(
            GITHUB_TOKEN_URL,
            params={
                "client_id": GITHUB_CLIENT_ID,
                "client_secret": GITHUB_CLIENT_SECRET,
                "code": code,
            },
            headers={"Accept": "application/json"},
        )

    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="GitHub authentication failed")

    # Extract the access token from the response
    token_data = response.json()
    print(token_data)
    access_token = token_data.get("access_token")
    if not access_token:
        raise HTTPException(status_code=400, detail="Access token missing")

    # Step 4: Store the token in the database
    github_token = GitHubToken(
        access_token=access_token,
        scope=token_data.get("scope"),
        token_type=token_data.get("token_type")
    )
    db.add(github_token)
    db.commit()
    db.refresh(github_token)

    # Step 5: Fetch user data from GitHub API
    async with httpx.AsyncClient() as client:
        # Fetch user profile information
        user_response = await client.get(
            GITHUB_API_URL,
            headers={"Authorization": f"Bearer {access_token}"},
        )

        if user_response.status_code != 200:
            raise HTTPException(status_code=400, detail="Failed to fetch GitHub user data")
        
        user_data = user_response.json()

        # Fetch user repositories information
        repos_response = await client.get(
            f"{GITHUB_API_URL}/repos",  # Fetch user repositories
            headers={"Authorization": f"Bearer {access_token}"},
        )

        if repos_response.status_code != 200:
            raise HTTPException(status_code=400, detail="Failed to fetch GitHub repositories")

        repos_data = repos_response.json()

    # Return both user profile and repository data
    return {
        "msg": "GitHub login successful",
        "user_data": user_data,
        "repositories": repos_data,  # Include the repositories data
    }
# 1. What is Authentication and Authorization?

# 1. Authentication = "Who are you?"

It is the process of verifying the identity of the user.


Example:

When a user provides an API key or token, we check if it's valid.

If yes → authenticated.

If no → request is blocked.

# 2. Authorization = "Are you allowed to do this?"

After verifying the user, authorization determines what they can access.

Example:

Admin can access /upload and /delete.

Normal user can only access /view.

# 3. Middleware = Gatekeeper for every request

Middleware is a piece of code that runs before your route and can:

	* Check for authentication

	* Validate tokens/API keys

	* Reject unauthorized users


# 2. Types of Authentication Methods

# 1. API Key Authentication :

How It Works?

A unique key is generated and assigned to the client (user or app).

The client sends this API key with each request.

The server verifies the key and grants access.

Example (Using API Key in Header)

GET /data HTTP/1.1

Host: myapp.com

Authorization: Api-Key 123456789abcdef

Example (Using API Key in Query Parameter - Not Recommended)

GET https://example.com/data?api-key=123456789abcdef

# 2. JWT (JSON Web Token) Authentication

This token consists of three parts: 

1) header

* Header (Metadata)

{
  "alg": "HS256",
  "typ": "JWT"
}


2) payload

* Payload (User information)

{
  "user-id": 123,
  "role": "admin",
  "iat": 1691855200,  
  "exp": 1691858800
}

3) signature

The Signature Component in JWT : 

The signature in a JSON Web Token (JWT) ensures data integrity and authenticity—meaning:

 * The token has not been tampered/changed with after it was created.
 
 * The token was issued by a trusted source (i.e., a server that holds the secret signing key).

A JWT looks like this:

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiIxMjMiLCJuYW1lIjoiSm9obiBEb2UifQ.s5aZ

# 3. OAuth 2.0 Authentication

How It Works?

* OAuth 2.0 is an authorization framework that allows     access without sharing credentials.

* It is a token based authentication system.

* It issues an Access Token instead of a password.

* Tokens have an expiry time for better security.

Steps Involved:

1. User logs in → API sends Authorization Code.

2. The app exchanges this code for an Access Token.

3. The client includes the Access Token in API requests.

4. API verifies the token and grants access.

# 3. Comparing API Key vs JWT vs OAuth

| Method |Best For | Security | Ease of Use|
|--------|---------|----------|------------|
|API Key | Server-to-server | Low | Easy |
|OAuth 2.0 | Third-party login (Google, Facebook) | High | Complex |
|JWT | Web & mobile apps | High | Moderate

# 4. When to Use Which Method?

Recommended:

- Public APIs   → API Key or OAuth 2.0

- Secure APIs  → OAuth 2.0 or JWT










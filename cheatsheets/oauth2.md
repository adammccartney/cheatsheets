# oauth2 

+ standard [rfc6749](https://datatracker.ietf.org/doc/html/rfc6749)

## Four Roles

1. resource owner (possibly an end user)
2. resource server (houses resource and has oauth enabled)
3. client (application making requests for protected resources on behalf of the
   resource owner and with its authorization)
4. authorization server (issues a token to the client after authenticating 
   the resource owner


## Authorization Code Grant

An oauth client can get a token from the authorization server after it has been
delegated authority by a resource owner.

```
4.1.  Authorization Code Grant

   The authorization code grant type is used to obtain both access
   tokens and refresh tokens and is optimized for confidential clients.
   Since this is a redirection-based flow, the client must be capable of
   interacting with the resource owner's user-agent (typically a web
   browser) and capable of receiving incoming requests (via redirection)
   from the authorization server.

     +----------+
     | Resource |
     |   Owner  |
     |          |
     +----------+
          ^
          |
         (B)
     +----|-----+          Client Identifier      +---------------+
     |         -+----(A)-- & Redirection URI ---->|               |
     |  User-   |                                 | Authorization |
     |  Agent  -+----(B)-- User authenticates --->|     Server    |
     |          |                                 |               |
     |         -+----(C)-- Authorization Code ---<|               |
     +-|----|---+                                 +---------------+
       |    |                                         ^      v
      (A)  (C)                                        |      |
       |    |                                         |      |
       ^    v                                         |      |
     +---------+                                      |      |
     |         |>---(D)-- Authorization Code ---------'      |
     |  Client |          & Redirection URI                  |
     |         |                                             |
     |         |<---(E)----- Access Token -------------------'
     +---------+       (w/ Optional Refresh Token)

   Note: The lines illustrating steps (A), (B), and (C) are broken into
   two parts as they pass through the user-agent.

                     Figure 3: Authorization Code Flow

```

### implementation notes

+ From within in client, we typically want to implement some sort of a redirect
  function that directs the user to the authorization server.


## creating a protected resource

there are three methods for passing a token: [rfc6750](https://datatracker.ietf.org/doc/html/rfc6750)
+ Authorization Request Header Field
+ Form-Encoded Body Parameter
+ URI Query Parameter (this SHOULD NOT be used unless the previous two are
  impossible)


## Leveraging oauth scope mechanism

This lets you create tailor made access for resources that are not simply
behind a wall guarding a bunch of static assets.


## Authorization Server

Required to have two endpoints: authorization endpoint for front-channel
interactions and the token endpoint which serves back-channel interactions.

Authorization form is not part of the oauth2 protocol, nevertheless it appears
in many authorization servers and is a common pattern.


1. process the request, validate the client, and send the user to the approval
   page
2. process the results of the approval page, authorize the client
3. process the request, issue and access token


### Notes:

Upon receiving an authorization request, the server checks to see if the client
exists. If it does, the first step it takes is to generate the code -> this
code needs to be stored somewhere on the server so that it can be accessed
later (typically written to the database)


# oauth2 in the real world

## grant types

### implicit
+ uses front-channel only
+ typical for browser clients in javascript
+ no refresh token
+ no authentication

### client credentials
+ no explicit resource owner / client and resource owner are same
+ uses back-channel only
+ again no refresh (client can request new token at any time)


### resource owner credentials

+ resource owner has username/password at authorization server, client prompts
  the user for these and sends them over the wire (A BAD IDEA!)
+ antipattern
+ don't do this in real life

### Assertion grant types
+ two existing formats (SAML, JWT)
+ uses back-channel exclusively


# client security

## common mistakes

+ use oauth as an authentication protocol without taking any extra precautions.

### CSRF attack against the client

cross-site request forgery

[Detailed info on csrf attacks](https://owasp.org/www-community/attacks/csrf)


# Protected Resource Server Security

Formatting the responses correctly is a better mode of protection than simply
ensuring the strings themselves are properly sanatized. i.e. the protected
resource server should be returning explicit json.


There are two useful headers that we can include with the response:
```
res.setHeader('X-Content-Type-Options', 'nosniff');
res.setHeader('X-XSS-Protection', '1; mode=block');
```

# authorization server vurnerabilities

## Session hijacking
If the authorization server does not explicitly disallow reuse of authorization
codes, it becomes possible for an attacker to gain access to another user's
protected resource by accessing the shared browser history on the computer where the
previous authorization code has been stored.

# JSON Web Tokens (JWT)

Token will contain a header and a claims set.


| claim name  |        Claim Description                                     |
|-------------|--------------------------------------------------------------|
| iss         | issues of token. This is often the authorization server.     |
|             | claim is a single string. *who created the token*            |
| sub         | The subject of the token. *who the token is about*, often    |
|             | a uuid for the resource owner. Mostly, subject needs to be   |
|             | unique only in within the scope of the issuer.               |
| aud         | Audience of the token. *who is suppposed to accept the token*|
|             | often includes the URI of the protected resource. This can be| 
|             | a string or array of strings                                 | 
| exp         | The expiration timestamp. *when the token will expire*       |
|             | int num secs since UNIX Epoch.                               |
| nbf         | *not-before-timestamp* - indicator of *when the token will*  |
|             | *begin to be valid*.                                         |
| iat         | *issued-at-timestamp* - indicates *when it was created*      |
| jti         | *unique identifier* of the token                             | 
|             | this is *unique to each token created by the issuer* often   |
|             | cryptographically random to prevent collisions. Useful for   |
|             | preventing token guessing and replay attacks by adding a     |
|             | component of randomized entropy to the structured token that |
|             | would not be available to the attacker.                      |





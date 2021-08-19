# General  tour 
## About

Before run project there is steps must achieve and this is General tour 

- **Point 1** : Applications
- **Point 2** : API
- **Point 3** : Role
- **Point 4** : About fronted side
- **Point 5** : About backend side
- **Point 6** : Token result

# P**oint 1** : Applications

Create  a new [Auth0.com](http://auth0.com)  account and a new single page web application 

![Auth1](https://user-images.githubusercontent.com/85417706/130055619-c3c16877-e18f-48c7-af71-a045267e9a4a.png)


From Settings there is a unique Domain [`coffee-shop3.us.auth0.com`](http://coffee-shop3.us.auth0.com/) 

![Auth2](https://user-images.githubusercontent.com/85417706/130055757-265e3596-8b58-4974-962c-98231175eb55.png)

Allowed Callback URLs `http:localhost8100/tabs/user-page`

![Auth3](https://user-images.githubusercontent.com/85417706/130055803-15d3d716-3154-4972-b685-3a8b8875f125.png)


## P**oint 2** : API

Create API called `drinks`

![Auth4](https://user-images.githubusercontent.com/85417706/130055901-afb2c3a8-7198-482a-bbcd-b91239cdc59d.png)

Create new API permissions:

- `get:drinks`
- `get:drinks-detalil`
- `post:drinks`
- `pactch:drinks`
- `delete:drinks`

![Auth5](https://user-images.githubusercontent.com/85417706/130055972-7eb72475-824e-4130-be36-abb8702a9071.png)

## P**oint 3** : Role

From Role create Manger and Barista 

Barista can 

- `get:drinks-detalil`

Manger can  

- `get:drinks`
- `get:drinks-detalil`
- `post:drinks`
- `pactch:drinks`
- `delete:drinks`

![Auth6](https://user-images.githubusercontent.com/85417706/130056023-92816157-64e1-486a-9063-39844e5dbf82.png)

# **Point 4** : About fronted side

After see  `[./frontend/](notion://www.notion.so/samapower/frontend/README.md)`  and run `npm install` , `ionic serve`

- go to   `/frontend/src/environments/environment.ts` and Update values

this is my value :  

```jsx
export const environment = {
  production: false,
  apiServerUrl: 'http://127.0.0.1:5000', // the running FLASK api server url
  auth0: {
    url: 'coffee-shop3.us', // the auth0 domain prefix
    audience: 'drinks', // the audience set for the auth0 app
    clientId: 'KZ0Jb0Y0EvRa1hAfEtFPiPdO0CWIHlT8', // the client id generated for the auth0 app
    callbackURL: 'http://localhost:8100', // the base url of the running ionic application. 
  }
};
```

# Point 5 : About backend side

 in `./src/auth/auth.py`` Update values 

this is my value :

```python
AUTH0_DOMAIN = 'coffee-shop3.us.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'drinks'
```

# Token result

 After run project successfully and test endpoint with [Postman](https://getpostman.com/)

- Register 2 users - assign the Barista role to one and Manager role to the other.
- Sign into each account and make note of the JWT.
- After Token generated  go to [jwt.io](http://jwt.io) to validate Token

### **Barista Account** 

![jwtB](https://user-images.githubusercontent.com/85417706/130056077-0fa7b226-e468-45f4-82cd-56f46f0df964.png)

### **Manger Account** 

![JWTm](https://user-images.githubusercontent.com/85417706/130056138-2eeebb4c-eb21-4580-acf4-06a413e6529d.png)

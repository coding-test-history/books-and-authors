
## Tech Stack

**Server:** FastAPI |  Python 3, MySQL | PostgreSQL | SQlite, sqlalchemy, alembic
## Features

 - Login
 - User Registration
 - Logout
 - User Management including (User, Role, Dynamic Nested Menu, Permission)
 - Audit Trail including (ID user, Username, Menu Activity, Method Activity, Time Activity, Create detail layout for add and update activity)
## Installation
<!-- install composer
```bash
  composer install
```
db config on env    
```bash
  DB_HOST="" 
  DB_PORT= #3306 for mysql, 5432 for PostgreSQL
  DB_DATABASE=""
  DB_USERNAME=""
  DB_PASSWORD=""
  DB_CONNECTION= #input mysql for mysql and input pgsql for PostgreSQL
```
input your jwt secret key
```bash
  JWT_SECRET_KEY= 
``` -->
## Account

- Username : user1 / user2 / user3
- Password : password

## API Reference
<!-- 
#### Login
```http
  POST /api/auth/login
```

#### Get customer list
```http
  GET /api/customer/data
```

#### Get customer detail
```http
  GET /api/customer/get/{id}
```

#### Update customer data
```http
  PUT /api/customer/update/{id}
```

#### Delete customer data
```http
  DELETE /api/customer/delete/{id}
```

#### Get order list
```http
  GET /api/order/data
```

#### Get detail order
```http
  GET /api/order/get/{id}
```

#### Update order data
```http
  PUT /api/order/update/{id}
```

#### Delete order data
```http
  DELETE /api/order/delete/{id}
```
# FastApi with MongoDB y JWT!

I want to share this simple example of how we can use FastApi to connect with MongoDB and add security to our endpoints with the help of JWT. As a virtual environment I am using [Poetry](https://python-poetry.org/)

## Packages
For this project I have used the following packages

 - Fastapi
 - Uvicorn
 - PyMongo
 - PyJwt
 - Dotenv

## Environment Variables
To run the project you need to configure the following environment variables

    MONGO_HOST=localhost  
    MONGO_PORT=27017  
    MONGO_USER=root  
    MONGO_PASSWORD=mongotest  
      
    ACCESS_TOKEN_EXPIRE_MINUTES=30  
    SECRET_TOKEN=secret  
    ALGORITHM_TOKEN=HS256

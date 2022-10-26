from fastapi import Request, status
from fastapi.responses import JSONResponse
from functions.jwt import validate_token
from fastapi.routing import APIRoute


class VerifyTokenRoute(APIRoute):
    def get_route_handler(self):
        original_route = super().get_route_handler()

        async def verify_token_middleware(request: Request):

            if request.headers.__contains__("Authorization"):
                token = request.headers["Authorization"].split(" ")[1]

                validation_response = validate_token(token, output=False)
                if validation_response == None:
                    return await original_route(request)
                else:
                    return validation_response
            else:
                return JSONResponse(content={"message": "Access denied"}, status_code=status.HTTP_401_UNAUTHORIZED)

        return verify_token_middleware

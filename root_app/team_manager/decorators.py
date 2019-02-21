from rest_framework.response import Response
from rest_framework.views import status
from validate_email import validate_email


def validate_request_contact_data(fn):
    def decorated(*args, **kwargs):
        # args[0] == GenericView Object
        #print(args[0].request.data.get("id", ""),"dec")
        pk = args[0].request.data.get("id", None)
        first_name = args[0].request.data.get("first_name", "")
        second_name = args[0].request.data.get("second_name", "")
        email = args[0].request.data.get("email", "")
        
        if not first_name and not second_name and not email:
            return Response(
                data={
                    "message": "All first_name, second_name and email  are required to add a contact"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        is_valid =  validate_email(email) 
        if not is_valid:
            return Response(
                data={
                    "message": "Given Email ('{}') is invalid!".format(email)
                },
                status=status.HTTP_400_BAD_REQUEST
            )
                 
        return fn(*args, **kwargs)
    return decorated

           
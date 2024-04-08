def generate_response(data=None, status=200, message=None):
    '''
    Generates a response with the specified data, status, and message.
    '''
    response = {
        "data": data,
        "status": status,
        "message": message
    }
    return response
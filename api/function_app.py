import azure.functions as func
import logging
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="system_info")
def system_info(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # A simple JSON response demonstrating the API works
    data = {
        "status": "success",
        "message": "Hello from your Automated CI/CD Pipeline!",
        "project": "DevOps Portfolio",
        "version": "1.0"
    }

    return func.HttpResponse(
        json.dumps(data),
        mimetype="application/json",
        status_code=200
    )
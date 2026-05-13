import azure.functions as func
import logging
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="system_info")
def system_info(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Personalized JSON response for your portfolio
    data = {
        "developer": "AFFAN",
        "current_focus": "Transitioning to DevOps Engineer",
        "message": "Welcome to my Serverless API! This infrastructure was built using Terraform and deployed via GitHub Actions.",
        "core_skills": [
            "Microsoft Azure", 
            "Terraform", 
            "Python", 
            "CI/CD Automation"
        ],
        "project_status": "Success! 🚀"
    }

    return func.HttpResponse(
        json.dumps(data),
        mimetype="application/json",
        status_code=200
    )

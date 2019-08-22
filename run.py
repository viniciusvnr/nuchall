from flask import Flask
from api_v1 import api_bp_v1


app = Flask(__name__)
app.register_blueprint(api_bp_v1)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
# TODO: Log app initialization (info)
#     try:
#         app.run(debug=True, host='0.0.0.0')
#         logger.info("Application Started")
#     except Exception as e:
#         logger.error(e)
# logger.info("Application Shutdown")

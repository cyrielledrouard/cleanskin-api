from flask import Flask
from controllers.productcontroller import product_app


app = Flask(__name__)
app.register_blueprint(product_app, url_prefix="/products")
app.run()






from flask import Flask

app = Flask(__name__, 
            template_folder='path_to_your_templates',  # Change to your templates directory
            static_folder='path_to_your_static')       # Change to your static files directory

# Your existing route definitions and app logic...

if __name__ == '__main__':
    app.run()
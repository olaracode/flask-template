# Va a permitir levantar el servior de flask en el servidor web
from src.app import app as application

if __name__ == '__main__':
    application.run()
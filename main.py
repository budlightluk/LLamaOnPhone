from networking.server import app as server_app
from utils.logging import log

def main():
    log("Запуск приложения...")
    server_app.run()

if __name__ == '__main__':
    main()

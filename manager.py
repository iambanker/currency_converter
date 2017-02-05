from app import create_app

app = create_app()


def main():
    from flask_script import Manager

    manager = Manager(app)
    manager.run()


if __name__ == '__main__':
    main()

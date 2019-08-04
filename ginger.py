"""
    create by Gray 2019-07-08
"""
from app.app import create_app


app = create_app()


if __name__ == '__main__':
    app.run(debug=True)

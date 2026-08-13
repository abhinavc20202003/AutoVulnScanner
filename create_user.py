from app import app, db, User

with app.app_context():
    db.create_all()

    # remove old users (optional clean)
    User.query.delete()

    # create fresh admin user
    user = User(username="admin", password="admin")
    db.session.add(user)
    db.session.commit()

    print("User created:", user.username)


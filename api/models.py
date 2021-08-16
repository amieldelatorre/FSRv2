from . import db


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    rating = db.Column(db.Integer)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    saved_jobs = db.Column(db.ARRAY(db.Integer))
    owned_jobs = db.relationship('Job', backref='owned_jobs')


class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    position = db.Column(db.String(50))
    company = db.Column(db.String(50))
    qualification_description = db.Column(db.String(250))
    phone = db.Column(db.String(50))
    email = db.Column(db.String(50))
    expiry_date = db.Column(db.Date(50))
    salary = db.Column(db.Integer)
    skills = db.Column(db.ARRAY(db.String(50)))
    location = db.Column(db.String(50))
    job_type = db.column(db.String(50))
    user_id = db.column(db.Integer, db.ForeignKey('user.id'))

    
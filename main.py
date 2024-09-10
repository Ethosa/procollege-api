from fastapi import FastAPI

from mounts.user import user_app
from mounts.branches import branches_app
from mounts.teachers import teacher_app
from mounts.blogs import blogs_app


app = FastAPI()

app.mount('/user', user_app)
app.mount('/branches', branches_app)
app.mount('/teachers', teacher_app)
app.mount('/blogs', blogs_app)

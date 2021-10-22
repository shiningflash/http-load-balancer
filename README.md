# http-load-balancer

Implement a Load Balancer in Python using TDD (Test Driven Development).

### technologies:

- Python
- Flask
- pytest
- Docker
- requests

### routing

- host-based `$ git checkout host-based` or default `main`
- path-based `$ git checkout path-based`

### procedure

##### set up environment

```
$ virtualenv venv
$ source venv/bin/activate # for linux
```

#### next procedure

1. To install all required packages - `$ pip3 install requirements.txt`

2. add a Dockerfile

To build the image `$ docker build -t server .`

After pulling the Python 3 base image, we installed Flask, copied app.py over to the container, and ran the app.

3. We can use this image to spin up multiple containers with Docker Compose

To spin up the containers `$ docker-compose up -d`

```
Test the applications to ensure they work as expected:

$ curl localhost:8081
This is the google application.

$ curl localhost:8082
This is the google application.

$ curl localhost:9081
This is the apple application.

$ curl localhost:9082
This is the apple application.
```

4. After the test, bring the container down `$ docker-compose down`

5. Next, to automate spinning up and then tearing the down, add a _Makefile_ to the project root.

6. To send HTTP request to the backend server `$ pip3 install requests`

7. Run the test, `$ make test`. It should pass all the tests.

### test

- To run pytest - `$ python -m pytest`
- **To automate the test, run `$ make test`**

---

reference: [testdriven.io](https://testdriven.io/courses/http-load-balancer/concepts/)

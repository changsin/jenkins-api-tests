# jenkins-api-tests
POC of controlling builds through Jenkins remote API in Python

The project contains a POC for manipulating Jenkins builds through [Remote Access API](https://www.jenkins.io/doc/book/using/remote-access-api)

## Setup
Python-Jenkins is a wrapper of Remote Access API.
Install [python-jenkins](https://python-jenkins.readthedocs.io/en/latest/api.html#module-jenkins)

```commandline
pip install python-jenkins
```

## Issues
1. **Canceling a job**:
Getting build info and scheduling a build can be done.
But cancelling a build does not seem to work.
FROM python:3.9.7

WORKDIR /Users/User/Desktop

COPY assignment.py .

COPY error_assignment.py .



CMD [ "python" ,"./assignment.py"]

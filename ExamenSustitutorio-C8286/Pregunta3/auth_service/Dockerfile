FROM python:3.9-slim   
WORKDIR /app
COPY auth_service.py /app
RUN pip install flask
CMD ["python", "auth_service.py"]
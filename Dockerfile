FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY employee_evaluation.py .
COPY test_employee_evaluation.py .

CMD ["python", "employee_evaluation.py"]

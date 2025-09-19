FROM python:3.14-rc-alpine
ADD elevator.py .
CMD ["python", "./elevator.py"]
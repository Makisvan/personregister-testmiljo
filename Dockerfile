FROM python:3.11-slim

WORKDIR /app

# Vi kopierar fortfarande app.py för build, men volymen kommer skriva över det
COPY app.py /app/app.py

# Default CMD = bash, så containern hålls igång
CMD ["bash"]




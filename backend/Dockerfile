FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# psycopg[binary] und xhtml2pdf liefern Wheels – kein Compiler nötig
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app/

# collectstatic + migrate laufen beim Container-Start (siehe docker-compose.yml)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]

FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLAG_CONTENT=fodase_primeira_chall

WORKDIR /app

COPY ./chall_1 /app

RUN python3 -c "import random, string, os; open(''.join(random.choices(string.ascii_lowercase, k=8)) + '_flag.txt', 'w').write(os.getenv('FLAG_CONTENT'))"

COPY ./chall_1/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python3", "app.py"]

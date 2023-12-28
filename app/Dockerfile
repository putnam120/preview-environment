FROM python:3.10-slim-bookworm

WORKDIR /app
RUN apt update && apt install -y wget
COPY . .
# RUN wget https://github.com/mitsuhiko/rye/releases/latest/download/rye-x86_64-linux.gz
# RUN gunzip rye-x86_64-linux.gz
# RUN chmod +x ./rye-x86_64-linux && mv ./rye-x86_64-linux /usr/local/bin/rye
# RUN rye pin 3.10 && rye sync
RUN sed '/-e/d' requirements.lock > requirements.txt
RUN pip install -r requirements.txt
CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
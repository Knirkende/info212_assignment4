FROM python:3.8-slim-buster AS builder

RUN python -m pip install --no-cache-dir --upgrade pip \
    && pip install pipenv

COPY web_api /web_api
WORKDIR /web_api
RUN pipenv requirements > requirements.txt

FROM python:3.8-slim-buster AS final

# Configure apt and install packages
RUN python -m pip install --no-cache-dir --upgrade pip \
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/* 
COPY --from=builder /web_api /web_api
RUN pip install --no-cache-dir -r /web_api/requirements.txt

RUN python web_api/manage.py makemigrations web_api
RUN python web_api/manage.py migrate
CMD [ "python", "web_api/manage.py", "runserver", "0.0.0.0:8000" ]
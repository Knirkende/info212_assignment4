FROM python:3.8-slim-buster AS builder

RUN python -m pip install --no-cache-dir --upgrade pip \
    && pip install pipenv

COPY consumer /consumer
WORKDIR /consumer
RUN pipenv lock --requirements > requirements.txt

FROM python:3.8-slim-buster AS final

# Configure apt and install packages
RUN python -m pip install --no-cache-dir --upgrade pip \
    ### for confluent-kafka
    && apt-get update && apt-get install -y \ 
        librdkafka-dev \
    #
    ## Clean up
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/* 
COPY --from=builder /consumer /consumer
RUN pip install --no-cache-dir -r /consumer/requirements.txt

CMD [ "python", "./consumer" ]
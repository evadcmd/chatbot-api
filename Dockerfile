FROM python:3.11-slim AS builder
# install pdm
RUN pip install -U pip setuptools wheel
RUN pip install pdm
RUN pdm config python.use_venv false

WORKDIR /chatbot-api
# copy files
COPY . .
RUN mkdir __pypackages__ && pdm sync --prod --no-editable


FROM python:3.11-slim AS runner

WORKDIR /opt/chatbot-api

ENV PYTHONPATH=./lib
COPY --from=builder /chatbot-api/__pypackages__/3.11/lib ${PYTHONPATH}
COPY --from=builder /chatbot-api/__pypackages__/3.11/bin/* /bin/

COPY .env ./log.conf ./log.dev.conf ./
COPY ./chatbot ./chatbot

ENTRYPOINT [ "uvicorn", "chatbot.main:api", "--host", "0.0.0.0", "--port", "5200" ]

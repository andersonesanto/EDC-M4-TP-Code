FROM python:3.8-slim

COPY ./carga-CadOp.py carga-CadOp.py
COPY ./requirements.txt requirements.txt

RUN /bin/bash -c "pip install -r requirements.txt"

CMD python carga-CadOp.py
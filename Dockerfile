FROM python:3.8-slim

COPY ./carga-CadOp.py carga-CadOp.py
COPY ./carga-CadOp-requirements.txt carga-CadOp-requirements.txt

RUN /bin/bash -c "pip install -r carga-CadOp-requirements.txt"

CMD python carga-CadOp.py
FROM alpine:3.8

RUN apk add --update --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

COPY requirements.txt /src/requirements.txt

RUN pip install -r /src/requirements.txt

COPY app.py /src

COPY buzz /src/buzz

CMD python /src/app.py
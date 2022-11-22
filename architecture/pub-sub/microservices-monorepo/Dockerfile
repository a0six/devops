FROM python:3.8-alpine as builder

LABEL maintainer="aureliano.buendias@outlook.com"

# Install build dependancies
RUN apk update && apk add --upgrade --no-cache g++ make

RUN pip install --no-cache-dir --upgrade pip
RUN pip install pipenv

WORKDIR /usr/local/src

ADD Pipfile.lock Pipfile /usr/local/src/

RUN PIPENV_VENV_IN_PROJECT=1 pipenv sync

FROM python:3.8-alpine as runtime

# Create the user mdm
RUN addgroup --gid 1000 mdm
RUN adduser --disabled-password --home /home/mdm --ingroup mdm \
            --uid 1000 mdm

USER mdm
WORKDIR /home/mdm
COPY src .
COPY --from=builder /usr/local/src/.venv /home/mdm/.venv

ENTRYPOINT ["./.venv/bin/python"]
CMD ["subscriber.py"]
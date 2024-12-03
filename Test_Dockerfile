FROM mcr.microsoft.com/playwright/python:v1.49.0-noble
MAINTAINER Deniz Hamamcioglu - denizhamamcioglu@gmail.com

WORKDIR /cteleport-assignment

ARG PYTEST_ARGS

COPY bash_files .

RUN chmod +x ./bash_scripts/docker-test-entrypoint.sh
CMD ["./bash_scripts/docker-test-entrypoint.sh"]

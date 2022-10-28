FROM mcr.microsoft.com/playwright/python:v1.27.0-focal
WORKDIR /src
COPY . /src
RUN pip3 install -r requirements.txt
RUN playwright install --with-deps
ENTRYPOINT ["/src/entrypoint.sh"]
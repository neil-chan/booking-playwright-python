FROM mcr.microsoft.com/playwright/python:v1.27.0-focal
COPY . ./src
WORKDIR ./src
RUN pip3 install -r requirements.txt
RUN playwright install --with-deps
ENTRYPOINT ["/src/entrypoint.sh"]
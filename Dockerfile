FROM python:3.5

COPY . /app_docker

RUN python3 -m compileall -b app_docker

WORKDIR /app_docker

RUN find . -type f -name "*.py" -delete
ENV PATH=/root/.local/bin:$PATH

RUN pip install --default-timeout=100 --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt

EXPOSE 8080

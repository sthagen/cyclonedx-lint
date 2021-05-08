FROM python:3.9.5-slim-buster
LABEL maintainer="stefan@hagen.link" version="0.0.2" st.efan.hagen.vendor="Stefan Hagen" 
RUN export DEBIAN_FRONTEND=noninteractive && \
apt-get update && \
apt-get -y upgrade && \
apt-get install -y --no-install-recommends tini && \
apt-get -y clean && \
    rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
RUN useradd --create-home action
USER action
WORKDIR /app
COPY cyclonedx_lint .
ENV PYTHONFAULTHANDLER=1
ENTRYPOINT ["tini", "--", "python", "-m", "cyclonedx_lint"]

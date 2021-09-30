FROM ubuntu:bionic
RUN apt-get update
RUN apt-get install -y python3 git
WORKDIR docker-exo1
COPY hello.py .
CMD ["python3", "hello.py"]

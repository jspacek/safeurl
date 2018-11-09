FROM ubuntu:latest
MAINTAINER Jodi Spacek "jodi.spacek@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential curl
COPY . /safeurl
WORKDIR /safeurl
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["service.py"]

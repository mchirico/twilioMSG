# You can change these for your project
project=python
tag=test
gcpProject=mchirico
port=3000

docker-build:
	docker build --no-cache -t gcr.io/$(gcpProject)/$(project):$(tag) -f Dockerfile .

push:
	docker push gcr.io/$(gcpProject)/$(project):$(tag)


run:
	docker run --rm -it -p $(port):$(port)  gcr.io/$(gcpProject)/$(project):$(tag) /bin/bash

test:
	docker run --rm  -p $(port):$(port)  gcr.io/$(gcpProject)/$(project):$(tag) pytest

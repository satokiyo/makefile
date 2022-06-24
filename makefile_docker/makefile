ABSOLUTE_PATH?=$(shell pwd)
CMD=

# build
IMAGE_NAME?=ubuntu_python
TAG_PREFIX:=sample
IMAGE_VERSION:=0.0.1
DOCKERFILE:=Dockerfile

.PHONY: build
build:
	docker build \
		-t $(IMAGE_NAME):$(TAG_PREFIX)_$(IMAGE_VERSION) \
		-f $(DOCKERFILE) \
		.

.PHONY: run
run:
	docker run \
		--rm \
		-it \
		--name $(IMAGE_NAME) \
        --volume "$(ABSOLUTE_PATH)/workspace:/sample/workspace" \
		$(IMAGE_NAME):$(TAG_PREFIX)_$(IMAGE_VERSION) \
		$(CMD)

.PHONY: run_compose_service
run_compose_service: compose_up
	docker-compose exec \
		sample \
		/bin/bash

.PHONY: compose_up
compose_up:
	docker-compose up -d

.PHONY: stop
stop:
	docker rm -f $(IMAGE_NAME)

.PHONY: stop_compose
stop_compose:
	docker-compose down

.PHONY: push
push:
	docker push $(IMAGE_NAME):$(IMAGE_NAME)_$(IMAGE_VERSION)

.PHONY: build_all
build_all: build

.PHONY: run_all
run_all: run

.PHONY: push_all
push_all: push
# Retrieve the absolute paths of the directories
SRC_DIR := $(shell pwd)/src
TEST_DIR := $(shell pwd)/tests

.PHONY: dev

dev:
	@docker build . --target dev -t ethic-ai && \
	docker run -it --rm \
		--name ethic-ai-dev \
		-v $(SRC_DIR):/src \
		-v $(TEST_DIR):/tests \
		ethic-ai bash

stop-dev:
	@docker rm ethic-ai-dev
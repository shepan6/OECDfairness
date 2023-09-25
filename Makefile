# Retrieve the absolute paths of the directories
SRC_DIR := $(shell pwd)/ethically
TEST_DIR := $(shell pwd)/tests

.PHONY: dev

dev:
	@docker build . -t ethic-ai && \
	docker run -it --rm \
		--name ethic-ai-dev \
		-v $(SRC_DIR):/app/ethically \
		-v $(TEST_DIR):/app/tests \
		-w /app \
		ethic-ai bash

stop-dev:
	@docker rm ethic-ai-dev
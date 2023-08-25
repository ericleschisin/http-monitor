all: build up logs

build:
	docker build -f Dockerfile -t monitor:latest .

up:
	docker-compose -f docker-compose.yml up -d

down:
	docker-compose -f docker-compose.yml down

logs:
	docker logs -f $$(docker ps -aqf "name=^monitor$$")


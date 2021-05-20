make up:
	docker-compose up -d

make down:
	docker-compose down

make base:
	python3 make_database/generate.py
docker-build:
	docker build -t "cicd-buzz-app" .
docker-run:
	docker run -it --rm -p 5000:5000 cicd-buzz-app
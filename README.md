docker run --name postgres20252 \
 -e POSTGRES_PASSWORD=123456 -e POSTGRES_USER=pweb2 -e POSTGRES_DB=censoescolar \
 -p 5434:5432 \
 postgres:18.1-alpine3.22

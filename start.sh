#!/bin/sh
#
docker compose --env-file=.env --env-file=.env.stats_db --env-file=.env.docker-compose up

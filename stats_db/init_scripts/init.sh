#!/bin/bash

set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
	CREATE DATABASE tgfe_stats_db;

	CREATE USER tgfe_stats_admin;
    ALTER USER tgfe_stats_admin PASSWORD '$TGFE_STATS_ADMIN_PASS';
EOSQL

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname tgfe_stats_db <<-EOSQL
    REVOKE CONNECT ON DATABASE tgfe_stats_db FROM PUBLIC;

	GRANT ALL PRIVILEGES ON DATABASE tgfe_stats_db TO tgfe_stats_admin;
    ALTER DEFAULT PRIVILEGES 
        FOR ROLE tgfe_stats_admin
        GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO tgfe_stats_admin;
EOSQL

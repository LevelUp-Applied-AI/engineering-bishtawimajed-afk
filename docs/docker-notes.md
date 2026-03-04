# Docker Setup Notes

* **Docker Engine Version:** 29.2.1
* **Resource Allocation:** 4GB RAM (via .wslconfig)
* **Postgres Container:** Running `postgres:15-alpine` as `pg-prework`


# Docker Notes — Day 9

## Docker Version
[ Client:
 Version:           29.2.1
 API version:       1.53
 Go version:        go1.25.6
 Git commit:        a5c7197
 Built:             Mon Feb  2 17:20:16 2026
 OS/Arch:           windows/amd64
 Context:           desktop-linux

Server: Docker Desktop 4.63.0 (220185)
 Engine:
  Version:          29.2.1
  API version:      1.53 (minimum version 1.44)
  Go version:       go1.25.6
  Git commit:       6bc6209
  Built:            Mon Feb  2 17:17:24 2026
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
  Version:          v2.2.1
  GitCommit:        dea7da592f5d1d2b7755e3a161be07f43fad8f75
 runc:
  Version:          1.3.4
  GitCommit:        v1.3.4-0-gd6d73eb8
 docker-init:
  Version:          0.19.0
  GitCommit:        de40ad0
]

## Hello World Test
[   Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
17eec7bbc9d7: Pull complete
ea52d2000f90: Download complete
Digest: sha256:ef54e839ef541993b4e87f25e752f7cf4238fa55f017957c2eb44077083d7a6a
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
]

## Postgres Container

Command used:
```bash
docker run -d \
  --name pg-prework \
  -e POSTGRES_PASSWORD=prework \
  -p 5432:5432 \
  postgres:15-alpine

  Startup Logs

Output of docker logs pg-prework:

[The files belonging to this database system will be owned by user "postgres".
This user must also own the server process.

The database cluster will be initialized with locale "en_US.utf8".
The default database encoding has accordingly been set to "UTF8".
The default text search configuration will be set to "english".

Data page checksums are disabled.

fixing permissions on existing directory /var/lib/postgresql/data ... ok
creating subdirectories ... ok
selecting dynamic shared memory implementation ... posix
selecting default max_connections ... 100
selecting default shared_buffers ... 128MB
selecting default time zone ... UTC
creating configuration files ... ok
running bootstrap script ... ok
sh: locale: not found
2026-03-04 10:56:28.100 UTC [36] WARNING:  no usable system locales were found
performing post-bootstrap initialization ... ok
syncing data to disk ... ok

initdb: warning: enabling "trust" authentication for local connections
initdb: hint: You can change this by editing pg_hba.conf or using the option -A, or --auth-local and --a
uth-host, the next time you run initdb.

Success. You can now start the database server using:

    pg_ctl -D /var/lib/postgresql/data -l logfile start

waiting for server to start....2026-03-04 10:56:29.014 UTC [42] LOG:  starting PostgreSQL 15.17 on x86_6
4-pc-linux-musl, compiled by gcc (Alpine 15.2.0) 15.2.0, 64-bit
2026-03-04 10:56:29.151 UTC [42] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
2026-03-04 10:56:29.166 UTC [45] LOG:  database system was shut down at 2026-03-04 10:56:28 UTC
2026-03-04 10:56:29.176 UTC [42] LOG:  database system is ready to accept connections
 done
server started

/usr/local/bin/docker-entrypoint.sh: ignoring /docker-entrypoint-initdb.d/*

waiting for server to shut down....2026-03-04 10:56:29.237 UTC [42] LOG:  received fast shutdown request
2026-03-04 10:56:29.241 UTC [42] LOG:  aborting any active transactions
2026-03-04 10:56:29.246 UTC [42] LOG:  background worker "logical replication launcher" (PID 48) exited
with exit code 1
2026-03-04 10:56:29.246 UTC [43] LOG:  shutting down
2026-03-04 10:56:29.250 UTC [43] LOG:  checkpoint starting: shutdown immediate
2026-03-04 10:56:29.342 UTC [43] LOG:  checkpoint complete: wrote 3 buffers (0.0%); 0 WAL file(s) added,
 0 removed, 0 recycled; write=0.045 s, sync=0.005 s, total=0.096 s; sync files=2, longest=0.003 s, avera
ge=0.003 s; distance=0 kB, estimate=0 kB
2026-03-04 10:56:29.352 UTC [42] LOG:  database system is shut down
 done
server stopped

PostgreSQL init process complete; ready for start up.

2026-03-04 10:56:29.475 UTC [1] LOG:  starting PostgreSQL 15.17 on x86_64-pc-linux-musl, compiled by gcc
 (Alpine 15.2.0) 15.2.0, 64-bit
2026-03-04 10:56:29.478 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
2026-03-04 10:56:29.478 UTC [1] LOG:  listening on IPv6 address "::", port 5432
2026-03-04 10:56:29.486 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
2026-03-04 10:56:29.497 UTC [56] LOG:  database system was shut down at 2026-03-04 10:56:29 UTC
2026-03-04 10:56:29.505 UTC [1] LOG:  database system is ready to accept connections
2026-03-04 11:01:29.547 UTC [54] LOG:  checkpoint starting: time
2026-03-04 11:01:33.792 UTC [54] LOG:  checkpoint complete: wrote 43 buffers (0.3%); 0 WAL file(s) added
, 0 removed, 0 recycled; write=4.150 s, sync=0.014 s, total=4.247 s; sync files=11, longest=0.006 s, ave
rage=0.002 s; distance=252 kB, estimate=252 kB
2026-03-04 14:01:25.581 UTC [1] LOG:  received fast shutdown request
2026-03-04 14:01:25.613 UTC [1] LOG:  aborting any active transactions
2026-03-04 14:01:25.670 UTC [1] LOG:  background worker "logical replication launcher" (PID 59) exited w
ith exit code 1
2026-03-04 14:01:25.675 UTC [54] LOG:  shutting down
2026-03-04 14:01:25.684 UTC [54] LOG:  checkpoint starting: shutdown immediate
2026-03-04 14:01:25.766 UTC [54] LOG:  checkpoint complete: wrote 0 buffers (0.0%); 0 WAL file(s) added,
 0 removed, 0 recycled; write=0.037 s, sync=0.001 s, total=0.091 s; sync files=0, longest=0.000 s, avera
ge=0.000 s; distance=0 kB, estimate=227 kB
2026-03-04 14:01:25.804 UTC [1] LOG:  database system is shut down

PostgreSQL Database directory appears to contain a database; Skipping initialization

2026-03-04 14:01:29.489 UTC [1] LOG:  starting PostgreSQL 15.17 on x86_64-pc-linux-musl, compiled by gcc
 (Alpine 15.2.0) 15.2.0, 64-bit
2026-03-04 14:01:29.492 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
2026-03-04 14:01:29.492 UTC [1] LOG:  listening on IPv6 address "::", port 5432
2026-03-04 14:01:29.507 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
2026-03-04 14:01:29.529 UTC [29] LOG:  database system was shut down at 2026-03-04 14:01:25 UTC
2026-03-04 14:01:29.556 UTC [1] LOG:  database system is ready to accept connections
2026-03-04 14:01:55.485 UTC [1] LOG:  received fast shutdown request
2026-03-04 14:01:55.494 UTC [1] LOG:  aborting any active transactions
2026-03-04 14:01:55.512 UTC [1] LOG:  background worker "logical replication launcher" (PID 32) exited w
ith exit code 1
2026-03-04 14:01:55.512 UTC [27] LOG:  shutting down
2026-03-04 14:01:55.528 UTC [27] LOG:  checkpoint starting: shutdown immediate
2026-03-04 14:01:55.555 UTC [27] LOG:  checkpoint complete: wrote 3 buffers (0.0%); 0 WAL file(s) added,
 0 removed, 0 recycled; write=0.009 s, sync=0.005 s, total=0.043 s; sync files=2, longest=0.004 s, avera
ge=0.003 s; distance=0 kB, estimate=0 kB
2026-03-04 14:01:55.565 UTC [1] LOG:  database system is shut down

PostgreSQL Database directory appears to contain a database; Skipping initialization

2026-03-04 14:01:56.630 UTC [1] LOG:  starting PostgreSQL 15.17 on x86_64-pc-linux-musl, compiled by gcc
 (Alpine 15.2.0) 15.2.0, 64-bit
2026-03-04 14:01:56.632 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
2026-03-04 14:01:56.632 UTC [1] LOG:  listening on IPv6 address "::", port 5432
2026-03-04 14:01:56.650 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
2026-03-04 14:01:56.668 UTC [29] LOG:  database system was shut down at 2026-03-04 14:01:55 UTC
2026-03-04 14:01:56.690 UTC [1] LOG:  database system is ready to accept connections
2026-03-04 14:06:56.654 UTC [27] LOG:  checkpoint starting: time
2026-03-04 14:06:56.790 UTC [27] LOG:  checkpoint complete: wrote 3 buffers (0.0%); 0 WAL file(s) added,
 0 removed, 0 recycled; write=0.056 s, sync=0.009 s, total=0.138 s; sync files=2, longest=0.006 s, avera
ge=0.005 s; distance=0 kB, estimate=0 kB
2026-03-04 14:11:23.124 UTC [1] LOG:  received fast shutdown request
2026-03-04 14:11:23.211 UTC [1] LOG:  aborting any active transactions
2026-03-04 14:11:23.251 UTC [1] LOG:  background worker "logical replication launcher" (PID 32) exited w
ith exit code 1
2026-03-04 14:11:23.256 UTC [27] LOG:  shutting down
2026-03-04 14:11:23.263 UTC [27] LOG:  checkpoint starting: shutdown immediate
2026-03-04 14:11:23.317 UTC [27] LOG:  checkpoint complete: wrote 0 buffers (0.0%); 0 WAL file(s) added,
 0 removed, 0 recycled; write=0.029 s, sync=0.001 s, total=0.061 s; sync files=0, longest=0.000 s, avera
ge=0.000 s; distance=0 kB, estimate=0 kB
2026-03-04 14:11:23.342 UTC [1] LOG:  database system is shut down

PostgreSQL Database directory appears to contain a database; Skipping initialization

2026-03-04 14:11:36.930 UTC [1] LOG:  starting PostgreSQL 15.17 on x86_64-pc-linux-musl, compiled by gcc
 (Alpine 15.2.0) 15.2.0, 64-bit
2026-03-04 14:11:36.933 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
2026-03-04 14:11:36.933 UTC [1] LOG:  listening on IPv6 address "::", port 5432
2026-03-04 14:11:36.943 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
2026-03-04 14:11:36.963 UTC [29] LOG:  database system was shut down at 2026-03-04 14:11:23 UTC
2026-03-04 14:11:37.001 UTC [1] LOG:  database system is ready to accept connections
2026-03-04 14:16:36.908 UTC [27] LOG:  checkpoint starting: time
2026-03-04 14:16:37.053 UTC [27] LOG:  checkpoint complete: wrote 3 buffers (0.0%); 0 WAL file(s) added,
 0 removed, 0 recycled; write=0.042 s, sync=0.007 s, total=0.149 s; sync files=2, longest=0.004 s, avera
ge=0.004 s; distance=0 kB, estimate=0 kB
2026-03-04 15:08:15.066 UTC [1] LOG:  received fast shutdown request
2026-03-04 15:08:15.075 UTC [1] LOG:  aborting any active transactions
2026-03-04 15:08:15.098 UTC [1] LOG:  background worker "logical replication launcher" (PID 32) exited w
ith exit code 1
2026-03-04 15:08:15.108 UTC [27] LOG:  shutting down
2026-03-04 15:08:15.115 UTC [27] LOG:  checkpoint starting: shutdown immediate
2026-03-04 15:08:15.154 UTC [27] LOG:  checkpoint complete: wrote 0 buffers (0.0%); 0 WAL file(s) added,
 0 removed, 0 recycled; write=0.020 s, sync=0.001 s, total=0.046 s; sync files=0, longest=0.000 s, avera
ge=0.000 s; distance=0 kB, estimate=0 kB
2026-03-04 15:08:15.175 UTC [1] LOG:  database system is shut down

PostgreSQL Database directory appears to contain a database; Skipping initialization

2026-03-04 15:10:58.452 UTC [1] LOG:  starting PostgreSQL 15.17 on x86_64-pc-linux-musl, compiled by gcc
 (Alpine 15.2.0) 15.2.0, 64-bit
2026-03-04 15:10:58.455 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
2026-03-04 15:10:58.455 UTC [1] LOG:  listening on IPv6 address "::", port 5432
2026-03-04 15:10:58.460 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
2026-03-04 15:10:58.476 UTC [29] LOG:  database system was shut down at 2026-03-04 15:08:15 UTC
2026-03-04 15:10:58.511 UTC [1] LOG:  database system is ready to accept connections
 ]

Startup confirmation line found: LOG:  database system is ready to accept connections

Stop and Restart
Command: docker stop pg-prework (Container status: Exited)

Command: docker restart pg-prework (Container status: Up)

Final Log Check: LOG: database system is ready to accept connections


Issues Encountered
Initially encountered a container name conflict because "pg-prework" was already in use. I resolved this by running docker rm -f pg-prework to remove the old container before successfully running the new one.
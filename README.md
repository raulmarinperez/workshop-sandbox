# The Observability Workshop Sandbox
Welcome to the *Observability Workshop Sandbox* repo, a place where I'll be consolidating resources I find here and there aiming to easily reproduce some of the most typical scenarios SREs and DevOps teams have to deal with day in day out.

This is what the sandbox provides/covers at the moment:

1. A stripped down deployment of the ["The New Stack (TNS) observability app"](https://github.com/grafana/tns) relying on Docker Compose, with the following elements:
   - Grafana Agent
   - Container mimicking a Database service (db)
   - Container mimicking an Application service (app)
   - Container producing some load on the previous services (loadgen)
2. Grafana Cloud as the Observability Stack to handle metrics and logs; **spin up your own Grafana Cloud Free (forver) Tier** by visiting [this link](https://grafana.com/auth/sign-up/create-user).

Additional elements will be introduced over time to address more advanced scenarios such us:

- Tracing
- Unified Alerting
- Advanced Incident Management
- ...

Stay tuned ;)

Raúl

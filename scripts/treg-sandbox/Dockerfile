# Sandbox for the Treg CLI, used only to call MobiusEngine Jobs Data (scripts/mobius-search.py).
# No host files are mounted. The home folder is a named Docker volume (treg-sandbox-home), so the Treg
# sign-in and the connected MobiusEngine key survive between runs. Plain CLI only: no [proxy] extra
# (its local certificate authority), no skill or MCP server written into any agent, telemetry off.
#
# Build:   docker build -t treg-sandbox:0.30.0 scripts/treg-sandbox
# Sign in: docker run --rm -it --name treg-sandbox -v treg-sandbox-home:/home/treg treg-sandbox:0.30.0 bash
#          then, inside: treg login ; treg connections connect --provider mobiusengine-jobs
# Remove:  docker volume rm treg-sandbox-home ; docker rmi treg-sandbox:0.30.0
FROM python:3.12-slim
ENV DO_NOT_TRACK=1 TREG_TELEMETRY=0 PIP_NO_CACHE_DIR=1 PIP_DISABLE_PIP_VERSION_CHECK=1
RUN pip install "tools-registry==0.30.0" && useradd -m treg
USER treg
WORKDIR /home/treg
CMD ["bash"]

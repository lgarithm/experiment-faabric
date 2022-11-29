# Build the experiments' code
FROM faasm/examples-build:0.2.0_0.2.0 as build

RUN rm -rf /code \
    && mkdir -p /code \
    && cd /code \
    # TODO: clone from main eventually
    && git clone -b llvm https://github.com/faasm/examples /code/faasm-examples \
    && cd /code/faasm-examples \
    && git submodule update --init -f cpp \
    && git submodule update --init -f python \
    && git submodule update --init -f examples/Kernels \
    && git submodule update --init -f examples/lammps \
    && git submodule update --init -f examples/LULESH \
    && ./bin/create_venv.sh \
    && source ./venv/bin/activate \
    && inv \
        kernels --native \
        kernels \
        lammps --native \
        lammps \
        lulesh --native \
        lulesh

# Prepare the runtime to run the native experiments
FROM faasm/openmpi:0.2.0

COPY --from=build --chown=mpirun:mpirun /code/faasm-examples /code/faasm-examples

# Install OpenMP
ARG DEBIAN_FRONTEND=noninteractive
RUN apt update \
    && apt install -y libomp-13-dev

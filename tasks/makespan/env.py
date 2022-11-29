from os.path import join
from tasks.util.env import PROJ_ROOT

MAKESPAN_DIR = join(PROJ_ROOT, "tasks", "makespan")
MAKESPAN_NATIVE_COMPOSE_NAME = "makespan-native"
MAKESPAN_NATIVE_DIR = join(MAKESPAN_DIR, "native")
MAKESPAN_WASM_DIR = join(MAKESPAN_DIR, "wasm")
MAKESPAN_IMAGE_NAME = "experiment-makespan"
MAKESPAN_DOCKERFILE = join(PROJ_ROOT, "docker", "makespan.dockerfile")

EXAMPLES_DOCKER_DIR = join("/code", "faasm-examples", "examples")
LAMMPS_DOCKER_DIR = join(EXAMPLES_DOCKER_DIR, "lammps")
LAMMPS_DOCKER_BINARY = join(LAMMPS_DOCKER_DIR, "build", "native", "lmp")
LAMMPS_DOCKER_WASM = join(LAMMPS_DOCKER_DIR, "build", "wasm", "lmp")
LULESH_DOCKER_DIR = join(EXAMPLES_DOCKER_DIR, "LULESH")
LULESH_DOCKER_BINARY = join(LULESH_DOCKER_DIR, "build", "native", "lulesh2.0")
LULESH_DOCKER_WASM = join(LULESH_DOCKER_DIR, "build", "wasm", "lulesh2.0")
LULESH_FAASM_USER = "lulesh"
LULESH_FAASM_FUNC = "main"
DGEMM_DOCKER_DIR = join(EXAMPLES_DOCKER_DIR, "Kernels")
DGEMM_DOCKER_BINARY = join(DGEMM_DOCKER_DIR, "build", "native", "omp_dgemm.o")
DGEMM_DOCKER_WASM = join(DGEMM_DOCKER_DIR, "build", "wasm", "omp_dgemm.wasm")
DGEMM_FAASM_USER = "dgemm"
DGEMM_FAASM_FUNC = "main"


# If we set the input parameters to:
# - (10, 2048, 32) it can take almost 5' for a two-threaded execution to finish
# - (2, 2048, 32) it takes about 1' for a two-threaded execution to finish
def get_dgemm_cmdline(
    num_threads, iterations=10, matrix_order=2048, tile_size=32
):
    return "{} {} {} {}".format(
        num_threads, iterations, matrix_order, tile_size
    )


def get_lulesh_cmdline(
    iterations=5000, cube_size=20, regions=11, cost=1, balance=1
):
    return " ".join(
        [
            "-i {}".format(iterations),
            "-s {}".format(cube_size),
            "-r {}".format(regions),
            "-c {}".format(cost),
            "-b {}".format(balance),
        ]
    )

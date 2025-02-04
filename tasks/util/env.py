from os.path import dirname, realpath, expanduser, join, exists
from shutil import rmtree
from os import getenv, makedirs
from subprocess import run

HOME_DIR = expanduser("~")
PROJ_ROOT = dirname(dirname(dirname(realpath(__file__))))
BIN_DIR = join(PROJ_ROOT, "bin")
GLOBAL_BIN_DIR = "/usr/local/bin"
CONFIG_DIR = join(PROJ_ROOT, "config")
FAASM_ROOT = join(HOME_DIR, "faasm")
SYSTEM_NAME = "Granny"

K9S_VERSION = "0.32.2"

AZURE_RESOURCE_GROUP = "faasm"
ACR_NAME = "faasm.azurecr.io"
AKS_CLUSTER_NAME = getenv('USER') + "-faasm-cluster"
AKS_VM_SIZE = "Standard_DS5_v2"
AKS_NODE_COUNT = 4
AKS_REGION = "eastus"
AZURE_PUB_SSH_KEY = "~/.ssh/id_rsa.pub"
KUBECTL_BIN = join(PROJ_ROOT, "bin", "kubectl")

FAABRIC_EXP_IMAGE_NAME = "faabric-experiments"

NATIVE_BUILD_DIR = join(PROJ_ROOT, "build", "native")
NATIVE_INSTALL_DIR = join(PROJ_ROOT, "build", "native-install")

WASM_BUILD_DIR = join(PROJ_ROOT, "build", "wasm")
WASM_INSTALL_DIR = join(PROJ_ROOT, "build", "wasm-install")

RESULTS_DIR = join(PROJ_ROOT, "results")

PLOTS_ROOT = join(PROJ_ROOT, "plots")
PLOTS_FORMAT = "pdf"
MPL_STYLE_FILE = join(PROJ_ROOT, "faasm.mplstyle")

# ------------------------------------------
# Constants related to function upload and exectuion
# ------------------------------------------

EXAMPLES_BASE_DIR = join("/code", "faasm-examples")
EXAMPLES_DOCKER_DIR = join(EXAMPLES_BASE_DIR, "examples")

# --- DGEMM (OpenMP Kernel) ---

DGEMM_DOCKER_DIR = join(EXAMPLES_DOCKER_DIR, "Kernels")
DGEMM_DOCKER_BINARY = join(DGEMM_DOCKER_DIR, "build", "native", "omp_dgemm.o")
DGEMM_DOCKER_WASM = join(DGEMM_DOCKER_DIR, "build", "wasm", "omp_dgemm.wasm")
DGEMM_FAASM_USER = "dgemm"
DGEMM_FAASM_FUNC = "main"

# --- MPI Migration Microbenchmark

MPI_MIGRATE_WASM_BINARY = join(EXAMPLES_BASE_DIR, "mpi_migrate.wasm")
MPI_MIGRATE_FAASM_USER = "mpi"
MPI_MIGRATE_FAASM_FUNC = "migrate"


def get_version():
    ver_file = join(PROJ_ROOT, "VERSION")

    with open(ver_file, "r") as fh:
        version = fh.read()
        version = version.strip()

    return version


def clean_dir(dir_path, clean):
    if clean and exists(dir_path):
        rmtree(dir_path)

    if not exists(dir_path):
        makedirs(dir_path)


def get_docker_tag(img_name):
    img_tag = "{}/{}:{}".format(ACR_NAME, img_name, get_version())
    return img_tag


def push_docker_image(img_tag):
    run("docker push {}".format(img_tag), check=True, shell=True)

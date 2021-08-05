from invoke import Collection

from . import container
from . import data
from . import run
from . import wasm

ns = Collection(container, data, run, wasm)

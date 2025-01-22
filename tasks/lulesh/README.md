# LULESH Experiment

This experiment is a single execution of the LULESH simulation using OpenMP.

> [!WARNING]
> LULESH does a lot of forking in a tight loop. This is highly inefficient
> in our current implementation, so the results are very bad until we do
> something about it. The first easy fix is caching scheduling results
> locally, avoiding a round-trip to the planner.

## Start AKS cluster

Create a new cluster:

```bash
inv cluster.provision --vm Standard_D8_v5 --nodes 1
inv cluster.credentials
```

## Granny

Deploy the cluster:

```bash
faasmctl deploy.k8s --workers=1
```

Upload the WASM file:

```bash
inv lammps.wasm.upload
```

and run the experiment with:

```bash
inv lammps.run.granny -w compute -w network
```

To remove the cluster, run:

```bash
faasmctl delete
```

## Native

Deploy the cluster:

```bash
inv lammps.native.deploy
```

And run:

```bash
inv lammps.run.native -w compute -w network
```

finally, delete the native cluster:

```bash
inv lammps.native.delete
```

# Plot

To plot the results, you may run:

```bash
inv lammps.plot
```

which will generate a plot in [`./plots/lammps/runtime.png`](
./plots/lammps/runtime.png), we also include it below:

![LAMMPS Runtime Plot](./plots/lammps/runtime.png)

## Clean-Up

Remember to delete the cluster.

```bash
inv cluster.delete
```

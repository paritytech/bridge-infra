# Bridge Task-Force Infrastructure

## Prepare/Build/Deploy for Kusama <> Polkadot
This instruction simplifies the setup from [bridge-hub repository](https://github.com/paritytech/cumulus/tree/bridge-hub-rococo-wococo/parachains/runtimes/bridge-hubs#how-to-test-locally-rococo---wococo).

### Prepare empty directory for testing
```sh
mkdir -p ~/local_bridge_testing/bin
mkdir -p ~/local_bridge_testing/logs
```

### Install Zombienet
Go to [Zombienet Release page](https://github.com/paritytech/zombienet/releases), copy the apropriate binary
(`zombienet-linux`/`zombienet-macos`) from the latest release to `~/local_bridge_testing/bin`,
and rename it to `zombienet`. 

### Build polkadot binary
```sh
git clone https://github.com/paritytech/polkadot.git
cd polkadot
git checkout locked-for-gav-xcm-v3-and-bridges
cargo build --release
cp target/release/polkadot ~/local_bridge_testing/bin/polkadot
```

### Build Statemine/Statemint binary
```sh
git clone https://github.com/paritytech/cumulus.git
cd cumulus
git checkout bidzyyys/transact-over-bridges
cargo build --release --locked -p polkadot-parachain@0.9.300
cp target/release/polkadot-parachain ~/local_bridge_testing/bin/polkadot-parachain-mint
```

### Build BridgeHub Binary
```sh
git clone https://github.com/paritytech/cumulus.git
cd cumulus
git checkout bridge-hub-rococo-wococo
cargo build --release --locked -p polkadot-parachain@0.9.300
cp target/release/polkadot-parachain ~/local_bridge_testing/bin/polkadot-parachain
```

### Build substrate-relay binary
```sh
git clone https://github.com/paritytech/parity-bridges-common.git
cd parity-bridges-common
cargo build --release -p substrate-relay
cp target/release/substrate-relay ~/local_bridge_testing/bin/substrate-relay
```

### Create a symbolic link to `cumulus` local directory inside `bridge-infra` directory
**NOTE:** cumulus repository must be on `bridge-hub-rococo-wococo` branch.
```sh
ln -s <path_to_cumulus_local_dir> cumulus
```

### Run
In a separated terminal run Kusama side:
```sh
./scripts/kusama.sh
```

In a separated terminal run Polkadot side:
```sh
./scripts/polkadot.sh
```

In a separated terminal run relayer for Kusama <> Polkadot:
```sh
./scripts/relay.sh
```

Check if everything works as expected following the [instruction](https://github.com/paritytech/cumulus/blob/bridge-hub-rococo-wococo/parachains/runtimes/bridge-hubs/README.md#run-relayers-rococo-wococo).



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
git checkout 5d8164fdda
cargo build --release
cp target/release/polkadot ~/local_bridge_testing/bin/polkadot
```

### Build Statemine/Statemint binary
```sh
git clone https://github.com/paritytech/cumulus.git
cd cumulus
git checkout bridges-task-force/transact-experiments
cargo build --release --locked -p polkadot-parachain-bin
cp target/release/polkadot-parachain ~/local_bridge_testing/bin/polkadot-parachain-mint
```

### Build BridgeHub Binary
```sh
git clone https://github.com/paritytech/cumulus.git
cd cumulus
git checkout bridges-task-force/ethereum-playground
cargo build --release --locked -p polkadot-parachain-bin
cp target/release/polkadot-parachain ~/local_bridge_testing/bin/polkadot-parachain
```

### Build substrate-relay binary
```sh
git clone https://github.com/paritytech/parity-bridges-common.git
cd parity-bridges-common
git checkout 036e6696
cargo build --release -p substrate-relay
cp target/release/substrate-relay ~/local_bridge_testing/bin/substrate-relay
```

### Create a symbolic link to `cumulus` local directory inside `bridge-infra` directory
**NOTE:** cumulus repository must be on `bridges-task-force/ethereum-playground` branch.
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

### Ethereum setup

#### Create a symbolic link to `ethereum_xcm_builder` local directory inside `bridge-infra` directory
```sh
ln -s <path_to_ethereum_xcm_builder> ethereum_xcm_builder
```

#### Python
Follow the [instruction](https://mnzel.medium.com/how-to-activate-python-venv-on-a-mac-a8fa1c3cb511) to install Python, venv & activate venv.

#### Install requirements
Remember to load venv for the project:
```sh
source venv/bin/activate
```

Install Python dependencies for the Ethereum -> Polkadot relayer:
```sh
pip3 install --upgrade pip
pip3 install -r requirements.txt
```

#### Run Ethereum -> Polkadot relayer
Remember to load venv for the project:
```sh
source venv/bin/activate
```

Run Python script for relayer:
```sh
python3 main.py
```


Check if everything works as expected following the [instruction](https://github.com/paritytech/cumulus/blob/bridge-hub-rococo-wococo/parachains/runtimes/bridge-hubs/README.md#run-relayers-rococo-wococo).

### Play with it

#### Rococo side
- [Rococo](https://polkadot.js.org/apps/?rpc=ws://127.0.0.1:9942#/explorer)
- [Statemine](https://polkadot.js.org/apps/?rpc=ws://127.0.0.1:9910#/explorer)
- [Rococo BridgeHub](https://polkadot.js.org/apps/?rpc=ws%3A%2F%2F127.0.0.1%3A8943#/explorer)

#### Wococo side
- [Wococo](https://polkadot.js.org/apps/?rpc=ws://127.0.0.1:9945#/explorer)
- [Westmint](https://polkadot.js.org/apps/?rpc=ws://127.0.0.1:9010#/explorer)
- [Wococo BridgeHub](https://polkadot.js.org/apps/?rpc=ws://127.0.0.1:8945#/explorer)


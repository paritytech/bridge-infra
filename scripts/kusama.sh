# Rococo + BridgeHubRococo + Rockmine (mirroring Kusama)
POLKADOT_BINARY_PATH=~/local_bridge_testing/bin/polkadot \
POLKADOT_PARACHAIN_BINARY_PATH=~/local_bridge_testing/bin/polkadot-parachain \
POLKADOT_PARACHAIN_BINARY_PATH_FOR_ROCKMINE=~/local_bridge_testing/bin/polkadot-parachain \
	~/local_bridge_testing/bin/zombienet --provider native spawn ./network/bridge_hub_rococo_local_network.toml


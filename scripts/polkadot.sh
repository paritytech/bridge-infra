# Wococo + BridgeHubWococo + Wockmint (mirroring Polkadot)
POLKADOT_BINARY_PATH=~/local_bridge_testing/bin/polkadot \
POLKADOT_PARACHAIN_BINARY_PATH=~/local_bridge_testing/bin/polkadot-parachain \
POLKADOT_PARACHAIN_BINARY_PATH_FOR_WOCKMINT=~/local_bridge_testing/bin/polkadot-parachain \
PLAYGROUND_PARACHAIN_BINARY_PATH=~/local_bridge_testing/bin/trappist-collator \
	~/local_bridge_testing/bin/zombienet --provider native spawn ./network/bridge_hub_wococo_local_network.toml


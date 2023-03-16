from substrateinterface import SubstrateInterface, Keypair
from substrateinterface.exceptions import SubstrateRequestException

from web3 import Web3, WebsocketProvider
import time
import json

with open("ethereum_xcm_builder/out/Demo.sol/Demo.json") as f:
    demo_contract_json = json.load(f)

w3 = Web3(WebsocketProvider("ws://127.0.0.1:8545"))

demoContractABI = demo_contract_json["abi"]
demoContractAddress = "0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512"
demoContract = w3.eth.contract(
    address=demoContractAddress,
    abi=demoContractABI
)


substrateBridgeHub = SubstrateInterface(
    url="ws://127.0.0.1:8945"
)
keypair = Keypair.create_from_uri('//Alice')

def submit_to_bridge_hub(encoded_message):
    print(f"Sending message: '{encoded_message}'")
    call = substrateBridgeHub.compose_call(
        call_module='BridgeWococoMessages',
        call_function='execute_encoded_message',
        call_params={
            'message': encoded_message
        }
    )

    extrinsic = substrateBridgeHub.create_signed_extrinsic(call=call, keypair=keypair)
    receipt = substrateBridgeHub.submit_extrinsic(extrinsic, wait_for_inclusion=True)

    print(f"Extrinsic '{receipt.extrinsic_hash}' sent and included in a block '{receipt.block_hash}'")


def handle_event(event):
    if event.event == "BridgeMessageCreated":
        message_id = "0x" + event.args.messageId.hex()
        encoded_message = "0x" + event.args.encodedMessage.hex()
        print(f"Received event: '{message_id}' encoded message: '{encoded_message}'")
        submit_to_bridge_hub(encoded_message)
    else:
        print(f"Received unknown event: {event.event}")

def log_loop(event_filter, poll_interval):
    while True:
        for event in event_filter.get_new_entries():
            handle_event(event)
        time.sleep(poll_interval)

def main():
    bridge_event_filter = demoContract.events.BridgeMessageCreated.create_filter(fromBlock='latest')
    log_loop(bridge_event_filter, 2)

if __name__ == '__main__':
    main()

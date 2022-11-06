import subprocess

def get_puzzle_proof(solution, player_id):
    return {
        "proof": "0x08f48e2381b8695d6b6787ff12f4f12f5ef0cbbe85b1073b5a0689967b7d58340d073100a7661187456697d7ffcbd545e987e2cb7f0ac2719dc84eda9b140742184e1abe43228be25468db6a5fd98c68bbb05751c9ff24a205704003d592d0300230b4da1e9000ad07922761222355748e0ce1aa06ee6eb1e31ce64c48b8b04026683d1cb3e9cde151265a42a4dd81d14f05744b22dce5963f37b55f5066105b107f21fced93a35cc303b29b67bea7813cbbb6c664035d9a95afb268055320bc2eb51d5ba44fedf9f41ebe7e9d80e9096778abb5186df303b220ccdcf17aca7e1afc1d87b5d4d792688710937353f4c61649370f54afa54e104fdc6a2ff647d204d29a20c008f843d167e93692cecf6855035d719302ec40b3bb2fdb626b979717fcb9896880e2003728efcceb927626ef3a175ca5e1655da7ebbfe5d3ff998b1ad0780a94c19adf05dd100678ee3ea03b6134eddec0349c6a0e1f5ee2b75c8f172f10ee324aec62c0076abcdab5e79281dadfa810e0408a882be3946d26e92119df7619de05da30a76511c23d8458bb00e359a125accf8f8e0f4f99e3a719ae2f7f54247a3a070393156cab22b703b477a731d0c4d60a2bdc1e471eae975bdb14526dfa187a5533403536e742b6efc40a4b051495dedbf222b35d122b8d567b24531bc4edfc4d28d4d948f80c274038fd720e662d8fc67bb3184e016aeb825309f601ae64d9c5d7a14732af6b8874937769a8df7fc744823e4b89652510cac4169807b73363d96e28591dd2158e65a438f2ad6fe3e6e7bd873d1f6d1127da270df8ffa582ff18791630e20769a44daeefed8a6e4cbbf05cf11c17343012b249106e434e5fd6e376381ed7a8d38e7d977613aada5a53c018b5add595f7bed1b40b72a51adf3be0d8ad13dd1cad864da54a8888419e15456fa00fe9b043082aa12a02155f87c34b96db9ede712cc693204ebb0acb472d270806a40b684fa1d03403472d9df1a292a99819e4480f3bd57501fb167e465442fbea7c7ecee40f5d422b3d8bd0120eeef550eccf818bd2a8655e74810c84b24dcaa756e9818614e9f419e7f36bbec23ec65e4074a440770b40feb73634093a3070f26c75caa4c1247b",
        "public": ["0x0000000000000000000000000000000000000000000000000000000000000004",
                   "0x11a5ec837a18eaa4b083de1c5feea9821a11f3e3353fcae9ffeb11b46214f381",
                   "0x0f18eaab146445a9f48132e17f4a8b1eb62eb85e07b7d3cc7848863c59094bfb",
                   "0x28db2df574d6cb6d353c02c5b5ae1aa28702d9ccb8eaaa88e4a2c80c52d4368a"]
    }

# def get_puzzle_proof(solution, player_id):
#     return {
#         "proof": "0x08f48e2381b8695d6b6787ff12f4f12f5ef0cbbe85b1073b5a0689967b7d58340d073100a7661187456697d7ffcbd545e987e2cb7f0ac2719dc84eda9b140742184e1abe43228be25468db6a5fd98c68bbb05751c9ff24a205704003d592d0300230b4da1e9000ad07922761222355748e0ce1aa06ee6eb1e31ce64c48b8b04026683d1cb3e9cde151265a42a4dd81d14f05744b22dce5963f37b55f5066105b107f21fced93a35cc303b29b67bea7813cbbb6c664035d9a95afb268055320bc2eb51d5ba44fedf9f41ebe7e9d80e9096778abb5186df303b220ccdcf17aca7e1afc1d87b5d4d792688710937353f4c61649370f54afa54e104fdc6a2ff647d204d29a20c008f843d167e93692cecf6855035d719302ec40b3bb2fdb626b979717fcb9896880e2003728efcceb927626ef3a175ca5e1655da7ebbfe5d3ff998b1ad0780a94c19adf05dd100678ee3ea03b6134eddec0349c6a0e1f5ee2b75c8f172f10ee324aec62c0076abcdab5e79281dadfa810e0408a882be3946d26e92119df7619de05da30a76511c23d8458bb00e359a125accf8f8e0f4f99e3a719ae2f7f54247a3a070393156cab22b703b477a731d0c4d60a2bdc1e471eae975bdb14526dfa187a5533403536e742b6efc40a4b051495dedbf222b35d122b8d567b24531bc4edfc4d28d4d948f80c274038fd720e662d8fc67bb3184e016aeb825309f601ae64d9c5d7a14732af6b8874937769a8df7fc744823e4b89652510cac4169807b73363d96e28591dd2158e65a438f2ad6fe3e6e7bd873d1f6d1127da270df8ffa582ff18791630e20769a44daeefed8a6e4cbbf05cf11c17343012b249106e434e5fd6e376381ed7a8d38e7d977613aada5a53c018b5add595f7bed1b40b72a51adf3be0d8ad13dd1cad864da54a8888419e15456fa00fe9b043082aa12a02155f87c34b96db9ede712cc693204ebb0acb472d270806a40b684fa1d03403472d9df1a292a99819e4480f3bd57501fb167e465442fbea7c7ecee40f5d422b3d8bd0120eeef550eccf818bd2a8655e74810c84b24dcaa756e9818614e9f419e7f36bbec23ec65e4074a440770b40feb73634093a3070f26c75caa4c1247b",
#         "public": ["0x0000000000000000000000000000000000000000000000000000000000000004",
#                    "0x11a5ec837a18eaa4b083de1c5feea9821a11f3e3353fcae9ffeb11b46214f381",
#                    "0x0f18eaab146445a9f48132e17f4a8b1eb62eb85e07b7d3cc7848863c59094bfb",
#                    "0x28db2df574d6cb6d353c02c5b5ae1aa28702d9ccb8eaaa88e4a2c80c52d4368a"]
#     }

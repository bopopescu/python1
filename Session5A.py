#Single Value Container
num = 10

#Multi value Container
numbers = 10, 20, 30, 40, 50
"""
    state    partyA    partyB
-----------------------------------
    Punjab   34567     12345
    Haryana  23111     67655
    Himachal 76551     23982
    Up        11123    33121
    Goa       54134    12332
"""
punjabPartyA = 34567
haryanaPartyA = 23111
himachalPartyA = 76551
upPartyA = 11123
goaPartyA = 54134

punjabPartyB = 12345
haryanaPartyB = 67655
himachalPartyB = 23982
upPartyB = 33121
goaPartyB = 12332

partyAVoteCount = punjabPartyA + haryanaPartyA +himachalPartyA + upPartyA + goaPartyA
partyBVoteCount = punjabPartyB + haryanaPartyB+himachalPartyB + upPartyB + goaPartyB

print(">> partyAVoteCount:", partyAVoteCount)
print(">> partyBVoteCount:", partyBVoteCount)

if partyAVoteCount > partyBVoteCount:
    print(">> PartyA won election by",(partyAVoteCount - partyBVoteCount),"votes")
else:
    print(">> PartyB won election by", (partyBVoteCount - partyAVoteCount), "votes")

#                0       1      2        3      4
partyAVotes =  34567 , 23111 , 76551 , 11123 , 54134
partyBVotes =  12345 , 67655 , 23982 , 33121 , 12332

partyAVoteCount = 0
partyBVoteCount = 0








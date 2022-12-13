from enum import Enum


class ReplicaState(Enum):
    FOLLOWER = 0
    CANDIDATE = 1
    LEADER = 2

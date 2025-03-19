import ccxtProvider from "./ccxtProvider";
import { IAgentRuntime } from "@elizaos/core";

const data = ccxtProvider.get(this.runtime, {
    userId: this.runtime.agentId,
    roomId: roomId,
    agentId: this.runtime.agentId,
    content: {
        text: "generate tweet",
        action: "TWEET",
    },
});

console.log(data);
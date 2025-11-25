from mcp_servers.multiMCP import MultiMCP


class AgentLoop:

    def __init__(self, perception_prompt_path: str, decision_prompt_path: str, multi_mcp: MultiMCP, strategy: str = "exploratory"):

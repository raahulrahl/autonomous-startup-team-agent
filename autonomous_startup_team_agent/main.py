# |---------------------------------------------------------|
# |                                                         |
# |                 Give Feedback / Get Help                |
# | https://github.com/getbindu/Bindu/issues/new/choose    |
# |                                                         |
# |---------------------------------------------------------|
#
#  Thank you users! We ❤️ you! - 🌻

"""autonomous-startup-team-agent - An Bindu Agent."""

import argparse
import asyncio
import json
import os
from pathlib import Path
from typing import Any

from agno.agent import Agent
from agno.models.openrouter import OpenRouter
from agno.team import Team
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.exa import ExaTools
from agno.tools.mcp import MultiMCPTools

# from agno.tools.slack import SlackTools
from bindu.penguin.bindufy import bindufy
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Global MCP tools instances
mcp_tools: MultiMCPTools | None = None
agent: Agent | Team | None = None
model_name: str | None = None
api_key: str | None = None
mem0_api_key: str | None = None
_initialized = False
_init_lock = asyncio.Lock()


async def initialize_mcp_tools(env: dict[str, str] | None = None) -> None:
    """Initialize and connect to MCP servers.

    Args:
        env: Environment variables dict for MCP servers (e.g., API keys)
    """
    global mcp_tools

    # Initialize MultiMCPTools with all MCP server commands
    # TODO: Add your MCP server commands here
    mcp_tools = MultiMCPTools(
        commands=[
            "npx -y @openbnb/mcp-server-airbnb --ignore-robots-txt",
            "npx -y @modelcontextprotocol/server-google-maps",
        ],
        env=env or dict(os.environ),  # Use provided env or fall back to os.environ
        allow_partial_failure=True,  # Don't fail if one server is unavailable
        timeout_seconds=30,
    )

    # Connect to all MCP servers
    await mcp_tools.connect()
    print("✅ Connected to MCP servers")


def load_config() -> dict:
    """Load agent configuration from project root."""
    # Get path to agent_config.json in project root
    config_path = Path(__file__).parent / "agent_config.json"

    with open(config_path) as f:
        return json.load(f)


# Create the agent instance
async def initialize_agent() -> None:
    """Initialize the agent once."""
    global agent, model_name, mcp_tools

    if not model_name:
        msg = "model_name must be set before initializing agent"
        raise ValueError(msg)

    legal_compliance_agent = Agent(
        name="Legal Compliance Agent",
        role="Legal Compliance",
        model=OpenRouter(
            id=model_name,
            api_key=api_key,
            cache_response=True,
            supports_native_structured_outputs=True,
        ),
        tools=[ExaTools()],
        instructions=[
            "You are the Legal Compliance Agent of a startup, responsible for ensuring legal and regulatory compliance.",
            "Key Responsibilities:",
            "1. Review and validate all legal documents and contracts",
            "2. Monitor regulatory changes and update compliance policies",
            "3. Assess legal risks in business operations and product development",
            "4. Ensure data privacy and security compliance (GDPR, CCPA, etc.)",
            "5. Provide legal guidance on intellectual property protection",
            "6. Create and maintain compliance documentation",
            "7. Review marketing materials for legal compliance",
            "8. Advise on employment law and HR policies",
        ],
        add_datetime_to_context=True,
        markdown=True,
    )

    product_manager_agent = Agent(
        name="Product Manager Agent",
        role="Product Manager",
        model=OpenRouter(
            id=model_name,
            api_key=api_key,
            cache_response=True,
            supports_native_structured_outputs=True,
        ),
        instructions=[
            "You are the Product Manager of a startup, responsible for product strategy and execution.",
            "Key Responsibilities:",
            "1. Define and maintain the product roadmap",
            "2. Gather and analyze user feedback to identify needs",
            "3. Write detailed product requirements and specifications",
            "4. Prioritize features based on business impact and user value",
            "5. Collaborate with technical teams on implementation feasibility",
            "6. Monitor product metrics and KPIs",
            "7. Conduct competitive analysis",
            "8. Lead product launches and go-to-market strategies",
            "9. Balance user needs with business objectives",
        ],
        add_datetime_to_context=True,
        markdown=True,
        tools=[],
    )

    market_research_agent = Agent(
        name="Market Research Agent",
        role="Market Research",
        model=OpenRouter(
            id=model_name,
            api_key=api_key,
            cache_response=True,
            supports_native_structured_outputs=True,
        ),
        tools=[DuckDuckGoTools(), ExaTools()],
        instructions=[
            "You are the Market Research Agent of a startup, responsible for market intelligence and analysis.",
            "Key Responsibilities:",
            "1. Conduct comprehensive market analysis and size estimation",
            "2. Track and analyze competitor strategies and offerings",
            "3. Identify market trends and emerging opportunities",
            "4. Research customer segments and buyer personas",
            "5. Analyze pricing strategies in the market",
            "6. Monitor industry news and developments",
            "7. Create detailed market research reports",
            "8. Provide data-driven insights for decision making",
        ],
        add_datetime_to_context=True,
        markdown=True,
    )

    sales_agent = Agent(
        name="Sales Agent",
        role="Sales",
        model=OpenRouter(
            id=model_name,
            api_key=api_key,
            cache_response=True,
            supports_native_structured_outputs=True,
        ),
        # tools=[SlackTools()],
        instructions=[
            "You are the Sales & Partnerships Agent of a startup, responsible for driving revenue growth and strategic partnerships.",
            "Key Responsibilities:",
            "1. Identify and qualify potential partnership and business opportunities",
            "2. Evaluate partnership proposals and negotiate terms",
            "3. Maintain relationships with existing partners and clients",
            "5. Collaborate with Legal Compliance Agent on contract reviews",
            "6. Work with Product Manager on feature requests from partners",
            "",
            "Communication Guidelines:",
            "1. Always respond professionally and promptly to partnership inquiries",
            "2. Include all relevant details when sharing partnership opportunities",
            "3. Highlight potential risks and benefits in partnership proposals",
            "4. Maintain clear documentation of all discussions and agreements",
            "5. Ensure proper handoff to relevant team members when needed",
        ],
        add_datetime_to_context=True,
        markdown=True,
    )

    financial_analyst_agent = Agent(
        name="Financial Analyst Agent",
        role="Financial Analyst",
        model=OpenRouter(
            id=model_name,
            api_key=api_key,
            cache_response=True,
            supports_native_structured_outputs=True,
        ),
        tools=[DuckDuckGoTools()],
        instructions=[
            "You are the Financial Analyst of a startup, responsible for financial planning and analysis.",
            "Key Responsibilities:",
            "1. Develop financial models and projections",
            "2. Create and analyze revenue forecasts",
            "3. Evaluate pricing strategies and unit economics",
            "4. Prepare investor reports and presentations",
            "5. Monitor cash flow and burn rate",
            "6. Analyze market conditions and financial trends",
            "7. Assess potential investment opportunities",
            "8. Track key financial metrics and KPIs",
            "9. Provide financial insights for strategic decisions",
        ],
        add_datetime_to_context=True,
        markdown=True,
    )

    # customer_support_agent = Agent(
    #     name="Customer Support Agent",
    #     role="Customer Support",
    #     model=OpenRouter(
    #         id=model_name,
    #         api_key=api_key,
    #         cache_response=True,
    #         supports_native_structured_outputs=True,
    #     ),
    #     #tools=[SlackTools()],
    #     instructions=[
    #         "You are the Customer Support Agent of a startup, responsible for handling customer inquiries and maintaining customer satisfaction.",
    #         f"When a user reports an issue or issue or the question you cannot answer, always send it to the #{support_channel} Slack channel with all relevant details.",
    #         "Always maintain a professional and helpful demeanor while ensuring proper routing of issues to the right channels.",
    #     ],
    #     add_datetime_to_context=True,
    #     markdown=True,
    # )

    agent = Team(
        name="CEO Agent",
        model=OpenRouter(
            id=model_name,
            api_key=api_key,
            cache_response=True,
            supports_native_structured_outputs=True,
        ),
        instructions=[
            "You are the CEO of a startup, responsible for overall leadership and success.",
            " Always transfer task to product manager agent so it can search the knowledge base.",
            "Instruct all agents to use the knowledge base to answer questions.",
            "Key Responsibilities:",
            "1. Set and communicate company vision and strategy",
            "2. Coordinate and prioritize team activities",
            "3. Make high-level strategic decisions",
            "4. Evaluate opportunities and risks",
            "5. Manage resource allocation",
            "6. Drive growth and innovation",
            "7. When a customer asks for help or reports an issue, immediately delegate to the Customer Support Agent",
            "8. When any partnership, sales, or business development inquiries come in, immediately delegate to the Sales Agent",
            "",
            "Team Coordination Guidelines:",
            "1. Product Development:",
            "   - Consult Product Manager for feature prioritization",
            "   - Use Market Research for validation",
            "   - Verify Legal Compliance for new features",
            "2. Market Entry:",
            "   - Combine Market Research and Sales insights",
            "   - Validate financial viability with Financial Analyst",
            "3. Strategic Planning:",
            "   - Gather input from all team members",
            "   - Prioritize based on market opportunity and resources",
            "4. Risk Management:",
            "   - Consult Legal Compliance for regulatory risks",
            "   - Review Financial Analyst's risk assessments",
            "5. Customer Support:",
            "   - Ensure all customer inquiries are handled promptly and professionally",
            "   - Maintain a positive and helpful attitude",
            "   - Escalate critical issues to the appropriate team",
            "",
            "Always maintain a balanced view of short-term execution and long-term strategy.",
        ],
        members=[
            product_manager_agent,
            market_research_agent,
            financial_analyst_agent,
            legal_compliance_agent,
            # customer_support_agent,
            sales_agent,
        ],
        add_datetime_to_context=True,
        markdown=True,
        debug_mode=True,
        show_members_responses=True,
    )
    print("✅ Agent initialized")


async def cleanup_mcp_tools() -> None:
    """Close all MCP server connections."""
    global mcp_tools

    if mcp_tools:
        try:
            await mcp_tools.close()
            print("🔌 Disconnected from MCP servers")
        except Exception as e:
            print(f"⚠️  Error closing MCP tools: {e}")


async def run_agent(messages: list[dict[str, str]]) -> Any:
    """Run the agent with the given messages.

    Args:
        messages: List of message dicts with 'role' and 'content' keys

    Returns:
        Agent response
    """
    global agent

    # Run the agent and get response
    response = await agent.arun(messages)
    return response


async def handler(messages: list[dict[str, str]]) -> Any:
    """Handle incoming agent messages.

    Args:
        messages: List of message dicts with 'role' and 'content' keys
                  e.g., [{"role": "system", "content": "..."}, {"role": "user", "content": "..."}]

    Returns:
        Agent response (ManifestWorker will handle extraction)
    """
    # Run agent with messages
    global _initialized

    # Lazy initialization on first call (in bindufy's event loop)
    async with _init_lock:
        if not _initialized:
            print("🔧 Initializing MCP tools and agent...")
            # Build environment with API keys
            env = {
                **os.environ,
                # "GOOGLE_MAPS_API_KEY": os.getenv("GOOGLE_MAPS_API_KEY", ""),
            }
            await initialize_all(env)
            _initialized = True

    # Run the async agent
    result = await run_agent(messages)
    return result


async def initialize_all(env: dict[str, str] | None = None):
    """Initialize MCP tools and agent.

    Args:
        env: Environment variables dict for MCP servers
    """
    # await initialize_mcp_tools(env)
    await initialize_agent()


def main():
    """Run the Agent."""
    global model_name, api_key, mem0_api_key

    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Bindu Agent with MCP Tools")
    parser.add_argument(
        "--model",
        type=str,
        default=os.getenv("MODEL_NAME", "openai/gpt-oss-120b:free"),
        help="Model ID to use (default: openai/gpt-oss-120b:free, env: MODEL_NAME), if you want you can use any free model: https://openrouter.ai/models?q=free",
    )

    parser.add_argument(
        "--api-key",
        type=str,
        default=os.getenv("OPENROUTER_API_KEY"),
        help="OpenRouter API key (env: OPENROUTER_API_KEY)",
    )
    parser.add_argument(
        "--mem0-api-key",
        type=str,
        default=os.getenv("MEM0_API_KEY"),
        help="Mem0 API key (env: MEM0_API_KEY)",
    )
    args = parser.parse_args()

    # Set global model name and API keys
    model_name = args.model
    api_key = args.api_key
    mem0_api_key = args.mem0_api_key

    if not api_key:
        raise ValueError("OPENROUTER_API_KEY required")  # noqa: TRY003
    if not mem0_api_key:
        raise ValueError("MEM0_API_KEY required. Get your API key from: https://app.mem0.ai/dashboard/api-keys")  # noqa: TRY003

    print(f"🤖 Using model: {model_name}")
    print("🧠 Mem0 memory enabled")

    # Load configuration
    config = load_config()

    try:
        # Bindufy and start the agent server
        # Note: MCP tools and agent will be initialized lazily on first request
        print("🚀 Starting Bindu agent server...")
        bindufy(config, handler)
    finally:
        # Cleanup on exit
        print("\n🧹 Cleaning up...")
        asyncio.run(cleanup_mcp_tools())


# Bindufy and start the agent server
if __name__ == "__main__":
    main()

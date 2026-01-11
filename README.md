<p align="center">
  <img src="https://raw.githubusercontent.com/getbindu/create-bindu-agent/refs/heads/main/assets/light.svg" alt="bindu Logo" width="200">
</p>

<h1 align="center">autonomous-startup-team-agent</h1>

<p align="center">
  <strong>A multi-agent Agno Team that simulates an autonomous startup workforce. Specialized AI agents (e.g., Product Manager, Market Research, Sales, Legal, Finance, Support) coordinate under a CEO agent to self-organize tasks, make strategic decisions, and drive product development, market analysis, compliance, sales execution, and customer support. Built with Agno’s team orchestration, shared knowledge, and tool integrations, it showcases scalable AI collaboration for complex, real-world business workflows.</strong>
</p>

<p align="center">
  <a href="https://github.com/raahulrahl/autonomous-startup-team-agent/actions/workflows/main.yml?query=branch%3Amain">
    <img src="https://img.shields.io/github/actions/workflow/status/raahulrahl/autonomous-startup-team-agent/main.yml?branch=main" alt="Build status">
  </a>
  <a href="https://img.shields.io/github/license/raahulrahl/autonomous-startup-team-agent">
    <img src="https://img.shields.io/github/license/raahulrahl/autonomous-startup-team-agent" alt="License">
  </a>
</p>

---

## 📖 Overview

A multi-agent Agno Team that simulates an autonomous startup workforce. Specialized AI agents (e.g., Product Manager, Market Research, Sales, Legal, Finance, Support) coordinate under a CEO agent to self-organize tasks, make strategic decisions, and drive product development, market analysis, compliance, sales execution, and customer support. Built with Agno’s team orchestration, shared knowledge, and tool integrations, it showcases scalable AI collaboration for complex, real-world business workflows.. Built on the [Bindu Agent Framework](https://github.com/getbindu/bindu) for the Internet of Agents.

**Key Capabilities:**
- 🤝 **CEO-led Team Orchestration**: Coordinates 5 specialized agents for strategic decision-making
- 🔍 **Market Intelligence**: Real-time research via DuckDuckGo and Exa tools
- 💼 **Cross-functional Analysis**: Product, finance, legal, sales, and market perspectives
- 🧠 **Memory Persistence**: Maintains context across conversations with Mem0

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- [uv](https://github.com/astral-sh/uv) package manager
- API keys for OpenRouter, Mem0, and Exa

### Installation

```bash
# Clone the repository
git clone https://github.com/raahulrahl/autonomous-startup-team-agent.git
cd autonomous-startup-team-agent

# Create virtual environment
uv venv --python 3.12.9
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
uv sync

# Configure environment
cp .env.example .env
```

### Configuration

Edit `.env` and add your API keys:

| Key | Get It From | Required |
|-----|-------------|----------|
| `OPENROUTER_API_KEY` | [OpenRouter](https://openrouter.ai/keys) | ✅ Yes |
| `MEM0_API_KEY` | [Mem0 Dashboard](https://app.mem0.ai/dashboard/api-keys) | ✅ Yes |
| `EXA_API_KEY` | [Exa Dashboard](https://exa.ai/dashboard/api-keys) | ✅ Yes |

### Run the Agent

```bash
# Start the agent
uv run python -m autonomous_startup_team_agent

# Agent will be available at http://localhost:3773
```

### Github Setup

```bash
# Initialize git repository and commit your code
git init -b main
git add .
git commit -m "Initial commit"

# Create repository on GitHub and push (replace with your GitHub username)
gh repo create raahulrahl/autonomous-startup-team-agent --public --source=. --remote=origin --push
```

---

## 💡 Usage

### Example Queries

```bash
# Market entry strategy
"Analyze our market opportunity and create a go-to-market strategy for our new SaaS product"

# Partnership evaluation
"Review this partnership proposal and assess legal, financial, and strategic implications"

# Product roadmap
"Create a product roadmap based on current market trends and competitive analysis"
```

### Input Formats

**Plain Text:**
```
Analyze the market for our AI-powered analytics platform
```

**JSON:**
```json
{
  "role": "user",
  "content": "Evaluate partnership with TechCorp for API integration. They want 20% revenue share."
}
```

### Output Structure

The agent returns structured output with:
- **CEO Strategic Synthesis**: High-level recommendations and decisions
- **Individual Agent Responses**: Detailed insights from each specialized agent
- **Markdown Formatting**: Well-structured analysis with citations
- **Action Items**: Clear next steps and risk assessments

---

## 🔌 API Usage

The agent exposes a RESTful API when running. Default endpoint: `http://localhost:3773`

### Quick Start

For complete API documentation, request/response formats, and examples, visit:

📚 **[Bindu API Reference - Send Message to Agent](https://docs.getbindu.com/api-reference/all-the-tasks/send-message-to-agent)**


### Additional Resources

- 📖 [Full API Documentation](https://docs.getbindu.com/api-reference/all-the-tasks/send-message-to-agent)
- 📦 [Postman Collections](https://github.com/GetBindu/Bindu/tree/main/postman/collections)
- 🔧 [API Reference](https://docs.getbindu.com)

---

## 🎯 Skills

### Autonomous Startup Business Execution (v1.0.0)

**Primary Capability:**
- CEO agent orchestrates 5 specialized agents (Product Manager, Market Research, Financial Analyst, Legal Compliance, Sales)
- Cross-functional team coordination for strategic business decisions

**Features:**
- **Product Manager**: Roadmap planning, feature prioritization, requirements
- **Market Research**: Competitive analysis, trends, customer insights (DuckDuckGo, Exa)
- **Financial Analyst**: Projections, pricing models, cash flow analysis (DuckDuckGo)
- **Legal Compliance**: Regulatory compliance, contract review, IP protection (Exa)
- **Sales & Partnerships**: Business development, deal negotiation, relationship management

**Best Used For:**
- Strategic planning requiring cross-functional input
- Partnership and business development evaluation
- Product roadmap creation with market validation
- Comprehensive market entry analysis
- Legal compliance review for new initiatives

**Not Suitable For:**
- Simple single-function tasks
- Real-time customer support
- Technical implementation or coding
- Tasks requiring human legal/financial authority

**Performance:**
- Average processing time: ~5-10 seconds
- Max concurrent requests: 5
- Memory per request: 512MB

---

## 🐳 Docker Deployment

### Local Docker Setup

```bash
# Build and run with Docker Compose
docker-compose up --build

# Agent will be available at http://localhost:3773
```

### Docker Configuration

The agent runs on port `3773` and requires:
- `OPENROUTER_API_KEY` environment variable
- `MEM0_API_KEY` environment variable
- `EXA_API_KEY` environment variable

Configure these in your `.env` file before running.

### Production Deployment

```bash
# Use production compose file
docker-compose -f docker-compose.prod.yml up -d
```

---

## 🌐 Deploy to bindus.directory

Make your agent discoverable worldwide and enable agent-to-agent collaboration.

### Setup GitHub Secrets

```bash
# Authenticate with GitHub
gh auth login

# Set deployment secrets
gh secret set BINDU_API_TOKEN --body "<your-bindu-api-key>"
gh secret set DOCKERHUB_TOKEN --body "<your-dockerhub-token>"
```

Get your keys:
- **Bindu API Key**: [bindus.directory](https://bindus.directory) dashboard
- **Docker Hub Token**: [Docker Hub Security Settings](https://hub.docker.com/settings/security)

### Deploy

```bash
# Push to trigger automatic deployment
git push origin main
```

GitHub Actions will automatically:
1. Build your agent
2. Create Docker container
3. Push to Docker Hub
4. Register on bindus.directory

---

## 🛠️ Development

### Project Structure

```
autonomous-startup-team-agent/
├── autonomous_startup_team_agent/
│   ├── skills/
│   │   └── autonomous_startup_team_agent/
│   │       ├── skill.yaml          # Skill configuration
│   │       └── __init__.py
│   ├── __init__.py
│   ├── __main__.py
│   ├── main.py                     # Agent entry point
│   └── agent_config.json           # Agent configuration
├── tests/
│   └── test_main.py
├── .env.example
├── docker-compose.yml
├── Dockerfile.agent
└── pyproject.toml
```

### Running Tests

```bash
make test              # Run all tests
make test-cov          # With coverage report
```

### Code Quality

```bash
make format            # Format code with ruff
make lint              # Run linters
make check             # Format + lint + test
```

### Pre-commit Hooks

```bash
# Install pre-commit hooks
uv run pre-commit install

# Run manually
uv run pre-commit run -a
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Powered by Bindu

Built with the [Bindu Agent Framework](https://github.com/getbindu/bindu)

**Why Bindu?**
- 🌐 **Internet of Agents**: A2A, AP2, X402 protocols for agent collaboration
- ⚡ **Zero-config setup**: From idea to production in minutes
- 🛠️ **Production-ready**: Built-in deployment, monitoring, and scaling

**Build Your Own Agent:**
```bash
uvx cookiecutter https://github.com/getbindu/create-bindu-agent.git
```

---

## 📚 Resources

- 📖 [Full Documentation](https://raahulrahl.github.io/autonomous-startup-team-agent/)
- 💻 [GitHub Repository](https://github.com/raahulrahl/autonomous-startup-team-agent/)
- 🐛 [Report Issues](https://github.com/raahulrahl/autonomous-startup-team-agent/issues)
- 💬 [Join Discord](https://discord.gg/3w5zuYUuwt)
- 🌐 [Agent Directory](https://bindus.directory)
- 📚 [Bindu Documentation](https://docs.getbindu.com)

---

<p align="center">
  <strong>Built with 💛 by the team from Amsterdam 🌷</strong>
</p>

<p align="center">
  <a href="https://github.com/raahulrahl/autonomous-startup-team-agent">⭐ Star this repo</a> •
  <a href="https://discord.gg/3w5zuYUuwt">💬 Join Discord</a> •
  <a href="https://bindus.directory">🌐 Agent Directory</a>
</p>

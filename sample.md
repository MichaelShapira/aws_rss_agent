

---

# 🤖 Amazon Bedrock — AWS What's New Announcements
### 📅 Date Range: February 16–18, 2026 (Today, Yesterday & Two Days Ago)

> **Feed Source:** [AWS What's New RSS Feed](https://aws.amazon.com/about-aws/whats-new/recent/feed/)
> **Retrieved:** Wednesday, February 18, 2026

---

## 📊 Summary Dashboard

| # | Announcement | Date | Category |
|---|---|---|---|
| 1 | [Amazon Bedrock Reinforcement Fine-Tuning — Open-Weight Models + OpenAI APIs](#1-amazon-bedrock-reinforcement-fine-tuning-adds-support-for-open-weight-models-with-openai-compatible-apis) | Tue, Feb 17, 2026 | Model Customization / Fine-Tuning |
| 2 | [Claude Sonnet 4.6 Now Available in Amazon Bedrock](#2-claude-sonnet-46-now-available-in-amazon-bedrock) | Tue, Feb 17, 2026 | Foundation Model / AI |

> ✅ **2 Amazon Bedrock announcements** found within the specified date range (Feb 16–18, 2026).
> ❌ **0 announcements** found on Monday, February 16, 2026 for Amazon Bedrock.

---

---

## 1. Amazon Bedrock Reinforcement Fine-Tuning Adds Support for Open-Weight Models with OpenAI-Compatible APIs

---

### 🏷️ Title
**Amazon Bedrock reinforcement fine-tuning adds support for open-weight models with OpenAI-compatible APIs**

### 📅 Published
**Tuesday, February 17, 2026 — 21:17 UTC**

### 🔗 Announcement Link
[https://aws.amazon.com/about-aws/whats-new/2026/02/amazon-bedrock-reinforcement-fine-tuning-openai](https://aws.amazon.com/about-aws/whats-new/2026/02/amazon-bedrock-reinforcement-fine-tuning-openai)

### 📂 Categories
`Amazon Bedrock` · `Artificial Intelligence`

---

### 📝 Short Description
Amazon Bedrock now extends reinforcement fine-tuning (RFT) support to popular **open-weight models**, including OpenAI GPT-OSS and Qwen models, and introduces **OpenAI-compatible fine-tuning APIs**. These capabilities make it easier for developers to improve open-weight model accuracy without requiring deep ML expertise or large labeled datasets.

---

### 📖 Long Description

#### 🎯 What Is Reinforcement Fine-Tuning (RFT)?
Reinforcement fine-tuning is a model customization technique in Amazon Bedrock that improves foundation model performance by teaching models what constitutes a "good" response through **feedback signals called rewards**. Unlike traditional fine-tuning that depends on labeled datasets, RFT uses a **feedback-driven, iterative optimization** approach to maximize reward signals — making it ideal when you can define clear, measurable success criteria.

---

#### 🚀 Key Features & Benefits

| Feature | Details |
|---|---|
| **Open-Weight Model Support** | Now supports `qwen.qwen3-32b` (Qwen3 32B) and `openai.gpt-oss-20b` (GPT-OSS 20B) |
| **OpenAI-Compatible Fine-Tuning APIs** | Responses API and Chat Completions API work out-of-the-box after fine-tuning |
| **No Deep ML Expertise Needed** | Amazon Bedrock fully automates the end-to-end RFT workflow |
| **Small Dataset Support** | Train with small sets of prompts, not large labeled datasets |
| **Improved Accuracy** | Up to **66% improvement** on average vs. base models |
| **Custom Reward Functions** | Use AWS Lambda for custom grading logic; supports rule-based and AI-judge graders |
| **Built-in Templates** | Ready-made templates for objective tasks (code gen, math) & subjective tasks (instruction following) |
| **Intermediate Checkpoints** | Access mid-training checkpoints to evaluate, debug & select the best model |
| **Secure Environment** | All proprietary data remains within AWS's secure, governed environment |

---

#### ⚙️ How Reinforcement Fine-Tuning Works (Technical Details)

Amazon Bedrock automates the full RFT workflow using **Group Relative Policy Optimization (GRPO)**:

```
1. Model receives prompts from training dataset
2. Generates multiple responses per prompt
3. Responses are scored by a reward function
4. Prompt-response pairs + scores are used to train via GRPO policy-based learning
5. Training loop continues until end-of-data or manually stopped at a checkpoint
6. Output: A model optimized for your specific success metric
```

**Reward Function Options:**
- ✅ **Verifiable rule-based graders** — for objective tasks (code generation, math reasoning)
- ✅ **AI-based judges** — for subjective tasks (instruction following, conversational quality)
- ✅ **AWS Lambda custom grading logic** — for business-specific requirements

**Supported RFT Models at Launch:**

| Provider | Model | Model ID | Region |
|---|---|---|---|
| Amazon | Nova 2 Lite | `amazon.nova-2-lite-v1:0:256k` | US East (N. Virginia) |
| OpenAI | GPT-OSS 20B | `openai.gpt-oss-20b` | US West (Oregon) |
| Qwen | Qwen3 32B | `qwen.qwen3-32b` | US West (Oregon) |

**Post Fine-Tuning Inference:**
After fine-tuning completes, the resulting model can be used **immediately** for on-demand inference through Amazon Bedrock's OpenAI-compatible APIs — **no additional deployment steps required**.

---

#### 💼 Business Use Cases
RFT is ideal for:
- 🔢 **Mathematical problem-solving & code generation** — rule-based graders for objective evaluation
- 🔬 **Scientific reasoning & structured data analysis**
- ✍️ **Instruction following, content moderation, creative writing** — via AI-based judges
- 🔁 **Multi-turn problem solving** requiring step-by-step reasoning
- 💰 **Cost optimization** — fine-tune smaller, faster, cheaper models while maintaining quality
- 🏢 **Enterprise customization** — complex business rules and policies

---

#### 🛡️ Security & Compliance
- All proprietary training data stays within AWS's secure, governed environment
- No data leaves the AWS boundary during the customization process

---

#### 📚 AWS Documentation

- 📘 **[Reinforcement Fine-Tuning User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/reinforcement-fine-tuning.html)** — Complete documentation on customizing models with RFT
- 📘 **[Fine-tune Amazon Nova models with RFT](https://docs.aws.amazon.com/bedrock/latest/userguide/rft-nova-models.html)** — Nova-specific RFT guidance
- 📘 **[Fine-tune open-weight models using OpenAI-compatible APIs](https://docs.aws.amazon.com/bedrock/latest/userguide/fine-tuning-openai-apis.html)** — OpenAI API compatibility documentation
- 📘 **[Evaluate your RFT model](https://docs.aws.amazon.com/bedrock/latest/userguide/rft-evaluate-model.html)** — Evaluation & checkpointing guide

---

#### 💡 Best Practices (from AWS Docs)
> - **Start small**: Begin with 100–200 examples and scale gradually
> - **Baseline first**: Test base model performance before RFT. If rewards are >95%, RFT may be unnecessary
> - **Monitor training**: Watch for overfitting (train rewards increase, validation rewards decrease)
> - **Optimize reward functions**: Execute within seconds, minimize external API calls, use efficient algorithms

---

---

## 2. Claude Sonnet 4.6 Now Available in Amazon Bedrock

---

### 🏷️ Title
**Claude Sonnet 4.6 now available in Amazon Bedrock**

### 📅 Published
**Tuesday, February 17, 2026 — 15:43 UTC**

### 🔗 Announcement Link
[https://aws.amazon.com/about-aws/whats-new/2026/02/claude-sonnet-4.6-available-in-amazon-bedrock/](https://aws.amazon.com/about-aws/whats-new/2026/02/claude-sonnet-4.6-available-in-amazon-bedrock/)

### 📂 Categories
`Amazon Bedrock` · `Artificial Intelligence`

---

### 📝 Short Description
Amazon Bedrock now supports **Claude Sonnet 4.6** from Anthropic — their best computer use model to date. Sonnet 4.6 approaches Opus 4.6 intelligence at a lower cost, making it ideal for high-volume coding, knowledge work, browser-based automation, and multi-step agentic orchestration.

---

### 📖 Long Description

#### 🎯 What Is Claude Sonnet 4.6?
Claude Sonnet 4.6 is Anthropic's latest Sonnet-series model and represents a **direct upgrade to Claude Sonnet 4.5**. It delivers frontier performance across coding, autonomous agents, and professional work at scale. According to Anthropic, Sonnet 4.6 is their **best computer use model yet**, enabling organizations to deploy browser-based automation across business tools with near-human reliability.

---

#### 🚀 Key Features & Benefits

| Capability | Details |
|---|---|
| **Computer Use / Browser Automation** | Best-in-class for browser automation; near-human reliability across business tools |
| **Agentic Workflows** | Fills both lead agent & sub-agent roles in multi-model pipelines |
| **Context Compaction** | Advanced context compaction capabilities for long-horizon tasks |
| **High-Volume Coding** | Fast, high-quality task completion for large-scale coding workloads |
| **Professional Precision** | Domain-specific apps: spreadsheets, financial models, compliance review, data summarization |
| **Cost Efficiency** | Approaches Opus 4.6 intelligence at a significantly lower price point |
| **Easy Migration** | Only minor prompting adjustments needed from Sonnet 4.5 |
| **Conversation Quality** | Reliable single and multi-turn exchanges for search and chat applications |

---

#### ⚙️ Technical Details

**Model Positioning:**
```
Claude Model Hierarchy (Anthropic, Feb 2026):
├── Claude Opus 4.6   → Highest intelligence, best for complex enterprise agentic tasks
└── Claude Sonnet 4.6 → Near-Opus intelligence at lower cost, ideal for high-volume workloads
    └── Upgrade from: Claude Sonnet 4.5
```

**Strengths by Use Case:**

| Use Case | Capability |
|---|---|
| 🤖 **Agentic Tasks** | Complex multi-step orchestration, lead & sub-agent roles, less oversight needed |
| 💻 **Coding** | High-volume coding with iteration speed and accuracy |
| 🌐 **Browser Automation** | Near-human reliability for enterprise browser/GUI tasks |
| 📊 **Financial Analysis** | Spreadsheet creation, financial modelling, accelerated analysis workflows |
| ⚖️ **Compliance Review** | Meticulous attention to detail for regulatory and compliance processes |
| 📋 **Data Summarization** | Fast and accurate summarization at scale |
| 🔍 **Search & Chat** | Consistent conversational quality across single and multi-turn exchanges |

**Key Differentiators vs. Sonnet 4.5:**
- Superior computer use and browser automation (best in Anthropic lineup)
- Enhanced multi-model pipeline orchestration (lead + sub-agent roles)
- Better context compaction for extended workflows
- Only minor prompt changes required for migration

---

#### 🌍 Availability
Claude Sonnet 4.6 is now **generally available in Amazon Bedrock**. For a complete list of supported AWS Regions, see the supported models documentation below.

---

#### 📚 Relevant Links & Resources

| Resource | Link |
|---|---|
| 📘 **AWS Documentation — Supported Models** | [docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html) |
| 📰 **About Amazon Blog** | [aboutamazon.com — Anthropic Claude 4 Opus & Sonnet on Amazon Bedrock](https://www.aboutamazon.com/news/aws/anthropic-claude-4-opus-sonnet-amazon-bedrock) |
| 🖥️ **Amazon Bedrock Console** | [console.aws.amazon.com/bedrock/](https://console.aws.amazon.com/bedrock/) |
| 📘 **Anthropic Claude Models on Bedrock** | [docs.aws.amazon.com/bedrock/latest/userguide/claude-messages-supported-models.html](https://docs.aws.amazon.com/bedrock/latest/userguide/claude-messages-supported-models.html) |
| 🔀 **Model Features by Amazon Bedrock** | [docs.aws.amazon.com/bedrock/latest/userguide/models-features.html](https://docs.aws.amazon.com/bedrock/latest/userguide/models-features.html) |

---

#### 🔗 Related Bedrock Model — Claude Opus 4.6
Also launched recently (Feb 5, 2026), **Claude Opus 4.6** is Anthropic's most intelligent model and is also available in Amazon Bedrock:
- 🏆 **World's best model for coding**, enterprise agents, and professional work (per Anthropic)
- Supports **200K and 1M context tokens (preview)**
- Designed for complex, multi-step orchestration, large codebases, and end-to-end enterprise workflows
- [Announcement](https://aws.amazon.com/about-aws/whats-new/2026/2/claude-opus-4.6-available-amazon-bedrock/) | [About Amazon Blog](https://www.aboutamazon.com/news/aws/anthropic-claude-4-opus-sonnet-amazon-bedrock)

---

---

## 🔍 Additional Context — Amazon Bedrock Platform

These two announcements reinforce Amazon Bedrock's strategy as the **premier platform for enterprise generative AI**:

```
Amazon Bedrock Strategic Pillars (Feb 2026):
├── 🧠 Foundation Models — Growing catalog incl. Anthropic Claude, open-weight (Qwen, GPT-OSS), etc.
├── 🔧 Model Customization — RFT, supervised fine-tuning, custom model import
├── 🤝 OpenAI Compatibility — bedrock-mantle endpoint + OpenAI-compatible APIs (Chat, Responses)
├── 🔐 Enterprise Security — PrivateLink support, data never leaves AWS boundary
└── 🤖 Agentic Framework — AgentCore (Browser, Memory, Gateway), multi-agent collaboration
```

---

## 📎 Quick Reference — All Links

| Description | URL |
|---|---|
| 🔗 Amazon Bedrock RFT — Announcement | [aws.amazon.com/whats-new…bedrock-reinforcement-fine-tuning-openai](https://aws.amazon.com/about-aws/whats-new/2026/02/amazon-bedrock-reinforcement-fine-tuning-openai) |
| 🔗 Claude Sonnet 4.6 — Announcement | [aws.amazon.com/whats-new…claude-sonnet-4.6-available-in-amazon-bedrock](https://aws.amazon.com/about-aws/whats-new/2026/02/claude-sonnet-4.6-available-in-amazon-bedrock/) |
| 📘 RFT Documentation | [docs.aws.amazon.com/bedrock/…/reinforcement-fine-tuning.html](https://docs.aws.amazon.com/bedrock/latest/userguide/reinforcement-fine-tuning.html) |
| 📘 Fine-tune with OpenAI-Compatible APIs | [docs.aws.amazon.com/bedrock/…/fine-tuning-openai-apis.html](https://docs.aws.amazon.com/bedrock/latest/userguide/fine-tuning-openai-apis.html) |
| 📘 Evaluate RFT Models | [docs.aws.amazon.com/bedrock/…/rft-evaluate-model.html](https://docs.aws.amazon.com/bedrock/latest/userguide/rft-evaluate-model.html) |
| 📘 Supported Models in Bedrock | [docs.aws.amazon.com/bedrock/…/models-supported.html](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html) |
| 📘 Anthropic Claude Supported Models | [docs.aws.amazon.com/bedrock/…/claude-messages-supported-models.html](https://docs.aws.amazon.com/bedrock/latest/userguide/claude-messages-supported-models.html) |
| 📰 About Amazon Blog (Claude 4) | [aboutamazon.com/news/aws/anthropic-claude-4-opus-sonnet-amazon-bedrock](https://www.aboutamazon.com/news/aws/anthropic-claude-4-opus-sonnet-amazon-bedrock) |
| 🖥️ Amazon Bedrock Console | [console.aws.amazon.com/bedrock/](https://console.aws.amazon.com/bedrock/) |
| 📡 AWS What's New RSS Feed | [aws.amazon.com/about-aws/whats-new/recent/feed/](https://aws.amazon.com/about-aws/whats-new/recent/feed/) |

---

> 📌 **Note:** No Amazon Bedrock announcements were published on **Monday, February 16, 2026** (two days ago). All 2 relevant items were published on **Tuesday, February 17, 2026** (yesterday).
>
> *Generated from live AWS What's New RSS Feed on Wednesday, February 18, 2026.*

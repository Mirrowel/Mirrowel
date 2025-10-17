# Mirrowel

I like building small, practical systems that are easy to run, extend, and learn from. A lot of my recent work connects LLMs to apps, games, and tools — but I’m equally interested in general backend services, real-time features, release/automation tooling, and well-documented developer experiences.

<p align="left">
  <a href="https://github.com/Mirrowel">
    <img src="https://img.shields.io/github/followers/Mirrowel?label=Follow&style=flat&logo=github" alt="GitHub followers" />
  </a>
  <a href="https://github.com/Mirrowel">
    <img src="https://img.shields.io/github/stars/Mirrowel?affiliations=OWNER&style=flat&logo=github" alt="GitHub user stars" />
  </a>
  <a href="https://ko-fi.com/C0C0UZS4P">
    <img src="https://img.shields.io/badge/Support-Ko--fi-ff5f5f?logo=ko-fi&logoColor=white" alt="Ko-fi" />
  </a>
  <a href="https://img.shields.io/badge/PRs-welcome-brightgreen.svg">
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome" />
  </a>
  <a href="#">
    <img src="https://komarev.com/ghpvc/?username=Mirrowel&style=flat&color=blue" alt="Profile views" />
  </a>
  <a href="#"> 
    <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/Mirrowel/Mirrowel/main/badges/downloads-total.json" alt="Release downloads" /> 
  </a>
</p>

---

## TL;DR
Python/TS developer focused on small, reliable systems. Highlights: Mirrobot (Discord AI assistant), LLM-API-Key-Proxy (my “star” project), and ImaginAI (interactive fiction platform, WIP). Open to junior/mid roles, contract work, and collaborations.

---

## What I build (at a glance)
- Developer tooling that stays simple to deploy and operate
- Integrations and middleware that de-risk provider choices
- Bots and automation for communities (Discord assistance, moderation, support)
- Lightweight web apps and interactive experiences
- Modding/release utilities (uploaders, manifests, small GUIs)

I like clear docs, .env-first configuration, and observability that helps you debug under real-world conditions.

---

## Spotlight projects

### Mirrobot — Discord AI assistant for tech support + moderation
- What: An AI/LLM-integrated Discord assistant for server support, inline Q&A, pattern-based help, and moderation utilities (thread cleanup, role-aware permissions).
- Role: I maintain the codebase and own key features (AI chat, response/config system, permissions, thread management).
- Tech: Python, discord.py, asyncio; environment-based config; per-guild settings.
- Repo: https://github.com/Mirrowel/Mirrobot-py  
<!-- short demo GIF/screenshot here -->
<!-- <img src="https://your.cdn/demo/mirrobot.gif" alt="Mirrobot demo" width="600"/> -->

### LLM-API-Key-Proxy — OpenAI-compatible proxy + resilience library
- What: A self-hosted proxy exposing a single OpenAI-style API while managing provider keys, per-model cooldowns, retries, and detailed logging. Designed to be provider-agnostic and easy to test locally (Windows EXE included).
- Role: Author/maintainer; built the core key selection/cooldown logic and request tracing.
- Tech: Python, FastAPI, litellm; OpenAI-compatible endpoints.
- Repo: https://github.com/Mirrowel/LLM-API-Key-Proxy  
<!-- short architecture diagram/GIF -->
<!-- <img src="https://your.cdn/demo/proxy-arch.png" alt="LLM Proxy architecture" width="600"/> -->

### ImaginAI — Scenario-driven interactive fiction platform (WIP, main focus)
- What: A scenario-based interactive fiction platform where player actions drive LLM-generated storylines. The platform centers on:
  - Scenario Templates (plot essentials, AI instructions, “cards” for characters/locations/items)
  - Adventures as snapshots of scenarios (editable turns, retry/continue, local persistence)
  - A Python backend with a REST API and PostgreSQL database, plus a web frontend — all integrating the same LLM Proxy library for provider flexibility
- Vision: Grow into a small commercial IF platform — approachable authoring tools, smooth play sessions, and (future) multi-user features. Mod-friendly and portable by design.
- Status: Current repo runs browser-first; Python REST backend with PostgreSQL is in progress; the LLM proxy is the integration backbone.
- Repo: https://github.com/Mirrowel/ImaginAI  
<!-- short gameplay GIF/screenshot here -->
<!-- <img src="https://your.cdn/demo/imaginai.gif" alt="ImaginAI demo" width="600"/> -->

#### Contributions & maintenance
- TALKER (S.T.A.L.K.E.R. Anomaly mod) — currently the main maintainer; ensure compatibility and integrations (pairs nicely with the LLM Proxy).  
  https://github.com/danclave/TALKER
- QuizGard — university engineering project; I implemented the WebSocket layer (real-time connectivity and main game logic integration).  
  Note: private repository; code is closed per license (I retain access).

---

## Try it locally / quick links

- LLM-API-Key-Proxy
  - OpenAI client:
    ```python
    import openai
    client = openai.OpenAI(base_url="http://127.0.0.1:8000/v1", api_key="<PROXY_API_KEY>")
    resp = client.chat.completions.create(
        model="gemini/gemini-2.5-flash",
        messages=[{"role":"user","content":"Hello"}]
    )
    print(resp.choices[0].message.content)
    ```
  - curl:
    ```bash
    curl -X POST http://127.0.0.1:8000/v1/chat/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer <PROXY_API_KEY>" \
      -d '{"model":"gemini/gemini-2.5-flash","messages":[{"role":"user","content":"Hello"}]}'
    ```

- Mirrobot
  - Quick start: set bot token and AI provider via .env/config, invite bot, configure per-guild settings, run main.py. See repo README and /docs for commands and examples.

- ImaginAI
  - Current repo runs in the browser (see README for .env). Backend (Python REST + PostgreSQL) is in progress and will sit behind the LLM Proxy.

---

## Skills & tools
- Languages: Python, TypeScript/JavaScript, Lua
- Backend & systems: FastAPI, REST/WS, asyncio, real-time features
- Web: Vite, React, vanilla TS apps
- Bots & automation: discord.py, moderation helpers, server utilities
- Integrations: OpenAI-compatible APIs, Gemini/Gemma via litellm, provider-agnostic middleware
- Tooling: release uploaders, manifests, small desktop GUIs (Tkinter/CustomTkinter)
- Practices: .env-driven config, logging/observability, tidy docs and deployment guides

Note: While many repos here involve LLMs, I’m not limited to that space — I enjoy general backend work, real-time systems, and practical tooling.

---

## Other game mods (S.T.A.L.K.E.R. Anomaly)
- Scripts & game systems: Lua scripting for in-game logic and systems behavior.
- Assets integrated: textures, models, animations (sourced from other mods/creators; integration and configuration on my side).
- Focus: features that feel cohesive in-game and are friendly to maintain.

---

## Values & approach
- Practical resilience: build tooling that keeps running under real-world conditions (key rotation, per-model cooldowns, detailed logging).
- Interoperability: open, provider-agnostic interfaces (OpenAI-compatible proxy, modular providers).
- Community-first: tools for modders, server admins, and creators — from automated release uploaders to in-game dialogue AI.
- How I work: prefer small, well-documented modules, and clear “how to run it” guides.

---

## Now
- 🔭 I’m currently working on
  - ImaginAI: backend (Python REST + PostgreSQL), authoring tools, and gameplay UX; integrating the LLM Proxy across services.
  - [Codexia (prototyping)](https://gist.github.com/Mirrowel/7bfb15ac257d7f154fc42f256f2d6964): a self-hostable AI agent for GitHub repositories (daemon + orchestrator + sub-agents), with focus on resilience, sandboxing, and auditable transcripts.

- 🌱 I’m currently learning
  - Postgres schema design and migration workflows; REST API design for authoring/playback flows.
  - Production hardening for containerized agents: Docker sandboxing, network whitelisting, resource limits.
  - Observability stacks and structured logging for small services.
  - Persona/permissions systems, hierarchical config, and resumable agent runs.
  - Frontend UX for scenario editors and story playback; a bit more React/Vite ergonomics.

- 👯 I’m looking to collaborate on
  - ImaginAI: gameplay UX, scenario editor polish, persistence design, and (future) multi-user/playtesting.
  - Codexia: daemon orchestration, GitHub API tooling, action packaging, and sandbox/security policies.

- 🤔 I’m looking for help with
  - ImaginAI: playtesting, feedback on authoring flows, and ideas for scenario/card formats.
  - Codexia: best practices for container networking policies, circuit breakers, and checkpoint/resume strategies.

---

## Availability
Open to opportunities and collaborations (junior/mid roles, contract work). If you’re building with LLMs, bots, interactive systems, or just want reliable glue code and tooling, I’m happy to help.

## Contact
Reach out via GitHub issues in my repos for project questions or collaborations. You can also find me on:
- Discord: Mirrowel  
- Reddit: [u/Mirrowel](https://www.reddit.com/user/Mirrowel/)  
- Email: [mirrowel-github.appraiser015@aleeas.com](mailto:mirrowel-github.appraiser015@aleeas.com) — masked email for privacy reasons

<p>
  <a href="https://github-readme-stats.vercel.app/api/top-langs/?username=Mirrowel&layout=compact">
    <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=Mirrowel&layout=compact" alt="Top Languages" />
  </a>
</p>

<!-- Notes:
- CV is not public; I’m happy to share privately upon request.
-->


**Use the DARCM framework for all behavioural answers. See Interview Startegy.md for the full framework.**




Q1 — Difficult architectural decision under pressure

Question: "Tell me about a time you had to make a difficult architectural decision under time pressure."

DARCM Answer:

Decision:


We had to choose between a managed RAG service the client's cloud provider offered — quick to deploy, limited customisation — or building our own pipeline. Delivery deadline was 6 weeks.



Alternative rejected:


The managed service would have saved 2 weeks of engineering time but couldn't support the hybrid retrieval we needed for the client's technical jargon-heavy corpus. We evaluated it over 3 days and the retrieval precision was 0.58 vs 0.86 on our custom hybrid approach.



Risk navigated:


The risk of building custom was timeline. I reduced the scope of the first iteration, shipped a production-grade but narrower system by week 5, and built the full feature set in sprint 2.



Consequence at scale:


When the client scaled from 10 to 200 concurrent users in month 3, the custom pipeline held. The managed service we'd evaluated had a known rate limit that would have caused failures at that scale.



Measure:


Context precision at 0.86, faithfulness at 0.91 in production. Client renewed for a Phase 2 engagement.




Q2 — AI system failure in production

Question: "Describe a situation where an AI system you built failed in production. How did you handle it?"

DARCM Answer:

Decision (the one that led to the failure):


We shipped a RAG-based knowledge assistant using fixed 512-token chunks without upstream document distribution monitoring.



Alternative rejected (in hindsight):


We had considered parent-document retrieval but deprioritised it to hit the delivery date. That was the wrong call.



Risk navigated:


Three weeks after deployment, faithfulness dropped from 0.83 to 0.61. First step: confirm the problem was in the model, not the measurement pipeline. Then I pulled execution traces from LangSmith to find the first step where hallucination appeared.



Consequence & root cause:


The client had migrated their document management system, changing average document length from 3 to 18 pages. Our fixed chunks were cutting through natural section boundaries. Retrieval hit rate had dropped from 87% to 64%.



Measure & permanent fix:


Immediate mitigation: temperature to 0.0 + explicit uncertainty instruction. Permanent fix: parent-document retrieval with section-header-aware chunking. New monitoring: upstream document distribution as a health signal — P95 doc length and chunk count. This became our standard RAG deployment checklist.




Key insight for interviewers: The production monitoring improvement is the answer that wins interviews. Show that failures make your systems better.




Q3 — Convincing a stakeholder to change direction

Question: "Tell me about a time you had to convince a stakeholder to change direction on an AI/Data project."

DARCM Answer:

Decision (stakeholder's original position):


A client's CTO wanted to fine-tune a proprietary LLM on their internal documentation. Their documentation updated weekly.



Alternative I proposed:


RAG — because fine-tuning would require weekly retraining cycles at $800–1200 per run, and they had no labelled examples.



Risk navigated:


I didn't dismiss the CTO's instinct. I proposed a 2-day spike: build a RAG prototype alongside a realistic fine-tuning plan with actual timelines and costs. The fine-tuning plan showed a 3-week cycle per update. The RAG prototype returned 0.83 faithfulness in 48 hours.



Consequence:


"I didn't say 'you're wrong.' I said: 'Here's what fine-tuning would actually look like for your specific update frequency, and here's what we got from RAG in 48 hours. Which outcome serves your team better?' The decision became obvious."



Measure:


System deployed with RAG. Weekly index updates take 2 hours, zero retraining cost. System has been in production for 6 months.




The principle: Agree on the goal, be honest about the path. Let the data make the decision — not you.




Q4 — Staying current in a fast-moving field

Question: "How do you stay current in AI/ML given how fast the field moves?"

Model Answer:


I think about this in two layers — passive intake and active synthesis.

Intake: I follow Hugging Face, Papers With Code, and Anthropic/OpenAI research blogs weekly. I use a filtered ArXiv view for papers in my focus areas — retrieval, agents, and evaluation.

Active synthesis: I maintain a personal knowledge base where I connect new research to problems I've actually worked on. When I read about a new technique, I ask: "Would this have changed a decision I made on a past project?" That question converts reading into judgment.

Most recent application: I read the GraphRAG paper from Microsoft and redesigned the retrieval layer for a multi-document reasoning use case where standard RAG was failing on cross-document questions. The community detection approach improved multi-hop accuracy by approximately 34% on our eval set.

The honest answer to staying current is: you can't read everything. The skill is knowing what to prioritise, which requires knowing the problems you're likely to face next.




Always end with a specific recent example of something you read and actually applied. Name GraphRAG, DPO, MCP, or another current technique specifically.




Q5 — Mentoring a team member

Question: "Tell me about a time you mentored someone on the team. What was the outcome?"

Model Answer:


I mentored a mid-level ML engineer who was technically strong but couldn't communicate architectural decisions to stakeholders — a gap that was limiting their career progression.

What I noticed: In architecture reviews, they described what they built accurately but couldn't explain why they made the choices they made or what they'd considered and rejected.

What I did: Over 8 weeks, in every 1:1 I asked one question: "What did you consider and reject, and why?" After 3 weeks, they started anticipating the question and including the answer unprompted. I introduced Architecture Decision Records — a one-page format with decision, alternatives, rationale, trade-offs. Within 6 weeks these went directly to stakeholders with no editing from me.

Outcome: They presented a client engagement architecture independently 3 months later. The client specifically noted how clearly the decisions had been explained. They were promoted to Senior Engineer 6 months later.

The lesson: The most impactful thing you can do for a capable engineer is identify the one gap that's limiting their visibility, and focus relentlessly on that one thing.




Q6 — Saying no to a client request

Question: "Describe a time you had to say no to a client or stakeholder request. How did you handle it?"

Model Answer:


A client asked us to build an AI system that automatically scored job applicants from CVs and social media profiles with no human review step. Volume: 2,000 applications per month.

My assessment: Potential discrimination against protected characteristics, no right-to-appeal mechanism, and EU AI Act Article 22 exposure on automated employment decisions. Also commercially risky — reputational damage from a biased hiring system would far exceed any efficiency gain.

How I handled it: I didn't refuse immediately. I asked: "What's the core problem you're trying to solve — volume, consistency, or something else?" The real problem was screening inconsistency across 12 hiring managers.

Counter-proposal: An AI system that helped standardise evaluation criteria and surfaced structured signals from CVs — with a human making every yes/no decision, the AI providing recommendations only. Same efficiency gain. No regulatory risk. Defensible.

The framing: "I want to help you solve this problem, and I also want to make sure we solve it in a way that doesn't create a bigger problem 12 months from now."

Outcome: They accepted the redesigned approach.




The principle: A no without an alternative is a dead end. A no with a better path is a trust builder.




Q7 — Working with unfamiliar technology on a live project

Question: "Tell me about a time you had to deliver on a project using technology you hadn't used before."

DARCM Answer:

Decision:


I was assigned to lead the MLOps architecture for a client on GCP's Vertex AI Pipelines. My previous MLOps experience was on Kubeflow and MLflow — I had not built production pipelines on Vertex AI.



Alternative:


I could have flagged the gap and requested a different assignment or a longer discovery phase. I chose to take on the delivery because the underlying concepts — containerised pipeline steps, artifact tracking, model registry integration — were directly transferable.



Risk navigated:


I spent the first week in a structured self-learning mode: built a toy pipeline locally, read the Vertex AI documentation architecture sections (not tutorials — the architecture docs), and mapped every concept to its Kubeflow equivalent. I was transparent with the team about my learning curve and asked for 3 days before the first architecture review.



Consequence:


By day 5 I had a working skeleton pipeline. By week 3 I had deployed a training pipeline to production. The main difference from Kubeflow I had to adapt to was managed metadata tracking — Vertex ML Metadata has a different lineage model than MLflow's tracking server.



Measure:


Delivered on the original timeline. The client subsequently asked NashTech to extend the engagement to cover model monitoring — citing the quality of the pipeline architecture as the reason.




The takeaway for the interviewer: I'd rather be transparent about the learning curve and deliver on time than claim false expertise. The bridge between Kubeflow and Vertex AI was strong enough that the actual ramp-up was 3 working days, not 3 weeks.

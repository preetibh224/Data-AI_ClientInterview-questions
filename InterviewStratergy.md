**Interview Strategy**

**The Golden Rule**


Every answer must have three layers:


What you did technically
Why you made that choice over alternatives
What business outcome it drove


Missing any layer makes you sound like either a junior engineer or a strategy consultant. You need all three simultaneously.



**Stage 1 — Frame yourself as a problem solver, not a tool user**

The moment the interview starts, the client is deciding: "Is this person going to help us solve our problem, or will they need us to define it for them?"

Do this when introducing yourself:

Instead of listing your tech stack, say:


"I've spent X years helping organisations build AI systems that [specific business outcome]. Most recently I [one-sentence project with business impact]. What's the core challenge you're trying to solve?"


Opening line to practise:


"I help organisations go from AI experiments to production systems that actually work reliably. The gap between those two things is where I spend most of my time."


**Stage 2 — Lead with decisions, not descriptions**

The difference between a junior and senior candidate is not the technologies they know — it's whether they explain why they chose them.

Formula for every technical answer:

We chose [X] over [Y] because [constraint], 
accepting the trade-off of [acknowledged downside].

Example — wrong:


"We used Pinecone."

Example — right:

"We evaluated Pinecone against pgvector. We chose Pinecone because we needed sub-50ms retrieval at 2M documents — pgvector couldn't sustain that without significant engineering overhead on our timeline. The trade-off was vendor lock-in and higher cost at scale, which we accepted because speed-to-delivery was the priority."



Trigger phrase before every technical answer:


"The architectural decision I'm most proud of in that project was..."




**Stage 3 — The Exposure + Bridge Technique (most critical skill)**

When asked about a technology you haven't used directly, never say "I haven't worked with that" and stop there.

The formula:

ComponentWhat to doExposureName what you DO know that is related or analogousBridgeConnect your experience to the underlying conceptEagernessDemonstrate curiosity and fast-learning track record

Example — client asks about Databricks Unity Catalog (you haven't used it):


"I haven't worked with Unity Catalog specifically, but I've designed data governance and lineage tracking architectures using Delta Lake and Apache Atlas for similar problems — data cataloguing, access control, and lineage at scale. The core challenge they both solve is the same: ensuring data teams can trust and trace their data assets. I've been following Unity Catalog's rollout closely and reviewed its architecture for cross-workspace metadata sharing. I'd be very comfortable getting productive on it quickly."



**Key phrase:**


"I haven't used [X] specifically, but the problem it solves is [Y], which I've addressed using [Z]. The underlying approach is..."


**Stage 4 — Quantify everything**

Vague answers lose interviews. Before any interview, prepare these numbers for your last 3 projects:

DimensionWhat to captureScaleUsers, documents, queries, records per dayLatencyP95 in production, your SLAQualityEval metric, baseline, what you achievedCostWhat optimisation saved (% or absolute)BusinessRevenue, cost reduction, or risk reduction

The number test: If you can replace "significantly," "substantially," or "dramatically" with a specific number — do it. Every time.

Wrong: "It improved performance significantly."
Right: "It reduced inference latency from 1.8 seconds to 340 milliseconds, which unblocked the real-time use case the client needed."


**Stage 5 — Close every answer with a commercial connection**

Every technical answer should end with a sentence connecting it to business value.

Format:

[Technical outcome] which meant [business consequence] for the client.

Examples:
"...which reduced P95 latency from 800ms to 180ms — directly enabling the real-time customer-facing feature the product team had been blocked on for two sprints."
"...which reduced hallucination rate from 8% to 1.1% on our eval set — the specific threshold the client's legal team had set as a condition for going live."
"...which cut per-query inference cost by 48% — making the unit economics viable at the volume the client projected for Year 2."



The DARCM Framework (use instead of STAR)

STAR produces generic answers. For senior Data & AI roles, use DARCM:

LetterStands forWhat to coverDDecisionWhat architectural choice did you make?AAlternativeWhat did you evaluate and reject, and why?RRiskWhat failure mode did you design around?CConsequenceWhat happened at scale? What broke?MMeasureWhat business or technical metric improved?

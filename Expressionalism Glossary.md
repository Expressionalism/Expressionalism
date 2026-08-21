# **Expressionalism Glossary**

## **Section 1: Core Words, Terms, Phrases, Concepts (alphabetical)**

### **A**

**Adaptive Depth \[Toolkit\]**

> This toggle automatically chooses a shorter analysis for simple inputs or a deeper one for complex ones. In everyday use it keeps things manageable while still giving you the full power when you need it.

> Technical elaboration: Activates based on input variance and ambiguity score; includes Obtainment Focus sub-mode that emphasizes contrasts and obtainability in P1–P2.

> **Cross-references:** Density Probe; Light Output; Input Variance.

**Alignment \[Toolkit\]**

> This measures how well a supporting idea or reference fits with the main expression being analyzed. Higher alignment means the support is stronger and more reliable.

> Technical elaboration: Degree to which a secondary expression supports and coheres with the current primary expression; contributes 0.40 weight to Secondary Coherence Score (non-isolated components only).

> **Cross-references:** Secondary Coherence Score; Inter-Secondary Coherence; Traction.

**Alignability Spectrum \[P6\]**

> This shows how easily supporting ideas can be compared and translated relative to the main expression. It ranges from very loose connections to tight, natural fits.

> Technical elaboration: Spectrum of transduction and comparison (sparse / partial / dense) that provisions distances and divergences as utilities under P6.

> **Cross-references:** Comparability; Transduction; Secondary Synthesis Ledger.

**All-Isolated Edge Case \[Toolkit\]**

> This happens when every supporting idea falls below the minimum traction threshold. The analysis then stops relational scoring and reports a clear “no synthesis possible” result.

> Technical elaboration: Terminal state in which every component triggers hard isolation; forces Secondary Coherence Score to “N/A (all components isolated)” and Yield Type to Raw/Regressed. This is the terminal state registered by the Staging Axiom (see P1). Isolation Residual is then the isolation density of the whole abducted set.

> **Cross-references:** Hard Isolation Rule; Isolation Residual; P8 Gate.

**Ambiguity Score \[Toolkit\]**

> This number measures how clear or mixed the input chunks are. A high score tells the system the material is complex or unclear, so it adjusts settings automatically.

> Technical elaboration: Value calculated in Stage 1 from coherence of input chunks; high scores trigger Light Output and widen sigma for more porous material.

> **Cross-references:** Input Variance; Light Output.

**Anchor Priority of the Primary \[P5\]**

> The main expression being analyzed is always treated as the central reference point. All supporting ideas are judged by how well they connect back to it.

> Technical elaboration: Highest weight assigned to relations that point back to the primary (treated as related at \~1 certainty) under P5.

> **Cross-references:** Related; Secondary Coherence Score; Plurality of Expressions.

**Atomic Expression \[P4\]**

> A simple layered unit made of a sequence of basic parts that can act as a connector when placed inside something larger.

> Technical elaboration: Layered expression consisting of a sequence of relateds that functions as a relator while standing as a related when measured alone.

> **Cross-references:** Layer Spectrum; Related; Relator.

### **B**

**Balanced Yield \[P7\]**

> This is a stable result where the certainties clearly outweigh the uncertainties, giving a solid, usable summary.

> Technical elaboration: Yield type with high certainty dominance on the Yield Spectrum.

> **Cross-references:** Yield Spectrum; Tensive Yield.

**Binomial Falsification Threshold \[Toolkit\]**

> A statistical check that flags when an analysis is too inconsistent or contradictory. It uses a simple probability rule tailored to the type of input.

> Technical elaboration: Statistical check (p \= 0.18 with \+5 % reflexive tolerance) that flags persistent incoherence; uses data-type-aware thresholds (25 % for expressions, 30 % for phenomena) across 15 perturbations.

> **Cross-references:** Incoherence Flag.

**Bootstrap / Origination Asymmetry \[Computational Substrate Appendix\]**

> The system always starts with an already-formed main expression and cannot create the very first one from nothing. This is simply how the process works.

> Technical elaboration: Irreducible limit that the system always begins with an already-obtained primary expression and cannot generate the first stabilization ex nihilo; acknowledged as a methodological limit of the apparatus (Staging Axiom). Soft spot: left listed, not closed.

> **Cross-references:** P1: The Open Field; P8 Gate.

### **C**

**Candidate Claim / Proto-claim / Secondary Claim \[Toolkit\]**

> A supporting claim the toolkit guesses at and then scores. It is not one of the eight starting points.

> Technical elaboration: Operational-level items the toolkit abducts per secondary expression. Not called “presumptions.” Capped to the top items by alignment (and by explanatory coherence when the Peircean Abduction Heuristic is on).

> **Cross-references:** Eight Starting Points; Secondary Claim Temper; Required Claims for Secondary Truth Ledger.

**Certainty Table \[Toolkit\]**

> A list showing the strongest supporting ideas that passed the minimum traction test, along with how well they fit the main expression.

> Technical elaboration: Stage 3 output listing non-isolated certainties with alignment, inter-coherence, traction, and notes. Isolated components do not appear here.

> **Cross-references:** Uncertainty Table; Tempered Certainty Ledger.

**Certainty Temper Index \[Phase 5\]**

> This number shows how much careful second-guessing has softened the original strong supporting ideas.

> Technical elaboration: Metric quantifying how much reflexive doubt has softened original certainties. Isolated components generate no temper index.

> **Cross-references:** Reflexive Tension; Phase 5\.

**Certainty Temper Probe \[Toolkit\]**

> A setting that adds careful second-guessing to the strong supporting ideas during analysis. It has light and deep levels.

> Technical elaboration: Toggle that runs reflexive certainty tempering in Phase 5; includes Light and Deep sub-modes and works together with Uncertainty Probe.

> **Cross-references:** Phase 5; Temper-Probe.

**Certainty Yield Geo Avg \[Phase 3\]**

> The average strength of the best supporting ideas, calculated in a way that balances the overall set.

> Technical elaboration: Geometric mean of certainty yields; target range 0.7–0.9. Computed on non-isolated components only.

> **Cross-references:** Meaning Tension.

**Chaos Scale \[Toolkit\]**

> A control that makes the analysis more open to messy or uncertain material by widening the tolerance for variation.

> Technical elaboration: Tunable parameter (default 0.05) that increases porosity and fairness for chaotic or uncertain inputs; higher values widen sigma and raise uncertainty upper bound.

> **Cross-references:** Sigma; Uncertainty Upper Bound.

**Claim Coherence \[Phase 6\]**

> This number shows how well the claims required by the surviving supporting ideas hold together, once uncertainty is taken into account.

> Technical elaboration: Replaces Presumption Coherence. Metric of how coherently abducted or required claims support the primary while accounting for uncertainty. Formula: average alignment × (1 − 0.15 × uncertainty\_prob\_global), clamped \[0.25, 0.95\].

> **Cross-references:** Secondary Claim Temper.

**Claim-Tempered Yield \[Phase 6\]**

> This is the Tensive result after a further adjustment for how shaky or solid the required claims feel.

> Technical elaboration: Replaces Presumption-Tempered Yield. Existing relation: Tensive × (1 − 0.1 × SCT). Yield Type stays Tensive unless this variant is actually computed. Not the definition of meaning.

> **Cross-references:** Secondary Claim Temper; Tensive Yield.

**Complex Expression \[P4\]**

> A richly layered unit built from many parts and at least one connector, allowing deep nesting.

> Technical elaboration: Layered expression made of nests containing multiple relateds and at least one relator; allows unlimited nesting depth and functions as a standalone related.

> **Cross-references:** Layer Spectrum; Related; Relator.

**Connectability Gradient \[P3\]**

> How fully a difference or contrast can be woven into a usable connection rather than left as something unconnectable.

> Technical elaboration: One of the three co-emergent density dimensions of relational density (connectability, repeatability, directedness). These are not three modes.

> **Cross-references:** Relational Density Spectrum; Non-Relational Remainder.

**Contrarian \[Toolkit\]**

> A setting that deliberately looks for gaps and uncertainties by slightly lowering the expected smoothness of the input.

> Technical elaboration: Toggle that lowers input variance and actively probes non-relational gaps; often activates automatically on high ambiguity scores.

> **Cross-references:** Uncertainty Probe.

**Contrasting Parts \[P2\]**

> The natural differences, shades, or uncertainties that appear once something is being examined.

> Technical elaboration: Variances, fluid degrees, or uncertainties that appear once existence obtains under P1’s Door 1; they create the differentiations needed for later relational construction.

> **Cross-references:** P1: The Open Field; Relational Construction.

**Current Primary Expression \[P5\]**

> The main thing being looked at right now; it is treated as the central reference point during analysis.

> Technical elaboration: Immediate totality being analyzed; treated primarily as a related at \~1 certainty during analysis and co-exists with secondary expressions. Soft spot: \~1 language is left listed, not closed.

> **Cross-references:** Primary Expression; Related; Secondary Expression.

### **D**

**Data Type \[Toolkit\]**

> The system’s quick way of telling whether the input is a clear statement or something more sensory and open-ended.

> Technical elaboration: Automatic classification of an input as expression or phenomenon; adjusts incoherence thresholds and sigma. Phenomena receive wider sigma and higher uncertainty boosts.

> **Cross-references:** Phenomenal Probe.

**Decomposition Gate \[P3\]**

> The step that breaks usable differences into basic anchors and active connectors.

> Technical elaboration: Operation that breaks repeatable relational paths into relateds (passive anchors) and relators (active connectors) operating in one of two primary modes: self-pointing or other-pointing. Isolation Residual trigger is a weak flag that may trigger hard isolation; it is not a third peer mode.

> **Cross-references:** Relational Construction; Related; Relator; Two Primary Modes.

**Default Interpretive Restraint \[P6\]**

> When connections are weak or missing, the system stays cautious and does not force extra meaning.

> Technical elaboration: Operational heuristic that keeps further interpretive gestures relatively weak when traction is low or Synthesis Refusal appears; fully overridable under P8. Soft spot: left listed, not closed.

> **Cross-references:** Synthesis Refusal; P8 Gate.

**Density Probe \[Toolkit\]**

> A setting that looks inside the input to measure how layered and detailed it is.

> Technical elaboration: Toggle that computes internal variances and layering metrics in Phases 1 and 2; includes Base, Fuzzy, Weighted, and Iterative sub-modes.

> **Cross-references:** Layer Spectrum; Adaptive Depth.

**Diagnostics Block \[Toolkit\]**

> The first block of decisive numbers in a full run: what kind of yield you got, the main survivor score, and the isolation density.

> Technical elaboration: Executive Yield heading. Reports Yield Type, Secondary Coherence Score among survivors (with component disclosure), Isolation Residual as density, and Tensive when computed. Isolation Residual / isolation counts are disclosed here and in Run Metadata; later sections interpret rather than reprint.

> **Cross-references:** Secondary Coherence Score; Isolation Residual; Tensive Yield.

**Dilemma Gate \[P1\]**

> The basic check that decides whether there is enough connection to keep analyzing or whether the analysis should pause.

> Technical elaboration: Mechanism that evaluates obtainability through H(x); if result \> τ, proceeds with relational construction (Door 1); if ≤ τ, registers generative uncertainty or halts (Door 2). Soft spot: P1 door beside the halt stays listed.

> **Cross-references:** H(x); τ; P1: The Open Field.

**Directional Bleed \[Toolkit\]**

> A setting that allows influence to flow both ways between the main expression and its supporting ideas.

> Technical elaboration: Sub-toggle under Secondary Expression Equity that enables bidirectional resonance analysis; asymmetry \> 0.2 increases tension and fragility measures.

> **Cross-references:** Secondary Expression Equity.

**Dirichlet Priors \[Phase 2\]**

> A fair-sampling method that helps the system pick supporting ideas without favoring any particular viewpoint.

> Technical elaboration: Equity-balancing sampling method used to abduct secondary expressions; incorporates void-prior alphas for fair representation of non-relational gaps.

> **Cross-references:** Secondary Abduction; Secondary Expression Equity.

**δ (delta) \[Toolkit\]**

> An extra supporting number that can appear when you ask for the full density view. It is not part of the main score.

> Technical elaboration: Optional Secondary Synthesis Ledger column when Show Full Density Metrics is On. Supporting only; default weight into Secondary Coherence Score remains 0\. Isolated rows are labeled “pointing refused” rather than given a δ. Not a filled feature map.

> **Cross-references:** Secondary Synthesis Ledger; Pointing Refused.

### **E**

**Echo Mode \[Toolkit\]**

> This setting applies a gentle fading effect to older or less relevant supporting ideas so the analysis stays fresh and balanced.

> Technical elaboration: Sub-toggle under Uncertainty Probe that applies tradition-decay via priors for multiple uncertainties.

> **Cross-references:** Uncertainty Probe.

**Eight Starting Points (P1–P8) \[Framework\]**

> The eight high-level starting points the method uses. They are numbered P1 through P8 and stay numbered.

> Technical elaboration: Living name for P1–P8 in the body, Preface, Formal Model, Substrate, and Toolkit. Functional grouping: P1–P3 analysis-space starting points; P4–P5 functional conditions concerning the primitive; P6–P7 operational claims and the meaning thesis; P8 meta-rule / open renewal. The Author’s Note may still say “presumptions” as guesses-voice; do not flatten that Note into this heading, and do not put “Presumption 1” on the body titles. Ordinary “presuming” stays ordinary.

> **Cross-references:** P1–P8 (individual); Candidate Claim.

**Emptiness-First \[Toolkit\]**

> This setting flips the usual focus so that gaps and uncertainties are treated as an interpretive lens rather than problems to fix.

> Technical elaboration: Overlay only. May foreground the isolated mass interpretively. Formal Isolation Residual stays isolation density and is unaltered. The overlay does not identify Isolation Residual with the Non-relational Remainder.

> **Cross-references:** Isolation Residual; Non-Relational Remainder; Uncertainty Probe.

**Equity Sampler \[Toolkit\]**

> This setting adds a small amount of helpful randomness when choosing supporting ideas so that no single viewpoint is unfairly favored.

> Technical elaboration: Sub-toggle under Secondary Expression Equity that perturbs noise from Dirichlet priors.

> **Cross-references:** Secondary Expression Equity.

**Equitable Treatment / Reciprocity (or Secondary Expression Equity) \[Toolkit\]**

> This ensures the system draws supporting ideas from a balanced mix of sources and viewpoints rather than leaning toward any one tradition or style.

> Technical elaboration: Toggle that audits diversity and balances domains; includes multiple sub-modes for sourcing control and void emphasis.

> **Cross-references:** Dirichlet Priors; Equity Sampler.

**Expression \[Framework\]**

> Any temporary way of pulling together thoughts, feelings, or experiences into something that can be examined or shared. It can be a sentence, a memory, a painting, or even a quiet moment.

> Technical elaboration: Any provisional stabilization of secondary synthesis (thought, claim, artwork, scientific assertion, memory, perceptual scene, moment of silence, etc.).

> **Cross-references:** Pointing; Secondary Synthesis; Primary Expression.

### **F**

**Falsify Mode \[Toolkit\]**

> This setting makes the system stricter or more forgiving when checking for contradictions.

> Technical elaboration: Toggle that tightens or loosens incoherence thresholds (Lenient adds \+5 % tolerance; Strict subtracts 5 %).

> **Cross-references:** Incoherence Flag.

**Feedback-Adaptive \[Toolkit\]**

> This setting lets later stages of the analysis gently adjust earlier results so the whole picture stays consistent as new details emerge.

> Technical elaboration: Sub-toggle under Uncertainty Probe that retro-tempers Phase 1 and 2 metrics after later phases.

> **Cross-references:** Uncertainty Probe.

**Finite Multiplicity \[P5\]**

> This describes a moderate number of supporting ideas that feel complete and practical rather than endless or solitary. It is the usual default setting for most everyday analyses.

> Technical elaboration: Middle range of the MultiSpectrum; represents bounded clusters of secondary expressions and serves as the default pragmatic yield.

> **Cross-references:** MultiSpectrum; P5: Plurality of Expressions.

**Fragility Adjustment \[Harmony Index\]**

> This small boost rewards situations where the supporting ideas are productively tense or uncertain rather than perfectly smooth.

> Technical elaboration: Activates when metric variance exceeds 0.12 and raises Harmony Index by about 0.12–0.15.

> **Cross-references:** Harmony Index.

**Framework \[Framework\]**

> The main philosophical write-up of Expressionalism. You can use its distinctions without ever turning on the formal model.

> Technical elaboration: Primary philosophical articulation. Distinctions may be engaged directly without formalization. The Unified Formal Model is a representation, not a foundation.

> **Cross-references:** Unified Formal Model; Eight Starting Points.

**Functional Role Shift \[P8\]**

> Any part of the analysis can change its job — from being the main reference point to being a supporting connector — as you look at it again from a fresh angle.

> Technical elaboration: Perceptual and interpretive process allowing any node to move between related and relator status or change relational mode during re-expression; roles recorded as metadata. Hard isolation persists under any Functional Role Shift.

> **Cross-references:** P8 Gate; Related; Relator.

### **G**

**Governance Protocol \[Computational Substrate Appendix\]**

> The rule that says any change to the system’s settings must be carefully justified, tested again, logged, and treated as a brand-new starting point.

> Technical elaboration: Any parameter modification must include explicit justification against the design criteria, re-execution of validation (or equivalent), metadata logging, and treatment as a new primary expression under P8.

> **Cross-references:** Seven Design Criteria; P8 Gate.

**Guardrails \[Toolkit\]**

> This setting either brings back older safety checks for contradictions or uses gentler defaults so the analysis stays stable even when things look shaky.

> Technical elaboration: Toggle that enables old self-refutations on incoherence/low metrics or uses resilient defaults treating lows as tensive features.

> **Cross-references:** Falsify Mode.

### **H**

**Hard Isolation Rule \[Unified Formal Model / Toolkit\]**

> When a supporting idea is too weak to connect reliably, the system completely removes it from all scoring and simply notes it as an isolated gap that cannot be used.

> Technical elaboration: Post-processing filter after H(x) and the dilemma gate. Any component with traction\_i ≤ τ receives, on first occurrence in a major section, the exact label “Synthesis Refusal active — traction \= 0 — isolated remainder (excluded from aggregation and distributions)” and is excluded from all relational metrics, distributions, and yields. Later mentions in the same section may shorten to “Synthesis Refusal active.” Isolation Residual is the isolation density of those components. A single global uncertainty bump is then applied: uncertainty\_prob\_global ← clamp(uncertainty\_prob\_global \+ 0.05 × Isolation Residual, \[0.25, 0.9\]). Per-component exclusion (§6.2) and this one global bump (§6.4) are different operations, not a contradiction.

> **Cross-references:** Synthesis Refusal; Isolation Residual; τ; P8 Gate.

**Harmony Index \[Phase 6\]**

> This number shows how well the different strengths and uncertainties in the analysis balance each other out overall.

> Technical elaboration: Metric measuring balanced interplay among yields; computed as harmonic mean of yields plus fragility adjustment when variance \> 0.12. Non-isolated components only.

> **Cross-references:** Fragility Adjustment; Yield Spectrum.

### **I**

**Incoherence Flag \[Toolkit\]**

> A clear warning that appears when the supporting ideas contradict each other too much for a stable result.

> Technical elaboration: Explicit marker triggered when incidence exceeds data-type-aware thresholds across 15 perturbations with standard deviation \> 0.30; produces partial yields with boosted uncertainties.

> **Cross-references:** Binomial Falsification Threshold.

**Inferred Relator Mode Distribution (Derived) \[Toolkit / Unified Formal Model\]**

> After the weak connections have been set aside, this estimates whether the remaining supporting ideas mostly point the main expression at itself or at something else. Isolation density is reported beside that split, not as a third share of the pie.

> Technical elaboration: Computed exclusively on non-isolated components. Two-mode distribution over {Self-pointing, Other-pointing} summing to 1 on survivors. Isolation Residual is parked outside as isolation density and receives no probability mass and no positive directedness. The concrete feature map for the logits is not defined; do not restore R, D, T\_norm, U\_norm, Y\_centered.

> **Cross-references:** Two Primary Modes; Isolation Residual; Hard Isolation Rule.

**Inter-Secondary Clash \[Toolkit\]**

> A named pair of surviving supporting ideas that still pull against each other without falling out of the analysis.

> Technical elaboration: Uncertainty Table type for non-isolating tension inside the retained mesh. The Item field names the two (or few) retained secondaries. Emission is selective; silence is informative. Inter-Secondary Divergence (JSD) may inform, never force, a clash row.

> **Cross-references:** Uncertainty Table; Inter-Secondary Divergence (JSD); Retained Openness.

**Inter-Secondary Divergence (JSD) \[Toolkit\]**

> A supporting number for how much the surviving supporting ideas pull apart from one another, on average.

> Technical elaboration: Continuous supporting diagnostic of average pairwise soft-vector divergence among non-isolated secondaries. High pairwise divergence may inform (never require) an Inter-Secondary Clash row.

> **Cross-references:** Inter-Secondary Clash; Secondary Coherence Score.

**Isolation Density \[Unified Formal Model / Toolkit\]**

> The share of supporting ideas that failed to connect at all.

> Technical elaboration: Proportion of components with traction\_i ≤ τ. This is the measure of Isolation Residual. It is not 1 − \[P(Self-pointing) \+ P(Other-pointing)\]. “Parked outside” means sitting beside the two-mode softmax, not a leftover slice of that softmax.

> **Cross-references:** Isolation Residual; Hard Isolation Rule.

**Isolation Residual \[Unified Formal Model / Toolkit\]**

> The measurable density of supporting ideas that refused to connect. It is a count-based density, not a third way of pointing, and not the leftover mystery of the expression.

> Technical elaboration: Failure of a secondary to gain sufficient traction. Traction ≤ τ → hard isolation, exclusion from relational metrics and distributions, directedness undefined (“pointing refused”). Measured as isolation density. This is the primary technical sense formerly carried by the bare word “Residual.” Isolation Residual is not residual openness and is not the Non-relational Remainder. Residual openness, when used in prose, belongs to Remainder / horizon — it is not this density.

> **Cross-references:** Isolation Density; Pointing Refused; Hard Isolation Rule; Non-Relational Remainder; Retained Openness.

**Isolation Residual Trigger / Non-rel-probe \[P3 / Unified Formal Model\]**

> A weak warning flag that a contrast may not be connectable. It can send a supporting idea into isolation. It is not a third way of pointing.

> Technical elaboration: Weak flag only. May trigger isolation. Not a third peer mode. Receives no probability mass inside the two-mode distribution. Replaces living “Non-Rel-Probe Mode” as a peer of self-pointing and other-pointing.

> **Cross-references:** Isolation Residual; Two Primary Modes; Decomposition Gate.

### **(JK)**

### **L**

**Layer Spectrum \[P4\]**

> This shows how simply or complexly the parts of an expression are stacked together, from single pieces to deeply nested structures.

> Technical elaboration: Hierarchical spectrum ranging from low (subatomic lone relateds) through mid (atomic sequences functioning as relators) to high (complex nests); inherits from P3 relational density.

> **Cross-references:** P4: Layering in Expressions; Relational Density Spectrum.

**Layer Spectrum Avg \[Phase 1\]**

> An average score of how layered the input feels when the system is checking its internal structure.

> Technical elaboration: Supporting diagnostic that averages layered decompositions across the range 0.2–0.8 when Density Probe is active.

> **Cross-references:** Density Probe.

**Light Output \[Toolkit\]**

> This setting turns the full technical report into one easy-to-read paragraph that still keeps all the important numbers and ideas.

> Technical elaboration: Toggle that collapses all tables and ledgers into a single flowing narrative paragraph. Secondary Coherence Score remains a major diagnostic among survivors; Isolation Residual is named when isolation occurred. SCS is not treated as meaning.

> **Cross-references:** Secondary Coherence Score; Isolation Residual.

**Light Output Narrative \[Toolkit\]**

> The short, readable story version of any analysis produced when Light Output is turned on.

> Technical elaboration: Concise prose version of any toolkit run produced when Light Output is active. Same diagnostic voice as Light Output: SCS is a major diagnostic, not the definition of meaning.

> **Cross-references:** Light Output.

### **M**

**Meaning \[Framework\]**

> Meaning is the living tension between what an expression can make connectable and certain, and what it leaves uncertain, paused, or unconnectable. It is not a single score.

> Technical elaboration: The tensive ratio between the connectable certainties an expression establishes and the uncertainties, generative pauses, and non-relational gaps that remain. Two-sided by nature. This is the definition. Secondary Coherence Score, Tensive, Tension of Certainty, and Meaning Tension do not replace it.

> **Cross-references:** Tensive Yield; Non-Relational Remainder; Secondary Coherence Score.

**Meaning Tension \[Toolkit\]**

> A supporting number the toolkit can print for the balance between certain and uncertain yields. It is not the definition of meaning.

> Technical elaboration: Toolkit-level derived quantity. Not a core formal object. Not Tensive, not Tension of Certainty, and not meaning. No living formula in this glossary; a specimen run may still print a number. SCT Virtue Boost, when on, applies to this quantity, not to Tensive.

> **Cross-references:** Meaning; Tensive Yield; SCT Virtue Boost.

**Meta-Loop \[Toolkit\]**

> This setting lets the system treat its own previous result as a brand-new starting point and run the analysis again, up to three times.

> Technical elaboration: Toggle that automatically re-runs the yield as a new primary expression (up to three iterations); sub-modes include Rerun-Secondaries, Rephrase-Uncertainties, Max-Uncertainties, Max-Certainties, Contrast-Runs, and Doubt-Rerun.

> **Cross-references:** P8 Gate.

**Metric Evolution Table \[Stage 3\]**

> This table shows how all the important numbers change step by step as the analysis moves through its different phases.

> Technical elaboration: Single consolidated table with metrics as rows and phases as columns, including a Δ (to Final) column. Isolation Residual appears in the Final column; the isolation annotation records excluded components. When Density Probe or Show Full Density Metrics is On, this is the authoritative phase-by-phase record.

> **Cross-references:** Hard Isolation Rule; Isolation Residual.

**MultiSpectrum \[P5\]**

> This spectrum shows how many supporting ideas are present, from just one lone idea to a practical handful or an endless spread.

> Technical elaboration: Spectrum of multiplicity ranging from solitary (low) through finite (default pragmatic yield) to infinite (optional extension).

> **Cross-references:** P5: Plurality of Expressions.

### **N**

**Non-Dual \[Toolkit\]**

> This setting makes the analysis more comfortable with ideas that sit between clear opposites or feel paradoxical.

> Technical elaboration: Toggle that boosts mid-paradox tolerance and raises input variance; activates automatically on “void” or “paradox” keywords.

> **Cross-references:** Emptiness-First; Pentalemma Variant.

**Non-Relational Remainder / Gaps \[P3\]**

> These are the parts of any experience or idea that simply refuse to be turned into connections or explanations. They are left as they are.

> Technical elaboration: That which necessarily exceeds and resists every relational construction, even the construction of its own negation, without thereby becoming more fundamental. Registers from within the relational field as horizon/limit of obtainability. Not a peer mode. Not Isolation Residual (a density). Not Retained Openness (a table type). The Residual family heading does not make Remainder a Residual-species. Residual openness, when used in prose, belongs here / to the horizon — it is not a headword and not ρ.

> **Cross-references:** Synthesis Refusal; Isolation Residual; Retained Openness; Pointing Openness.

### **O**

**Obtainment Focus \[Adaptive Depth\]**

> This sub-setting steers the analysis to pay extra attention to what actually comes into view and what stays out of reach.

> Technical elaboration: Sub-mode of Adaptive Depth that skews emphasis toward contrasts and obtainability dynamics in P1–P2.

> **Cross-references:** Adaptive Depth.

**Other-pointing \[P3\]**

> One of the two primary ways an expression can point: toward something that is not itself.

> Technical elaboration: One of two primary directional / operational possibilities. When an expression is other-pointing, the method leaves open that the “something else” may not itself be available as an expression or relational object. That horizon is not a third peer mode.

> **Cross-references:** Self-pointing; Two Primary Modes; Non-Relational Remainder.

### **P**

**P1: The Open Field \[Framework\]**

> This is the wide, neutral starting space where any analysis can begin without assuming what reality must be like in advance.

> Technical elaboration: Starting point. Ontologically open permissive synthesis space; remains neutral toward substantive metaphysical commitments while advancing a minimal relational ontology. P1 is the field within which the toolkit abducts secondary expressions.

> **Cross-references:** Dilemma Gate; Eight Starting Points.

**P2: Contrasting Parts in the Field \[Framework\]**

> Once something is being examined, natural differences and shades of meaning become visible and usable.

> Technical elaboration: Starting point. Variances, fluid degrees, or uncertainties that appear once existence obtains under P1’s Door 1\.

> **Cross-references:** P1: The Open Field; Relational Construction.

**P3: Relational Construction of Contrasting Entities \[Framework\]**

> This step turns visible differences into usable connections, or notes where something simply cannot be connected.

> Technical elaboration: Starting point. Bifurcation of contrasting parts into connectable paths or unconnectable gaps, co-emergence with repeatability, and decomposition into relateds and relators operating in two primary modes (self-pointing or other-pointing). Isolation Residual trigger is a weak flag, not a third peer mode. “Toward what resists connection” is horizon under other-pointing, not a third directedness.

> **Cross-references:** Non-Relational Remainder; Related; Relator; Two Primary Modes.

**P4: Layering in Expressions \[Framework\]**

> This shows how simple or richly nested any expression can become, from single pieces to complex stacks.

> Technical elaboration: Starting point. Relators and relateds organize into subatomic, atomic, or complex expressions, provisioning primary expressions as self-contained at \~1 certainty.

> **Cross-references:** Layer Spectrum.

**P5: Plurality of Expressions \[Framework\]**

> Every main expression exists alongside other supporting expressions that help give it meaning.

> Technical elaboration: Starting point. Layered expressions manifest as a current primary expression co-existing with solitary, finite, or infinite secondary expressions.

> **Cross-references:** MultiSpectrum.

**P6: Comparability and Measurement of Expressions \[Framework\]**

> Once there are multiple supporting expressions, they can be compared and measured to see how well they fit together.

> Technical elaboration: Starting point. Plurality enables a spectrum of alignability and transduction, provisioning distances and divergences as utilities; includes default interpretive restraint.

> **Cross-references:** Alignability Spectrum.

**P7: Evaluation and Yield \[Framework\]**

> This step gathers everything that feels certain and everything that remains uncertain into one overall summary.

> Technical elaboration: Starting point. Comparability produces dialectical adjudication of certainties versus uncertainties, yielding balanced, tensive, tempered, or raw outputs.

> **Cross-references:** Yield Spectrum.

**P8: Perception and Orientation \[Framework\]**

> Once the analysis is finished, you are free to accept the result as it is or to change, add to, or even set the whole thing aside.

> Technical elaboration: Starting point. Adjudicated yields open to provisional acceptance (Door 1\) or any form of re-expression, refinement, modular incorporation, or outright discard (Door 2). Living renewal mechanism.

> **Cross-references:** Functional Role Shift; P8 Gate.

**P8 Gate \[Toolkit\]**

> The final step in every run where you decide whether the result is good enough for now or whether you want to explore further.

> Technical elaboration: Final perception gate in every run; Door 1 (provisional acceptance) or Door 2 (open re-expression including outright discard). Users may adjust τ within \[0.0001, 0.01\] or temporarily suspend hard isolation for exploratory analysis (visible warning, logged). Suspension is a new primary under P8, not a silent P7 adjudication. Hard isolation persists for the current run’s core calculations unless that election is explicit.

> **Cross-references:** P8: Perception and Orientation.

**Peircean Abduction Heuristic \[Toolkit\]**

> This setting ranks possible supporting ideas by how well they explain the main expression before choosing which ones to use.

> Technical elaboration: Toggle that ranks candidate secondary expressions by explanatory coherence before Dirichlet sampling.

> **Cross-references:** Secondary Abduction.

**Pentalemma Variant \[Toolkit\]**

> This setting adds extra room for ideas that sit between clear yes and no answers, especially when things feel fluid or paradoxical.

> Technical elaboration: Toggle that adds spectrum across affirm/negate/both/neither for fluid expressions.

> **Cross-references:** Tetralemma / Pentalemma Mapping.

**Per-Item Uncertainty \[Toolkit\]**

> This setting shows a separate uncertainty score for each individual certainty and uncertainty instead of one overall number.

> Technical elaboration: Toggle that displays per-certainty and per-uncertainty probability variants in Stage 3 ledgers.

> **Cross-references:** Uncertainty Table.

**Perspective / Secondary Lens \[Toolkit\]**

> This lets you choose exactly which supporting ideas or viewpoints you want the analysis to focus on.

> Technical elaboration: Parameter that lets users specify exactly which secondary expressions, lenses, or sources to prioritize.

> **Cross-references:** Secondary Expression Equity.

**Phenomenal Probe \[Toolkit\]**

> This setting treats sensory or wordless experiences as raw material and gives them extra room to stay open and uncertain.

> Technical elaboration: Toggle (auto-on for phenomena) that widens sigma and treats non-linguistic inputs as raw phenomenal flows.

> **Cross-references:** Sigma.

**Phase Structure (high-level overview) \[Toolkit\]**

> The analysis moves through six clear steps that build from basic foundations to a final summary.

> Technical elaboration: Phase 1 (foundations), Phase 2 (secondary expressions), Phase 3 (certainties), Phase 4 (uncertainties), Phase 5 (reflexive temper), Phase 6 (dialectical aggregation).

> **Cross-references:** Diagnostics Block.

**Pointing / Pointing-aspect \[Framework\]**

> The directed part of any expression that reaches toward itself or toward something else — and, when it reaches toward something else, may find that what is pointed at cannot be fully captured.

> Technical elaboration: Directed, representational, or reflexive aspect of any primary expression. Two primary modes: self-pointing and other-pointing. “Toward what resists” is horizon under other-pointing, not a third peer mode. When traction\_i ≤ τ, directedness is undefined (pointing refused).

> **Cross-references:** Expression; Two Primary Modes; Pointing Refused.

**Pointing Network / Expression Network \[Toolkit\]**

> The complete map of the main expression and all its supporting connections, shown as a web of links.

> Technical elaboration: Complete directed relational graph consisting of primary node, secondary nodes, Alignment edges, and Traction. Isolated nodes are labeled Synthesis Refusal / pointing refused.

> **Cross-references:** Secondary Synthesis Ledger; Traction Flow Diagram.

**Pointing Openness \[Framework\]**

> Another name for the Non-relational Remainder when the focus is on pointing: what is pointed at may not be available as a relation.

> Technical elaboration: Alias of Non-relational Remainder. Not a fourth object, not a density, not a table type.

> **Cross-references:** Non-Relational Remainder.

**Pointing Refused \[Unified Formal Model / Toolkit\]**

> The label used when a supporting idea has no usable pointing back to the main expression.

> Technical elaboration: Label when traction\_i ≤ τ: directedness is undefined. No positive directedness is attributed to Isolation Residual. Isolated δ cells use this label.

> **Cross-references:** Isolation Residual; Hard Isolation Rule; δ.

**Primary Expression \[Framework\]**

> The main thing you are examining or expressing right now.

> Technical elaboration: Any pointing that obtains as a provisional stabilization of secondary synthesis; during analysis treated primarily as a related whose standing is assessed.

> **Cross-references:** Current Primary Expression; Related.

### **(Q)**

### **R**

**Raw / Regressed Yield \[P7\]**

> This result shows an open pause where nothing solid enough has emerged to form a clear summary.

> Technical elaboration: Yield type near 0 on the Yield Spectrum; also the forced yield when every component triggers hard isolation.

> **Cross-references:** Yield Spectrum; All-Isolated Edge Case.

**Reflexive Tension \[Phase 5/6\]**

> This number measures how much careful second-guessing has introduced healthy doubt into the strong supporting ideas.

> Technical elaboration: Metric quantifying generative doubt introduced by reflexive tempering. Isolated components do not contribute. Downstream formulas that formerly used SPT use SCT.

> **Cross-references:** Phase 5; Secondary Claim Temper.

**Related \[P3\]**

> The main reference point that everything else connects to or supports during analysis.

> Technical elaboration: Functional role revealed through decomposition in analysis (not an intrinsic property); whole primary expressions default as relateds for standalone measurement; subject to Functional Role Shift under P8.

> **Cross-references:** Relator; Functional Role Shift.

**Relational Construction \[P3\]**

> The step that turns visible differences into usable connections while carefully noting what simply cannot be connected.

> Technical elaboration: Process of bifurcation, repeatability co-emergence, and decomposition that transforms contrasting parts into usable relational paths while providing operational protection for non-relational gaps.

> **Cross-references:** Non-Relational Remainder; Related; Relator.

**Relational Density Spectrum (three-dimensional) \[P3\]**

> The overall richness of connections that can be built from any difference, measured along three linked scales.

> Technical elaboration: Continuous spectrum built from three co-emergent density dimensions: connectability gradient, repeatability spectrum, and directedness. These are not three modes. The two primary modes live on the directedness dimension; Isolation Residual trigger is a weak flag, not a third directedness.

> **Cross-references:** Connectability Gradient; Repeatability Spectrum; Two Primary Modes.

**Relational Index \[Phase 6\]**

> This number gives an overall sense of how useful and connected the supporting ideas feel together.

> Technical elaboration: Overall measure of relational utility; computed as Harmony tempered by an uncertainty term. Non-isolated components only.

> **Cross-references:** Harmony Index.

**Relator \[P3\]**

> The active part that connects things together during analysis.

> Technical elaboration: Active connector revealed through decomposition (not an intrinsic property); operates in self-pointing or other-pointing; Isolation Residual trigger may isolate a component. Subject to Functional Role Shift under P8.

> **Cross-references:** Related; Inferred Relator Mode Distribution.

**Repeatability Spectrum \[P3\]**

> This measures how steadily or uniquely something can be recognized and reused.

> Technical elaboration: Atemporal density spectrum ranging from high (full invariants) through mid (sequences or parts) to low (uniques or phenomena). One of the three density dimensions, not a mode.

> **Cross-references:** Relational Density Spectrum.

**Required Claims for Secondary Truth Ledger (Supporting Claims Ledger) \[Stage 3\]**

> This list shows which claims required by the surviving supporting ideas are holding up well or feeling shaky.

> Technical elaboration: Replaces Required Presumptions for Secondary Truth Ledger. Columns: Starting Point / Claim, Stab, UProb, Shaky, Note. SCT is the harmonic mean of Stab and is reported here and in Final Metrics.

> **Cross-references:** Secondary Claim Temper; Eight Starting Points.

**Residual (umbrella) \[Framework / Toolkit\]**

> A family name for two operational limits that show up once analysis is underway: connections that fail outright, and openness that remains among what still stands. The leftover that exceeds every relation is not one of these two.

> Technical elaboration: Family heading for Isolation Residual and Retained Openness in the operational layer. Non-relational Remainder is the Framework’s philosophical limit/horizon; it is not a Residual-species. Residual is not a third symmetrical mode and receives no probability mass inside the two-mode distribution. This heading does not govern Remainder.

> **Cross-references:** Isolation Residual; Retained Openness; Non-Relational Remainder.

**Resolution / Granularity \[Toolkit\]**

> This setting controls how finely or coarsely the input is broken into pieces before analysis.

> Technical elaboration: Parameter (Low / Medium / High) that controls chunk depth for contrasts and repeats.

> **Cross-references:** Input Variance.

**Resonance \[Supporting Diagnostic\]**

> This number shows how smoothly and naturally the supporting ideas fit with the main expression.

> Technical elaboration: Metric measuring how well secondary expressions mesh with the primary; appears in Phases 1–3 depending on toggles.

> **Cross-references:** Stability.

**Retained Openness \[Toolkit\]**

> Openness or under-specification that remains among the supporting ideas that did stay in the analysis.

> Technical elaboration: Uncertainty Table type (formerly Residual Gap). A limit of determination among what already has standing. Not isolation density. Not a metric. Not a Formal-Model section. Not promoted into residual-side diagnostics. Not the Non-relational Remainder.

> **Cross-references:** Uncertainty Table; Isolation Residual; Non-Relational Remainder; Inter-Secondary Clash.

### **S**

**Secondary Abduction \[Stage 1\]**

> The step that gathers possible supporting ideas from the wide open space of analysis in a fair and balanced way.

> Technical elaboration: Process of drawing candidate secondary expressions within P1’s Open Field using Dirichlet priors for equity-balanced sampling.

> **Cross-references:** Secondary Expression; Peircean Abduction Heuristic.

**Secondary Claim Temper (SCT) \[Phase 5\]**

> This score shows how steady or shaky the claims required by the surviving supporting ideas are.

> Technical elaboration: Replaces Secondary Presumption Temper (SPT). Harmonic mean of per-secondary claim-stability (Stab) on non-isolated rows; shaky flag when Stab \< 0.50. Reported in the Required Claims ledger and in Final Metrics.

> **Cross-references:** Required Claims for Secondary Truth Ledger; Claim-Tempered Yield.

**Secondary Coherence Score \[Toolkit / Unified Formal Model\]**

> A major number for how strongly the surviving supporting ideas hold together and point back to the main expression. It is not “the meaning” of the expression, and it is not the only number that matters.

> Technical elaboration: Major diagnostic of secondary synthesis strength among components remaining after isolation. Formula: 0.40 × mean Alignment \+ 0.35 × mean Inter-Secondary Coherence \+ 0.25 × mean Traction Provided (non-isolated only; clamped \[0, 1\]). Residual-side diagnostics (Isolation Residual and post-isolation uncertainty) are commensurate. Not the definition of meaning. Not the single primary or central measure of the system.

> **Cross-references:** Hard Isolation Rule; Traction; Isolation Residual; Meaning.

**Secondary Expression \[P5\]**

> Any supporting idea or reference that helps give meaning to the main expression being examined.

> Technical elaboration: Provisional other that co-exists with the current primary expression and supplies truth relations or meaning ratios through alignment and traction. Treated as a relator for the duration of a run.

> **Cross-references:** Plurality of Expressions; Related.

**Secondary Expression Equity \[Toolkit\]**

> This setting makes sure the supporting ideas come from a balanced mix of different viewpoints and traditions.

> Technical elaboration: Toggle that audits diversity and balances domains.

> **Cross-references:** Dirichlet Priors; Equity Sampler.

**Secondary Expression Table \[Stage 3\]**

> This list shows every supporting idea that was chosen, where it came from, and a quick summary of its fit.

> Technical elaboration: Ledger listing abducted secondary expressions with ID, source, type, alignment score, and summary.

> **Cross-references:** Secondary Abduction.

**Secondary Synthesis \[Framework\]**

> The hidden work of pulling together supporting ideas that creates every main expression we can examine.

> Technical elaboration: Operative engine of the system; every primary expression is built from prior secondary expressions whose coherent meshing and pointing-back determine its standing.

> **Cross-references:** Synthesis Refusal.

**Secondary Synthesis Audit \[Toolkit\]**

> This setting moves the detailed table of supporting connections toward the top of the report so you see the connections early.

> Technical elaboration: Toggle that promotes the Secondary Synthesis Ledger and Traction Flow Diagram as the visual diagnostic section. It is not a “sole primary” diagnostic. All other tables remain full in their normal order.

> **Cross-references:** Secondary Synthesis Ledger.

**Secondary Synthesis Ledger \[Toolkit\]**

> The main table of every supporting idea: how well it fits, how well it fits the others, how strongly it points back, and whether it was kept or isolated.

> Technical elaboration: Replaces Secondary Alignment Ledger. Columns: ID, Source / Secondary Expression, Alignment, Inter-Coherence, Traction, Status / Flag, Notes; optional δ when Show Full Density Metrics is On. Isolated rows carry the isolation label (full string once, then shorten) and “pointing refused” under δ. Means of Alignment, Inter-Coherence, and Traction over non-isolated rows must match the SCS Components disclosure.

> **Cross-references:** Secondary Coherence Score; Traction Flow Diagram; Hard Isolation Rule.

**Secondary Transduction Gate \[P6\]**

> The step that translates and compares all the supporting ideas so they can be measured against the main expression.

> Technical elaboration: Gate that enables a spectrum of alignability and transduction between secondary expressions and the primary.

> **Cross-references:** Alignability Spectrum.

**Self-Echo Baseline \[Toolkit\]**

> This setting uses pieces of the main expression itself as temporary supporting ideas when no external ones are available.

> Technical elaboration: Sub-toggle under Secondary Expression Equity that uses internal chunks as pseudo-secondary expressions.

> **Cross-references:** Secondary Expression Equity.

**Self-pointing \[P3\]**

> One of the two primary ways an expression can point: toward itself.

> Technical elaboration: One of two primary directional / operational possibilities. Replaces living “Self-Mode” as a peer-mode name.

> **Cross-references:** Other-pointing; Two Primary Modes.

**Seven Design Criteria \[Computational Substrate Appendix\]**

> The jointly necessary rules that every parameter and structural choice in the toolkit must satisfy.

> Technical elaboration: Hard Isolation Preservation; Two-Mode Restriction (Isolation Residual parked outside as density — not a Residual Complement); Anchor Priority of Primary; Equity Toward Non-Relational Remainders; Empirical Stability; Revisability Under P8; Derivability from General Apparatus.

> **Cross-references:** Governance Protocol; H(x).

**SCT Virtue Boost \[Toolkit\]**

> This optional setting gives a small extra emphasis to supporting numbers when the required claims feel shaky, treating that shakiness as valuable rather than weak.

> Technical elaboration: Toggle (default Off) that adds \+0.05 or \+0.1 to Meaning Tension when SCT falls below 0.5. Applies to Meaning Tension, not to Tensive.

> **Cross-references:** Secondary Claim Temper; Meaning Tension.

**Sigma \[Toolkit\]**

> This control sets how much room the analysis leaves for variation and uncertainty in the input.

> Technical elaboration: Tunable standard deviation parameter (default \~0.07, widened for phenomena or porous inputs).

> **Cross-references:** Phenomenal Probe; Chaos Scale.

**Solitary Multiplicity \[P5\]**

> This describes a situation where the main expression stands almost alone with very little supporting context.

> Technical elaboration: Low end of the MultiSpectrum; represents isolated primary expressions as minimal certainties.

> **Cross-references:** MultiSpectrum.

**Stability \[Supporting Diagnostic\]**

> This number shows how consistent the supporting ideas remain across the different steps of analysis.

> Technical elaboration: Metric measuring consistency across phases; appears in Phases 1–3 depending on toggles.

> **Cross-references:** Resonance.

**Subatomic Expression \[P4\]**

> The simplest layered unit, consisting of just one basic reference point with nothing else attached.

> Technical elaboration: Layered expression consisting of a lone related functioning strictly as a passive anchor.

> **Cross-references:** Layer Spectrum; Related.

**Synthesis Refusal \[Framework / Toolkit\]**

> This marks the clear point where supporting ideas simply stop connecting and the main expression loses traction.

> Technical elaboration: Measurable limit of any secondary-synthesis audit; occurs when secondary expressions do not align or are absent, causing pointing to lose traction. Operationally registered as Isolation Residual (density) via hard isolation. Philosophically adjacent to, but not identical with, Non-relational Remainder. Cross-references both, separately.

> **Cross-references:** Hard Isolation Rule; Isolation Residual; Non-Relational Remainder.

### **T**

**τ (Dilemma-Gate Threshold) \[Unified Formal Model / Toolkit\]**

> This is the exact cutoff point that decides whether a supporting idea is strong enough to keep working with or should be set aside as too weak.

> Technical elaboration: Tunable threshold that separates sufficient obtainability for relational construction from generative uncertainty or halt. Default 0.001, adjustable \[0.0001, 0.01\] under P8.

> **Cross-references:** Dilemma Gate; Hard Isolation Rule.

**Temper-Probe \[Toolkit\]**

> This setting previews how strongly the analysis will soften its strong supporting ideas before committing to the final result.

> Technical elaboration: Toggle that previews temper aggressiveness (Soft sigmoid or Hard binary).

> **Cross-references:** Certainty Temper Probe.

**Tempered Certainty Ledger \[Stage 3\]**

> This list shows the original strong supporting ideas after they have been gently softened by careful second-guessing.

> Technical elaboration: Non-isolated components only. Columns: Secondary Expression, Unaddressed Starting Point, Tetralemma, Tempered Geo/Harm, C/U Ratio, Temper Index, Note. Isolated components generate no rows.

> **Cross-references:** Phase 5; Required Claims for Secondary Truth Ledger.

**Tension of Certainty \[Unified Formal Model / Toolkit\]**

> Another name for the Tensive yield number. It is one way of operationalizing the tensive ratio — not the definition of meaning.

> Technical elaboration: Tension of Certainty, when named, is the same quantity as Tensive: √(SCS × (1 − ρ)), with ρ \= Isolation Residual (isolation density). One formal operationalization of the Framework’s tensive ratio, provisional under P8. Isolation Residual is not the whole residual pole. Not meaning, not Meaning Tension.

> **Cross-references:** Tensive Yield; Meaning; Isolation Residual.

**Tensive Bands \[Toolkit\]**

> These are the shaded zones the system uses to map how tense or balanced the supporting ideas feel.

> Technical elaboration: Sub-toggle under Secondary Expression Equity that pentalemma-maps resonance and stability.

> **Cross-references:** Pentalemma Variant.

**Tensive Yield \[P7 / Unified Formal Model\]**

> This result sits in the middle where there is a lively mix of solid certainties and open uncertainties.

> Technical elaboration: Named yield type on the Yield Spectrum. Formal operationalization (Yields / Executive Yield only, not on the Takes): Tensive \= √(SCS × (1 − ρ)), where ρ is Isolation Residual (isolation density). Do not call (1 − ρ) residual openness. Hedge: this is one operationalization of the Framework’s tensive ratio, provisional under P8; Isolation Residual is not the whole residual pole. Survivors only. Not the definition of meaning.

> **Cross-references:** Yield Spectrum; Secondary Coherence Score; Isolation Residual; Tension of Certainty; Meaning.

**Tetralemma / Pentalemma Mapping \[Unified Formal Model\]**

> Gentle ways of mapping any idea onto a scale that includes clear yes, clear no, both, neither, or a full spectrum of in-between shades.

> Technical elaboration: Graduated mapping used across starting points and Phase 5 tempering: high values map to affirm; mid values with variance map to both; low-positive values map to neither (pause); zero maps to negate. Pentalemma variant adds spectrum for fluid expressions.

> **Cross-references:** Pentalemma Variant.

**The Four Takes \[Toolkit\]**

> Four short, plain-language summaries that explain the final result from the angles of what feels certain, what feels uncertain, what the second-guessing revealed, and an overall recap.

> Technical elaboration: Certainty Take, Uncertainty Take, Reflexive Take, Recap Take. Each treats Secondary Coherence Score as a major diagnostic of secondary synthesis strength among survivors and names residual-side diagnostics when they are in play. SCS is not treated as meaning. No Tensive formula on the Takes; Recap may name Yield Type \= Tensive and the number.

> **Cross-references:** Secondary Coherence Score; Meaning.

**Traction \[Toolkit\]**

> This measures how strongly a supporting idea actually points back to the main expression instead of drifting away.

> Technical elaboration: Strength with which a secondary expression points back to the primary; traction ≤ τ triggers hard isolation and “pointing refused.”

> **Cross-references:** Secondary Synthesis Ledger; Traction Flow Diagram.

**Traction Flow Diagram \[Stage 3\]**

> A text tree with the main expression at the root, surviving supporting ideas on one branch, and isolated supporting ideas on the other.

> Technical elaboration: One tree. Primary root; retained branch (optionally grouped high / mid-high / mid / low-mid); isolated branch labeled Synthesis Refusal. Replaces a flat list of arrows. No second diagram type.

> **Cross-references:** Secondary Synthesis Ledger.

**Traction Provided \[SCS\]**

> This checks whether each supporting idea actually adds useful connection or simply sits there without helping.

> Technical elaboration: Component measuring whether secondary expressions actually contribute relational utility; contributes 0.25 weight to Secondary Coherence Score.

> **Cross-references:** Secondary Coherence Score.

**Truth Alignment \[Phase 6\]**

> This number shows how well the supporting ideas line up with what can reasonably be called true or reliable.

> Technical elaboration: Metric quantifying how well secondary expressions support probabilistic truth relations. Downstream language is claim / starting-point, not presumption.

> **Cross-references:** Claim Coherence.

**Truth-Emphasis \[Toolkit\]**

> This setting leans the analysis toward sharper, more decisive connections when you want a clearer picture of what holds together.

> Technical elaboration: Toggle that boosts relational priors and narrows sigma for sharper alignments.

> **Cross-references:** Secondary Expression Equity.

**Two Primary Modes \[Framework / Unified Formal Model\]**

> There are two main ways an expression can point: at itself, or at something else.

> Technical elaboration: Self-pointing and other-pointing. There is no third peer mode that receives positive directedness or probability mass. Residual openness remains as horizon/limit, not as a third measurable mode.

> **Cross-references:** Self-pointing; Other-pointing; Isolation Residual.

### **U**

**Uncertainty Prob Global \[Toolkit\]**

> This overall number tracks how much of the analysis is still open, uncertain, or simply unconnectable.

> Technical elaboration: Global probability mass assigned to non-relational gaps and Synthesis Refusal; clamped \[0.25, dynamic upper\]. After isolation, a single bump is applied: \+0.05 × Isolation Residual.

> **Cross-references:** Isolation Residual; Uncertainty Upper Bound.

**Uncertainty Probe \[Toolkit\]**

> This setting actively looks for and gives extra weight to the parts that remain uncertain or unconnectable.

> Technical elaboration: Toggle that actively abducts and boosts non-relational gaps using adaptive Dirichlet alphas.

> **Cross-references:** Echo Mode; Feedback-Adaptive.

**Uncertainty Resonance \[Supporting Diagnostic\]**

> This number shows how strongly the uncertain or open parts of the analysis hang together in a meaningful way.

> Technical elaboration: Supporting metric that appears in later phases when Show Full Density Metrics is enabled.

> **Cross-references:** Uncertainty Stability.

**Uncertainty Stability \[Supporting Diagnostic\]**

> This number shows how steady or shaky the uncertain parts of the analysis remain across the different steps.

> Technical elaboration: Supporting metric that appears in later phases when Show Full Density Metrics is enabled.

> **Cross-references:** Uncertainty Resonance.

**Uncertainty Table \[Stage 3\]**

> This list shows every isolated or still-open part, along with how much weight it carries and a short note.

> Technical elaboration: Always full. Isolated components appear with Type \= Synthesis Refusal (the full isolation string lives once in the Secondary Synthesis Ledger). Non-isolated limit rows use Type \= Retained Openness or Inter-Secondary Clash.

> **Cross-references:** Retained Openness; Inter-Secondary Clash; Hard Isolation Rule.

**Uncertainty Upper Bound \[Toolkit\]**

> This is the highest level of uncertainty the system will allow before it starts clamping the numbers to keep the result readable.

> Technical elaboration: Dynamically calculated ceiling on uncertainty probability, clamped \[0.25, 0.9\]. Downstream formulas that formerly used SPT use SCT.

> **Cross-references:** Uncertainty Prob Global; Secondary Claim Temper.

**Uncertainty Yield Geo Avg \[Phase 4\]**

> This average measures the overall strength of the uncertain or open parts of the analysis.

> Technical elaboration: Geometric mean of uncertainty yields. Influences supporting Toolkit quantities; does not define meaning.

> **Cross-references:** Meaning Tension.

**Unified Formal Model \[Unified Formal Model\]**

> The mathematical write-up of the same distinctions the Framework already makes. Helpful, not required, and not in charge.

> Technical elaboration: Formal, mathematical representation of the Framework’s distinctions. Legitimate and useful. Not the definition of the method, not a required foundation, not a higher authority.

> **Cross-references:** Framework; H(x).

### **(VWX)**

### **Y**

**Yield Spectrum \[P7\]**

> This scale shows the overall balance of the final result, from mostly certain and stable to mostly open and unresolved.

> Technical elaboration: Dialectical metric ranging from high (balanced) through mid (tensive) to low (tempered) to near 0 (raw/regressed). Variants include Sum, Geometric, Harmonic, Tensive, and Claim-Tempered.

> **Cross-references:** Yield Type; Tensive Yield.

**Yield Type \[P7\]**

> The simple label given to the final result that tells you whether it feels solid, tense, weak, or completely open.

> Technical elaboration: Categorical interpretation of the final yield: Balanced, Tensive, Tempered (or Claim-Tempered when that variant is computed), or Raw/Regressed.

> **Cross-references:** Yield Spectrum.

### **(Z)**

## **Section 2: Mathematical Variables, Functions, Spectra, Equations, Symbols (alphabetical)**

**Alignability Spectrum \[P6\]**

> The spectrum that shows how easily secondary expressions can be compared and translated relative to the primary expression.

> Technical elaboration: Runs from sparse through partial to dense. Supplies distances and divergences used for measurement.

> **Cross-references:** P6; Secondary Synthesis Ledger.

**H(x) (general hybrid function) \[Unified Formal Model\]**

> The core mathematical engine that calculates how obtainable any element is within analysis. In simple terms, it combines fuzzy likelihood with updated probability to produce a single score between 0 and 1\.

> Technical elaboration:

> H(x) \= min(1, μ(x) × P\_norm(x | V)) ∈ \[0, 1\]

> where μ(x) is the fuzzy membership function and P\_norm(x | V) is the normalized Bayesian posterior.

> **Cross-references:** Dilemma Gate; τ; Relational Density Spectrum.

**Inferred Relator Mode Distribution (Derived) \[Toolkit / Unified Formal Model\]**

> After isolation, a two-mode distribution over {Self-pointing, Other-pointing} summing to 1 on survivors. Isolation Residual is parked outside as isolation density.

> Technical elaboration: Concrete feature map is not defined. Do not restore log-odds inputs R, D, T\_norm, U\_norm, Y\_centered, RT\_norm as live claims. Any P8-licensed map that yields a valid two-mode distribution on survivors remains open.

> **Cross-references:** Isolation Residual; Hard Isolation Rule; Two Primary Modes.

**Isolation Residual / Isolation density \[Unified Formal Model / Toolkit\]**

> The proportion of components with traction\_i ≤ τ.

> Technical elaboration: Isolation Residual \= (number of components with traction\_i ≤ τ) / N. Not max(0, 1 − \[P(Self-pointing) \+ P(Other-pointing)\]). Not residual openness. Not Remainder.

> **Cross-references:** Hard Isolation Rule; Inferred Relator Mode Distribution.

**Layer Spectrum \[P4\]**

> The spectrum that shows how elements stack into different levels of complexity within expressions.

> Technical elaboration: Ranges from low (subatomic lone relateds) through mid (atomic sequences) to high (complex nests).

> **Cross-references:** P4; Relational Density Spectrum.

**Meaning Tension \[Toolkit\]**

> A Toolkit-derived supporting quantity. Not meaning, not Tensive, not Tension of Certainty.

> Technical elaboration: No living formula in this glossary. A specimen run may still print a number.

> **Cross-references:** Meaning; Tensive Yield.

**μ(x) (fuzzy membership functions) \[Unified Formal Model\]**

> The mathematical way of assigning graded belonging instead of strict yes-or-no.

> Technical elaboration: Two families are used: linear ramp and clamped sigmoid.

> **Cross-references:** H(x); P\_norm(x | V).

**Multiplicity Spectrum \[P5\]**

> The spectrum that shows how many supporting expressions exist alongside the primary one.

> Technical elaboration: Ranges from solitary through finite (default) to infinite (optional).

> **Cross-references:** P5; Layer Spectrum.

**Obtainability Spectrum \[P1\]**

> The spectrum that measures how readily something can be registered within analysis.

> Technical elaboration: Inherits directly from H(x) and the dilemma gate.

> **Cross-references:** Dilemma Gate; H(x).

**P\_norm(x | V) (normalized Bayesian posterior) \[Unified Formal Model\]**

> The updated probability that incorporates new evidence while staying within the 0–1 range.

> Technical elaboration:

> P\_norm(x | V) \= \[P(x) · L(V | x)\] / Z

> with uniform prior and Gaussian likelihood.

> **Cross-references:** H(x); μ(x).

**Relational Density Spectrum (three-dimensional) \[P3\]**

> The combined spectrum built from three co-emergent density dimensions: connectability, repeatability, and directedness.

> Technical elaboration: These are not three modes. The two primary modes live on the directedness dimension.

> **Cross-references:** Connectability Gradient; Repeatability Spectrum; Two Primary Modes.

**Relational Index \[Phase 6\]**

> An overall measure of how useful the relational connections are within the current analysis.

> Technical elaboration: Computed as Harmony tempered by an uncertainty term. Non-isolated only.

> **Cross-references:** Harmony Index.

**Secondary Coherence Score formula \[Toolkit\]**

> SCS \= 0.40 × mean Alignment \+ 0.35 × mean Inter-Secondary Coherence \+ 0.25 × mean Traction Provided

> (clamped \[0, 1\]; computed exclusively on non-isolated components). Major diagnostic among survivors, not the definition of meaning.

> **Cross-references:** Hard Isolation Rule; Alignment; Traction.

**Seven Design Criteria \[Computational Substrate Appendix\]**

> Hard Isolation Preservation; Two-Mode Restriction with Isolation Residual parked outside as density; Anchor Priority of Primary; Equity Toward Non-Relational Remainders; Empirical Stability; Revisability Under P8; Derivability from General Apparatus.

> **Cross-references:** Governance Protocol; H(x).

**Spectra family (obtainability, contrast, repeatability, layering, multiplicity, alignment, yield) \[Unified Formal Model\]**

> The complete set of continuous spectra used throughout the system.

> Technical elaboration: All inherit from H(x) and the relational density spectrum of P3.

> **Cross-references:** Relational Density Spectrum; Layer Spectrum; Multiplicity Spectrum.

**τ (dilemma-gate / hard isolation threshold) \[Unified Formal Model / Toolkit\]**

> Default 0.001, adjustable \[0.0001, 0.01\] under P8.

> **Cross-references:** Dilemma Gate; Hard Isolation Rule.

**Tensive / Tension of Certainty \[Unified Formal Model / Toolkit\]**

> Tensive \= √(SCS × (1 − ρ)), ρ \= Isolation Residual (isolation density).

> Technical elaboration: One operationalization of the Framework’s tensive ratio, provisional under P8. Do not call (1 − ρ) residual openness. Formula lives in Yields / Executive Yield only, not on the Takes. Not the definition of meaning.

> **Cross-references:** Secondary Coherence Score; Isolation Residual; Meaning.

**Tetralemma / Pentalemma Mapping \[Unified Formal Model\]**

> Graduated mapping for binary, paradoxical, or fluid expressions without forcing artificial resolution.

> Technical elaboration: High values map to affirm; mid values with variance map to both; low-positive values map to neither; zero maps to negate.

> **Cross-references:** Pentalemma Variant.

**Uncertainty bump \[Unified Formal Model §6.4\]**

> uncertainty\_prob\_global ← clamp(uncertainty\_prob\_global \+ 0.05 × Isolation Residual, \[0.25, 0.9\])

> Technical elaboration: Single post-exclusion global bump. Distinct from per-component exclusion in §6.2.

> **Cross-references:** Isolation Residual; Hard Isolation Rule.

**Yield Spectrum / Yield Types (and variants) \[P7\]**

> Types: Balanced, Tensive, Tempered / Claim-Tempered, Raw/Regressed. Variants include Sum, Geometric, Harmonic, Tensive, and Claim-Tempered.

> **Cross-references:** Secondary Coherence Score; Tensive Yield.


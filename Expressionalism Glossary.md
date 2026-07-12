# **Expressionalism Glossary**

## **Section 1: Core Words, Terms, Phrases, Concepts (alphabetical)**

### **A**

#### **Adaptive Depth \[Toolkit\]**

Plain-language definition. This toggle automatically chooses a shorter analysis for simple inputs or a deeper one for complex ones. In everyday use it keeps things manageable while still giving you the full power when you need it.

**Technical elaboration.** Activates based on input variance and ambiguity score; includes Obtainment Focus sub-mode that emphasizes contrasts and obtainability in P1–P2.

**Cross-references:**

* Density Probe  
* Light Output  
* Input Variance.

#### **Alignment \[Toolkit\]**

Plain-language definition. This measures how well a supporting idea or reference fits with the main expression being analyzed. Higher alignment means the support is stronger and more reliable.

**Technical elaboration.** Degree to which a secondary expression supports and coheres with the current primary expression; contributes 0.4 weight to Secondary Coherence Score.

**Cross-references:**

* Secondary Coherence Score  
* Inter-Secondary Coherence  
* Traction.

#### **Alignability Spectrum \[P6\]**

Plain-language definition. This shows how easily supporting ideas can be compared and translated relative to the main expression. It ranges from very loose connections to tight, natural fits.

**Technical elaboration.** Spectrum of transduction and comparison (sparse / partial / dense) that provisions distances and divergences as utilities under P6.

**Cross-references:**

* Comparability  
* Transduction  
* Secondary Alignment Ledger.

#### **All-Isolated Edge Case \[Toolkit\]**

Plain-language definition. This happens when every supporting idea falls below the minimum traction threshold. The analysis then stops relational scoring and reports a clear “no synthesis possible” result.

**Technical elaboration.** Terminal state in which every component triggers hard isolation; forces Secondary Coherence Score to “N/A (all components isolated)” and Yield Type to Raw/Regressed. Validation: clean handling with no NaN, division-by-zero, or overflow.

**Cross-references:**

* Hard Isolation Rule  
* Residual  
* P8 Gate.

#### **Ambiguity Score \[Toolkit\]**

Plain-language definition. This number measures how clear or mixed the input chunks are. A high score tells the system the material is complex or unclear, so it adjusts settings automatically.

**Technical elaboration.** Value calculated in Stage 1 from coherence of input chunks; high scores trigger Light Output and widen sigma for more porous material.

**Cross-references:**

* Input Variance  
* Light Output.

#### **Anchor Priority of the Primary \[P5\]**

Plain-language definition. The main expression being analyzed is always treated as the central reference point. All supporting ideas are judged by how well they connect back to it.

**Technical elaboration.** Highest weight assigned to relations that point back to the primary (treated as related at \~1 certainty) under P5.

**Cross-references:**

* Related  
* Secondary Coherence Score  
* Plurality of Expressions.

#### **Atomic Expression \[P4\]**

Plain-language definition. A simple layered unit made of a sequence of basic parts that can act as a connector when placed inside something larger.

**Technical elaboration.** Layered expression consisting of a sequence of relateds that functions as a relator while standing as a related when measured alone.

**Cross-references:**

* Layer Spectrum  
* Related  
* Relator.

### **B**

#### **Balanced Yield \[P7\]**

Plain-language definition. This is a stable result where the certainties clearly outweigh the uncertainties, giving a solid, usable summary.

**Technical elaboration.** Yield type with high certainty dominance on the Yield Spectrum.

**Cross-references:**

* Yield Spectrum  
* Tensive Yield.

#### **Binomial Falsification Threshold \[Toolkit\]**

Plain-language definition. A statistical check that flags when an analysis is too inconsistent or contradictory. It uses a simple probability rule tailored to the type of input.

**Technical elaboration.** Statistical check (p \= 0.18 with \+5 % reflexive tolerance) that flags persistent incoherence; uses data-type-aware thresholds (25 % for expressions, 30 % for phenomena) across 15 perturbations. Validation: 0 % false positives below threshold incidence and 100 % correct triggering above it.

**Cross-references:**

* Incoherence Flag.

#### **Bootstrap / Origination Asymmetry \[CS Appendix\]**

Plain-language definition. The system always starts with an already-formed main expression and cannot create the very first one from nothing. This is simply how the process works.

**Technical elaboration.** Irreducible limit that the system always begins with an already-obtained primary expression and cannot generate the first stabilization ex nihilo; acknowledged transparently as a methodological commitment.

**Cross-references:**

* P1: The Open Field  
* P8 Gate.

### **C**

#### **Certainty Table \[Toolkit\]**

Plain-language definition. A list showing the strongest supporting ideas that passed the minimum traction test, along with how well they fit the main expression.

**Technical elaboration.** Stage 3 output listing non-isolated certainties with alignment, inter-coherence, traction, and notes.

**Cross-references:**

* Uncertainty Table  
* Tempered Certainty Ledger.

#### **Certainty Temper Index \[Phase 5\]**

Plain-language definition. This number shows how much careful second-guessing has softened the original strong supporting ideas.

**Technical elaboration.** Metric quantifying how much reflexive doubt has softened original certainties. Formula: $1 \- (\\text{layer spectrum} \\times (1 \- 0.15 \\times \\text{uncertainty probability global}))$ (clamped \[0.3, 0.7\]).

**Cross-references:**

* Reflexive Tension  
* Phase 5\.

#### **Certainty Temper Probe \[Toolkit\]**

Plain-language definition. A setting that adds careful second-guessing to the strong supporting ideas during analysis. It has light and deep levels.

**Technical elaboration.** Toggle that runs Deep reflexive certainty tempering in Phase 5; includes Light and Deep sub-modes and works together with Uncertainty Probe.

**Cross-references:**

* Phase 5  
* Temper-Probe.

#### **Certainty Yield Geo Avg \[Phase 3\]**

Plain-language definition. The average strength of the best supporting ideas, calculated in a way that balances the overall set.

**Technical elaboration.** Geometric mean of certainty yields; target range 0.7–0.9.

**Cross-references:**

* Meaning Tension.

#### **Chaos Scale \[Toolkit\]**

Plain-language definition. A control that makes the analysis more open to messy or uncertain material by widening the tolerance for variation.

**Technical elaboration.** Tunable parameter (default 0.05) that increases porosity and fairness for chaotic or uncertain inputs; higher values widen sigma and raise uncertainty upper bound.

**Cross-references:**

* Sigma  
* Uncertainty Upper Bound.

#### **Complex Expression \[P4\]**

Plain-language definition. A richly layered unit built from many parts and at least one connector, allowing deep nesting.

**Technical elaboration.** Layered expression made of nests containing multiple relateds and at least one relator; allows unlimited nesting depth and functions as a standalone related.

**Cross-references:**

* Layer Spectrum  
* Related  
* Relator.

#### **Connectability Gradient \[P3\]**

Plain-language definition. How fully a difference or contrast can be woven into a usable connection rather than left as something unconnectable.

**Technical elaboration.** One of the three co-emergent dimensions of relational density; measures how fully a contrasting part can participate in relational construction versus gesturing toward unconnectable gaps.

**Cross-references:**

* Relational Density Spectrum  
* Non-Relational Remainder.

#### **Contrarian \[Toolkit\]**

Plain-language definition. A setting that deliberately looks for gaps and uncertainties by slightly lowering the expected smoothness of the input.

**Technical elaboration.** Toggle that lowers input variance and actively probes non-relational gaps; often activates automatically on high ambiguity scores.

**Cross-references:**

* Uncertainty Probe.

#### **Contrasting Parts \[P2\]**

Plain-language definition. The natural differences, shades, or uncertainties that appear once something is being examined.

**Technical elaboration.** Variances, fluid degrees, or uncertainties that appear once existence obtains under P1’s Door 1; they create the differentiations needed for later relational construction.

**Cross-references:**

* P1: The Open Field  
* Relational Construction.

#### **Current Primary Expression \[P5\]**

Plain-language definition. The main thing being looked at right now; it is treated as the central reference point during analysis.

**Technical elaboration.** Immediate totality being analyzed; treated primarily as a related at \~1 certainty during analysis and co-exists with secondary expressions.

**Cross-references:**

* Primary Expression  
* Related  
* Secondary Expression.

#### **Data Type \[Toolkit\]**

Plain-language definition. The system’s quick way of telling whether the input is a clear statement or something more sensory and open-ended.

**Technical elaboration.** Automatic classification of an input as expression or phenomenon; adjusts incoherence thresholds and sigma. Phenomena receive wider sigma and higher uncertainty boosts.

**Cross-references:**

* Phenomenal Probe.

### **D**

#### **Decomposition Gate \[P3\]**

Plain-language definition. The step that breaks usable differences into basic anchors and active connectors.

**Technical elaboration.** Operation that breaks repeatable relational paths into relateds (passive anchors) and relators (active connectors) operating in self-mode, other-mode, or non-rel-probe mode.

**Cross-references:**

* Relational Construction  
* Related  
* Relator.

#### **Default Interpretive Restraint \[P6\]**

Plain-language definition. When connections are weak or missing, the system stays cautious and does not force extra meaning.

**Technical elaboration.** Operational heuristic that keeps further interpretive gestures relatively weak when traction is low or Synthesis Refusal appears; fully overridable under P8.

**Cross-references:**

* Synthesis Refusal  
* P8 Gate.

#### **Density Probe \[Toolkit\]**

Plain-language definition. A setting that looks inside the input to measure how layered and detailed it is.

**Technical elaboration.** Toggle that computes internal variances and layering metrics in Phases 1 and 2; includes Base, Fuzzy, Weighted, and Iterative sub-modes.

**Cross-references:**

* Layer Spectrum  
* Adaptive Depth.

#### **Dilemma Gate \[P1\]**

Plain-language definition. The basic yes/no check that decides whether there is enough connection to keep analyzing or whether the analysis should pause.

**Technical elaboration.** Mechanism that evaluates obtainability through H(x); if result \> τ, proceeds with relational construction (Door 1); if ≤ τ, registers generative uncertainty or halts (Door 2\) with reciprocal boosting.

**Cross-references:**

* H(x)  
* τ  
* P1: The Open Field.

#### **Directional Bleed \[Toolkit\]**

Plain-language definition. A setting that allows influence to flow both ways between the main expression and its supporting ideas.

**Technical elaboration.** Sub-toggle under Secondary Expression Equity that enables bidirectional resonance analysis; asymmetry \> 0.2 increases tension and fragility measures.

**Cross-references:**

* Secondary Expression Equity.

#### **Dirichlet Priors \[Phase 2\]**

Plain-language definition. A fair-sampling method that helps the system pick supporting ideas without favoring any particular viewpoint.

**Technical elaboration.** Equity-balancing sampling method used to abduct secondary expressions; incorporates void-prior alphas for fair representation of non-relational gaps.

**Cross-references:**

* Secondary Abduction  
* Secondary Expression Equity.

### **E**

#### **Echo Mode \[Toolkit\]**

Plain-language definition. This setting applies a gentle fading effect to older or less relevant supporting ideas so the analysis stays fresh and balanced. It helps prevent outdated assumptions from dominating the result.

**Technical elaboration.** Sub-toggle under Uncertainty Probe that applies tradition-decay via priors for multiple uncertainties; supports emptiness-focused analyses.

**Cross-references:**

* Uncertainty Probe.

#### **Emptiness-First \[Toolkit\]**

Plain-language definition. This setting flips the usual focus so that gaps and uncertainties are treated as the most important part of the picture rather than problems to fix. It makes room for mystery and open-endedness.

**Technical elaboration.** Toggle that reverses usual relational bias; treats non-relational gaps as primary lens and high-uncertainty yields as virtuous; raises uncertainty upper bound.

**Cross-references:**

* Non-Dual  
* Uncertainty Probe.

#### **Equity Sampler \[Toolkit\]**

Plain-language definition. This setting adds a small amount of helpful randomness when choosing supporting ideas so that no single viewpoint is unfairly favored. It keeps the analysis fair across different kinds of material.

**Technical elaboration.** Sub-toggle under Secondary Expression Equity that perturbs noise from Dirichlet priors; increases uncertainty yield for marginal or underrepresented cases.

**Cross-references:**

* Secondary Expression Equity.

#### **Equitable Treatment / Reciprocity (or Secondary Expression Equity) \[Toolkit\]**

Plain-language definition. This ensures the system draws supporting ideas from a balanced mix of sources and viewpoints rather than leaning toward any one tradition or style. It keeps the analysis fair.

**Technical elaboration.** Toggle that audits diversity and balances domains; includes multiple sub-modes for sourcing control and void emphasis.

**Cross-references:**

* Dirichlet Priors  
* Equity Sampler.

#### **Expression \[Framework\]**

Plain-language definition. Any temporary way of pulling together thoughts, feelings, or experiences into something that can be examined or shared. It can be a sentence, a memory, a painting, or even a quiet moment.

**Technical elaboration.** Any provisional stabilization of secondary synthesis (thought, claim, artwork, scientific assertion, memory, perceptual scene, moment of silence, etc.).

**Cross-references:**

* Pointing  
* Secondary Synthesis  
* Primary Expression.

### **F**

#### **Falsify Mode \[Toolkit\]**

Plain-language definition. This setting makes the system stricter or more forgiving when checking for contradictions, depending on how careful you want the analysis to be.

**Technical elaboration.** Toggle that tightens or loosens incoherence thresholds (Lenient adds \+5 % tolerance; Strict subtracts 5 %).

**Cross-references:**

* Incoherence Flag.

#### **Feedback-Adaptive \[Toolkit\]**

Plain-language definition. This setting lets later stages of the analysis gently adjust earlier results so the whole picture stays consistent as new details emerge.

**Technical elaboration.** Sub-toggle under Uncertainty Probe that retro-tempers Phase 1 and 2 metrics after Phases 2 and 3; shifts \> 0.1 trigger “Recursive Boost” notes for P8 consideration.

**Cross-references:**

* Uncertainty Probe.

#### **Finite Multiplicity \[P5\]**

Plain-language definition. This describes a moderate number of supporting ideas that feel complete and practical rather than endless or solitary. It is the usual default setting for most everyday analyses.

**Technical elaboration.** Middle range of the MultiSpectrum; represents bounded clusters of secondary expressions and serves as the default pragmatic yield.

**Cross-references:**

* MultiSpectrum  
* P5: Plurality of Expressions.

#### **Fragility Adjustment \[Harmony Index\]**

Plain-language definition. This small boost rewards situations where the supporting ideas are productively tense or uncertain rather than perfectly smooth.

**Technical elaboration.** Activates exactly when metric variance exceeds 0.12 and raises Harmony Index by \~0.12–0.15; rewards productive tension. Validation: consistent uplift at the designed threshold (Stage 6 PASS).

**Cross-references:**

* Harmony Index.

#### **Functional Role Shift \[P8\]**

Plain-language definition. Any part of the analysis can change its job — from being the main reference point to being a supporting connector — as you look at it again from a fresh angle.

**Technical elaboration.** Perceptual and interpretive process allowing any node to move between related and relator status or change relational mode during re-expression; roles recorded as metadata.

**Cross-references:**

* P8 Gate  
* Related  
* Relator.

### **G**

#### **Governance Protocol \[CS Appendix\]**

Plain-language definition. The rule that says any change to the system’s settings must be carefully justified, tested again, logged, and treated as a brand-new starting point.

**Technical elaboration.** Rule that any parameter modification must include explicit justification against the seven design criteria, re-execution of validation (or equivalent), metadata logging, and treatment as a new primary expression.

**Cross-references:**

* Seven Design Criteria  
* P8 Gate.

#### **Guardrails \[Toolkit\]**

Plain-language definition. This setting either brings back older safety checks for contradictions or uses gentler defaults so the analysis stays stable even when things look shaky.

**Technical elaboration.** Toggle that enables old self-refutations on incoherence/low metrics or uses resilient defaults treating lows as tensive features.

**Cross-references:**

* Falsify Mode.

### **H**

#### **Hard Isolation Rule \[Unified Model / Toolkit\]**

Plain-language definition. When a supporting idea is too weak to connect reliably, the system completely removes it from all scoring and simply notes it as an isolated gap that cannot be used.

**Technical elaboration.** Post-processing filter applied after H(x) and dilemma gate evaluation; any component with traction\_i ≤ τ receives the exact label “Synthesis Refusal active — traction \= 0 — isolated remainder (excluded from aggregation and distributions)” and is fully excluded from all relational metrics, distributions, and yields. Validation: deterministic triggering at exact threshold and adjacent floating-point values; zero leakage (Stage 1 PASS).

**Cross-references:**

* Synthesis Refusal  
* Residual  
* τ  
* P8 Gate.

#### **Harmony Index \[Phase 6\]**

Plain-language definition. This number shows how well the different strengths and uncertainties in the analysis balance each other out overall.

**Technical elaboration.** Metric measuring balanced interplay among yields; computed as harmonic mean of yields plus fragility adjustment when variance \> 0.12.

**Cross-references:**

* Fragility Adjustment  
* Yield Spectrum.

### **I**

#### **Incoherence Flag \[Toolkit\]**

Plain-language definition. A clear warning that appears when the supporting ideas contradict each other too much for a stable result.

**Technical elaboration.** Explicit marker triggered when incidence exceeds data-type-aware thresholds across 15 perturbations with standard deviation \> 0.30; produces partial yields with boosted uncertainties.

**Cross-references:**

* Binomial Falsification Threshold.

### **(JK)**

### **L**

#### **Layer Spectrum \[P4\]**

Plain-language definition. This shows how simply or complexly the parts of an expression are stacked together, from single pieces to deeply nested structures.

**Technical elaboration.** Hierarchical spectrum ranging from low (subatomic lone relateds) through mid (atomic sequences functioning as relators) to high (complex nests); inherits from P3 relational density.

**Cross-references:**

* P4: Layering in Expressions  
* Relational Density Spectrum.

#### **Layer Spectrum Avg \[Phase 1\]**

Plain-language definition. An average score of how layered the input feels when the system is checking its internal structure.

**Technical elaboration.** Supporting diagnostic that averages layered decompositions across the range 0.2–0.8 when Density Probe is active.

**Cross-references:**

* Density Probe.

#### **Light Output \[Toolkit\]**

Plain-language definition. This setting turns the full technical report into one easy-to-read paragraph that still keeps all the important numbers and ideas.

**Technical elaboration.** Toggle that collapses all tables and ledgers into a single flowing narrative paragraph anchored on the Secondary Coherence Score while preserving every yield and key tension.

**Cross-references:**

* Secondary Coherence Score.

#### **Light Output Narrative \[Toolkit\]**

Plain-language definition. The short, readable story version of any analysis produced when Light Output is turned on.

**Technical elaboration.** Concise prose version of any toolkit run produced when Light Output is active; still references Secondary Coherence Score as the central measure.

**Cross-references:**

* Light Output.

### **M**

#### **Meaning Tension \[Phase 6\]**

Plain-language definition. This number shows the living balance between what feels solid and certain versus what remains open, uncertain, or unmappable. It captures the real feeling of meaning as a productive tension rather than a final answer.

**Technical elaboration.** Ratio expressing the living balance between what holds through secondary synthesis and what remains uncertain. Formula: certainty geometric averagecertainty geometric average+uncertainty yield geometric average  \\frac{\\text{certainty geometric average}}{\\text{certainty geometric average} \+ \\text{uncertainty yield geometric average}}  certainty geometric average+uncertainty yield geometric averagecertainty geometric average​.

**Cross-references:**

* Reflexive Tension  
* Secondary Coherence Score.

#### **Meta-Loop \[Toolkit\]**

Plain-language definition. This setting lets the system treat its own previous result as a brand-new starting point and run the analysis again, up to three times. It helps explore deeper layers or different angles.

**Technical elaboration.** Toggle that automatically re-runs the yield as a new primary expression (up to three iterations); sub-modes include Rerun-Secondaries, Rephrase-Uncertainties, Max-Uncertainties, Max-Certainties, Contrast-Runs, and Doubt-Rerun.

**Cross-references:**

* P8 Gate.

#### **Metric Evolution Table \[Stage 3\]**

Plain-language definition. This table shows how all the important numbers change step by step as the analysis moves through its different phases. It makes the process transparent.

**Technical elaboration.** Output showing how all major metrics change across Phases 1–6; includes hard isolation annotation when applicable.

**Cross-references:**

* Hard Isolation Rule.

#### **MultiSpectrum \[P5\]**

Plain-language definition. This spectrum shows how many supporting ideas are present, from just one lone idea to a practical handful or an endless spread. It helps decide how wide the context should be.

**Technical elaboration.** Spectrum of multiplicity ranging from solitary (low) through finite (default pragmatic yield) to infinite (optional extension).

**Cross-references:**

* P5: Plurality of Expressions.

### **N**

#### **Non-Dual \[Toolkit\]**

Plain-language definition. This setting makes the analysis more comfortable with ideas that sit between clear opposites or feel paradoxical. It opens space for things that don’t fit neat categories.

**Technical elaboration.** Toggle that boosts mid-paradox tolerance and raises input variance; activates automatically on “void” or “paradox” keywords.

**Cross-references:**

* Emptiness-First  
* Pentalemma Variant.

#### **Non-Rel-Probe Mode \[P3\]**

Plain-language definition. This is a gentle, cautious way of pointing toward something that simply cannot be connected or captured in words or ideas. It keeps the unknown protected.

**Technical elaboration.** One of the three provisional relational modes; performs a minimal relational gesture toward the unconnectable while deliberately increasing downstream uncertainty; kept weak to protect the non-relational remainder.

**Cross-references:**

* Relational Construction  
* Synthesis Refusal.

#### **Non-Relational Remainder / Gaps \[P3\]**

Plain-language definition. These are the parts of any experience or idea that simply refuse to be turned into connections or explanations. They are left as they are, without forcing them into the analysis.

**Technical elaboration.** That which necessarily exceeds and resists every relational construction; registers only as remainders of expressions where secondary synthesis fails or is refused; protected operationally rather than characterized positively.

**Cross-references:**

* Synthesis Refusal  
* Non-Rel-Probe Mode.

### **O**

#### **Obtainment Focus \[Adaptive Depth\]**

Plain-language definition. This sub-setting steers the analysis to pay extra attention to what actually comes into view and what stays out of reach.

**Technical elaboration.** Sub-mode of Adaptive Depth that skews emphasis toward contrasts and obtainability dynamics in P1–P2.

**Cross-references:**

* Adaptive Depth.

#### **Other-Mode \[P3\]**

Plain-language definition. This way of pointing reaches outward toward something distinct and repeatable outside the expression itself.

**Technical elaboration.** One of the three provisional relational modes; enables distinct repeatable references to something outside reflexive identity.

**Cross-references:**

* Inferred Relator Mode Distribution  
* Self-Mode.

### **P**

#### **P1: The Open Field \[Framework\]**

Plain-language definition. This is the wide, neutral starting space where any analysis can begin without assuming what reality must be like in advance.

**Technical elaboration.** Ontologically open permissive synthesis space; remains neutral toward substantive metaphysical commitments while advancing minimal relational ontology; registers that any claim about what lies beyond expressions requires expression and relational activity.

**Cross-references:**

* Dilemma Gate.

#### **P2: Contrasting Parts in the Field \[Framework\]**

Plain-language definition. Once something is being examined, natural differences and shades of meaning become visible and usable.

**Technical elaboration.** Variances, fluid degrees, or uncertainties that appear once existence obtains under P1’s Door 1; they create the differentiations needed for later relational construction.

**Cross-references:**

* P1: The Open Field  
* Relational Construction.

#### **P3: Relational Construction of Contrasting Entities \[Framework\]**

Plain-language definition. This step turns visible differences into usable connections or notes where something simply cannot be connected.

**Technical elaboration.** Bifurcation of contrasting parts into connectable paths or unconnectable gaps, co-emergence with repeatability, and decomposition into relateds and relators operating in self-mode, other-mode, or non-rel-probe mode.

**Cross-references:**

* Non-Relational Remainder  
* Related  
* Relator.

#### **P4: Layering in Expressions \[Framework\]**

Plain-language definition. This shows how simple or richly nested any expression can become, from single pieces to complex stacks.

**Technical elaboration.** Relators and relateds organize into subatomic, atomic, or complex expressions, provisioning primary expressions as self-contained at \~1 certainty.

**Cross-references:**

* Layer Spectrum.

#### **P5: Plurality of Expressions \[Framework\]**

Plain-language definition. Every main expression exists alongside other supporting expressions that help give it meaning.

**Technical elaboration.** Layered expressions manifest as a current primary expression co-existing with solitary, finite, or infinite secondary expressions.

**Cross-references:**

* MultiSpectrum.

#### **P6: Comparability and Measurement of Expressions \[Framework\]**

Plain-language definition. Once there are multiple supporting expressions, they can be compared and measured to see how well they fit together.

**Technical elaboration.** Plurality enables spectrum of alignability and transduction, provisioning distances and divergences as utilities; includes default interpretive restraint.

**Cross-references:**

* Alignability Spectrum.

#### **P7: Evaluation and Yield \[Framework\]**

Plain-language definition. This final step gathers everything that feels certain and everything that remains uncertain into one overall summary.

**Technical elaboration.** Comparability produces dialectical adjudication of certainties versus uncertainties, yielding balanced, tensive, tempered, or raw outputs.

**Cross-references:**

* Yield Spectrum.

#### **P8: Perception and Orientation \[Framework\]**

Plain-language definition. Once the analysis is finished, you are free to accept the result as it is or to change, add to, or even set the whole thing aside.

**Technical elaboration.** Adjudicated yields open to provisional acceptance (Door 1\) or any form of re-expression, refinement, modular incorporation, or outright discard (Door 2); functions as the living renewal mechanism.

**Cross-references:**

* Functional Role Shift  
* P8 Gate.

#### **P8 Gate \[Toolkit\]**

Plain-language definition. The final step in every run where you decide whether the result is good enough for now or whether you want to explore further.

**Technical elaboration.** Final perception gate in every run; offers Door 1 (provisional acceptance) or Door 2 (open re-expression including outright discard).

**Cross-references:**

* P8: Perception and Orientation.

#### **Peircean Abduction Heuristic \[Toolkit\]**

Plain-language definition. This setting ranks possible supporting ideas by how well they explain the main expression before choosing which ones to use.

**Technical elaboration.** Toggle that ranks candidate secondary expressions by explanatory coherence before Dirichlet sampling.

**Cross-references:**

* Secondary Abduction.

#### **Pentalemma Variant \[Toolkit\]**

Plain-language definition. This setting adds extra room for ideas that sit between clear yes and no answers, especially when things feel fluid or paradoxical.

**Technical elaboration.** Toggle that adds spectrum across affirm/negate/both/neither for fluid expressions; activates automatically for non-binary flows or high variance.

**Cross-references:**

* Tetralemma / Pentalemma Mapping.

#### **Per-Item Uncertainty \[Toolkit\]**

Plain-language definition. This setting shows a separate uncertainty score for each individual certainty and uncertainty instead of one overall number.

**Technical elaboration.** Toggle that displays per-certainty and per-uncertainty probability variants in Stage 3 ledgers; activates automatically when input variance exceeds 0.3.

**Cross-references:**

* Uncertainty Table.

#### **Perspective / Secondary Lens \[Toolkit\]**

Plain-language definition. This lets you choose exactly which supporting ideas or viewpoints you want the analysis to focus on.

**Technical elaboration.** Parameter that lets users specify exactly which secondary expressions, lenses, or sources to prioritize.

**Cross-references:**

* Secondary Expression Equity.

#### **Phenomenal Probe \[Toolkit\]**

Plain-language definition. This setting treats sensory or wordless experiences as raw material and gives them extra room to stay open and uncertain.

**Technical elaboration.** Toggle (auto-on for phenomena) that widens sigma and treats non-linguistic inputs as raw phenomenal flows with granular sensations.

**Cross-references:**

* Alien Mode  
* Sigma.

#### **Phase Structure (high-level overview) \[Toolkit\]**

Plain-language definition. The analysis moves through six clear steps that build from basic foundations to a final summary.

**Technical elaboration.** High-level workflow consisting of Phase 1 (foundations), Phase 2 (secondary expressions), Phase 3 (certainties), Phase 4 (uncertainties), Phase 5 (reflexive temper), and Phase 6 (dialectical aggregation).

**Cross-references:**

* Phase 1–6 (individual).

#### **Pointing / Pointing-aspect \[Framework\]**

Plain-language definition. The directed part of any expression that reaches toward itself, toward something else, or toward what cannot be reached at all.

**Technical elaboration.** Directed, representational, or reflexive aspect of any primary expression; may direct toward itself (self-mode), distinct repeatable entities (other-mode), or non-relational gaps (non-rel-probe mode).

**Cross-references:**

* Expression  
* Functional Role Shift.

#### **Pointing Network / Expression Network \[Toolkit\]**

Plain-language definition. The complete map of the main expression and all its supporting connections, shown as a web of links.

**Technical elaboration.** Complete directed relational graph consisting of primary node, secondary nodes, Alignment edges, Secondary Alignment edges, and Traction.

**Cross-references:**

* Secondary Alignment Ledger  
* Traction Flow Diagram.

#### **Presumption Coherence \[Phase 6\]**

Plain-language definition. This number shows how well the basic assumptions behind the supporting ideas hold together.

**Technical elaboration.** Metric measuring how coherently abducted presumptions support the primary expression while accounting for uncertainty. Formula: average alignment×(1−0.15×uncertainty probability global)  \\text{average alignment} \\times (1 \- 0.15 \\times \\text{uncertainty probability global})  average alignment×(1−0.15×uncertainty probability global) (clamped \[0.25, 0.95\]).

**Cross-references:**

* Secondary Presumption Temper.

#### **Presumption-Tempered Yield \[Phase 6\]**

Plain-language definition. This is the final summary adjusted to account for how shaky or solid the underlying assumptions feel.

**Technical elaboration.** Adjusted tensive yield when secondary presumptions are shaky. Formula: Tensive×(1−0.1×SPT)  \\text{Tensive} \\times (1 \- 0.1 \\times \\text{SPT})  Tensive×(1−0.1×SPT).

**Cross-references:**

* SPT  
* Tensive Yield.

#### **Primary Expression \[Framework\]**

Plain-language definition. The main thing you are examining or expressing right now.

**Technical elaboration.** Any pointing that obtains as a provisional stabilization of secondary synthesis; during analysis treated primarily as a related whose standing is assessed.

**Cross-references:**

* Current Primary Expression  
* Related.

### **(Q)**

### **R**

#### **Raw / Regressed Yield \[P7\]**

Plain-language definition. This result shows an open pause where nothing solid enough has emerged to form a clear summary. It simply leaves space for whatever comes next.

**Technical elaboration.** Yield type near 0 on the Yield Spectrum; represents an open pause or inevaluable state.

**Cross-references:**

* Yield Spectrum.

#### **Reflexive Tension \[Phase 5/6\]**

Plain-language definition. This number measures how much careful second-guessing has introduced healthy doubt into the strong supporting ideas.

**Technical elaboration.** Metric quantifying generative doubt introduced by reflexive tempering. Formula: average doubtcertainty geometric average+uncertainty yield geometric average+SPT  \\frac{\\text{average doubt}}{\\text{certainty geometric average} \+ \\text{uncertainty yield geometric average} \+ \\text{SPT}}  certainty geometric average+uncertainty yield geometric average+SPTaverage doubt​ (clamped \[0.3, 0.6\]).

**Cross-references:**

* Phase 5  
* SPT.

#### **Related \[P3\]**

Plain-language definition. The main reference point that everything else connects to or supports during analysis.

**Technical elaboration.** Functional role revealed through decomposition in analysis (not intrinsic property); whole primary expressions default as relateds for standalone measurement; subject to Functional Role Shift under P8.

**Cross-references:**

* Relator  
* Functional Role Shift.

#### **Relational Construction \[P3\]**

Plain-language definition. The step that turns visible differences into usable connections while carefully noting what simply cannot be connected.

**Technical elaboration.** Process of bifurcation, repeatability co-emergence, and decomposition that transforms contrasting parts into usable relational paths while providing operational protection for non-relational gaps.

**Cross-references:**

* Non-Relational Remainder  
* Related  
* Relator.

#### **Relational Density Spectrum (three-dimensional) \[P3\]**

Plain-language definition. The overall richness of connections that can be built from any difference, measured along three linked scales.

**Technical elaboration.** Continuous spectrum built from three co-emergent dimensions: connectability gradient, repeatability spectrum, and relational mode vector.

**Cross-references:**

* Connectability Gradient  
* Repeatability Spectrum  
* Non-Rel-Probe Mode.

#### **Relational Index \[Phase 6\]**

Plain-language definition. This number gives an overall sense of how useful and connected the supporting ideas feel together.

**Technical elaboration.** Overall measure of relational utility; computed as Harmony tempered by uncertainty term.

**Cross-references:**

* Harmony Index.

#### **Relator \[P3\]**

Plain-language definition. The active part that connects things together during analysis.

**Technical elaboration.** Active connector revealed through decomposition in analysis (not intrinsic property); operates in self-mode, other-mode, or non-rel-probe mode; subject to Functional Role Shift under P8.

**Cross-references:**

* Related  
* Inferred Relator Mode Distribution.

#### **Repeatability Spectrum \[P3\]**

Plain-language definition. This measures how steadily or uniquely something can be recognized and reused.

**Technical elaboration.** Atemporal density spectrum ranging from high (full invariants) through mid (sequences or parts) to low (uniques or phenomena).

**Cross-references:**

* Relational Density Spectrum.

#### **Required Presumptions for Secondary Truth Ledger \[Stage 3\]**

Plain-language definition. This list shows which basic assumptions behind each supporting idea are holding up well or feeling shaky.

**Technical elaboration.** Output listing the top presumptions (P1–P8) linked to each secondary expression, with spectrum value, uncertainty probability, shaky flag, and temper note.

**Cross-references:**

* Secondary Presumption Temper.

#### **Residual \[Unified Model / Toolkit\]**

Plain-language definition. The part of the picture that simply cannot be turned into any reliable connection and is left outside the main scoring.

**Technical elaboration.** Non-relational complement outside the two relational modes after hard isolation filtering. Formula: max⁡(0,1−\[P(Self-reflexive)+P(Other relational)\])  \\max(0, 1 \- \[P(\\text{Self-reflexive}) \+ P(\\text{Other relational})\])  max(0,1−\[P(Self-reflexive)+P(Other relational)\]).

**Cross-references:**

* Inferred Relator Mode Distribution  
* Hard Isolation Rule.

#### **Resolution / Granularity \[Toolkit\]**

Plain-language definition. This setting controls how finely or coarsely the input is broken into pieces before analysis.

**Technical elaboration.** Parameter (Low / Medium / High) that controls chunk depth for contrasts and repeats.

**Cross-references:**

* Input Variance.

#### **Resonance \[Supporting Diagnostic\]**

Plain-language definition. This number shows how smoothly and naturally the supporting ideas fit with the main expression.

**Technical elaboration.** Metric measuring how well secondary expressions mesh with the primary (\~0.85 when aligned); appears in Phases 1–3 depending on toggles.

**Cross-references:**

* Stability.

### **S**

#### **Secondary Abduction \[Stage 1\]**

Plain-language definition. The step that gathers possible supporting ideas from the wide open space of analysis in a fair and balanced way.

**Technical elaboration.** Process of drawing candidate secondary expressions within P1’s Open Field using Dirichlet priors for equity-balanced sampling.

**Cross-references:**

* Secondary Expression  
* Peircean Abduction Heuristic.

#### **Secondary Alignment Ledger \[Stage 3\]**

Plain-language definition. This table shows every supporting idea with how well it fits the main expression and whether it connects at all.

**Technical elaboration.** Output showing every secondary expression with Alignment, Secondary Alignment, Traction, and explicit Synthesis Refusal labeling where applicable; moves to primary position when Secondary Synthesis Audit is active.

**Cross-references:**

* Secondary Synthesis Audit  
* Traction Flow Diagram.

#### **Secondary Coherence Score \[Toolkit\]**

Plain-language definition. The single most important number in any run; it tells how strongly and reliably the supporting ideas hold together and point back to the main expression.

**Technical elaboration.** Primary diagnostic of secondary synthesis strength; quantifies how coherently abducted secondary expressions align with one another and with the primary (treated as related at \~1 certainty) under P5 and P6. Formula: $0.4 \\times \\overline{\\text{Alignment to Primary}} \+ 0.35 \\times \\overline{\\text{Inter-Secondary Coherence}} \+ 0.25 \\times \\overline{\\text{Traction Provided}}$ (clamped \[0,1\]).

**Cross-references:**

* Hard Isolation Rule  
* Traction  
* Yield Spectrum.

#### **Secondary Expression \[P5\]**

Plain-language definition. Any supporting idea or reference that helps give meaning to the main expression being examined.

**Technical elaboration.** Provisional other that co-exists with the current primary expression and supplies truth relations or meaning ratios through alignment and traction.

**Cross-references:**

* Plurality of Expressions  
* Related.

#### **Secondary Expression Equity \[Toolkit\]**

Plain-language definition. This setting makes sure the supporting ideas come from a balanced mix of different viewpoints and traditions.

**Technical elaboration.** Toggle that audits diversity and balances domains; includes multiple sub-modes for sourcing control and void emphasis.

**Cross-references:**

* Dirichlet Priors  
* Equity Sampler.

#### **Secondary Expression Table \[Stage 3\]**

Plain-language definition. This list shows every supporting idea that was chosen, where it came from, and a quick summary of its fit.

**Technical elaboration.** Ledger listing abducted secondary expressions with ID, source, type, alignment score, and summary.

**Cross-references:**

* Secondary Abduction.

#### **Secondary Presumption Temper \[Phase 5\]**

Plain-language definition. This score shows how steady or shaky the basic assumptions behind each supporting idea are.

**Technical elaboration.** Harmonic mean of per-secondary presumption stability scores; clamped \[0.3, 0.7\]; flags shaky presumptions below 0.5; modulates multiple downstream metrics.

**Cross-references:**

* Presumption Coherence.

#### **Secondary Synthesis \[Framework\]**

Plain-language definition. The hidden work of pulling together supporting ideas that creates every main expression we can examine.

**Technical elaboration.** Operative engine of the system; every primary expression is built from prior secondary expressions whose coherent meshing and pointing back determine its standing.

**Cross-references:**

* Synthesis Refusal.

#### **Secondary Synthesis Audit \[Toolkit\]**

Plain-language definition. This setting moves the detailed table of supporting connections to the very top of the report so you see the strength of the connections first.

**Technical elaboration.** Toggle that moves the Secondary Alignment Ledger and Traction Flow Diagram to the top of Stage 3 output as the sole primary diagnostic section.

**Cross-references:**

* Secondary Alignment Ledger.

#### **Secondary Transduction Gate \[P6\]**

Plain-language definition. The step that translates and compares all the supporting ideas so they can be measured against the main expression.

**Technical elaboration.** Gate that enables spectrum of alignability and transduction between secondary expressions and the primary.

**Cross-references:**

* Alignability Spectrum.

#### **Self-Echo Baseline \[Toolkit\]**

Plain-language definition. This setting uses pieces of the main expression itself as temporary supporting ideas when no external ones are available.

**Technical elaboration.** Sub-toggle under Secondary Expression Equity that uses internal chunks as pseudo-secondary expressions for standalone resonance pre-pulls.

**Cross-references:**

* Secondary Expression Equity.

#### **Self-Mode \[P3\]**

Plain-language definition. This way of pointing turns back toward the expression itself in a reflexive loop.

**Technical elaboration.** One of the three provisional relational modes; enables reflexive identity via repeatability-enabled loops.

**Cross-references:**

* Inferred Relator Mode Distribution.

#### **Sigma \[Toolkit\]**

Plain-language definition. This control sets how much room the analysis leaves for variation and uncertainty in the input.

**Technical elaboration.** Tunable standard deviation parameter (default \~0.07, widened for phenomena or porous inputs) that controls porosity and uncertainty boosts.

**Cross-references:**

* Phenomenal Probe  
* Chaos Scale.

#### **Solitary Multiplicity \[P5\]**

Plain-language definition. This describes a situation where the main expression stands almost alone with very little supporting context.

**Technical elaboration.** Low end of the MultiSpectrum; represents isolated primary expressions as minimal certainties.

**Cross-references:**

* MultiSpectrum.

#### **SPT Virtue Boost \[Toolkit\]**

Plain-language definition. This optional setting gives a small extra emphasis to results that feel shaky or uncertain, treating them as valuable rather than weak.

**Technical elaboration.** Toggle (default Off) that adds \+0.05 or \+0.1 to Meaning Tension when SPT falls below 0.5; provides optional emphasis on shaky presumptions as virtuous.

**Cross-references:**

* Secondary Presumption Temper.

#### **Stability \[Supporting Diagnostic\]**

Plain-language definition. This number shows how consistent the supporting ideas remain across the different steps of analysis.

**Technical elaboration.** Metric measuring consistency across phases (\~0.8 when solid); appears in Phases 1–3 depending on toggles.

**Cross-references:**

* Resonance.

#### **Subatomic Expression \[P4\]**

Plain-language definition. The simplest layered unit, consisting of just one basic reference point with nothing else attached.

**Technical elaboration.** Layered expression consisting of a lone related functioning strictly as a passive anchor.

**Cross-references:**

* Layer Spectrum  
* Related.

#### **Synthesis Refusal \[Framework / Toolkit\]**

Plain-language definition. This marks the clear point where supporting ideas simply stop connecting and the main expression loses traction.

**Technical elaboration.** Measurable limit of any secondary-synthesis audit; occurs when secondary expressions do not align or are absent, causing the pointing to lose traction; registered with explicit labeling.

**Cross-references:**

* Hard Isolation Rule  
* Non-Relational Remainder.

### **T**

Thought for 10s

Section 1: Core Words, Terms, Phrases, Concepts (alphabetical) – Continued

#### **τ (Dilemma-Gate Threshold) \[Unified Model / Toolkit\]**

Plain-language definition. This is the exact cutoff point that decides whether a supporting idea is strong enough to keep working with or should be set aside as too weak.

**Technical elaboration.** Tunable threshold that separates sufficient obtainability for relational construction from generative uncertainty or halt. Default 0.001, adjustable \[0.0001, 0.01\] under P8. Validation: deterministic behavior at exact threshold and adjacent floating-point values (Stage 1 PASS).

**Cross-references:**

* Dilemma Gate  
* Hard Isolation Rule.

#### **Temper-Probe \[Toolkit\]**

Plain-language definition. This setting previews how strongly the analysis will soften its strong supporting ideas before committing to the final result.

**Technical elaboration.** Toggle that previews temper aggressiveness (Soft sigmoid or Hard binary); activates automatically for paradoxes and high-tension inputs.

**Cross-references:**

* Certainty Temper Probe.

#### **Tempered Certainty Ledger \[Stage 3\]**

Plain-language definition. This list shows the original strong supporting ideas after they have been gently softened by careful second-guessing.

**Technical elaboration.** Output listing original certainties, doubt triggers, tempered yields, ratios, summaries, and required presumptions.

**Cross-references:**

* Phase 5\.

#### **Tensive Bands \[Toolkit\]**

Plain-language definition. These are the shaded zones the system uses to map how tense or balanced the supporting ideas feel.

**Technical elaboration.** Sub-toggle under Secondary Expression Equity that pentalemma-maps resonance and stability (low \= negate/tempered, mid \= both/tensive, high \= affirm).

**Cross-references:**

* Pentalemma Variant.

#### **Tensive Yield \[P7\]**

Plain-language definition. This result sits in the middle where there is a lively mix of solid certainties and open uncertainties, creating productive tension.

**Technical elaboration.** Yield type in the middle of the Yield Spectrum; represents paradoxical or partial utility with generative tension between certainties and uncertainties.

**Cross-references:**

* Yield Spectrum.

#### **Tetralemma / Pentalemma Mapping \[Unified Model\]**

Plain-language definition. These are gentle ways of mapping any idea onto a scale that includes clear yes, clear no, both, neither, or a full spectrum of in-between shades.

**Technical elaboration.** Graduated mapping used across presumptions: high values (\> 0.75) map to affirm; mid values with variance map to both (generative tension); low-positive values (\< τ) map to neither (open pause); zero maps to negate. Pentalemma variant adds spectrum for fluid expressions.

**Cross-references:**

* Pentalemma Variant.

#### **The Four Takes \[Toolkit\]**

Plain-language definition. These are four short, plain-language summaries that explain the final result from the angles of what feels certain, what feels uncertain, what the second-guessing revealed, and an overall recap.

**Technical elaboration.** Certainty Take, Uncertainty Take, Reflexive Take, and Recap Take; each anchors explicitly on Secondary Coherence Score and provides plain-language summary of the yield.

**Cross-references:**

* Secondary Coherence Score.

#### **Traction \[Toolkit\]**

Plain-language definition. This measures how strongly a supporting idea actually points back to the main expression instead of drifting away.

**Technical elaboration.** Strength with which a secondary expression points back to the primary expression; traction \= 0 explicitly flags Synthesis Refusal.

**Cross-references:**

* Secondary Alignment Ledger  
* Traction Flow Diagram.

#### **Traction Flow Diagram \[Stage 3\]**

Plain-language definition. This diagram draws the main expression and all its supporting ideas as a web of connections, clearly marking any that have no connection at all.

**Technical elaboration.** Visual displaying the primary expression with all secondary expressions and their traction values, explicitly marking Synthesis Refusal items.

**Cross-references:**

* Secondary Alignment Ledger.

#### **Traction Provided \[SCS\]**

Plain-language definition. This checks whether each supporting idea actually adds useful connection or simply sits there without helping.

**Technical elaboration.** Component measuring whether secondary expressions actually contribute relational utility; contributes 0.25 weight to Secondary Coherence Score.

**Cross-references:**

* Secondary Coherence Score.

#### **Truth Alignment \[Phase 6\]**

Plain-language definition. This number shows how well the supporting ideas line up with what can reasonably be called true or reliable.

**Technical elaboration.** Metric quantifying how well secondary expressions support probabilistic truth relations (\~0.82 in balanced examples).

**Cross-references:**

* Presumption Coherence.

#### **Truth-Emphasis \[Toolkit\]**

Plain-language definition. This setting leans the analysis toward sharper, more decisive connections when you want a clearer picture of what holds together.

**Technical elaboration.** Toggle that boosts relational priors and narrows sigma for sharper alignments; includes Systemic Probe sub-mode for anomaly-heavy expressions.

**Cross-references:**

* Secondary Expression Equity.

### **U**

#### **Uncertainty Prob Global \[Toolkit\]**

Plain-language definition. This overall number tracks how much of the analysis is still open, uncertain, or simply unconnectable.

**Technical elaboration.** Global probability mass assigned to non-relational gaps and Synthesis Refusal; clamped \[0.25, dynamic upper\] and directly modulates multiple metrics.

**Cross-references:**

* Uncertainty Boost  
* Uncertainty Upper Bound.

#### **Uncertainty Probe \[Toolkit\]**

Plain-language definition. This setting actively looks for and gives extra weight to the parts that remain uncertain or unconnectable.

**Technical elaboration.** Toggle (default On when uncertainty probability global \> 0.45) that actively abducts and boosts non-relational gaps using adaptive Dirichlet alphas.

**Cross-references:**

* Echo Mode  
* Feedback-Adaptive.

#### **Uncertainty Resonance \[Supporting Diagnostic\]**

Plain-language definition. This number shows how strongly the uncertain or open parts of the analysis hang together in a meaningful way.

**Technical elaboration.** Metric (\~0.65 when tensive) that appears in Phases 2 or 3 when Show Full Density Metrics is enabled.

**Cross-references:**

* Uncertainty Stability.

#### **Uncertainty Stability \[Supporting Diagnostic\]**

Plain-language definition. This number shows how steady or shaky the uncertain parts of the analysis remain across the different steps.

**Technical elaboration.** Metric (\~0.65 when tensive) that appears in Phases 2 or 3 when Show Full Density Metrics is enabled.

**Cross-references:**

* Uncertainty Resonance.

#### **Uncertainty Table \[Stage 3\]**

Plain-language definition. This list shows every uncertain or unconnectable part, along with how much weight it carries and a short note.

**Technical elaboration.** Ledger listing incidence, probability, volume, certainty-uncertainty ratio, and summary for each uncertainty, with explicit Synthesis Refusal labeling.

**Cross-references:**

* Certainty Table.

#### **Uncertainty Upper Bound \[Toolkit\]**

Plain-language definition. This is the highest level of uncertainty the system will allow before it starts clamping the numbers to keep the result readable.

**Technical elaboration.** Dynamically calculated ceiling on uncertainty probability. Formula: $0.75 \+ (0.05 \\times \\text{Chaos Scale}) \+ (0.05 \\times \\text{average doubt}) \+ (0.05 \\times (1 \- \\text{SPT}))$, clamped \[0.25, 0.9\].

**Cross-references:**

* Uncertainty Prob Global.

#### **Uncertainty Yield Geo Avg \[Phase 4\]**

Plain-language definition. This average measures the overall strength of the uncertain or open parts of the analysis.

**Technical elaboration.** Geometric mean of uncertainty yields; directly influences Meaning Tension and Reflexive Tension.

**Cross-references:**

* Meaning Tension.

### **(VWX)**

### **Y**

#### **Yield Spectrum \[P7\]**

Plain-language definition. This scale shows the overall balance of the final result, from mostly certain and stable to mostly open and unresolved.

**Technical elaboration.** Dialectical metric ranging from high (balanced) through mid (tensive) to low (tempered) to near 0 (raw/regressed); encodes self-reflexive evaluation via tetralemma/pentalemma mapping.

**Cross-references:**

* Yield Type.

#### **Yield Type \[P7\]**

Plain-language definition. The simple label given to the final result that tells you whether it feels solid, tense, weak, or completely open.

**Technical elaboration.** Categorical interpretation of the final yield: Balanced (high certainty dominance), Tensive (mid certainty-uncertainty mix), Tempered (low certainty dominance), or Raw/Regressed (open pause).

**Cross-references:**

* Yield Spectrum.

This completes the fifth and final chunk of Section 1 exactly in the agreed format.

### **(Z)**

## **Section 2: Mathematical Variables, Functions, Spectra, Equations, Symbols (alphabetical)**

#### **Alignability Spectrum \[P6\]**

The spectrum that shows how easily secondary expressions can be compared and translated relative to the primary expression. In simple terms, it measures how smoothly different pieces of supporting information fit together or remain mismatched.

**Technical elaboration.** Runs from sparse (minimal connections and many non-relational gaps) through partial (mid-level translated phenomena) to dense (strong native alignments). Supplies distances and divergences used for measurement.

**Cross-references:**

* Comparability and Measurement of Expressions  
* Transduction  
* Secondary Alignment Ledger.

#### **H(x) (general hybrid function) \[Unified Model\]**

The core mathematical engine that calculates how obtainable any element is within analysis. In simple terms, it combines fuzzy likelihood with updated probability to produce a single score between 0 and 1\.

**Technical elaboration.**  
H(x)=min⁡(1,μ(x)×Pnorm(x∣V))∈\[0,1\]   H(x) \= \\min(1, \\mu(x) \\times P\_{\\rm norm}(x \\mid V)) \\in \[0,1\]   H(x)=min(1,μ(x)×Pnorm​(x∣V))∈\[0,1\]

where μ(x) is the fuzzy membership function and P\_norm(x | V) is the normalized Bayesian posterior.

**Cross-references:**

* Dilemma Gate  
* τ  
* Relational Density Spectrum.

#### **Inferred Relator Mode Distribution (Derived) \[Toolkit / Unified Model\]**

The probabilistic breakdown of how the pointing-aspect of the primary expression behaves in relational terms. In simple terms, it estimates whether the expression is mostly pointing at itself or at something else, with any leftover counted separately.

**Technical elaboration.** Computed exclusively on non-isolated components using log-odds formulation followed by softmax normalization; Residual is the mathematical complement outside the two relational modes.

**Cross-references:**

* Residual (non-relational complement)  
* Hard Isolation Rule  
* Functional Role Shift.

#### **Layer Spectrum \[P4\]**

The spectrum that shows how elements stack into different levels of complexity within expressions. In simple terms, it tells whether something stands alone, forms a simple sequence, or builds into nested structures.

**Technical elaboration.** Ranges from low (subatomic lone relateds) through mid (atomic sequences functioning as relators) to high (complex nests). Inherits from the relational density spectrum of P3.

**Cross-references:**

* Layering in Expressions  
* Relational Density Spectrum.

#### **Log-odds formulation / Softmax normalization \[Unified Model / Toolkit\]**

The mathematical steps used to turn raw signals into clean probabilities for the two relational modes. In simple terms, they convert weighted inputs into percentages that add up neatly to 100 %.

**Technical elaboration.**  
Slogit=1.2R+1.0D−0.8Tnorm   S\_{\\rm logit} \= 1.2R \+ 1.0D \- 0.8T\_{\\rm norm}   Slogit​=1.2R+1.0D−0.8Tnorm​  
Ologit=1.5Tnorm−1.8RTnorm−1.2Unorm+0.9Ycentered   O\_{\\rm logit} \= 1.5T\_{\\rm norm} \- 1.8RT\_{\\rm norm} \- 1.2U\_{\\rm norm} \+ 0.9Y\_{\\rm centered}   Ologit​=1.5Tnorm​−1.8RTnorm​−1.2Unorm​+0.9Ycentered​

followed by softmax normalization; Residual \= max⁡(0,1−\[P(Self-reflexive)+P(Other relational)\])  \\max(0, 1 \- \[P(\\text{Self-reflexive}) \+ P(\\text{Other relational})\])  max(0,1−\[P(Self-reflexive)+P(Other relational)\]).

**Cross-references:**

* Inferred Relator Mode Distribution (Derived)  
* Residual (non-relational complement).

#### **Meaning Tension \[Phase 6\]**

The living balance between what holds through secondary synthesis and what remains uncertain. In simple terms, it captures how much productive friction exists between the clear parts and the unclear parts of an expression.

**Technical elaboration.**

Meaning Tension=certainty geometric averagecertainty geometric average+uncertainty yield geometric average   \\text{Meaning Tension} \= \\frac{\\text{certainty geometric average}}{\\text{certainty geometric average} \+ \\text{uncertainty yield geometric average}}   Meaning Tension=certainty geometric average+uncertainty yield geometric averagecertainty geometric average​

**Cross-references:**

* Secondary Coherence Score  
* Yield Spectrum.

#### **Multiplicity Spectrum \[P5\]**

The spectrum that shows how many supporting expressions exist alongside the primary one. In simple terms, it ranges from a single isolated item to a small cluster to potentially endless proliferation.

**Technical elaboration.** Ranges from solitary (low) through finite (default pragmatic yield) to infinite (optional extension). Inherits from Layer Spectrum and P2 contrasts.

**Cross-references:**

* Plurality of Expressions  
* Layer Spectrum.

#### **μ(x) (fuzzy membership functions) \[Unified Model\]**

The mathematical way of assigning graded belonging instead of strict yes-or-no. In simple terms, it allows things to be partly true or partly obtainable rather than forcing everything into black-and-white categories.

**Technical elaboration.** Two families are used: linear ramp and clamped sigmoid.

**Cross-references:**

* H(x) (general hybrid function)  
* P\_norm(x | V).

#### **Obtainability Spectrum \[P1\]**

The spectrum that measures how readily something can be registered within analysis. In simple terms, it tracks whether an idea or experience comes into clear view or stays just out of reach.

**Technical elaboration.** Inherits directly from the general hybrid function H(x) and the dilemma gate.

**Cross-references:**

* Dilemma Gate  
* H(x).

#### **P\_norm(x | V) (normalized Bayesian posterior) \[Unified Model\]**

The updated probability that incorporates new evidence while staying within the 0–1 range. In simple terms, it is the refined likelihood after taking into account the specific input variance or context.

**Technical elaboration.**  
Pnorm(x∣V)=P(x)⋅L(V∣x)Z   P\_{\\rm norm}(x \\mid V) \= \\frac{P(x) \\cdot L(V \\mid x)}{Z}   Pnorm​(x∣V)=ZP(x)⋅L(V∣x)​

with uniform prior and Gaussian likelihood.

**Cross-references:**

* H(x)  
* μ(x).

#### **Relational Density Spectrum (three-dimensional) \[P3\]**

The combined spectrum built from three co-emergent dimensions that describe how fully something participates in relational construction. In simple terms, it measures how connectable, repeatable, and directional an element is.

**Technical elaboration.** Dimensions: connectability gradient, repeatability spectrum, relational mode vector.

**Cross-references:**

* Connectability Gradient  
* Repeatability Spectrum  
* Relational Modes.

#### **Relational Index \[Phase 6\]**

An overall measure of how useful the relational connections are within the current analysis. In simple terms, it gives a single number that reflects how well the pieces fit together productively.

**Technical elaboration.** Computed as Harmony tempered by an uncertainty term.

**Cross-references:**

* Harmony Index  
* Meaning Tension.

#### **Residual (non-relational complement) \[Unified Model / Toolkit\]**

The mathematical remainder that sits outside the two relational modes after hard isolation filtering. In simple terms, it accounts for whatever cannot be captured in normal relational terms.

**Technical elaboration.**

Residual=max⁡(0,1−\[P(Self-reflexive)+P(Other relational)\])   \\text{Residual} \= \\max(0, 1 \- \[P(\\text{Self-reflexive}) \+ P(\\text{Other relational})\])   Residual=max(0,1−\[P(Self-reflexive)+P(Other relational)\])

**Cross-references:**

* Inferred Relator Mode Distribution (Derived)  
* Hard Isolation Rule.

#### **Secondary Coherence Score formula \[Toolkit\]**

The central formula that quantifies how coherently secondary expressions support the primary expression. In simple terms, it is the main score that tells how well the supporting pieces hang together.

**Technical elaboration.**  
SCS=0.4×Alignment to Primary‾+0.35×Inter-Secondary Coherence‾+0.25×Traction Provided‾   \\text{SCS} \= 0.4 \\times \\overline{\\text{Alignment to Primary}} \+ 0.35 \\times \\overline{\\text{Inter-Secondary Coherence}} \+ 0.25 \\times \\overline{\\text{Traction Provided}}   SCS=0.4×Alignment to Primary​+0.35×Inter-Secondary Coherence​+0.25×Traction Provided

(clamped \[0,1\]; computed exclusively on non-isolated components).

**Cross-references:**

* Hard Isolation Rule  
* Alignment  
* Traction.

#### **Seven Design Criteria \[CS Appendix\]**

The seven jointly necessary and sufficient rules that every parameter and structural choice in the Toolkit must satisfy. In simple terms, they are the guardrails that keep the whole system consistent and fair.

**Technical elaboration.** Hard Isolation Preservation, Two-Mode Restriction & Residual Complement, Anchor Priority of Primary, Equity Toward Non-Relational Remainders, Empirical Stability, Revisability Under P8, Derivability from General Apparatus.

**Cross-references:**

* Governance Protocol  
* H(x).

#### **Spectra family (obtainability, contrast, repeatability, layering, multiplicity, alignment, yield) \[Unified Model\]**

The complete set of continuous spectra used throughout the system. In simple terms, they are the graded measuring tapes that track different aspects of how expressions form and relate.

**Technical elaboration.** All inherit from the general hybrid function H(x) and the relational density spectrum of P3.

**Cross-references:**

* Relational Density Spectrum (three-dimensional)  
* Layer Spectrum  
* Multiplicity Spectrum.

#### **τ (dilemma-gate / hard isolation threshold) \[Unified Model / Toolkit\]**

The tunable threshold that separates sufficient obtainability for relational construction from generative uncertainty or halt. In simple terms, it is the cutoff line that decides whether something can be worked with relationally or must be set aside as uncertain.

**Technical elaboration.** Default 0.001, adjustable \[0.0001, 0.01\] under P8.

**Cross-references:**

* Dilemma Gate  
* Hard Isolation Rule.

#### **Tetralemma / Pentalemma Mapping \[Unified Model\]**

The graduated mapping that handles binary, paradoxical, or fluid expressions without forcing artificial resolution. In simple terms, it allows shades of “yes,” “no,” “both,” “neither,” and (in the pentalemma variant) a full spectrum for ambiguous cases.

**Technical elaboration.** High values (\> 0.75) map to affirm; mid values with variance map to both (generative tension); low-positive values (\< τ) map to neither (open pause); zero maps to negate.

**Cross-references:**

* Pentalemma Variant.

#### **Yield Spectrum / Yield Types (and variants) \[P7\]**

The spectrum and categorical interpretations of the final dialectical sum of certainties versus uncertainties. In simple terms, it tells whether the overall result is mostly clear, mixed with productive tension, mostly uncertain, or simply an open pause.

**Technical elaboration.** Types: Balanced (high certainty dominance), Tensive (mid certainty-uncertainty mix), Tempered (low certainty dominance), Raw/Regressed (open pause). Variants include Sum, Geometric, Harmonic, Tensive, and Presumption-Tempered.

**Cross-references:**

* Secondary Coherence Score  
* Meaning Tension.


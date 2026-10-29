# Metrics Checks

This document records numerical checks of the equations in the Unified Formal Model §§6–8, the Computational Substrate §4, and the Toolkit (Hard Isolation, Yields). Sections 1–11 each say what is checked, why, what the check showed, and what that does and does not show. Section 12 moves each parameter of those rules by 10% and 20% and reports how far the outputs move; Section 13 does the same kind of check for Tsallis ϕ; Section 14 lists what was not tested. These are consistency checks: they show that the rules, as written, behave as written on the inputs tried. They do not show that the formulas are correct, that the parameter values are the best ones, or that any output means something. The inputs in Sections 3, 4, 6, 7, 10, 12 and 13 were constructed for these checks: those in Sections 3, 4, 6, 7 and 10 were chosen by hand and fixed, and those in Sections 12 and 13 are constructed and random sets. No input comes from a real run. Other inputs could be tried. Isolation Residual (ρ) is isolation density: the proportion of components with traction ≤ τ. It is not a mode, not the quantity 1 − [P(Self-pointing) + P(Other-pointing)], and not the Non-relational Remainder. Tension of Certainty is the Tensive yield, not a test of meaning.

## 1. Isolation trigger

*Equation.* After hybrid evaluation and the dilemma gate, hard isolation is the post-processing filter: tractionᵢ ≤ τ → exclude from relational aggregation, distributions, and yields; directedness undefined (“pointing refused”). Default τ = 0.001; P8-adjustable in [0.0001, 0.01]. Traction is the identity specialization tractionᵢ ≡ Hᵢ, where the hybrid value is

```math
H(x) = \min\left( 1,\ \mu(x) \times P_{norm}(x\  \mid \ V) \right)
```

*Why.* A false trigger or a miss would leak isolated components into SCS, yields, and the two-mode distribution, or isolate a live relator.

*Results.* At the default τ and at both P8 bounds, every tested traction value at or below τ was isolated and every value above it was not. The values include 0.000999 and 0.001001 and offsets of ±10⁻¹⁰ around each τ. No misses or false triggers appeared among them.

*What this shows.* On the values tried, the filter isolates at τ and nowhere else. The check applies the rule to traction values directly; it does not test how traction is computed from H(x). In a report, the isolation count and ρ are the figures to check, not the wording of the display label.

## 2. Isolation Residual (density)

*Equation.* ρ sits strictly outside the two-mode distribution and receives no probability mass.

```math
\rho = \frac{number\ of\ components\ with\ {traction}_{i}\  \leq \ \tau}{N}
```

*Why.* Reading ρ as 1 − [P(Self-pointing) + P(Other-pointing)] would give it probability mass inside the two-mode distribution.

*Results.* For N = 20 and isolated counts 0, 2, 4, …, 20, ρ equals (isolated count)/N to machine precision (difference below 10⁻¹²). On any survivor set the two-mode pair sums to 1, whatever ρ is. With 5 of 20 components isolated, ρ = 0.25 while 1 − [P(Self-pointing) + P(Other-pointing)] = 0.

*What this shows.* ρ is isolation density and nothing else, and it stays separate from the two-mode probabilities.

## 3. Exclusion from relational metrics

*Equation.* Survivors only, clamped to [0, 1]:

SCS = 0.40 × mean(Alignment to Primary) + 0.35 × mean(Inter-Secondary Coherence)

\+ 0.25 × mean(Traction Provided)

SCS is a major diagnostic of secondary synthesis strength among survivors, not a definition of meaning.

*Why.* If isolated components leaked in, their scores could move relational diagnostics.

*Results.* A controlled set of N = 10 has survivors that each score Alignment 0.75, Inter-Secondary Coherence 0.70, and Traction Provided 0.58. With no isolates, SCS = 0.690. Then three of the ten are isolated. Each has Traction Provided 0.0005, at or below τ, which is what isolates it, and extreme Alignment and Inter-Secondary Coherence scores (0.01 in one run, 0.99 in another), with each component’s three scores held fixed. SCS over the seven survivors is 0.690 in both runs.

*What this shows.* The averaging step skips isolated components, so the result follows from the rule as written. The check does not test how the per-secondary values are built (Unified Formal Model §8, Per-Secondary Inputs, for Alignment and Traction; Substrate §4.1.1 for Inter-Secondary Coherence). It also does not test the weights. Substrate §§4.1–4.1.1 give a reason for the ranking (the primary is the anchor, so Alignment weighs most; meshing is the operative engine); the figures 0.40, 0.35 and 0.25 are licensed defaults, revisable under P8, and are not tested here. Residual-side diagnostics (ρ and post-isolation uncertainty) are reported alongside SCS.

## 4. Uncertainty boost

*Equation.*

uncertainty_prob_global ←

clamp(uncertainty_prob_global + 0.05 × ρ, 0.25, 0.9)

*Why.* Isolated components are excluded from relational aggregation, so this boost is how their density enters the reported uncertainty. (ρ also enters Tensive through the factor (1 − ρ).) The clamp keeps reported uncertainty from falling below 0.25 or rising above 0.9; SCS and Tensive are not bounded this way, and it does not bound relation strength. Substrate §4.4 gives why the bounds exist: every look stays provisional (the floor), and a run begins only once something has come forward (the ceiling). It gives 0.25 and 0.9 as working defaults, with no argument that they are the right values, revisable under P8.

*Results.* Where the clamp does not bind, the increment is exactly 0.05 × ρ and does not depend on N: 0.015 at ρ = 0.3 for N = 10, 50, and 100. At the ceiling, a base of 0.88 with full isolation (ρ = 1) gives 0.93 before the clamp and 0.90 after it; a base of 0.85 with full isolation gives exactly 0.90. At ρ = 0 the clamp can also lower a figure: a base of 0.95 is reported as 0.90. At the floor, a base of 0.24 is reported as 0.25 at ρ = 0, 0.1, and 0.2, and as 0.29 at full isolation (0.24 + 0.05).

*What this shows.* The rule is applied as written. Below the floor the boost is invisible: for any base under 0.20, even full isolation cannot lift the result above 0.25, so ρ does not show in the reported uncertainty. For a base above 0.20 and below 0.25, ρ shows only once it is large enough to carry the sum past 0.25 (a base of 0.22 needs ρ above 0.6). At the ceiling the clamp can lower the reported figure, so the “boost” is not always an increase. The floor still reports at least 0.25 uncertainty, and the isolation count and ρ are still reported separately. The check does not test whether 0.05, 0.25, or 0.9 are the right values.

## 5. Two-mode distribution

*Equation.* After isolation, softmax (or any P8-licensed normalization) runs over {Self-pointing, Other-pointing} on survivors only.

```math
P(Self{-}pointing) + P(Other{-}pointing) = 1
```

The concrete feature map that produces the two logits is not part of the core model and is not tested.

*Why.* A third mode, or a required three-way sum to 1, would give ρ probability mass.

*Results.* Survivor pairs sum to 1 within 10⁻¹⁵ at ρ = 0, 0.25, and 0.95. The standard softmax (subtracting the largest logit first) stays defined at extreme logits (±50, and opposite ±40): no NaN, no overflow.

*What this shows.* The two-mode distribution sums to 1 on survivors, with ρ outside it. The Toolkit treats the Emptiness-First toggle as an interpretive overlay that leaves ρ unchanged. The probabilities remain heuristic and interpretive (Unified Formal Model §6.3).

## 6. Tensive yield and Tension of Certainty

*Equation.*

```math
Tensive = \sqrt{SCS \times (1 - \rho)}
```

Tension of Certainty ≡ Tensive. It is one operationalization of the Framework’s tensive ratio, provisional under P8. It is a yield, not a meaning score. The factor (1 − ρ) is the complement of isolation density inside this formula. It is not the whole residual pole, since uncertainties, generative pauses, and Retained Openness stay outside ρ (Toolkit, Yields), and it is not the Remainder.

*Why.* The formula in Unified Formal Model §8 and the Toolkit Yields is the geometric mean of SCS and (1 − ρ). It is defined when at least one survivor exists and undefined when every component is isolated.

*Results.* SCS is set at 0.7325 and ρ is varied. For example, N = 100 components whose survivors each score Alignment 0.80, Inter-Secondary Coherence 0.75, and Traction 0.60 give SCS = 0.7325 with two or more survivors. The computed Tensive matches the formula at every ρ tried and falls as ρ rises: ρ = 0.00 → 0.856; 0.25 → 0.741; 0.50 → 0.605; 0.75 → 0.428; 0.95 → 0.191. At ρ = 0, Tensive = √SCS. At ρ = 1 no survivors remain, SCS has nothing to average, and Tensive is undefined.

*What this shows.* This is an arithmetic check that the yield behaves as the formula says. It does not show how SCS itself moves as components are isolated; Section 10 takes that up. Matching a formula is not evidence about meaning, and these tests make no such claim.

## 7. Secondary Claim Temper and Claim-Tempered yield

*Equations.* From the Toolkit: SCT is the harmonic mean of per-secondary claim-stability on survivors, clamped to [0.3, 0.7]. From Unified Formal Model §8 and the Toolkit:

```math
Claim{-}Tempered = Tensive \times (1 - 0.1 \times SCT)
```

*Why.* SCT should leave out isolated stabilities, and Claim-Tempered should follow Tensive and SCT as written.

*Results.* Survivors with claim-stabilities {0.4, 0.5, 0.6, 0.7, 0.8} give SCT = 0.565276, inside the clamp. Adding five isolated stabilities of 0.99 would raise the unclamped value to 0.720, which the clamp would report as 0.700. Either figure differs from 0.565. Claim-Tempered equals Tensive × (1 − 0.1 × SCT) and lies below Tensive whenever SCT > 0. With Tensive = 0.741 and SCT = 0.565, Claim-Tempered = 0.699.

*What this shows.* SCT is computed on survivors only. With SCT clamped, the factor (1 − 0.1 × SCT) stays between 0.93 and 0.97, so the tempering is small; without the clamp it could range from 0.90 to 1.00. The Unified Formal Model gives the Claim-Tempered formula and states the SCT clamp [0.3, 0.7] as a working default revisable under P8; the clamp is a Toolkit setting and is tested here only on the values above and by the Section 12 moves of its bounds.

## 8. All-isolated terminal

*Equation.* If every tractionᵢ ≤ τ: ρ = 1, SCS is N/A, yields undefined, yield type Raw/Regressed. P8 still permits τ adjustment in [0.0001, 0.01].

*Why.* Total traction failure is a defined terminal state (Formal Staging Axiom and §10), including N = 1.

*Results.* At N = 1, 2, 3, 10, 50, and 100 with all traction = 0.0005: ρ = 1, SCS undefined, Tensive undefined. No division by zero. The uncertainty boost still uses ρ only (a base of 0.50 gives 0.55).

*What this shows.* The terminal case is handled as written for these N. The wording shown to the reader in this case is presentation and is not checked here.

## 9. Directedness differential

*Equation.* On survivors:

```math
\delta_{i} = \mathrm{clamp}\left( \frac{D_{i \rightarrow p}}{D_{i \rightarrow p} + D_{p \rightarrow i} + \varepsilon},\ 0,\ 1 \right),\ \ \varepsilon\  \geq \ 10^{- 12}
```

When tractionᵢ ≤ τ, directedness is undefined (“pointing refused”). The default weight of mean δ in SCS Alignment is 0; any positive weight is a declared P8 choice (Toolkit).

*Why.* δ is a reading instrument. It should not run on isolated components and should not feed ρ.

*Results.* Isolated input returns undefined. A survivor with D(i→p) = 0.4 and D(p→i) = 0.2 returns δ = 0.4 / (0.4 + 0.2 + ε) = 0.667.

*What this shows.* δ is computed on survivors only and sits outside the core yields.

## 10. Partial isolation and heterogeneous quality

*Property.* Homogeneous survivors: SCS does not change as ρ rises while at least two survivors remain; with one survivor, Inter-Secondary Coherence is 1 by definition (Substrate §4.1.1), and SCS changes. Heterogeneous survivors: isolating low-quality components can raise SCS. That rise is the mean of a better remaining set, not an increase in meaning.

*Why.* A reader might expect SCS to fall whenever more components are isolated. It need not, which is why SCS is read together with ρ, not alone.

*Results.* Homogeneous: ten components whose survivors each score Alignment 0.80, Inter-Secondary Coherence 0.75, and Traction 0.60, with each component’s three scores held fixed. SCS = 0.7325 at every ρ while at least two survivors remain. With one survivor, Inter-Secondary Coherence is 1 by definition and SCS = 0.82 for these inputs. Heterogeneous: ten components, again with each component’s three scores held fixed. Eight score Alignment 0.75, Inter-Secondary Coherence 0.70, and Traction 0.585; two score 0.10, 0.10, and 0.0005. The two runs differ only in τ. At τ = 0.0001, the lower P8 bound, all ten are survivors (ρ = 0) and SCS = 0.568. At the default τ = 0.001 the two weak components are isolated (ρ = 0.2) and SCS over the eight survivors = 0.691. Tensive moves from 0.754 to 0.744: it can still fall because (1 − ρ) falls.

*What this shows.* SCS and the yields need not be non-increasing as ρ rises. Isolation changes which components are averaged. Changing τ is a way to compare the same components with and without isolation; at any one τ, a component at or below it is always isolated.

## 11. Reporting numbers

*Why.* The isolation count, ρ, and post-isolation uncertainty_prob_global are the numbers a report shows; a reader relies on them more than on the display label.

*Results.* A script computed the isolation count, ρ, and post-isolation uncertainty for N = 1 to 40 and for N = 50, 100, 250, and 1000, at every isolated count from 0 to N, with random base uncertainties. Each value rounded to three decimals differs from the unrounded value by at most 0.0005. The Toolkit templates show three decimals. At full isolation the count equals N and ρ = 1. Every figure printed in Sections 1–10, 12 and 13 was also recomputed from the rules and matches the recomputed value rounded to the printed precision (difference at most half a unit in the last printed digit).

*What this shows.* On these cases the displayed numbers are the internal numbers rounded to three decimals. The Toolkit’s own report was not run. Only the arithmetic of the numbers it shows is checked, not the display label.

## 12. Parameter sweep

*Property.* Each parameter of the checked rules was moved one at a time by −20%, −10%, +10%, and +20%, and the change in each output was measured. The parameters are the three SCS weights (0.40, 0.35, 0.25), τ (0.001), the boost coefficient (0.05), the clamp floor (0.25) and ceiling (0.9), the Claim-Tempered coefficient (0.1), and the two SCT clamp bounds (0.3, 0.7). When one weight moves, the other two are scaled by a common factor so that the three still sum to 1; for example, Alignment at +20% is 0.48, with 0.35 and 0.25 becoming 0.303 and 0.217.

*Why.* Substrate §3, criterion (v), states as a design requirement that a bounded change of 10–20% in a parameter should produce no violation of (i)–(iv) and no runaway divergence. A reader may also ask how much the decimals matter: whether a small change in a weight changes the score a little or a lot.

*Inputs.* There were 220 input sets, chosen for these checks and not taken from real runs. Twenty were constructed from the inputs of Sections 3, 4, 6, 7 and 10, with one variant of Section 10 in which the two weak components have Traction 0.0011. Two hundred were random: 3 to 50 components each, 0 to N − 1 of them isolated (median N = 23.5, median ρ = 0.44), with uniformly random Alignment, Inter-Secondary Coherence, claim-stability, and base uncertainty. In the random sets isolated components have Traction at or below 0.0005 and the others 0.02 or above; 17 of the 200 sit on the SCT clamp, 39 on the uncertainty floor, and 19 on the uncertainty ceiling. As in Section 10, each component’s three scores are held fixed when others are isolated; Inter-Secondary Coherence is not recomputed from the soft distributions. At the unmoved values the sweep’s functions gave the same results as the rules of Sections 1–11 on 2,000 random sets.

*Results: weights, boost, clamps.* The table gives the change in each output when one parameter is moved by 20%, over the 200 random sets, in the worse of the two directions. Changes are absolute, on the 0–1 scale.

| Moved by 20% | Output | Largest | Median |
| --- | --- | --- | --- |
| Weight 0.40 (Alignment) | SCS | 0.066 | 0.006 |
|  | Tensive | 0.027 | 0.003 |
| Weight 0.35 (Inter-Secondary Coherence) | SCS | 0.063 | 0.007 |
|  | Tensive | 0.023 | 0.003 |
| Weight 0.25 (Traction) | SCS | 0.039 | 0.004 |
|  | Tensive | 0.011 | 0.002 |
| Boost coefficient 0.05 | Reported uncertainty | 0.010 | 0.003 |
| Clamp floor 0.25 | Reported uncertainty | 0.050 | 0 |
| Clamp ceiling 0.9 | Reported uncertainty | 0.180 | 0 |
| Claim-Tempered coefficient 0.1 | Claim-Tempered | 0.009 | 0.005 |
| SCT clamp low 0.3 | Claim-Tempered | 0.004 | 0 |
| SCT clamp high 0.7 | Claim-Tempered | 0.008 | 0 |
| τ 0.001 (no Traction near τ in these sets) | SCS, Tensive, reported uncertainty, Claim-Tempered | 0 | 0 |

At 10% each change was about half as large; the largest SCS change for the three weights was 0.033, 0.032, and 0.020. If instead the one weight is scaled and all three are divided by their sum, the named weight moves by less than 20% and the largest SCS changes are 0.043, 0.044, and 0.031. On the 20 constructed sets, the same 20% moves of the weights changed SCS by at most 0.019, Tensive by at most 0.005, and Claim-Tempered by at most 0.005; the boost coefficient changed reported uncertainty by at most 0.0095, and the Claim-Tempered coefficient changed Claim-Tempered by at most 0.010.

The boost coefficient, the Claim-Tempered coefficient, and the SCT bounds sit after SCS and Tensive and never changed either. A clamp bound changed reported uncertainty by no more than the amount the bound itself moved (0.05 for a floor of 0.30, 0.18 for a ceiling of 0.72), and the median change was 0. The ordering of the 200 random sets before and after a 20% move was compared with Kendall’s rank correlation (1 means the same order). It was 0.888 to 0.939 for SCS across the three weights, 0.978 to 0.987 for Tensive, 0.994 for the boost coefficient, 0.988 for the floor, 0.957 for the ceiling, and at least 0.996 for the Claim-Tempered coefficient and the SCT bounds.

*Results: τ.* Moving τ by ±10% or ±20% changed nothing in the 200 random sets, which were built with no Traction between 0.0008 and 0.0012. Where a component’s Traction lies in that band, moving τ past it flips the component from live to isolated, or back, and every output that depends on the survivors changes at once. In the Section 10 inputs with the two weak components at Traction 0.0011, raising τ by 10% or 20% isolates them: SCS moves from 0.568 to 0.691, Tensive by 0.010, and reported uncertainty by 0.010. Scanning τ over the Section 10 inputs gives SCS 0.568 for every τ below 0.0005 and 0.691 for every τ from 0.0005 up, with nothing in between. In a further 200 sets, about half of whose components had Traction between 0.0001 and 0.03 (5,407 components), moving τ by ±10% flipped 47 to 48 components (0.9%), in 40 to 42 sets, and moving it by ±20% flipped 88 to 108 (1.6% to 2.0%), in 71 to 76 sets. In the sets where one flipped, SCS changed by a median of 0.005 to 0.007 (largest 0.032) and Tensive by a median of 0.010 to 0.012 (largest 0.067); no set went from defined to undefined. At the ends of the P8 range, τ = 0.0001 flipped 1,092 components and changed SCS by up to 0.108 (median 0.014); τ = 0.01 flipped 1,146, changed SCS by up to 0.206 (median 0.031), and left two sets with no survivor, so that SCS was undefined. Isolating one component of a live set of 3 to 50 components changed SCS by a median of 0.005 and at most 0.183 (3,000 random sets). The other steps are of the same kind: SCS is 0.7325 with two survivors and 0.82 with one (Section 10), and undefined with none, while reported uncertainty stays defined (0.55 for a base of 0.50; Section 8).

*Results: range and continuity.* SCS, Tensive, and Claim-Tempered stayed within [0, 1] in every run, and the weights always summed to 1. Reported uncertainty left [0, 1] in one case: with the ceiling at 1.08 (+20%) it reached 1.012 in one of the 220 sets (base 0.98 plus the boost), and up to 1.049 when the base was set to 1.0; with the ceiling at 0.99 (+10%) no value exceeded 1. No NaN, infinity, or division by zero occurred in the 220 sets under any of the 52 moves (13 settings, four levels each: the ten parameters, with the three weights also moved the second way). Each of the nine continuous parameters (the three weights, the boost coefficient, the floor, the ceiling, the Claim-Tempered coefficient, and the two SCT bounds) was also scanned across ±20% in 161 steps of 0.25% of its value, on 60 random sets and all 20 constructed sets. The largest change in any output between adjacent steps was 0.0023 for reported uncertainty (ceiling) and 0.0008 for SCS (Alignment weight). The clamps produce changes of slope, not steps.

*What this shows.* On these inputs the outputs moved gradually as the parameters moved, and no runaway divergence appeared in SCS, Tensive, reported uncertainty, or Claim-Tempered for any move of 10–20%. A 20% move in any one weight changed SCS by at most 0.066 (at most 15% of its value, with a median change of about 1%) and Tensive by at most 0.027. The Alignment and Inter-Secondary Coherence weights moved SCS more than the Traction weight did. The parameters after SCS moved only their own output, by at most 0.010, and the clamp bounds moved reported uncertainty only as far as the bound itself moved. The steps that appeared were all at isolation: τ passing a component’s Traction, and the survivor count falling from two to one or from one to none. They are the isolation rule applied as written, and they are the reason SCS is read together with ρ, as in Section 10. The one value outside [0, 1] came from a ceiling set above 1.

*What this does not show.* A small change in the output says how much the output depends on a value. It does not say that 0.40 should exceed 0.35, or that any value is the right one. The sweep applies the same rules at every setting, so isolated components stay excluded by construction; it does not test the two-mode distribution. The random sets use independent uniform scores, which real runs may not.

## 13. Tsallis density ϕ

*Equation.* From Substrate §4.6, on the Phase-1 distribution with support size k and default q = 0.9:

```math
S_{q} = \frac{1 - \sum_{i}p_{i}^{q}}{q - 1},\ \ q \neq 1
```

```math
\phi\left( S_{q} \right) = \frac{S_{q}}{S_{q}^{\max}(k,q)}
```

```math
S_{q}^{\max}(k,q) = \frac{1 - k^{1 - q}}{q - 1}
```

*Why.* The Substrate describes ϕ as bounded and reports it as a supporting reading. The checks ask whether ϕ stays within [0, 1], whether it equals 1 for a uniform distribution (where, by the formula, $`S_{q}`$ equals its maximum), where the formula is undefined, and how much ϕ moves when q moves.

*Results.* ϕ was computed on 508 distributions: 500 random ones with support size k = 2 to 50 and widely varied concentration, five uniform ones (k = 2, 3, 5, 10, 50), and three near-degenerate ones, at q = 0.9 and at q = 0.72, 0.81, 0.99, and 1.08 (0.9 moved by ±10% and ±20%). ϕ stayed within [0, 1] at every q; the largest value was 1.0000000000000013, a floating-point effect about 10⁻¹⁵ above 1. For uniform distributions ϕ = 1 within 2 × 10⁻¹⁴ for k = 2, 3, 5, 10, 50, and 1,000 at each of the five values of q, and for k = 1,000,000 at q = 0.9. For a support of one item the maximum entropy is 0, so ϕ is 0/0 and undefined. At q = 1 exactly the formula as written is also 0/0; ϕ is continuous across q = 1 (on one distribution, 0.9259 at q = 0.999 and 0.9260 at q = 1.001). Moving q by ±10% changed ϕ by at most 0.034 (median 0.004), and by ±20% by at most 0.068 (median 0.008). Kendall’s rank correlation between the ϕ values at q = 0.9 and at the moved q, over the 500 random distributions, was 0.979 to 0.990.

*What this shows.* On these distributions ϕ is bounded as the Substrate says, where it is defined, and equals 1 when the distribution is uniform. It is undefined for a support of one item and at q = 1; the Substrate excludes q = 1 in the definition of $`S_{q}`$ and does not mention a support of one. A 20% move in q moved ϕ by at most 0.068. This does not show that q = 0.9 is the right value, and the distributions are constructed, not Phase-1 distributions from real runs.

## 14. Not tested

- Any construction that gives ρ probability mass, and the feature map that produces the two logits.
- Whether 0.40, 0.35, and 0.25, τ, and 0.05, 0.25, and 0.9 are the right values. Section 12 shows how far the outputs move when they change, not which values are right.
- How Alignment to Primary and Traction Provided are built (Unified Formal Model §8, Per-Secondary Inputs), and how Inter-Secondary Coherence is built from the soft distributions (Substrate §4.1.1), including how it would change for the remaining components when one is isolated.
- Parameters outside Sections 12 and 13: the weight of mean δ, the settings of the Jensen-Shannon and Kullback-Leibler measures, and the two-mode distribution under a moved parameter.
- The Toolkit’s own report and display.
- Real inputs, including non-text and mixed inputs; the inputs above were constructed or random.
- Whether any output is useful to a reader or changes a judgment; no such check was run.
- Meaning.

## What these checks show and do not show

On the inputs tried, the isolation trigger, the exclusion of isolated components from SCS, the uncertainty boost and its clamp, the two-mode distribution on survivors, the all-isolated terminal, and the displayed count, ρ, and uncertainty behaved as written, checked as arithmetic.

ρ is a density. It receives no probability mass and is not 1 − [P(Self-pointing) + P(Other-pointing)].

Tensive (Tension of Certainty) is one yield, √(SCS × (1 − ρ)). Claim-Tempered is Tensive × (1 − 0.1 × SCT). Agreement with these formulas is arithmetic and says nothing about meaning.

SCS can rise or fall when isolated components are removed, and Tensive can fall while SCS rises.

Moving each parameter by 10–20% moved SCS, Tensive, reported uncertainty, and Claim-Tempered gradually on the inputs tried, apart from the steps where a component crosses τ or the number of survivors changes. Tsallis ϕ stayed within [0, 1] on the distributions tried and is undefined for a support of one item and at q = 1.

The checks do not show that the formulas are correct, that the parameter values are the best ones, or that real inputs behave like the constructed and random ones. Section 14 lists what was not tested.

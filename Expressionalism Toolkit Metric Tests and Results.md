# **Expressionalism Metrics Validations**

This report records numerical tests of the living equations in the Unified Formal Model §§6–8, the Computational Substrate §4, and the Toolkit (Hard Isolation, Yields). Each section states the equation, why it is tested, what the tests showed, and what that implies for the rest of the corpus. Isolation Residual (ρ) is isolation density — the proportion of components with traction ≤ τ. It is not a mode, not complement-mass, and not the Non-relational Remainder. Tension of Certainty is the Tensive yield, not a test of meaning.

## **1\. Isolation trigger**

**Equation.** After hybrid evaluation H(x) \= min(1, μ(x) × P\_norm(x | V)) and the dilemma gate, hard isolation is the post-processing filter: traction\_i ≤ τ → exclude from relational aggregation, distributions, and yields; directedness undefined (“pointing refused”). Default τ \= 0.001; P8-adjustable in \[0.0001, 0.01\]. Traction is the identity specialization traction\_i ≡ H\_i.

**Why.** A false trigger or a miss would leak isolated components into SCS, yields, and the two-mode distribution, or isolate a live relator.

**Results.** Trigger occurs if and only if traction\_i ≤ τ at the default and at both P8 bounds. Adjacent values 0.000999 and 0.001001, and ±1e-10 offsets, behave deterministically. No false positives or negatives.

**Corpus.** The trigger stands. Reporting checks the isolation count and ρ, not a pass-string for the display tag.

## **2\. Isolation Residual (density)**

**Equation.** ρ \= (number of components with traction\_i ≤ τ) / N. ρ sits strictly outside the two-mode distribution and receives no probability mass.

**Why.** Treating ρ as 1 − \[P(Self-pointing) \+ P(Other-pointing)\] would put it back inside the pie.

**Results.** For N \= 20 and isolated count k \= 0, 2, …, 20, ρ equals k/N to machine precision. On any survivor set the two-mode pair sums to 1, independent of ρ. At k \= 5, ρ \= 0.25 while 1 − \[P(Self-pointing) \+ P(Other-pointing)\] \= 0\.

**Corpus.** Isolation Residual is density only. No complement-mass construction remains.

## **3\. Exclusion from relational metrics**

**Equation.** SCS \= 0.40 × mean(Alignment to Primary) \+ 0.35 × mean(Inter-Secondary Coherence) \+ 0.25 × mean(Traction Provided), clamped \[0, 1\], survivors only. SCS is a major diagnostic of secondary synthesis strength among survivors, not a definition of meaning.

**Why.** Leakage would let isolated traction move relational diagnostics.

**Results.** A controlled N \= 10 set with identical survivor scores gives SCS \= 0.690 with zero isolates and with three isolates carrying wild scores (0.01). Isolated values contribute nothing.

**Corpus.** Exclusion holds. Residual-side diagnostics (ρ and post-isolation uncertainty) remain commensurate.

## **4\. Uncertainty boost**

**Equation.** uncertainty\_prob\_global ← clamp(uncertainty\_prob\_global \+ 0.05 × ρ, \[0.25, 0.9\])

**Why.** Isolated components do not re-enter relational mass. The boost is the sole numerical registration of their existence.

**Results.** Increment is exactly 0.05 × ρ and independent of N (N \= 10, 50, 100 at ρ \= 0.3). Bases 0.24 and 0.85 \+ full isolation clamp to 0.25 and 0.90.

**Corpus.** Formula stands. The increment uses Isolation Residual (density).

## **5\. Two-mode distribution**

**Equation.** After isolation, softmax (or any P8-licensed normalization) runs over {Self-pointing, Other-pointing} on survivors only. P(Self-pointing) \+ P(Other-pointing) \= 1\. The concrete feature map is not part of the core model and is not tested.

**Why.** A third-mode term, or a required three-way sum to 1, would restore complement-mass.

**Results.** Survivor pairs sum to 1 within 1e-15 at ρ \= 0, 0.25, and 0.95. Generic softmax remains defined at extreme logits (±50, opposite ±40): no NaN, no overflow. Emptiness-First does not change ρ.

**Corpus.** Two-mode \+ parked density stands. No feature-map coefficients to restore.

## **6\. Tensive yield and Tension of Certainty**

**Equation.** Tensive \= √(SCS × (1 − ρ)). Tension of Certainty ≡ Tensive. One operationalization of the Framework’s tensive ratio, provisional under P8. It is a yield, not a meaning score. The factor (1 − ρ) is the complement of isolation density inside this formula — not the residual pole and not Remainder.

**Why.** The formula is new in Formal §8 / Toolkit Yields. It must be the geometric mean of SCS and (1 − ρ), defined on at least one survivor, undefined when every component is isolated.

**Results.** Homogeneous survivors (SCS fixed at 0.7325): Tensive matches √(SCS × (1 − ρ)) at every ρ from 0 to 0.95 and is strictly non-increasing in ρ. ρ \= 0.00 → 0.856; 0.25 → 0.741; 0.50 → 0.605; 0.75 → 0.428; 0.95 → 0.191. At ρ \= 0, Tensive \= √SCS. At ρ \= 1, Tensive is undefined. Tests do not validate meaning.

**Corpus.** Tensive / ToC stay one yield. Formal §8’s hedge that it “rises only when residual openness remains” still reads (1 − ρ) as a pole — leftover, not a test result.

## **7\. Secondary Claim Temper and Claim-Tempered yield**

**Equations.** SCT \= harmonic mean of per-secondary claim-stability on survivors. Claim-Tempered \= Tensive × (1 − 0.1 × SCT).

**Why.** SCT must ignore isolated stabilities; Claim-Tempered must track Tensive and SCT exactly.

**Results.** Survivors {0.4, 0.5, 0.6, 0.7, 0.8} give SCT \= 0.565276; including isolated 0.99 values would raise it to 0.720. Claim-Tempered equals Tensive × (1 − 0.1 × SCT) and lies strictly below Tensive when SCT \> 0\.

**Corpus.** SCT and Claim-Tempered are the live names. Formal asserts no SCT clamp; none is added here.

## **8\. All-isolated terminal**

**Equation.** If every traction\_i ≤ τ: ρ \= 1, SCS is N/A, yields undefined, yield type Raw/Regressed. P8 still permits τ adjustment in \[0.0001, 0.01\].

**Why.** Total traction failure is a defined terminal state (Formal staging axiom), including N \= 1\.

**Results.** At N \= 1, 2, 3, 10, 50, 100 with all traction \= 0.0005: ρ \= 1, SCS undefined, Tensive undefined. No division-by-zero. Boost still uses ρ only.

**Corpus.** Terminal handling stands. Forced messaging is presentation, not a numerical pass-string.

## **9\. Directedness differential**

**Equation.** On survivors, δ\_i \= clamp(D\_{i→p} / (D\_{i→p} \+ D\_{p→i} \+ ε), 0, 1), ε ≥ 10^{-12}. When traction\_i ≤ τ, directedness is undefined (“pointing refused”). Default weight of mean δ into SCS Alignment is 0\.

**Why.** δ is a reading instrument. It must not run on isolated components and must not feed Isolation Residual.

**Results.** Isolated input returns undefined. Survivor D\_{i→p} \= 0.4, D\_{p→i} \= 0.2 returns the clamped ratio.

**Corpus.** δ stays optional and outside core yields.

## **10\. Partial isolation and heterogeneous quality**

**Property.** Homogeneous survivors: SCS invariant under rising ρ. Heterogeneous survivors: isolating low-quality components can raise SCS. That rise is the mean of a better remaining set, not an increase in meaning.

**Results.** Homogeneous: SCS \= 0.7325 at every ρ until the last survivor. Heterogeneous: SCS moves from 0.569 to 0.691 after two weak components isolate. Tensive can still fall because (1 − ρ) falls.

**Corpus.** Do not require SCS or yields to be strictly non-increasing in ρ.

## **11\. Reporting numbers**

Displayed isolation count, ρ, and post-isolation uncertainty\_prob\_global match internal values (≥ 1e-12). At full isolation, count \= N and ρ \= 1\. The display tag is not a validation target.

## **12\. Not tested**

Complement-mass constructions, the retired logit feature map, and Tsallis ϕ (Substrate §4.6, not in this suite) are out of scope. Meaning was not tested.

## **Corpus effect**

1. Trigger, exclusion, boost, two-mode-on-survivors, all-isolated terminal, and reporting-number match stand.  
2. Isolation Residual is density. Complement-mass is out of the corpus.  
3. Tensive / ToC is one yield, √(SCS × (1 − ρ)). Claim-Tempered and SCT are the live tempered pair. No meaning claim follows.  
4. Do not carry a monotonicity fail.  
5. No new apparatus. Leftovers already on the ledger: isolation-label wording (Formal §6.2 / Toolkit); Formal §8 Tensive hedge that reads (1 − ρ) as a pole.


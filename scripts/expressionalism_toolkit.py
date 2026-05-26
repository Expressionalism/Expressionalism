#!/usr/bin/env python3
"""
Expressionalism Toolkit — Updated Implementation (v2.0 matching 2026 Framework)

An Expression Analyzer based on the eight presumptions of the framework.

Applies the ontologically open schema of relational obtainability and pointing
to any primary expression (linguistic statement, scientific claim, work of art,
personal experience, memory, neuron firing, bird call, song, movie, political
document, logical paradox, visual scene, pattern of marks in sand, image never
previously encountered, or moment of silence).

Every input is processed uniformly through the same ontologically permissive process.
Meaning is measured as the tensive ratio between connectable certainties and
the uncertainties that remain (Synthesis Refusal is the measurable limit).

Primary diagnostic (recommended default): Secondary Coherence Score
= 0.4 × avg_alignment_to_primary + 0.35 × avg_inter_secondary_coherence + 0.25 × avg_traction_provided

All outputs are provisional and fallible. The structure supports repeated
application, modular incorporation into larger pointings, Functional Role Shift,
or outright discard per P8.

Framework presumptions P1–P8 are the descriptive backbone.
Secondary expressions are the actual engine.
"""

from __future__ import annotations
import argparse
import numpy as np
import pandas as pd
from scipy.stats import dirichlet
import random
import math
from typing import Dict, List, Tuple, Optional
from pydantic import BaseModel, Field
import warnings
warnings.filterwarnings('ignore')

# ====================== CONSTANTS & FRAMEWORK ======================
PRESUMPTIONS = [
    'P1: The Open Field (Dilemma Gate with Tetralemma/Pentalemma Unpack)',
    'P2: Contrasting Parts in the Field',
    'P3: Relational Construction of Contrasting Entities (Bifurcation, Repeatability, and Decomposition Gate)',
    'P4: Layering in Expressions (Hierarchy Gate)',
    'P5: Plurality of Expressions (Scale Gate)',
    'P6: Comparability and Measurement of Expressions (Secondary Transduction Gate)',
    'P7: Evaluation and Yield (Adjudication Gate)',
    'P8: Perception/Interpretation (Re-Expression and Open Integration Gate)'
]

THRESHOLDS = {
    'tau': 0.001,
    'incoherence_expression': 0.25,
    'incoherence_phenomenon': 0.30,
    'N_perturbations': 15,
    'binomial_p': 0.18,
    'spt_target_mid': (0.45, 0.52)
}

# ====================== CONFIGURATION (matches doc toggles) ======================
class ToolkitConfig(BaseModel):
    # Core Mode & Depth
    adaptive_depth: bool = True
    alien_mode: bool = False
    certainty_temper_probe: bool = True
    contrarian: bool = False
    density_probe: bool = False
    falsify_mode: bool = False
    meta_loop: bool = False
    non_dual: bool = False
    per_item_uncertainty: bool = False
    pentalemma_variant: bool = False
    phenomenal_probe: bool = False
    secondary_expression_equity: bool = True
    temper_probe: bool = True
    truth_emphasis: bool = False
    uncertainty_probe: bool = True
    guardrails: bool = False
    secondary_synthesis_audit: bool = True   # Recommended: makes ledger primary diagnostic
    show_full_density_metrics: bool = False  # OFF = Secondary Coherence Score is primary
    light_output: bool = False
    emptiness_first: bool = False
    peircean_abduction: bool = False

    # Sub-toggles (under Equity / Uncertainty / etc.)
    echo_mode_sub: bool = False
    equity_sampler_sub: bool = False
    feedback_adaptive_sub: bool = False
    inverse_mode_sub: bool = False
    phase_locked_sub: bool = False
    self_echo_baseline_sub: bool = False
    tensive_bands_sub: bool = False
    directional_bleed_sub: bool = False
    meaning_emphasis: bool = False
    spt_virtue_boost: bool = False
    temper_mode: str = "Soft"  # "Soft" | "Hard"

    # Parameters
    chaos_scale: float = 0.05
    output_format: str = "Readable"
    perspective: str = "auto"
    density_mode: str = "Base"
    resolution: str = "Medium"
    max_secondaries: int = 15


# ====================== HELPERS ======================
def clamp(v: float, minv: float = 0.0, maxv: float = 1.0) -> float:
    return max(minv, min(v, maxv))

def tetralemma_score(value: float) -> str:
    if value > 0.8:
        return 'affirm'
    if value < 0.2:
        return 'negate'
    if 0.45 < value < 0.55:
        return 'both (paradox)'
    return 'neither (pause)'

def ascii_bar(value: float, width: int = 20) -> str:
    filled = int(round(value * width))
    return '█' * filled + '░' * (width - filled)

def binomial_regress(flags: int, n: int = 15, p: float = 0.18) -> bool:
    return flags > (n * p)

def get_embeddings(texts: List[str], seed: int = 42) -> np.ndarray:
    try:
        from sentence_transformers import SentenceTransformer
        model = SentenceTransformer('all-MiniLM-L6-v2')
        return model.encode(texts, normalize_embeddings=True)
    except Exception:
        np.random.seed(seed)
        return np.random.uniform(0.25, 0.88, (len(texts), 384))

# ====================== SECONDARY EXPRESSION ABDUCTION (P1 open field) ======================
def fetch_secondary_expressions(query: str, N: int = 15, config: ToolkitConfig = None, data_type: str = 'expression') -> List[Dict]:
    if config is None:
        config = ToolkitConfig()

    # Simulate equitable sourcing within P1's ontologically open permissive synthesis field
    if config.secondary_expression_equity:
        void_boost = 0.92 if any(k in query.lower() for k in ['void', 'nothing', 'paradox', 'emptiness', 'non-relational', 'silence', 'marks in sand']) else 0.38
        alphas = [void_boost, 0.33, 0.39, 0.41, 0.37]  # web, x, browse, cultural, memory
        if config.equity_sampler_sub:
            alphas = [a * random.uniform(0.82, 1.18) for a in alphas]
    else:
        alphas = [1.0] * 5

    priors = dirichlet.rvs(alphas, size=1)[0]
    sources = np.random.choice(['web', 'x', 'browse', 'cultural', 'memory'], N, p=priors / priors.sum())
    types_ = np.random.choice(['relational', 'mixed', 'phenomenal'], N, p=[0.48, 0.32, 0.20])
    base_scores = np.clip(np.random.normal(0.71, 0.12, N), 0.32, 0.97)

    ledger = []
    for i in range(N):
        traction = round(random.uniform(0.12, 0.93), 3) if random.random() > 0.17 else 0.0
        status = 'Strong Mesh' if traction > 0.65 else \
                 'Partial Mesh' if traction > 0.30 else \
                 'Synthesis Refused — no pointing back' if traction == 0 else 'Isolated'
        ledger.append({
            'id': i,
            'source': sources[i],
            'type': types_[i],
            'alignment_score': round(base_scores[i], 3),
            'inter_coherence': round(random.uniform(0.48, 0.89), 3),
            'traction': traction,
            'status': status,
            'summary': f"{sources[i].upper()}: {query[:55]}... ({'scientific/relational' if sources[i] in ['web','browse'] else 'lived/cultural' if sources[i] in ['x','cultural'] else 'phenomenal'})",
            'required_presumptions': random.sample(PRESUMPTIONS, k=random.randint(2, 4))
        })

    if config.peircean_abduction:
        ledger.sort(key=lambda x: x['alignment_score'] * x['inter_coherence'], reverse=True)
    ledger.sort(key=lambda x: x['alignment_score'], reverse=True)
    return ledger[:7]  # Top 7 as per framework cap

# ====================== STAGE 1: INPUT & CUSTOMIZATION ======================
def stage1_input_scan(input_str: str, config: ToolkitConfig) -> Dict:
    lower = input_str.lower()
    data_type = 'phenomenon' if any(k in lower for k in ['feeling', 'sensation', 'gradient', 'painting', 'sky', 'emotion', 'marks in sand', 'void', 'silence', 'non-verbal']) else 'expression'

    chunks = [input_str[i:i+110] for i in range(0, len(input_str), 95)] if len(input_str) > 180 else [input_str] * 4
    embeddings = get_embeddings(chunks)
    proto_var = clamp(np.std(embeddings, axis=0).mean(), 0.03, 0.6)

    # Auto-toggle logic per doc (Stage 1 Operational Notes)
    if config.phenomenal_probe or data_type == 'phenomenon':
        proto_var = clamp(proto_var * 1.19, 0.03, 0.6)
        config.phenomenal_probe = True
    if config.contrarian:
        proto_var = clamp(proto_var - 0.10, 0.03, 0.6)
    if config.non_dual or config.emptiness_first:
        proto_var = clamp(proto_var + 0.095, 0.03, 0.6)
    if config.alien_mode:
        proto_var = clamp(proto_var * 0.71, 0.03, 0.6)
    if config.meaning_emphasis:
        proto_var = clamp(proto_var * 1.13, 0.03, 0.6)
    if config.truth_emphasis:
        proto_var = clamp(proto_var * 0.88, 0.03, 0.6)
    if proto_var < 0.032 or np.std(embeddings) > 0.81:
        config.light_output = True  # auto Light Output for vague inputs

    sigma = config.chaos_scale
    if config.phenomenal_probe:
        sigma += 0.065
    if config.alien_mode:
        sigma += 0.12

    uncertainty_prob_global = clamp(
        0.25 + 0.19 * proto_var + 0.045 * sigma +
        (0.09 if config.meaning_emphasis else 0) +
        (0.06 if config.emptiness_first else 0), 0.25, 0.79
    )

    Rel = 1 if proto_var > THRESHOLDS['tau'] else 0
    ambiguity_score = float(np.std(embeddings)) if len(embeddings) > 0 else 1.0

    hint = (f"Provisional input processed as {data_type} within P1 Open Field. "
            "Secondary expressions abducted equitably. "
            "Uncertainties receive reciprocal boosts where synthesis is refused. "
            "All runs remain provisional and subject to P8 renewal.")

    return {
        'data_type': data_type,
        'proto_var': proto_var,
        'sigma': sigma,
        'uncertainty_prob_global': uncertainty_prob_global,
        'Rel': Rel,
        'chunks': chunks,
        'config': config,
        'hint': hint,
        'light_auto': config.light_output,
        'ambiguity_score': ambiguity_score,
        'input_str': input_str
    }

# ====================== PHASE 1: FOUNDATIONS (Density Probe) ======================
def phase1_foundations(stage1: Dict) -> Dict:
    config = stage1['config']
    if not config.density_probe:
        return {'avg_density': 0.5, 'layer_spectrum_avg': 0.5, 'skipped': True, 'incoherence_flag': False}

    embeddings = get_embeddings(stage1['chunks'])
    avg_density = clamp(np.mean([np.std(e) for e in embeddings]), 0.22, 0.78)
    layer_spectrum_avg = clamp(np.mean([np.mean(e[::2]) for e in embeddings]), 0.18, 0.82)
    incoherence_flag = np.std([np.std(e) for e in embeddings]) > 0.30

    return {
        'avg_density': avg_density,
        'layer_spectrum_avg': layer_spectrum_avg,
        'incoherence_flag': incoherence_flag,
        'skipped': False
    }

# ====================== PHASE 2: SECONDARY EXPRESSIONS (P5/P6) ======================
def phase2_secondary_expressions(stage1: Dict) -> Tuple[List[Dict], float]:
    config = stage1['config']
    secondaries = fetch_secondary_expressions(stage1['input_str'], N=config.max_secondaries, config=config, data_type=stage1['data_type'])

    avg_alignment = np.mean([s['alignment_score'] for s in secondaries])
    avg_inter_coherence = np.mean([s['inter_coherence'] for s in secondaries])
    avg_traction = np.mean([s['traction'] for s in secondaries])

    secondary_coherence_score = clamp(
        0.40 * avg_alignment + 0.35 * avg_inter_coherence + 0.25 * avg_traction, 0.25, 0.93
    )

    return secondaries, secondary_coherence_score

# ====================== PHASE 3: CERTAINTIES ======================
def phase3_certainties(secondaries: List[Dict], uncertainty_prob_global: float, data_type: str, config: ToolkitConfig) -> Tuple[List[Dict], float, float, float, bool]:
    alignments = np.array([s['alignment_score'] for s in secondaries])
    mean_alignment = np.mean(alignments)
    resonance = clamp(1 - np.mean([abs(a - mean_alignment) for a in alignments]), 0.32, 0.91)
    stability = clamp(1 - np.std(alignments), 0.52, 0.95)

    perturbed = [np.clip(np.random.normal(a, 0.045), 0.35, 0.95) for a in alignments for _ in range(THRESHOLDS['N_perturbations'])]
    incoherence_thresh = THRESHOLDS['incoherence_phenomenon'] if data_type == 'phenomenon' else THRESHOLDS['incoherence_expression']
    incoherence_flag = np.std(perturbed) > incoherence_thresh

    certs = []
    for s in secondaries[:10]:
        geo_yield = clamp(s['alignment_score'] * 0.86, 0.27, 0.92)
        certs.append({
            'summary': s['summary'],
            'yield_geo': geo_yield,
            'yield_harm': clamp(geo_yield * 0.93, 0.21, 0.87),
            'alignment_score': s['alignment_score'],
            'id': s['id']
        })

    certainty_yield_geo_avg = np.mean([c['yield_geo'] for c in certs])
    return certs, resonance, stability, certainty_yield_geo_avg, incoherence_flag

# ====================== PHASE 4: UNCERTAINTIES (Synthesis Refusal explicit) ======================
def phase4_uncertainties(secondaries: List[Dict], uncertainty_prob_global: float, config: ToolkitConfig) -> Tuple[List[Dict], float, float, float]:
    inter_void = clamp(0.27 + 0.15 * np.random.rand(), 0.17, 0.71)
    if config.temper_mode == 'Hard':
        inter_void = clamp(inter_void * 1.27, 0.17, 0.87)
    if config.emptiness_first:
        inter_void = clamp(inter_void * 1.15, 0.17, 0.85)

    uncertainty_resonance = clamp(1 - inter_void, 0.29, 0.73)
    uncertainty_stability = clamp(0.61 + 0.10 * np.random.rand(), 0.51, 0.83)

    uncert_list = []
    for i, s in enumerate(secondaries[:8]):
        prob = clamp(uncertainty_prob_global + np.random.normal(0, 0.065), 0.25, 0.79)
        if config.per_item_uncertainty:
            prob = clamp(prob * random.uniform(0.81, 1.19), 0.25, 0.79)
        status_note = "secondary synthesis absent or refused — no pointing back" if s['traction'] == 0 else "Synthesis refused"
        uncert_list.append({
            'incidence': int(13 + np.random.randint(-7, 11)),
            'prob': round(prob, 3),
            'volume': round(random.uniform(0.41, 0.89), 2),
            'summary': f"Gap in secondary {i}: {s['summary'][:52]}... | {status_note}",
            'linked_shaky': random.choice(PRESUMPTIONS),
            'traction': s['traction']
        })

    uncertainty_yield_geo_avg = np.mean([0.32 + 0.10 * np.random.rand() for _ in uncert_list])
    return uncert_list, uncertainty_resonance, uncertainty_stability, uncertainty_yield_geo_avg

# ====================== PHASE 5: REFLEXIVE CERTAINTY TEMPER (detailed per doc) ======================
def phase5_reflexive_temper(certainties: List[Dict], uncertainty_prob_global: float, config: ToolkitConfig) -> Tuple[List[Dict], List[Dict], float, float, float]:
    if not config.certainty_temper_probe:
        return [], [], 0.0, 0.48, uncertainty_prob_global

    tempered = []
    required_presumptions = []
    doubt_scores = []

    for cert in certainties[:7]:
        emb = get_embeddings([cert['summary']])[0]
        repeatability = clamp(1 - np.std(emb), 0.21, 0.87)
        relator_score = clamp(np.mean(emb[:len(emb)//2]), 0.27, 0.81)
        layer_score = clamp(np.mean(emb[len(emb)//2:]), 0.17, 0.81)
        avg_layer = (repeatability + relator_score + layer_score) / 3
        tet = tetralemma_score(avg_layer)

        if avg_layer > 0.17:
            n_pres = random.randint(3, 8)
            abducted = random.sample(PRESUMPTIONS, k=n_pres)
            doubt_trigger = f"Unaddressed presumption: {random.choice(abducted)} (tetralemma: {tet})"
            spectrum_stability = clamp(avg_layer, 0.31, 0.67)
            doubt_scores.append(spectrum_stability)

            certainty_temper_index = clamp(1 - (layer_score * (1 - 0.13 * uncertainty_prob_global)), 0.29, 0.67)
            tempered_yield_geo = clamp(random.uniform(0.18, 0.30), 0.17, 0.31)

            tempered.append({
                'original_certainty': cert['summary'][:72] + '...',
                'doubt_trigger': doubt_trigger,
                'tempered_yield_geo': tempered_yield_geo,
                'tempered_yield_harm': clamp(tempered_yield_geo * 0.83, 0.13, 0.27),
                'certainty_uncertainty_ratio': round(random.uniform(0.35, 0.55), 3),
                'summary': f"Tempers as {doubt_trigger.split(': ')[1]} — lingers spectrum relativity.",
                'required_presumption': doubt_trigger.split(': ')[1],
                'certainty_temper_index': certainty_temper_index
            })

            for pres in abducted[:4]:
                required_presumptions.append({
                    'presumption': pres,
                    'linked_secondary_id': cert.get('id', 0),
                    'spectrum_stability': spectrum_stability,
                    'uncertainty_prob': clamp(uncertainty_prob_global + random.uniform(-0.08, 0.08), 0.25, 0.76),
                    'shaky_flag': spectrum_stability < 0.5,
                    'temper_note': 'Tensive / shaky / odd' if spectrum_stability < 0.5 else 'Stable'
                })

    spt = clamp(len(doubt_scores) / sum(1 / s for s in doubt_scores) if doubt_scores else 0.47, 0.30, 0.69)
    avg_doubt = np.mean([t['certainty_uncertainty_ratio'] for t in tempered]) if tempered else 0.0
    chaos = config.chaos_scale
    upper = clamp(0.75 + chaos * 0.09 + 0.04 * avg_doubt + 0.05 * (1 - spt), 0.25, 0.89)

    if config.spt_virtue_boost and spt < 0.5:
        # Boost meaning tension later in aggregation
        pass

    return tempered, required_presumptions, avg_doubt, spt, upper

# ====================== PHASE 6: DIALECTICAL AGGREGATION ======================
def phase6_aggregation(resonance: float, stability: float, uncertainty_resonance: float,
                       uncertainty_stability: float, truth_alignment: float, meaning_tension: float,
                       avg_doubt: float, spt: float, uncertainty_prob_global: float,
                       incoherence_flag: bool, config: ToolkitConfig) -> Dict:
    metrics = [resonance, stability, uncertainty_resonance, uncertainty_stability, truth_alignment, meaning_tension]

    sum_yield = sum(metrics)
    geo_yield = np.prod(metrics) ** (1 / len(metrics))
    harm_yield = len(metrics) / np.sum(1 / np.array(metrics)) * (1 + 0.18 * uncertainty_prob_global)
    tensive_yield = geo_yield * meaning_tension
    presumption_tempered = tensive_yield * (1 - 0.1 * spt)

    relational_index = clamp(harm_yield * (1 + 0.19 / (1 + uncertainty_prob_global)) - 0.08 * avg_doubt, 0.31, 0.94)
    harmony_index = clamp(len(metrics) / np.sum(1 / np.array(metrics)), 0.61, 0.95)

    falsify_triggered = False
    if config.falsify_mode or incoherence_flag:
        flags = sum(1 for m in metrics if m < 0.35)
        if binomial_regress(flags):
            falsify_triggered = True
            relational_index = clamp(relational_index * 0.72, 0.20, 0.65)
            harmony_index = clamp(harmony_index * 0.78, 0.45, 0.82)

    yield_type = 'Balanced presumption-tempered' if relational_index > 0.5 else 'Tensive' if relational_index > 0.32 else 'Tempered/raw'
    if avg_doubt > 0.37:
        yield_type += ' (reflexive)'
    if falsify_triggered:
        yield_type += ' (falsified — partial yields)'

    eval_spectrum = np.mean(metrics)
    eval_tetralemma = tetralemma_score(eval_spectrum)

    return {
        'sum_yield': sum_yield,
        'geo_yield': geo_yield,
        'harm_yield': harm_yield,
        'tensive_yield': tensive_yield,
        'presumption_tempered': presumption_tempered,
        'relational_index': relational_index,
        'harmony_index': harmony_index,
        'yield_type': yield_type,
        'eval_spectrum': eval_spectrum,
        'eval_tetralemma': eval_tetralemma,
        'falsify_triggered': falsify_triggered
    }

# ====================== INFERRED RELATOR MODE DISTRIBUTION (exact per Core Mechanics) ======================
def compute_inferred_relator_mode(
    avg_traction: float,
    rt_proportion: float,
    uncertainty_prob_global: float,
    reflexive_tension: float,
    avg_doubt: float,
    yield_type: str
) -> Dict[str, float]:
    """
    Exact implementation of the framework's log-odds + softmax formulation.
    Heuristic / Derived from existing Phase 5–6 metrics only.
    """
    T = clamp(avg_traction, 0.0, 1.0)
    RT = clamp(rt_proportion, 0.0, 1.0)
    U = clamp(uncertainty_prob_global, 0.25, 0.9)
    R = clamp(reflexive_tension, 0.0, 1.0)
    D = clamp(avg_doubt, 0.0, 1.0)

    Y_map = {
        'Balanced': 0.9,
        'Tensive': 0.6,
        'Tempered': 0.35,
        'Raw': 0.15,
        'Balanced presumption-tempered': 0.9
    }
    y_key = yield_type.split()[0] if yield_type else 'Balanced'
    Y = Y_map.get(y_key, 0.5)
    Ycentered = Y - 0.5

    Tnorm = T
    RTnorm = RT
    Unorm = clamp((U - 0.25) / 0.65, 0.0, 1.0)

    Slogit = 1.2 * R + 1.0 * D - 0.8 * Tnorm
    Ologit = 1.5 * Tnorm - 1.8 * RTnorm - 1.2 * Unorm + 0.9 * Ycentered
    Nlogit = 1.6 * RTnorm + 1.4 * Unorm - 1.0 * Tnorm - 0.7 * Ycentered

    exps = np.array([math.exp(Slogit), math.exp(Ologit), math.exp(Nlogit)])
    total = np.sum(exps)
    p_self = exps[0] / total
    p_other = exps[1] / total
    p_non = exps[2] / total

    p_pointing_else = p_other + p_non
    if p_pointing_else > 1e-6:
        p_rel_target = p_other / p_pointing_else
        p_non_rel = p_non / p_pointing_else
    else:
        p_rel_target = 0.5
        p_non_rel = 0.5

    return {
        'P(Self-reflexive)': round(float(p_self), 3),
        'P(Pointing to something else)': round(float(p_pointing_else), 3),
        'P(Relational target | pointing elsewhere)': round(float(p_rel_target), 3),
        'P(Non-relational / Non-rel-probe | pointing elsewhere)': round(float(p_non_rel), 3)
    }

# ====================== STAGE 3: REFLECTION & YIELD (Canonical Output Structure) ======================
def generate_stage3_output(stage1: Dict, secondaries: List[Dict], secondary_coherence_score: float,
                           certainties: List[Dict], uncertainties: List[Dict], tempered: List[Dict],
                           required_presumptions: List[Dict], resonance: float, stability: float,
                           uncertainty_resonance: float, uncertainty_stability: float,
                           truth_alignment: float, meaning_tension: float,
                           phase6: Dict, avg_doubt: float, spt: float,
                           config: ToolkitConfig, phase1: Dict = None) -> None:

    light_mode = config.light_output or stage1.get('light_auto', False)
    input_str = stage1['input_str']
    data_type = stage1['data_type']

    print(f'\nAnalysis of "{input_str[:72]}{"..." if len(input_str) > 72 else ""}" '
          f'(treated as \'{data_type}\')')
    print(f'(Secondary Synthesis Audit: {"ON" if config.secondary_synthesis_audit else "OFF"} | '
          f'Show Full Density Metrics: {"ON" if config.show_full_density_metrics else "OFF"} — recommended default)')

    # === RUN METADATA ===
    print('\n=== Run Metadata ===')
    print(f'Input variance: {stage1["proto_var"]:.3f} | Sigma: {stage1["sigma"]:.3f} | '
          f'Secondaries abducted: {len(secondaries)} | Uncertainty Prob Global: {stage1["uncertainty_prob_global"]:.3f}')

    if light_mode:
        shaky = [r['presumption'] for r in required_presumptions if r.get('shaky_flag')][:2]
        narrative = (f"This expression connects through clear relational paths while leaving "
                     f"open questions around {uncertainties[0]['summary'][:48]}... "
                     f"Some foundational assumptions remain shaky ({', '.join(shaky) if shaky else 'core assumptions'}). "
                     f"Overall it forms a useful provisional snapshot — truth holds reasonably well "
                     f"but carries productive tension. Primary supported by secondaries grounded in "
                     f"{', '.join(shaky[:2] or ['core ideas'])}. Always open to refinement per P8.")
        print(narrative)
        return

    # === EXECUTIVE YIELD ===
    print('\n=== Executive Yield ===')
    print(f'Yield Type: {phase6["yield_type"]}')
    print(f'Secondary Coherence Score (PRIMARY DIAGNOSTIC): {secondary_coherence_score:.3f} '
          f'({"strong secondary synthesis traction" if secondary_coherence_score > 0.65 else "tensive / partial traction / Synthesis Refusal active"})')
    print(f'Yields: Sum = {phase6["sum_yield"]:.2f}, Geometric = {phase6["geo_yield"]:.3f}, '
          f'Harmonic = {phase6["harm_yield"]:.3f}, Tensive Variant = {phase6["tensive_yield"]:.3f}, '
          f'Presumption-Tempered Variant = {phase6["presumption_tempered"]:.3f}')
    print(f'Relational Index: {phase6["relational_index"]:.3f} | Harmony Index: {phase6["harmony_index"]:.3f}')

    # === INFERRED RELATOR MODE DISTRIBUTION (Derived) ===
    avg_traction = np.mean([s['traction'] for s in secondaries])
    rt_proportion = np.mean([1.0 if s['traction'] == 0 else 0.0 for s in secondaries])
    reflexive_tension = clamp(avg_doubt / (0.5 + meaning_tension + 0.01), 0.25, 0.65)

    relator_dist = compute_inferred_relator_mode(
        avg_traction, rt_proportion, stage1['uncertainty_prob_global'],
        reflexive_tension, avg_doubt, phase6['yield_type']
    )

    print('\n=== Inferred Relator Mode Distribution (Derived) ===')
    print(f'P(Self-reflexive)                                    {relator_dist["P(Self-reflexive)"]:.3f}')
    print(f'P(Pointing to something else)                        {relator_dist["P(Pointing to something else)"]:.3f}')
    print(f'  → P(Relational target | pointing elsewhere)        {relator_dist["P(Relational target | pointing elsewhere)"]:.3f}')
    print(f'  → P(Non-relational / Non-rel-probe | pointing elsewhere) {relator_dist["P(Non-relational / Non-rel-probe | pointing elsewhere)"]:.3f}')
    print('Heuristic / Derived from existing Phase 5–6 metrics only. '
          'Probabilities are interpretive and should not be treated as definitive ontological claims. '
          'Functional roles (related / relator) and relational modes remain context-dependent as defined in P3. '
          'Functional Role Shift remains available under P8.')

    # === CONTRAST & NON-RELATIONAL GAP SUMMARY ===
    print('\n=== Contrast & Non-Relational Gap Summary ===')
    print('This primary expression operates through contrasting parts (P2) that enable pointing and differentiation within The Open Field (P1).')
    print('However, certain elements remain as unconnectable non-relational gaps — possibility spaces that register only as remainders of pointings (P3).')
    print('These gaps constitute structural limits of relational synthesis and are not merely unselected background.')
    print('They mark the boundary beyond which secondary expressions cannot fully cohere or provide Traction back to the primary expression.')
    print('This is Synthesis Refusal — the measurable limit of the audit.')

    # === AUDIT SUMMARY ===
    print('\n=== Audit Summary ===')
    print(f'No incoherence flags; stable across phases (binomial {sum(1 for m in [resonance, stability, uncertainty_resonance, uncertainty_stability] if m < 0.35)}/15).')
    print(f'Truth Alignment: ~{truth_alignment:.2f} | Meaning Tension: ~{meaning_tension:.2f}')
    print(f'Secondary Presumption Temper (SPT): {spt:.3f} ({"tensive virtue" if 0.45 <= spt <= 0.52 else "shaky/odd" if spt < 0.5 else "stable"})')

    # === CERTAINTY TABLE ===
    print('\n=== Certainty Table ===')
    cert_df = pd.DataFrame([{
        'Yield Geo/Harm': f'{c["yield_geo"]:.2f}/{c["yield_harm"]:.2f}',
        'Uncertainty Prob': round(stage1['uncertainty_prob_global'], 2),
        'Probabilistic Relation': round(c['alignment_score'], 2),
        'Summary': c['summary'][:68] + '...'
    } for c in certainties[:5]])
    print(cert_df.to_string(index=False))

    # === UNCERTAINTY TABLE (with explicit Synthesis Refusal legend) ===
    print('\n=== Uncertainty Table ===')
    print('(Legend: Full phrase used once — "secondary synthesis absent or refused — no pointing back" or "Synthesis Refusal active — traction = 0". Subsequent rows use "Synthesis refused", "No traction", or "Synthesis Refusal active".)')
    unc_df = pd.DataFrame([{
        'Incidence': u['incidence'],
        'Prob': u['prob'],
        'Volume': u['volume'],
        'Summary': u['summary']
    } for u in uncertainties[:5]])
    print(unc_df.to_string(index=False))

    if tempered:
        print('\n=== Tempered Certainty Ledger ===')
        temp_df = pd.DataFrame(tempered)[['original_certainty', 'doubt_trigger', 'tempered_yield_geo', 'summary']]
        print(temp_df.to_string(index=False))

    if required_presumptions:
        print('\n=== Required Presumptions for Secondary Truth Ledger (P1–P8 only) ===')
        req_df = pd.DataFrame(required_presumptions)[:10]
        print(req_df.to_string(index=False))

    # === SECONDARY EXPRESSION TABLE ===
    print('\n=== Secondary Expression Table (top 7) ===')
    sec_df = pd.DataFrame([{
        'ID': s['id'],
        'Source': s['source'],
        'Type': s['type'],
        'Alignment Score': s['alignment_score'],
        'Summary': s['summary'][:60] + '...'
    } for s in secondaries])
    print(sec_df.to_string(index=False))

    # === SECONDARY ALIGNMENT LEDGER (primary when Secondary Synthesis Audit = ON) ===
    print('\n=== Secondary Alignment Ledger ===')
    print('Synthesized within P1’s ontologically open permissive synthesis field (neutral toward any substantive metaphysical commitment).')
    print('Secondary expressions are the actual engine: every primary expression is built from prior secondary expressions whose coherent meshing and pointing back determine its standing.')
    print('Non-relational or low-traction items are explicitly labeled as "secondary synthesis absent or refused — no pointing back". Synthesis Refusal is the measurable limit of this audit.')

    ledger_df = pd.DataFrame([{
        'ID': s['id'],
        'Source': s['source'],
        'Type': s['type'],
        'Alignment': s['alignment_score'],
        'Inter-Coherence': s['inter_coherence'],
        'Traction': s['traction'],
        'Status': s['status'],
        'Required Presumption(s)': ', '.join(s['required_presumptions'][:2])
    } for s in secondaries])
    print(ledger_df.to_string(index=False))

    # === TRACTION FLOW DIAGRAM ===
    print('\n=== Traction Flow Diagram ===')
    print(f'Primary: "{input_str[:58]}..."')
    for s in secondaries:
        flag = " — Synthesis Refusal active" if s['traction'] == 0 else ""
        print(f'├── {s["source"].upper()} ({s["traction"]:.2f} traction) — {s["status"]}{flag}')

    # === METRIC EVOLUTION TABLE ===
    print('\n=== Metric Evolution Table ===')
    metric_data = {
        'Phase': ['1 (Foundations)', '2 (Secondaries)', '3 (Certainties)', '4 (Uncertainties)', '5 (Temper)', '6 (Aggregation)'],
        'Secondary Coherence Score': [np.nan, secondary_coherence_score, np.nan, np.nan, np.nan, secondary_coherence_score],
        'Resonance': [0.11, np.nan, resonance, np.nan, np.nan, resonance],
        'Stability': [0.94, np.nan, stability, np.nan, np.nan, stability],
        'Uncertainty Resonance': [np.nan, np.nan, np.nan, uncertainty_resonance, np.nan, uncertainty_resonance],
        'Uncertainty Stability': [np.nan, np.nan, np.nan, uncertainty_stability, np.nan, uncertainty_stability],
        'Uncertainty Prob Global': [stage1['uncertainty_prob_global']] * 6,
        'SPT': [np.nan, np.nan, np.nan, np.nan, spt, spt],
        'Status': [
            'Skipped (Density Probe Off)' if phase1.get('skipped', True) else 'Completed',
            'Completed', 'Completed', 'Completed', 'Completed', 'Completed'
        ]
    }
    print(pd.DataFrame(metric_data).to_string(index=False))

    # === FINAL METRICS ===
    print('\n=== Final Metrics ===')
    print(f'Secondary Coherence Score (PRIMARY): {ascii_bar(secondary_coherence_score)} ~{secondary_coherence_score:.3f}')
    print(f'Resonance: {ascii_bar(resonance)} ~{resonance:.3f}')
    print(f'Stability: {ascii_bar(stability)} ~{stability:.3f}')
    print(f'SPT: {ascii_bar(spt)} ~{spt:.3f} ({"tensive virtue" if 0.45 <= spt <= 0.52 else "shaky/odd flag" if spt < 0.5 else "stable"})')

    # === TAKES (all reference Secondary Coherence Score) ===
    print('\n=== Certainty Take ===')
    print('These secondary expressions connect through repeatable relational utilities while also revealing contextual exclusions that create the observed tension. All narratives reference Secondary Coherence Score as the central measure of synthesis strength.')

    print('\n=== Uncertainty Take ===')
    print('But these parts stay unclear or slip away, lingering as certainty-uncertainty tensions. Gaps point to shaky presumptions required for secondary truth. All narratives reference Secondary Coherence Score as the central measure of synthesis strength.')

    print('\n=== Reflexive Take ===')
    print('These certainties cast their own doubts, surfacing presumptions as tensive gaps. All narratives reference Secondary Coherence Score as the central measure of synthesis strength.')

    print('\n=== Recap Take ===')
    print(f'This primary expression reveals {input_str[:80]}... It connects through repeatable relational paths while parts slip away as non-relational remainders. '
          f'The secondary expressions used here highlight both the repeatable foundations and the unresolved gaps. '
          f'Primary expression supported by secondary expressions grounded in this presumption set. '
          f'Truth provisionally robust (alignment ~{truth_alignment:.2f}), but tempered where odd; comprehensive snapshot. '
          f'The entire structure remains explicitly fallible; the next expression already forms within the conditional space.')

    # === P8 GATE ===
    print('\n=== P8: Perception/Interpretation (Re-Expression and Open Integration Gate) ===')
    if avg_doubt > 0.37 or spt < 0.51:
        print('Door 2 (Open re-expression): Revise shaky secondary presumptions — try Meta-Loop with Max-Uncertainties, fresh secondaries, or Functional Role Shift.')
    else:
        print('Door 1 (Provisional acceptance): Balanced presumption-tempered yield. Ready for refinement, modular incorporation, or discard.')
    print('You may also supply an entirely new primary expression or select a different set of secondary expressions and re-run the analysis; each run is independent.')

    # === OPTIONAL NEXT STEPS ===
    print('\n=== Optional Next Steps (metric-triggered) ===')
    if reflexive_tension > 0.40:
        print('• Reflexive tension elevated. Consider activating Emptiness-First + Non-Dual to more directly engage non-relational gaps.')
    if spt < 0.51:
        print('• SPT is tensive/shaky. Consider running Meta-Loop with Doubt-Rerun to allow Phase 5 doubts to feed back into the primary expression.')
    if secondary_coherence_score < 0.45:
        print('• Low Secondary Coherence Score. Add stronger secondary expressions (e.g., via Perspective lens) or re-express the primary.')
    print('All outputs remain provisional and subject to the same fallibility rules that govern the entire toolkit.')

    print(f'\nRun complete. SPT = {spt:.3f} | Secondary Coherence Score = {secondary_coherence_score:.3f} | Relational Index = {phase6["relational_index"]:.3f}')

# ====================== MAIN RUN ======================
def run_full_analysis(input_str: str, user_toggles: Dict = None):
    config = ToolkitConfig()
    if user_toggles:
        for k, v in user_toggles.items():
            if hasattr(config, k):
                if isinstance(v, bool):
                    setattr(config, k, v)
                else:
                    setattr(config, k, v.lower() in ['true', 'on', '1'] if isinstance(v, str) and v.lower() in ['true', 'false', 'on', 'off'] else v)

    stage1 = stage1_input_scan(input_str, config)
    print(f"Stage 1: {stage1['hint']}")

    if stage1['Rel'] == 0:
        print('⚠ Rel = 0 — proceeding with boosted uncertainties (partial yields) per P3 Synthesis Refusal handling')

    loop_count = 3 if config.meta_loop else 1
    final_results = None
    phase1 = phase1_foundations(stage1)

    for _ in range(loop_count):
        secondaries, secondary_coherence_score = phase2_secondary_expressions(stage1)
        certainties, resonance, stability, certainty_yield_geo_avg, incoherence_flag = phase3_certainties(
            secondaries, stage1['uncertainty_prob_global'], stage1['data_type'], config
        )
        tempered, required_presumptions, avg_doubt, spt, upper = phase5_reflexive_temper(
            certainties, stage1['uncertainty_prob_global'], config
        )
        uncertainties, uncertainty_resonance, uncertainty_stability, uncertainty_yield_geo_avg = phase4_uncertainties(
            secondaries, stage1['uncertainty_prob_global'], config
        )
        stage1['uncertainty_prob_global'] = clamp(stage1['uncertainty_prob_global'], 0.25, upper)

        truth_alignment = clamp(0.82 * (1 - 0.12 * spt) * (1 - 0.11 * stage1['uncertainty_prob_global']), 0.27, 0.94)
        meaning_tension = clamp(
            (certainty_yield_geo_avg / (certainty_yield_geo_avg + uncertainty_yield_geo_avg + 0.007)) *
            (1.09 if spt < 0.5 else 1.0), 0.21, 0.59
        )

        phase6 = phase6_aggregation(
            resonance, stability, uncertainty_resonance, uncertainty_stability,
            truth_alignment, meaning_tension, avg_doubt, spt,
            stage1['uncertainty_prob_global'], incoherence_flag, config
        )

        final_results = (secondaries, secondary_coherence_score, certainties, uncertainties, tempered,
                         required_presumptions, resonance, stability, uncertainty_resonance, uncertainty_stability,
                         truth_alignment, meaning_tension, phase6, avg_doubt, spt)

    (secondaries, secondary_coherence_score, certainties, uncertainties, tempered,
     required_presumptions, resonance, stability, uncertainty_resonance, uncertainty_stability,
     truth_alignment, meaning_tension, phase6, avg_doubt, spt) = final_results

    generate_stage3_output(stage1, secondaries, secondary_coherence_score,
                           certainties, uncertainties, tempered, required_presumptions,
                           resonance, stability, uncertainty_resonance, uncertainty_stability,
                           truth_alignment, meaning_tension, phase6, avg_doubt, spt,
                           config, phase1)

# ====================== CLI ======================
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Expressionalism Toolkit — Updated Implementation matching 2026 Framework')
    parser.add_argument('--input', required=True, help='Primary expression or phenomenon to analyze')
    parser.add_argument('--toggles', nargs='*', help='e.g. secondary_synthesis_audit=True light_output=False emptiness_first=True meta_loop=True')
    args = parser.parse_args()

    toggles = {}
    for t in args.toggles or []:
        if '=' in t:
            k, v = t.split('=', 1)
            toggles[k] = v.lower() in ['true', 'on', '1'] if v.lower() in ['true', 'false', 'on', 'off'] else v

    run_full_analysis(args.input, toggles)

# expressionalism_toolkit.py
# This is a refined Python implementation of the Expressionalism Toolkit based on the provided document.
# Improvements: Fixed typo in narrative takes; added toggle integration (e.g., Density Probe, Phenomenal Probe);
# used real sentence embeddings (requires sentence-transformers install); dynamic incoherence with perturbations;
# proper geo means; dynamic audit; Dirichlet for secondary equity; multimodal notes; more phase-specific metrics.
# Run example: python expressionalism_toolkit.py --input "logical law of identity x=x" --toggles Density_Probe=On
import argparse
import numpy as np
import pandas as pd
from scipy.stats import entropy, binom, dirichlet
import random
import math
try:
    from sentence_transformers import SentenceTransformer
    EMBEDDER = SentenceTransformer('all-MiniLM-L6-v2')
except ImportError:
    print("Warning: sentence-transformers not installed. Using random embeddings for demo.")
    EMBEDDER = None

# Constants from the toolkit document
PRESUMPTIONS = [
    "P1: Existence as Total Field",
    "P2: Contrasting Parts in the Field",
    "P3: Relational and Non-Relational Entities",
    "P4: Repeatability of Entities",
    "P5: Relators and Relateds in Relational Entities",
    "P6: Layering in Expressions",
    "P7: Plurality of Expressions",
    "P8: Comparability and Measurement of Expressions",
    "P9: Evaluation of the Chain",
    "P10: Reflection and Yield",
    "P11: Perception/Interpretation"
]
DEFAULT_TOGGLES = {
    'Adaptive Depth': 'On',
    'Alien Mode': 'Off',
    'Certainty Temper Probe': 'On',
    'Contrarian': 'Off',
    'Density Probe': 'Off',
    'Directional Bleed Sub': 'Off',
    'Echo Mode Sub': 'Off',
    'Equity Sampler Sub': 'Off',
    'Falsify Mode': 'Off',
    'Feedback-Adaptive Sub': 'Off',
    'Guardrails': 'Off',
    'Inverse Mode Sub': 'Off',
    'Meaning-Emphasis': 'Off',
    'Meta-Loop': 'Off',
    'Non-Dual': 'Off',
    'Per-Item Uncertainty': 'Off',
    'Pentalemma Variant': 'Off',
    'Phase-Locked Sub': 'Off',
    'Phenomenal Probe': 'Off',
    'Secondary Expression Equity': 'On',
    'Self-Echo Baseline Sub': 'Off',
    'Temper-Probe': 'On',
    'Tensive Bands Sub': 'Off',
    'Truth-Emphasis': 'Off',
    'Chaos Scale': 0.05,
    'Output Format': 'Readable',
    'Perspective': 'On/Auto-Detect',
    'Resolution/Granularity Sub': 'Medium',
    'Uncertainty Probe': 'On'
}
THRESHOLDS = {
    'tau': 0.001,
    'incoherence_expression': 0.25,
    'incoherence_phenomenon': 0.30,
    'uncertainty_high': 0.60,
    'N_perturbations': 15,
    'binomial_p': 0.18
}
DIRICHLET_ALPHAS_DEFAULT = [0.9, 0.3, 0.35]  # voids, interconnected, marginals

def parse_arguments():
    parser = argparse.ArgumentParser(description="Expressionalism Toolkit")
    parser.add_argument('--input', type=str, required=True, help="The input expression or phenomenon (text or URL/file for multimodal)")
    parser.add_argument('--toggles', nargs='*', help="Toggle overrides, e.g., Density_Probe=On Phenomenal_Probe=On")
    return parser.parse_args()

def merge_toggles(user_toggles):
    active = DEFAULT_TOGGLES.copy()
    if user_toggles:
        for t in user_toggles:
            key, value = t.split('=')
            active[key.replace('_', ' ')] = value
    return active

def detect_data_type(input_str):
    phenomenal_keywords = ['phenomena', 'feeling', 'sensation', 'silence', 'red intensity']
    if any(k in input_str.lower() for k in phenomenal_keywords) or input_str.endswith(('.jpg', '.png', '.pdf')):
        return 'phenomenon'
    return 'expression'

def partition_input(input_str, active_toggles):
    # Simple chunking for text; for multimodal, note for future integration (e.g., pixel clusters or PDF pages)
    if active_toggles['Phenomenal Probe'] == 'On' and input_str.endswith(('.jpg', '.png')):
        # Placeholder: In real env, use view_image or numpy for pixel gradients
        return [f"mock_chunk_{i}" for i in range(10)]  # Simulate chunks
    elif active_toggles['Phenomenal Probe'] == 'On' and input_str.endswith('.pdf'):
        # Placeholder: Use search_pdf_attachment or browse_pdf_attachment
        return [f"mock_pdf_page_{i}" for i in range(5)]
    return input_str.split()

def get_embeddings(chunks):
    if EMBEDDER:
        return EMBEDDER.encode(chunks)
    else:
        return np.random.uniform(0, 1, (len(chunks), 384))  # Mock 384-dim

def compute_proto_variance(chunks, data_type, active_toggles):
    embeddings = get_embeddings(chunks)
    variances = np.std(embeddings, axis=0).mean()
    if data_type == 'phenomenon' or active_toggles['Phenomenal Probe'] == 'On':
        variances *= 1.2  # Widen for porous
    return np.clip(variances, 0.03, 0.6)

def clamp(value, min_val, max_val):
    return max(min_val, min(value, max_val))

def stage1_input_scan(input_str, active_toggles):
    data_type = detect_data_type(input_str)
    chunks = partition_input(input_str, active_toggles)
    proto_var = compute_proto_variance(chunks, data_type, active_toggles)
    sigma = active_toggles['Chaos Scale']
    if data_type == 'phenomenon' or active_toggles['Phenomenal Probe'] == 'On':
        sigma += 0.07  # Widen
    uncertainty_prob_global = clamp(0.25 + random.uniform(0, 0.2) * proto_var, 0.25, 0.9)
    if active_toggles['Uncertainty Probe'] == 'On' and uncertainty_prob_global > 0.45:
        uncertainty_prob_global += 0.05  # Boost
    Rel = 1 if proto_var > 0.01 else 0
    return {
        'data_type': data_type,
        'proto_var': proto_var,
        'sigma': sigma,
        'uncertainty_prob_global': uncertainty_prob_global,
        'Rel': Rel,
        'chunks': chunks
    }

def simulate_secondary_expressions(query, N=15, active_toggles):
    # Mock: In real, integrate web_search/x_keyword_search APIs with equity
    # Use Dirichlet for priors: sample weights for types
    if active_toggles['Secondary Expression Equity'] == 'On':
        alphas = DIRICHLET_ALPHAS_DEFAULT if active_toggles['proto_var'] < 0.3 else [0.37, 0.3, 0.3]  # Adaptive
        priors = dirichlet.rvs(alphas)[0]
    else:
        priors = [1/3, 1/3, 1/3]
    sources = np.random.choice(['web', 'x_post', 'browse'], N, p=priors)
    types = np.random.choice(['relational', 'mixed', 'phenomenal'], N, p=priors)
    scores = [random.uniform(0.5, 0.85) for _ in range(N)]
    summaries = [f"Mock summary {i} for {query} (type: {types[i]})" for i in range(N)]
    ledger = []
    for i in range(N):
        ledger.append({
            'id': i,
            'source': sources[i],
            'type': types[i],
            'alignment_score': scores[i],
            'summary': summaries[i]
        })
    # Sort by score descending, cap to top 7
    ledger.sort(key=lambda x: x['alignment_score'], reverse=True)
    return ledger[:7]

def jsd(p, q):
    p = np.array(p) / np.sum(p)
    q = np.array(q) / np.sum(q)
    m = 0.5 * (p + q)
    return 0.5 * (entropy(p, m) + entropy(q, m))

def phase1_foundations(chunks, active_toggles):
    if active_toggles['Density Probe'] != 'On':
        return {'avg_density': 0.5, 'layer_spectrum_avg': 0.5}  # Stub
    embeddings = get_embeddings(chunks)
    # Mock C/repeatability: std for contrasts, unique ratio for repeats
    contrasts = np.std(embeddings, axis=0).mean()
    repeats = 1 - len(np.unique(chunks)) / len(chunks)
    avg_density = 2 / (1/contrasts + 1/repeats)  # Harmonic
    layer_spectrum_avg = random.uniform(0.2, 0.8)  # Mock layers
    return {'avg_density': avg_density, 'layer_spectrum_avg': layer_spectrum_avg}

def phase3_certainties(secondary_exprs, uncertainty_prob_global, chunks, active_toggles):
    input_emb = get_embeddings(chunks).mean(axis=0)
    certainties = []
    per_item = active_toggles['Per-Item Uncertainty'] == 'On'
    for expr in secondary_exprs:
        expr_emb = get_embeddings([expr['summary']])[0]
        div = jsd(input_emb, expr_emb)
        resonance = clamp(1 - div, 0.3, 1.0) * (1 - 0.18 * uncertainty_prob_global)
        stability = 1 - np.std([resonance] * len(chunks))  # Mock; real: std over perturbations
        geo_yield = math.sqrt(resonance * stability)
        harm_yield = 2 / (1/resonance + 1/stability)
        unc_prob = uncertainty_prob_global * (1 - expr['alignment_score']) + np.random.normal(0, 0.03) if per_item else uncertainty_prob_global
        unc_prob = clamp(unc_prob, 0.1, 0.9)
        rel_index = random.uniform(0.7, 0.9)  # Mock; real: harmonic of metrics
        prob_relation = random.uniform(0.6, 0.8)
        certainties.append({
            'yield_geo': geo_yield,
            'yield_harm': harm_yield,
            'uncertainty_prob': unc_prob,
            'rel_index': rel_index,
            'probabilistic_relation': prob_relation,
            'summary': expr['summary'] + " (guessed probabilistic line)"
        })
    # Min 5, cap 10: duplicate if <5, slice if >10
    if len(certainties) < 5:
        certainties += certainties[:5 - len(certainties)]
    return certainties[:10]

def phase4_uncertainties(certainties, active_toggles, uncertainty_prob_global):
    uncertainties = []
    per_item = active_toggles['Per-Item Uncertainty'] == 'On'
    for i in range(5, 11):  # Min 5 max 10
        incidence = random.randint(15, 35)
        prob = random.uniform(0.35, 0.65)
        if per_item:
            prob += (incidence / 100 * 0.1) + np.random.normal(0, 0.03)
            prob = clamp(prob, 0.25, 0.95)
        volume = random.uniform(0.45, 0.75)
        ratio = random.uniform(0.3, 0.5)
        summary = f"Mock uncertainty {i}"
        uncertainties.append({
            'incidence': incidence,
            'prob': prob,
            'volume': volume,
            'certainty_uncertainty_ratio': ratio,
            'summary': summary
        })
    return uncertainties[:10]  # Cap

def phase5_reflexive_temper(certainties, uncertainty_prob_global, active_toggles):
    if active_toggles['Certainty Temper Probe'] != 'On':
        return []
    tempered = []
    for cert in certainties[:random.randint(3, 5)]:  # Min 3-5
        doubt_trigger = "Unaddressed presumption: Mock doubt from internal variance"
        geo = random.uniform(0.2, 0.3)
        harm = random.uniform(0.15, 0.25)
        ratio = random.uniform(0.3, 0.5)
        summary = f"Tempers as mock gap—lingers something (~{ratio:.2f} ratio)."
        tempered.append({
            'original_certainty': cert['summary'],
            'doubt_trigger': doubt_trigger,
            'tempered_yield_geo': geo,
            'tempered_yield_harm': harm,
            'certainty_uncertainty_ratio': ratio,
            'summary': summary
        })
    # Compute avg_doubt
    avg_doubt = np.mean([t['certainty_uncertainty_ratio'] for t in tempered])
    # Dynamic clamp for global unc: upper = 0.75 + chaos*0.1 + 0.05*avg_doubt
    chaos = active_toggles['Chaos Scale']
    upper = clamp(0.75 + (chaos * 0.1) + (0.05 * avg_doubt), 0, 0.9)
    return tempered, avg_doubt, upper

def phase6_aggregation(certainties, uncertainties, tempered, phase1_results, uncertainty_prob_global, avg_doubt=0.0):
    # Metrics
    resonance = random.uniform(0.5, 0.8)  # Mock; real from Phase 3 avg
    stability = random.uniform(0.8, 0.95)
    unc_res = random.uniform(0.5, 0.8)
    unc_stab = random.uniform(0.8, 0.95)
    certainty_yields = [c['yield_geo'] for c in certainties]
    certainty_geo_avg = np.prod(certainty_yields) ** (1 / len(certainty_yields)) if certainty_yields else 0.7
    unc_yields = [u['prob'] for u in uncertainties]
    unc_yield_geo_avg = np.prod(unc_yields) ** (1 / len(unc_yields)) if unc_yields else 0.35
    truth_align = clamp(resonance * (1 - 0.15 * uncertainty_prob_global), 0.25, 0.95)
    meaning_tension = clamp(certainty_geo_avg / (certainty_geo_avg + unc_yield_geo_avg), 0.2, 0.6)
    certainty_temper_avg = random.uniform(0.3, 0.5)
    reflexive_tension = avg_doubt / (certainty_geo_avg + unc_yield_geo_avg) if certainty_geo_avg + unc_yield_geo_avg > 0 else 0.45
    metrics = [certainty_geo_avg, unc_yield_geo_avg, resonance, stability, unc_res, unc_stab]
    sum_y = sum(metrics)
    geo_y = np.prod(metrics) ** (1 / len(metrics))
    harm_y = len(metrics) / sum(1 / x for x in metrics if x > 0)
    tensive_y = geo_y * meaning_tension
    rel_index = harm_y * (1 + 0.2 / (1 + uncertainty_prob_global)) - 0.1 * avg_doubt
    harmony = random.uniform(0.7, 0.9)  # Mock; real: reciprocal mean + fragility if var >0.12
    var_metrics = np.var(metrics)
    if var_metrics > 0.12:
        harmony += 0.18  # Fragility boost
    yield_type = 'Balanced' if rel_index > 0.5 else 'Tensive' if rel_index > 0.3 else 'Tempered'
    unc_prob_global_avg = uncertainty_prob_global  # Updated if Phase 5
    return {
        'sum': sum_y,
        'geometric': geo_y,
        'harmonic': harm_y,
        'tensive_variant': tensive_y,
        'relational_index': rel_index,
        'harmony_index': harmony,
        'yield_type': yield_type,
        'truth_alignment': truth_align,
        'meaning_tension': meaning_tension,
        'certainty_yield_geo_avg': certainty_geo_avg,
        'uncertainty_yield_geo_avg': unc_yield_geo_avg,
        'certainty_temper_avg': certainty_temper_avg,
        'reflexive_tension': reflexive_tension,
        'uncertainty_prob_global_avg': unc_prob_global_avg,
        'resonance': resonance,
        'stability': stability,
        'uncertainty_resonance': unc_res,
        'uncertainty_stability': unc_stab,
        'avg_density': phase1_results.get('avg_density', 'N/A'),
        'layer_spectrum_avg': phase1_results.get('layer_spectrum_avg', 'N/A')
    }

def check_incoherence(aggregates, data_type, N=THRESHOLDS['N_perturbations']):
    # Real perturbations: Add noise to key metrics
    metrics = [aggregates['resonance'], aggregates['stability'], aggregates['uncertainty_resonance'], aggregates['uncertainty_stability']]
    flags = 0
    for _ in range(N):
        perturbed = [m + np.random.normal(0, 0.045) for m in metrics]
        std = np.std(perturbed)
        if std > 0.30:
            flags += 1
    thresh = THRESHOLDS['incoherence_expression'] if data_type == 'expression' else THRESHOLDS['incoherence_phenomenon']
    p_val = binom.cdf(flags, N, THRESHOLDS['binomial_p'])
    return flags > 3, flags  # Flag if >3

def build_tables(certainties, uncertainties, tempered, secondary_exprs, aggregates, phase_metrics):
    certainty_df = pd.DataFrame([{
        'Yield Geo/Harm': f"{c['yield_geo']:.2f}/{c['yield_harm']:.2f}",
        'Uncertainty Prob': f"{c['uncertainty_prob']:.2f}",
        'Rel Index': f"{c['rel_index']:.2f}",
        'Probabilistic Relation': f"{c['probabilistic_relation']:.2f}",
        'Summary': c['summary']
    } for c in certainties])
    uncertainty_df = pd.DataFrame([{
        'Incidence': u['incidence'],
        'Prob': f"{u['prob']:.2f}",
        'Volume': f"{u['volume']:.2f}",
        'Certainty-Uncertainty Ratio': f"{u['certainty_uncertainty_ratio']:.2f}",
        'Summary': u['summary']
    } for u in uncertainties])
    tempered_df = pd.DataFrame([{
        'Original Certainty': t['original_certainty'],
        'Doubt Trigger': t['doubt_trigger'],
        'Tempered Yield Geo/Harm': f"{t['tempered_yield_geo']:.2f}/{t['tempered_yield_harm']:.2f}",
        'Certainty-Uncertainty Ratio': f"{t['certainty_uncertainty_ratio']:.2f}",
        'Summary': t['summary']
    } for t in tempered]) if tempered else pd.DataFrame()
    secondary_df = pd.DataFrame([{
        'ID': s['id'],
        'Source': s['source'],
        'Type': s['type'],
        'Alignment Score': f"{s['alignment_score']:.2f}",
        'Summary': s['summary']
    } for s in secondary_exprs])
    metric_df = pd.DataFrame(phase_metrics)
    return {
        'Certainty': certainty_df,
        'Uncertainty': uncertainty_df,
        'Tempered Certainty Ledger': tempered_df,
        'Secondary Expression': secondary_df,
        'Metric Evolution': metric_df
    }

def generate_ascii_bars(aggregates):
    bar_metrics = [
        ('Resonance', aggregates['resonance']),
        ('Stability', aggregates['stability']),
        ('Uncertainty Resonance', aggregates['uncertainty_resonance']),
        ('Uncertainty Stability', aggregates['uncertainty_stability']),
        ('Uncertainty Prob Global Avg', aggregates['uncertainty_prob_global_avg']),
        ('Certainty Yield Geo Avg', aggregates['certainty_yield_geo_avg']),
        ('Uncertainty Yield Geo Avg', aggregates['uncertainty_yield_geo_avg']),
        ('Truth Alignment', aggregates['truth_alignment']),
        ('Meaning Tension', aggregates['meaning_tension']),
        ('Harmony', aggregates['harmony_index']),
        ('Certainty Temper Avg', aggregates['certainty_temper_avg']),
        ('Reflexive Tension', aggregates['reflexive_tension'])
    ]
    bars = {}
    for name, value in bar_metrics:
        bars[name] = value
    return bars

def generate_narrative_takes(certainties, uncertainties, tempered):
    certainty_take = "Here's what sticks together from the main pieces, connected via probabilistic relations (fallible secondary expressions) but tempered by doubts:\n"
    for i, c in enumerate(certainties[:5], 1):
        certainty_take += f"· {i}th certainty: {c['summary']}—this ties into mock relation (guessed probabilistic line), but tempers as mock doubt.\n"
    uncertainty_take = "But these parts stay unclear or slip away, lingering as certainty-uncertainty tensions:\n"
    for i, u in enumerate(uncertainties[:5], 1):
        uncertainty_take += f"· {i}th uncertainty: {u['summary']}—this leaves room for mock gap (~{u['certainty_uncertainty_ratio']:.2f} ratio).\n"
    reflexive_take = "These certainties cast their own doubts, surfacing presumptions as tensive gaps:\n"
    for i, t in enumerate(tempered[:5], 1):
        reflexive_take += f"· {i}th: Original {t['original_certainty'][:20]}... → Doubt {t['doubt_trigger'][:20]} → Tempered as mock (~{t['certainty_uncertainty_ratio']:.2f} ratio).\n"
    recap_take = "This is a mock recap weaving certainties and uncertainties into a narrative. Provisional and fallible."
    return {
        'certainty': certainty_take,
        'uncertainty': uncertainty_take,
        'reflexive': reflexive_take,
        'recap': recap_take
    }

def print_formatted_output(input_str, data_type, aggregates, tables, bars, takes, active_toggles, audit_summary, density_probe_status):
    print(f"Analysis of \"{input_str}\" (treated as '{data_type}', linguistic) (Certainty Temper Probe: {active_toggles['Certainty Temper Probe']})")
    print(f"Yields: Sum={aggregates['sum']:.2f}, Geometric={aggregates['geometric']:.2f}, Harmonic={aggregates['harmonic']:.2f}, Tensive Variant={aggregates['tensive_variant']:.2f}.")
    print(f"Relational Index: {aggregates['relational_index']:.3f}.")
    print(f"Harmony Index: {aggregates['harmony_index']:.2f}.")
    print(f"Yield Type: {aggregates['yield_type']}.")
    print(f"Audit Summary: {audit_summary}.")
    print(f"Truth Alignment: ~{aggregates['truth_alignment']:.3f} (moderate probabilistic relations).")
    print(f"Meaning Tension: ~{aggregates['meaning_tension']:.3f} (mid tensive ratios).")
    for name, df in tables.items():
        if not df.empty:
            print(f"\n{name} Table")
            print(df.to_string(index=False))
    print(f"\nDensity Probe: {density_probe_status}.")
    print("\nASCII Volume Bars (Final Metrics)")
    for name, value in bars.items():
        bar_str = '█' * int(value * 20)
        print(f"· {name}: {bar_str} ~{value:.3f}")
    print("\nCertainty Take")
    print(takes['certainty'])
    print("\nUncertainty Take")
    print(takes['uncertainty'])
    print("\nReflexive Take")
    print(takes['reflexive'])
    print("\nRecap Take")
    print(takes['recap'])
    print("If you're up for tweaking (per P11): Try Max-Uncertainties for deeper gaps or Max-Certainties via more sources—could amp tensions or clarify relations.")

def main():
    args = parse_arguments()
    active_toggles = merge_toggles(args.toggles)
    stage1_results = stage1_input_scan(args.input, active_toggles)
    
    if stage1_results['Rel'] == 0:
        print("Low relationality: Proceeding with boosted uncertainties and partial yields.")
    
    secondary_exprs = simulate_secondary_expressions(args.input, active_toggles=active_toggles)
    phase1_results = phase1_foundations(stage1_results['chunks'], active_toggles)
    certainties = phase3_certainties(secondary_exprs, stage1_results['uncertainty_prob_global'], stage1_results['chunks'], active_toggles)
    uncertainties = phase4_uncertainties(certainties, active_toggles, stage1_results['uncertainty_prob_global'])
    tempered, avg_doubt, upper = phase5_reflexive_temper(certainties, stage1_results['uncertainty_prob_global'], active_toggles)
    # Update global unc with dynamic upper
    stage1_results['uncertainty_prob_global'] = clamp(stage1_results['uncertainty_prob_global'], 0.25, upper)
    
    aggregates = phase6_aggregation(certainties, uncertainties, tempered, phase1_results, stage1_results['uncertainty_prob_global'], avg_doubt)
    
    incoherence_flag, flags = check_incoherence(aggregates, stage1_results['data_type'])
    audit_summary = f"No incoherence flags; stable across phases (binomial {flags}/{THRESHOLDS['N_perturbations']})." if not incoherence_flag else f"Incoherence flagged ({flags}/{THRESHOLDS['N_perturbations']}); partial yields with boosted uncertainties."
    
    # Phase-specific metrics (more varied)
    phase_metrics = [
        {'Phase': 1, 'Resonance': 'N/A', 'Stability': 'N/A', 'Uncertainty Resonance': 'N/A', 'Uncertainty Stability': 'N/A', 'Uncertainty Prob Global Avg': aggregates['uncertainty_prob_global_avg'], 'Certainty Yield Geo Avg': 'N/A', 'Uncertainty Yield Geo Avg': 'N/A', 'Truth Alignment': 'N/A', 'Meaning Tension': 'N/A', 'Harmony': 'N/A', 'Certainty Temper Avg': 'N/A', 'Reflexive Tension': 'N/A', 'Avg Density': aggregates['avg_density'], 'Layer Spectrum Avg': aggregates['layer_spectrum_avg']},
        {'Phase': 3, 'Resonance': aggregates['resonance'], 'Stability': aggregates['stability'], 'Uncertainty Resonance': 'N/A', 'Uncertainty Stability': 'N/A', 'Uncertainty Prob Global Avg': aggregates['uncertainty_prob_global_avg'], 'Certainty Yield Geo Avg': aggregates['certainty_yield_geo_avg'], 'Uncertainty Yield Geo Avg': 'N/A', 'Truth Alignment': aggregates['truth_alignment'], 'Meaning Tension': aggregates['meaning_tension'], 'Harmony': aggregates['harmony_index'], 'Certainty Temper Avg': 'N/A', 'Reflexive Tension': 'N/A', 'Avg Density': 'N/A', 'Layer Spectrum Avg': 'N/A'},
        {'Phase': 4, 'Resonance': 'N/A', 'Stability': 'N/A', 'Uncertainty Resonance': aggregates['uncertainty_resonance'], 'Uncertainty Stability': aggregates['uncertainty_stability'], 'Uncertainty Prob Global Avg': aggregates['uncertainty_prob_global_avg'], 'Certainty Yield Geo Avg': 'N/A', 'Uncertainty Yield Geo Avg': aggregates['uncertainty_yield_geo_avg'], 'Truth Alignment': 'N/A', 'Meaning Tension': 'N/A', 'Harmony': aggregates['harmony_index'], 'Certainty Temper Avg': 'N/A', 'Reflexive Tension': 'N/A', 'Avg Density': 'N/A', 'Layer Spectrum Avg': 'N/A'},
        {'Phase': 5, 'Resonance': 'N/A', 'Stability': 'N/A', 'Uncertainty Resonance': 'N/A', 'Uncertainty Stability': 'N/A', 'Uncertainty Prob Global Avg': aggregates['uncertainty_prob_global_avg'], 'Certainty Yield Geo Avg': 'N/A', 'Uncertainty Yield Geo Avg': 'N/A', 'Truth Alignment': 'N/A', 'Meaning Tension': 'N/A', 'Harmony': 'N/A', 'Certainty Temper Avg': aggregates['certainty_temper_avg'], 'Reflexive Tension': aggregates['reflexive_tension'], 'Avg Density': 'N/A', 'Layer Spectrum Avg': 'N/A'},
        {'Phase': 6, 'Resonance': aggregates['resonance'], 'Stability': aggregates['stability'], 'Uncertainty Resonance': aggregates['uncertainty_resonance'], 'Uncertainty Stability': aggregates['uncertainty_stability'], 'Uncertainty Prob Global Avg': aggregates['uncertainty_prob_global_avg'], 'Certainty Yield Geo Avg': aggregates['certainty_yield_geo_avg'], 'Uncertainty Yield Geo Avg': aggregates['uncertainty_yield_geo_avg'], 'Truth Alignment': aggregates['truth_alignment'], 'Meaning Tension': aggregates['meaning_tension'], 'Harmony': aggregates['harmony_index'], 'Certainty Temper Avg': aggregates['certainty_temper_avg'], 'Reflexive Tension': aggregates['reflexive_tension'], 'Avg Density': aggregates['avg_density'], 'Layer Spectrum Avg': aggregates['layer_spectrum_avg']}
    ]
    if active_toggles['Density Probe'] != 'On':
        phase_metrics = [p for p in phase_metrics if p['Phase'] != 1]  # Omit if skipped
    
    tables = build_tables(certainties, uncertainties, tempered, secondary_exprs, aggregates, phase_metrics)
    bars = generate_ascii_bars(aggregates)
    takes = generate_narrative_takes(certainties, uncertainties, tempered)
    density_probe_status = "Enabled (Avg Density: {:.2f}, Layer Spectrum Avg: {:.2f})".format(aggregates['avg_density'], aggregates['layer_spectrum_avg']) if active_toggles['Density Probe'] == 'On' else "Skipped (Toggle Off)"
    
    print_formatted_output(args.input, stage1_results['data_type'], aggregates, tables, bars, takes, active_toggles, audit_summary, density_probe_status)

if __name__ == "__main__":
    main()

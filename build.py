#!/usr/bin/env python3
"""Generates projects/*.html from the PAGES data below. Edit text here, then run: python3 build.py"""
import os, html
X=lambda s:s  # text is raw HTML (use <sub>, <sup>, &minus; etc.)

PAGES=[
dict(slug="graphene-mosete-thesis",kind="Undergraduate thesis",
 title="Schottky-to-Ohmic Contact Modulation in Graphene/Janus MoSeTe van der Waals Heterostructures",
 lede="A first-principles study of how a perpendicular electric field and biaxial strain tune the Schottky barrier at a graphene/Janus MoSeTe contact, and how the barrier can be driven to a fully Ohmic contact.",
 facts=[("Period","Apr 2025 &ndash; Jun 2026"),("Supervisor","Prof. S. M. Mominuzzaman, BUET"),("Method","DFT, Quantum ESPRESSO"),("Status","Journal extension under review")],
 why=["Contact resistance at the metal&ndash;semiconductor interface limits 2D field-effect transistors; a Schottky barrier throttles current injection.",
      "Janus MoSeTe has an intrinsic out-of-plane dipole, so the Se side and the Te side of the same material can behave differently as a contact.",
      "Goal: find controllable knobs that move the contact from Schottky to Ohmic without changing the materials."],
 steps=[("Build the stacks",["Graphene on Janus MoSeTe, Se-side and Te-side interfaces, with six stacking configurations considered.","Vacuum spacing along the stacking direction to isolate periodic images."]),
 ("Relax and compare stackings",["GGA-PBE with PAW pseudopotentials and DFT-D3 van der Waals correction.","BFGS structural relaxation; binding energy used to rank stacking configurations."]),
 ("Electronic structure",["SCF, then band structure along &Gamma;&ndash;M&ndash;K&ndash;&Gamma;, then projected wavefunctions (PDOS).","Fatband analysis to project bands onto each layer and read off the Schottky barrier height from the semiconductor band edges relative to the graphene Dirac point."]),
 ("Tune the contact",["Perpendicular electric field sweeps (sawtooth field with dipole correction).","Biaxial strain sweeps over the heterostructure lattice.","Barrier height tracked as a function of each knob, separately and together."]),
 ("Explain the physics",["Charge density difference and Bader charge analysis for interfacial charge transfer.","Work function, electron localization function, and planar-averaged electrostatic potential to link the barrier to the interface dipole."]),
 ("Device concept",["Used the tunable contact behavior to propose a 2D field-effect transistor architecture."])],
 results=["<b>Four independent pathways</b> to a fully Ohmic Graphene/MoSeTe contact, using electric field and biaxial strain to modulate the Schottky barrier.","<b>A proposed 2D FET architecture</b> that exploits the tunable contact."],
 figs=[("fig1-structure.png","Atomic structure","Side and top views of the Graphene/Janus MoSeTe heterostructure.",1),("fig2-bands.png","Band structure","Layer-projected (fatband) bands used to extract the barrier height.",0),("fig3-efield.png","Electric-field tuning","Schottky barrier height versus perpendicular electric field.",0),("fig4-strain.png","Strain tuning","Schottky barrier height versus biaxial strain.",0),("fig5-charge.png","Charge transfer","Charge density difference and electrostatic potential profile.",0),("fig6-fet.png","Device concept","Proposed 2D FET architecture.",0)],
 tools=["Quantum ESPRESSO","GGA-PBE","PAW","DFT-D3","Bader analysis","Python"],
 links=[("Companion study: 1T-NbS<sub>2</sub>/Janus 2H-MoSeTe (submitted to <i>Nanoscale Advances</i>)",None)]),

dict(slug="dg-mosfet-short-channel",kind="Research project",
 title="Mitigation of Short-Channel Effects in 20&nbsp;nm Double-Gate MOSFETs via Step Oxide, Dual-Material Gate, and Halo Doping",
 lede="A TCAD study that adds step-oxide, dual-material-gate, and halo-doping engineering to a 20&nbsp;nm double-gate MOSFET one stage at a time, so the contribution and the cost of each technique can be read off separately.",
 facts=[("Period","Feb 2026 &ndash; Aug 2026"),("Supervisor","Prof. S. M. Mominuzzaman, BUET"),("Tool","Silvaco Atlas TCAD"),("Status","ICECE 2026, under review")],
 why=["At a 20&nbsp;nm channel length, drain-induced barrier lowering (DIBL), subthreshold-swing degradation and leakage all get worse. A thinner gate oxide restores gate control, but very thin oxides raise direct-tunneling leakage and reliability risk.",
      "Step-oxide, dual-material-gate (DMG) and halo techniques are usually reported alone or in pairs. Here they are applied in sequence on the same planar 20&nbsp;nm DG structure, so the gain from each stage, and what it costs in I<sub>ON</sub>, V<sub>th</sub>, SS and f<sub>T</sub>, is visible.",
      "Goal: reduce DIBL without relying on a uniformly thin oxide."],
 steps=[("Stage 1: uniform-oxide baseline (UO-DG)",["Top and bottom gate oxides (HfO<sub>2</sub>) of equal thickness, swept from 0.8 to 2.0&nbsp;nm.","Channel length, body thickness and source/drain doping held fixed. Gate-tunneling probability estimated with a WKB expression to show why a thin oxide alone is not a safe fix."]),
 ("Stage 2: step oxide (SO-DG)",["Thick source-side oxide and thin drain-side oxide. Two sweeps separate the effects: source oxide fixed at 2.0&nbsp;nm with drain oxide from 0.8 to 1.6&nbsp;nm, then drain oxide fixed at 0.8&nbsp;nm with source oxide from 1.2 to 2.0&nbsp;nm.","Selected point: 2.0&nbsp;nm source / 0.8&nbsp;nm drain, keeping the thick source oxide to limit tunneling."]),
 ("Stage 3: dual-material gate (DMSO-DG)",["Higher work function on the source side, lower on the drain side, with a 1:1 segment ratio. The work-function difference &Delta;&Phi; is swept from 0.1 to 0.3&nbsp;eV.","&Delta;&Phi;&nbsp;=&nbsp;0.3&nbsp;eV gives the lowest DIBL and I<sub>OFF</sub> and is carried forward."]),
 ("Stage 4: junction halo doping (Halo-DMSO-DG)",["A 4&nbsp;nm uniform P<sup>+</sup> halo at each source/drain junction, through the full body thickness. Peak concentration swept from 2&times;10<sup>18</sup> to 1&times;10<sup>19</sup>&nbsp;cm<sup>&minus;3</sup>; channel P<sup>&minus;</sup> at 8&times;10<sup>14</sup>&nbsp;cm<sup>&minus;3</sup>, source/drain N<sup>+</sup> at 5&times;10<sup>20</sup>&nbsp;cm<sup>&minus;3</sup>.","Higher halo doping narrows the drain depletion region (roughly &prop;&nbsp;N<sup>&minus;1/2</sup>), which limits drain influence on the source-side barrier."]),
 ("Simulation setup and metrics",["Silvaco Atlas with drift-diffusion transport, Van Dort quantum correction and a self-consistent Gummel&ndash;Newton solver. Same mesh and models for every variant. V<sub>DD</sub>&nbsp;=&nbsp;0.8&nbsp;V.","V<sub>th</sub> by the constant-current method; DIBL from V<sub>th</sub> at V<sub>DS</sub>&nbsp;=&nbsp;0.08&nbsp;V and 0.8&nbsp;V; SS over one decade below threshold; f<sub>T</sub>&nbsp;=&nbsp;g<sub>m</sub>/[2&pi;(C<sub>gs</sub>+C<sub>gd</sub>)] from a 1&nbsp;MHz small-signal AC sweep at V<sub>GS</sub>&nbsp;=&nbsp;V<sub>DS</sub>&nbsp;=&nbsp;V<sub>DD</sub>.","I<sub>OFF</sub> is subthreshold channel leakage at V<sub>GS</sub>&nbsp;=&nbsp;0. The drift-diffusion model has no tunneling component, so it does not include gate-dielectric tunneling."])],
 results=["<b>DIBL cut by 60%</b> versus the 2.0&nbsp;nm uniform-oxide baseline: 67.21 &rarr; 55.10 &rarr; 32.95 &rarr; 26.77&nbsp;mV/V across the step-oxide, DMG and halo stages.","<b>I<sub>ON</sub>/I<sub>OFF</sub> improved nearly sixfold</b>, from 3.05&times;10<sup>4</sup> to 18.05&times;10<sup>4</sup>, with I<sub>OFF</sub> falling from 134.4 to 14.94&nbsp;nA/&micro;m.","<b>The gains cost something.</b> I<sub>ON</sub> falls from 4.10 to 2.70&nbsp;mA/&micro;m, SS ends at 77.27&nbsp;mV/dec (best was 71.22 at the step-oxide stage), V<sub>th</sub> rises to 0.490&nbsp;V and f<sub>T</sub> drops from 491 to 466&nbsp;GHz at the highest halo level.","<b>Best halo trade-off at 2&times;10<sup>18</sup>&nbsp;cm<sup>&minus;3</sup></b>: DIBL 28.37&nbsp;mV/V, I<sub>OFF</sub> 20.19&nbsp;nA/&micro;m, V<sub>th</sub> unchanged and f<sub>T</sub> slightly higher. Beyond that the returns shrink while penalties grow."],
 table=dict(caption="Selected operating point at each stage (V<sub>DD</sub>&nbsp;=&nbsp;0.8&nbsp;V)",
  head=["Stage","I<sub>ON</sub>/I<sub>OFF</sub> (&times;10<sup>4</sup>)","V<sub>th</sub> (V)","SS (mV/dec)","DIBL (mV/V)","f<sub>T</sub> (GHz)"],
  rows=[["UO-DG, 2.0&nbsp;nm uniform (baseline)","3.05","0.344","74.89","67.21","491.43"],
        ["UO-DG, 0.8&nbsp;nm (tunneling-unsafe, reference)","19.23","0.364","69.10","43.48","431.81"],
        ["SO-DG, 2.0&nbsp;nm source / 0.8&nbsp;nm drain","8.19","0.358","71.22","55.10","478.09"],
        ["DMSO-DG, &Delta;&Phi;&nbsp;=&nbsp;0.3&nbsp;eV","8.91","0.463","77.82","32.95","475.19"],
        ["Halo-DMSO-DG, 2&times;10<sup>18</sup>&nbsp;cm<sup>&minus;3</sup>","15.38","0.463","77.08","28.37","476.66"],
        ["Halo-DMSO-DG, 1&times;10<sup>19</sup>&nbsp;cm<sup>&minus;3</sup>","18.05","0.490","77.27","26.77","466.13"]]),
 figs=[("fig1-structure.png","Device structures","The four simulated variants: UO-DG (uniform oxide), SO-DG (step oxide), DMSO-DG (step oxide + dual-material gate) and Halo-DMSO-DG (adds junction halo).",1),
 ("fig2-uo-transfer.png","Stage 1: transfer characteristics","I<sub>D</sub>&ndash;V<sub>GS</sub> at V<sub>DS</sub>&nbsp;=&nbsp;0.8&nbsp;V for uniform oxide from 0.8 to 2.0&nbsp;nm. Thicker oxide raises I<sub>OFF</sub> and lowers I<sub>ON</sub>.",0),
 ("fig3-uo-bands.png","Stage 1: band profiles","OFF-state conduction and valence band edges along the channel. Thicker oxide gives stronger drain-side band bending and a lower source-side barrier.",0),
 ("fig4-uo-trends.png","Stage 1: DIBL, SS and f<sub>T</sub>","DIBL and SS rise with oxide thickness (left); f<sub>T</sub> also rises with oxide thickness (right), so thinning the oxide costs speed.",1),
 ("fig5-so-current-density.png","Stage 2: OFF-state current density","Atlas total current density at V<sub>GS</sub>&nbsp;=&nbsp;0, V<sub>DS</sub>&nbsp;=&nbsp;0.8&nbsp;V for the uniform-oxide and step-oxide devices.",1),
 ("fig6-so-potential.png","Stage 2: potential perturbation","&Delta;&psi;(x) along the channel between V<sub>DS</sub>&nbsp;=&nbsp;0 and 0.8&nbsp;V. The drain-induced change stays more confined to the drain side in the step-oxide device.",0),
 ("fig7-so-bands.png","Stage 2: band profiles","Conduction and valence bands at V<sub>DS</sub>&nbsp;=&nbsp;0.08&nbsp;V and 0.8&nbsp;V. The shift near the source-side barrier is smaller for SO-DG, consistent with its lower DIBL.",0),
 ("fig8-dmg-bands.png","Stage 3: conduction band vs &Delta;&Phi;","Conduction band along the gate in the OFF state (left) and ON state (right). The gate-material boundary creates a potential step that raises the source-side barrier as &Delta;&Phi; increases.",1),
 ("fig9-dmg-current.png","Stage 3: current density","ON-state (left axis) and OFF-state (right axis) current density for &Delta;&Phi; from 0.1 to 0.3&nbsp;eV. OFF-state current falls as &Delta;&Phi; rises.",0),
 ("fig10-dmg-ft.png","Stage 3: f<sub>T</sub> vs V<sub>GS</sub>","The f<sub>T</sub> peak moves to higher V<sub>GS</sub> as &Delta;&Phi; increases, following the rise in V<sub>th</sub>.",0),
 ("fig11-dmg-potential.png","Stage 3: potential maps","Atlas potential distribution at V<sub>GS</sub>&nbsp;=&nbsp;V<sub>DS</sub>&nbsp;=&nbsp;0.8&nbsp;V for &Delta;&Phi;&nbsp;=&nbsp;0.1, 0.2 and 0.3&nbsp;eV.",1),
 ("fig12-halo-schematic.png","Stage 4: halo concept","Depletion-region extent without and with P<sup>+</sup> halo. The higher local doping keeps the drain-side depletion boundary closer to the junction.",1),
 ("fig13-halo-trends.png","Stage 4: halo concentration sweep","DIBL and SS (left), I<sub>ON</sub>/I<sub>OFF</sub> (middle) and f<sub>T</sub> (right) versus halo concentration. DIBL and leakage improve with diminishing returns, while f<sub>T</sub> falls at the highest level.",1)],
 tools=["Silvaco Atlas","DeckBuild","TonyPlot","Python"],links=[]),

dict(slug="mac-unit-rtl-to-gdsii",kind="Academic project &middot; Level 4, Term 2",
 title="RTL-to-GDSII Implementation of an Optimised Multiply-Accumulate Unit",
 lede="A parameterized MAC unit taken from RTL to GDSII on two independent flows, one commercial and one open-source, to check whether synthesis conclusions hold across toolchains.",
 facts=[("Year","2026"),("Flow A","Cadence Genus/Innovus, GPDK045 (45&nbsp;nm)"),("Flow B","OpenROAD, IHP SG13G2 (130&nbsp;nm)"),("Outcome","ICECE 2026 paper, under review")],
 why=["The MAC is the core of DSP and ML accelerators; its area, timing, and power depend heavily on synthesis constraints.","Most results come from a single toolchain. Repeating the study on a second flow tests whether the trends are real or tool artifacts."],
 steps=[("Parameterized RTL",["SystemVerilog MAC unit with configurable parameters."]),("Synthesis constraint sweep",["Constraints varied and the resulting area, timing, and power compared."]),("Physical implementation",["Place and route to GDSII in Innovus on GPDK045 and in OpenROAD on IHP SG13G2."]),("Cross-toolchain validation",["Same design and sweeps on both flows to compare trends."])],
 results=[],figs=[("fig1-flow.png","Design flow","RTL-to-GDSII flow on both toolchains.",1),("fig2-layout.png","Final layout","GDSII layout of the MAC unit.",0),("fig3-sweep.png","Constraint sweep","Area/timing trade-off from the synthesis sweep.",0)],
 tools=["SystemVerilog","Cadence Genus","Cadence Innovus","OpenROAD"],links=[]),

dict(slug="led-optical-classification",kind="Academic project &middot; Level 4, Term 2",
 title="Optical Quality Classification of LEDs Using KNN and Random Forest",
 lede="A low-cost optical characterization rig and a machine-learning pipeline that classifies LED quality from measured optical features.",
 facts=[("Year","2026"),("Hardware","BPW34 photodiode, TCS34725 sensor, Arduino"),("Models","KNN, Random Forest"),("Outcome","ICECE 2026 paper, under review")],
 why=["Visual or spectrometer-based LED screening is slow or expensive.","A cheap sensor setup plus a classifier could grade LEDs consistently."],
 steps=[("Measurement rig",["BPW34 photodiode and TCS34725 colour sensor read by an Arduino.","Readings streamed to the PC over serial (PySerial)."]),("Feature engineering",["Features derived from the raw optical readings before training."]),("Classification",["KNN and Random Forest models trained and compared (scikit-learn, pandas)."]),("Interface",["Streamlit app for live measurement and classification."])],
 results=[],figs=[("fig1-rig.jpg","Measurement rig","Arduino with photodiode and colour sensor.",0),("fig2-app.png","Streamlit interface","Live classification interface.",0),("fig3-results.png","Model comparison","KNN versus Random Forest performance.",0)],
 tools=["Python","scikit-learn","pandas","Streamlit","Arduino","PySerial"],links=[]),

dict(slug="rf-pa-433mhz",kind="Academic project &middot; Level 4, Term 1",
 title="Class-A RF Power Amplifier for the 433&nbsp;MHz ISM Band",
 lede="A common-emitter Class-A power amplifier designed and simulated in Cadence Virtuoso on a 90&nbsp;nm process.",
 facts=[("Year","2025"),("Process","gpdk090 (90&nbsp;nm)"),("Band","433&nbsp;MHz ISM"),("Published","ICECTE 2026, IEEE Xplore")],
 why=["433&nbsp;MHz ISM links need an amplifier with enough gain and output power at low complexity, and a good input match."],
 steps=[("Design",["Class-A common-emitter stage biased for linear operation."]),("Simulate",["Gain, saturated output power, power-added efficiency, and S-parameters in Cadence Virtuoso; QUCS Studio used alongside."])],
 results=["<b>10.11&nbsp;dB</b> gain","<b>18.01&nbsp;dBm</b> P<sub>sat</sub>","<b>7.52%</b> power-added efficiency","S<sub>11</sub> of about <b>&minus;33.5&nbsp;dB</b>"],
 figs=[("fig1-schematic.png","Schematic","Amplifier schematic in Virtuoso.",0),("fig2-gain.png","Gain and power","Gain and output power sweeps.",0),("fig3-s11.png","Input match","S<sub>11</sub> versus frequency.",0)],
 tools=["Cadence Virtuoso","gpdk090","QUCS Studio"],
 links=[("GitHub","https://github.com/mohammad-al-hosan/Class_A_RF_Power_Amplifier_433MHz.git"),("IEEE Xplore","https://doi.org/10.1109/ICECTE69292.2026.11429413")]),

dict(slug="iot-fruit-storage",kind="Academic project &middot; Level 4, Term 1",
 title="IoT-Based Monitoring and Preservation System for Small-Scale Fruit Storage",
 lede="An embedded system that senses storage conditions, actuates cooling and misting automatically, logs to the cloud, and allows a remote override.",
 facts=[("Year","2025"),("Controller","Arduino Mega + ESP8266"),("Sensors","DHT22, MQ135"),("Published","ICECTE 2026, IEEE Xplore")],
 why=["Small-scale storage loses fruit to heat, humidity, and ripening gases, and cold-chain equipment is out of reach for small operators."],
 steps=[("Sense",["DHT22 for temperature and humidity; MQ135 for air quality."]),("Act",["Relay-driven Peltier cooling and misting."]),("Connect",["ESP8266 for cloud logging and remote override."])],
 results=[],figs=[("fig1-block.png","System block diagram","Sensing, control, and cloud paths.",1),("fig2-hardware.jpg","Prototype","Assembled hardware.",0),("fig3-dashboard.png","Cloud dashboard","Logged readings and remote override.",0)],
 tools=["Arduino Mega","ESP8266","DHT22","MQ135","Peltier"],
 links=[("GitHub","https://github.com/mohammad-al-hosan/IOT_Fruit_Storage_System.git"),("IEEE Xplore","https://doi.org/10.1109/ICECTE69292.2026.11429225")]),
]

def page(p):
    s=p['slug']
    facts=''.join(f'<div class="fact"><b>{b}</b><span>{a}</span></div>' for a,b in p['facts'])
    why=''.join(f'<li>{w}</li>' for w in p['why'])
    steps=''.join(f'<li><h3>{t}</h3><ul>'+''.join(f'<li>{b}</li>' for b in bs)+'</ul></li>' for t,bs in p['steps'])
    t=p.get('table')
    tbl=(f'<div class="tblw"><table class="tbl"><caption>{t["caption"]}</caption><thead><tr>'+''.join(f'<th>{h}</th>' for h in t['head'])+'</tr></thead><tbody>'+''.join('<tr>'+''.join(f'<td>{c}</td>' for c in r)+'</tr>' for r in t['rows'])+'</tbody></table></div>') if t else ''
    res=(f'<section><h2>Results</h2><ul class="res">'+''.join(f'<li>{r}</li>' for r in p['results'])+f'</ul>{tbl}</section>') if p['results'] else ''
    figs=''.join(f'<figure class="{"wide" if w else ""}"><img src="../assets/img/{s}/{f}" alt="{t}" loading="lazy"><figcaption><b>{t}.</b> {c}</figcaption></figure>' for f,t,c,w in p['figs'])
    chips=''.join(f'<span class="chip">{t}</span>' for t in p['tools'])
    links=''.join((f'<a class="btn" href="{u}" target="_blank" rel="noopener">{t}</a>' if u else f'<p class="note">{t}</p>') for t,u in p['links'])
    links=f'<section><h2>Links</h2><div class="links">{links}</div></section>' if links else ''
    plain=html.unescape(p['title']).replace('<sub>','').replace('</sub>','')
    return f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{plain} | M. A. H. Kanon</title>
<meta name="description" content="{html.escape(html.unescape(p['lede']))}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,72,400;0,72,500;0,72,600;1,72,400&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../assets/style.css"></head><body>
<header class="nav"><div class="nav-in"><span class="mark"><b>M. A. H. Kanon</b> / EEE, BUET</span>
<nav><a href="../index.html">Home</a><a href="../index.html#research">Research</a><a href="../index.html#projects">Projects</a><a href="../index.html#contact">Contact</a><button class="tt" id="tt" type="button" aria-label="Toggle dark mode">&#9789;</button></nav></div></header>
<main class="wrap">
<a class="back" href="../index.html#{'research' if 'thesis' in p['kind'].lower() or 'research' in p['kind'].lower() else 'projects'}">&larr; Back to portfolio</a>
<div class="ph"><div class="kind">{p['kind']}</div><h1>{p['title']}</h1><p class="lede">{p['lede']}</p>
<div class="facts pf">{facts}</div></div>
<section><h2>Motivation</h2><div class="card"><ul>{why}</ul></div></section>
<section><h2>How it was done</h2><ol class="steps">{steps}</ol></section>
<section><h2>Figures</h2><div class="figs">{figs}</div></section>
{res}
<section><h2>Tools</h2><div class="chips">{chips}</div></section>
{links}
</main><footer><div class="wrap"><p class="fine">&copy; Mohammad Al Hosan Kanon &middot; <a href="../index.html">Portfolio</a></p></div></footer>
<script src="../assets/site.js"></script></body></html>'''

os.makedirs('projects',exist_ok=True)
lst=[]
for p in PAGES:
    open(f"projects/{p['slug']}.html",'w').write(page(p))
    os.makedirs(f"assets/img/{p['slug']}",exist_ok=True)
    lst.append(f"## {p['slug']}  (assets/img/{p['slug']}/)\n"+''.join(f"- {f}: {html.unescape(t)} - {html.unescape(c)}\n" for f,t,c,w in p['figs']))
open('IMAGES.md','w').write("# Images to add\nDrop each file in the folder shown. Missing images are hidden automatically, so add them whenever ready.\n\n"+'\n'.join(lst))
print("built",len(PAGES),"pages")

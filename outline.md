# Report outline — "Altermagnets and spin liquids"

Target: ~10 pages total. Page 1 carries title block + abstract (~0.5 p), bibliography at the
end (~0.5 p), so plan for **~9 pages of body text**. Page budgets below include figures — with
3–4 figures (roughly a half page each) the text share per chapter shrinks accordingly.

Chapter order mirrors the presentation (approved with Prof. Scheurer):
motivation → model → classical phases → QSL/Schwinger-boson machinery → nearby spin liquids →
altermagnetic spin liquid → outlook.

---

## Abstract (~0.3 p, write last)

- One sentence each: (i) context — altermagnets as ordered phases are well studied; (ii) question
  — does altermagnetic character survive when quantum fluctuations destroy spin order?; (iii)
  method — checkerboard J₁–J₂–K model, classical phase diagram, Schwinger-boson theory of the
  neighboring spin liquids; (iv) result — a Z₂ *altermagnetic spin liquid*: no spin order, but a
  persistent staggered scalar-chirality pattern invariant under T·C₄z.

## 1. Introduction (~1 p)

Depth: broad strokes, no equations. This is the "why should anyone care" chapter — set up the
question and announce the answer.

- Altermagnets in one paragraph: collinear compensated magnets where the sublattices are related
  by a point-group operation (e.g. C₄z), not translation/inversion → zero net moment but
  T-breaking, spin-split bands. One or two sentences only — the seminar audience (and the other
  handouts) cover ordered AMs; cite Šmejkal/Sinova/Jungwirth-type references from the paper's
  intro [refs 1–67 block of the paper].
- Point out what all of that physics has in common: it assumes long-range spin order — a static
  spin texture that breaks time reversal in a specific pattern.
- Pose the central question of the report: what happens in the adjacent regime, when frustration
  is strong and quantum fluctuations prevent the spins from ordering (⟨Sᵢ⟩ = 0 even at T = 0)?
  Does anything altermagnetic survive?
- Preview the answer and the logic of the report (one short paragraph = roadmap): yes — but it
  survives in spin-rotation-invariant observables (scalar spin chirality), and describing the
  disordered phase requires the language of quantum spin liquids, partons, and emergent gauge
  fields. Name the main result: the altermagnetic Z₂ spin liquid.
- Mention experimental relevance flagged in the paper's intro: hints of interplay between
  altermagnetism and frustration in Mn₅Si₃ thin films and CsCr₃Sb₅ — keeps the question from
  looking purely academic.
- Source: paper Sec. I + your slide-2 notes ("From Altermagnets to Spin Liquids").

## 2. The model: a frustrated checkerboard altermagnet (~1 p)

Depth: give the Hamiltonian, Eq. (1) of the paper, and explain every coupling in words. One
figure: the lattice with couplings (paper Fig. 1(a) or your own redraw). No derivations.

- Setup: two sublattices A and B per unit cell, placed on the bonds of a square lattice; spins Ŝᵢ
  on those bonds. Reproduce the Hamiltonian with J₁ (nearest-neighbor, antiferromagnetic),
  J₂ (next-nearest-neighbor, checkerboard pattern), K (ring exchange over four spins around a
  common vertex, preserving C₄v, T, spin rotation, translation).
- The symmetry point (this is the crux of the chapter, give it a full paragraph): with J₁ only,
  the model is just a 45°-rotated square-lattice antiferromagnet — there is an *artificial*
  translation symmetry connecting A and B. J₂ and K break that translation, leaving A and B
  related only by C₄z. That is precisely the altermagnetic symmetry: net moment forced to zero by
  a rotation, not by translation.
- Role of each coupling in one line each: J₂ introduces frustration / competing orders; K lifts
  degeneracies and (crucially, foreshadow) stabilizes a noncoplanar phase.
- Close with a scope remark from the talk: the construction is general, this model is just a
  minimal explicit example.
- Source: paper Sec. II first half + slide 3 notes.

## 3. Classical phase diagram and SR-invariant observables (~2.5 p)

Depth: the workhorse descriptive chapter. Two figures budgeted: the phase diagram + spin
textures (paper Fig. 1(b),(c)) and, if space allows, the S_EP/χ_EP cuts (Fig. 1(d),(e)). Give
the classical ansatz equation and the definitions of S_EP and χ_EP explicitly; describe each
phase in a few sentences (a table condensing paper Table I is worth the space and saves prose).

### 3.1 Method (~0.5 p)
- Classical limit S → ∞: spins as classical unit vectors, no quantum fluctuations.
- The variational ansatz, Eq. (2): general spiral with ordering wavevector Q, sublattice phase
  shift ϕ, out-of-plane cantings η_A, η_B. Explain what each parameter encodes (Q = period and
  direction, ϕ = relative angle between sublattices, η = noncoplanarity — zero in all coplanar
  phases).
- Energy minimized over {Qx, Qy, ϕ, η_A, η_B} per (J₂, K) point (grid + gradient descent; one
  sentence, cite paper Appendix A — don't reproduce the numerics).

### 3.2 Why SR-invariant observables (~0.5 p) — conceptually load-bearing, don't rush it
- Motivation stated *before* the phase walk-through, as in the talk: later, quantum melting will
  restore spin-rotation symmetry and ⟨Sᵢ⟩ = 0 everywhere — any conventional order parameter dies.
  We need observables that can stay nonzero without spin polarization.
- Define both plaquette observables:
  - S_EP = (S₁·S₂, S₂·S₃, S₃·S₄, S₄·S₁): SR-invariant; all components equal ⇒ C₄z intact;
    alternating pattern ⇒ C₄z broken → nematicity detector.
  - χ_EP = (S₁·(S₂×S₃), …): scalar spin chirality; needs noncoplanar spins (vanishes for any
    coplanar texture); odd under T (triple product of flipped vectors) → time-reversal detector
    in the SR-invariant sector.
- One sentence: together they diagnose *whether and how* C₄z and T are broken — the pattern of
  breaking is what defines the altermagnet.

### 3.3 The phases (~1.5 p)
Walk through in the talk's order; ~1 short paragraph per phase, anchored by the table.
- **A1 — collinear altermagnet** (the anchor): antiparallel sublattices, Q = 0, ϕ = π. S_EP =
  −(1,1,1,1) uniform, χ_EP = 0. All magnetic point symmetries preserved modulo spin rotation;
  M = 0 guaranteed by C₄z, not translation.
- **A2 — canted AM**: second-order transition at larger K; both sublattices cant (η_A = η_B),
  finite magnetization M ≠ 0, but S_EP still uniform, χ_EP = 0 — same SR-invariant symmetries
  as A1.
- **A3 — orthogonal AFM**: large J₂, Q = (π,π), ϕ = π/2; neighboring spins perpendicular ⇒
  S_EP = (0,0,0,0); four-spin enlarged unit cell picture; still nonchiral.
- **B1, B2 — the two nematics**: break C₄z in SR-invariant observables while preserving T.
  B1: S_EP = (−1,1,−1,1) (alternating); B2: S_EP = (1,1,−1,−1) (pairwise), i.e. two distinct
  breaking patterns. χ_EP = 0 for both. One line on how they're reached (B1 first-order from A3
  by flipping sign of K; B2 when K > 0 dominates).
- **C — the orbital altermagnet** (give this phase the most room, ~0.5 p; it's the reason the
  paper exists):
  - Most frustrated region; spins cant *oppositely* out of plane (η_A = −η_B) ⇒ noncoplanar.
  - Reached from A1 by a *second-order* transition — χ_EP turns on continuously (paper
    Fig. 1(e)).
  - S_EP stays uniform (not nematic!), but χ_EP ∝ (−1,1,−1,1): staggered scalar chirality.
  - The symmetry argument, spelled out step by step (this is the payoff of 3.2): χ_EP odd under
    T alone, odd under C₄z alone, invariant under the product T·C₄z — the defining symmetry
    structure of an altermagnet, now living in the chirality channel instead of the spin channel.
  - Why "orbital": in an itinerant system, plaquette scalar chirality induces circulating orbital
    currents whose staggered pattern has the same T·C₄z invariance — moments finite locally, zero
    globally via C₄z rather than translation. (Keep to 2–3 sentences; Sec. IV itself is out of
    scope.)
- Source: paper Sec. II second half + Table I + slides 4–9, 22, 23.

## 4. Quantum spin liquids and the Schwinger-boson construction (~2.5 p)

Depth: the pedagogical/theory chapter, drawing on Savary & Balents (Secs. 1 and 3) for the
concepts and the paper's Sec. III for the formalism. Equations needed: SB representation +
constraint, the mean-field Hamiltonian H_b, and the gauge-transformation statement for the IGG.
No Bogoliubov algebra — describe the diagonalization in words.

### 4.1 What is a quantum spin liquid (~0.75 p) — from Savary Sec. 1
- Definition by three properties, exactly as in the talk: (i) no static magnetic order,
  ⟨Sᵢ⟩ = 0 even at T = 0; (ii) long-range-entangled ground state — not adiabatically connected
  to any product state (this separates a QSL from a trivial paramagnet); (iii) fractionalized
  excitations — spin-½ spinons not creatable by any local operator — plus emergent gauge fields.
- RVB picture as the visual anchor: superposition of all singlet pairings; no bond dominates, no
  spin order by construction, and manifestly not a product state over any finite region.
- One contrast sentence for the seminar context: spinons are *not* magnons — magnons are spin-1
  Goldstone modes of a broken-symmetry state; spinons exist precisely because no symmetry is
  broken.
- One or two sentences from Savary Sec. 3 (gauge theory) at the appropriate depth: the emergent
  gauge structure is what makes fractionalization stable/meaningful — deconfined phases of an
  emergent gauge theory; in 2D, a U(1) gauge structure is generically confining (unstable) while
  Z₂ can be a stable deconfined (topologically ordered) phase. This pre-loads the IGG discussion
  in 4.3 — keep it qualitative, no lattice-gauge-theory formalism.

### 4.2 Schwinger bosons: fractionalize, decouple, diagonalize (~1 p)
- The parton step: rewrite Ŝᵢ = ½ b̂†_{iσ} σ_{σσ'} b̂_{iσ'} with two bosons per site and local
  constraint n̂ᵢ = 2S. Stress: exact rewriting, embeds the spin Hilbert space in a larger one;
  the price is a local U(1) gauge redundancy b̂_j → e^{iφ_j} b̂_j that leaves all spin operators
  unchanged. (This delivers the "parton theories: fractionalization + constraint" item from the
  goal statement.)
- Mean-field decoupling of the quartic interaction → two bond fields, with physical meaning
  spelled out (the talk's framing is good, reuse it):
  - A_ij: singlet pairing amplitude — creates/destroys a spin-0 pair on the bond; "the RVB
    valence bond made explicit."
  - B_ij: spin-preserving boson hopping — standard tight-binding-like hopping.
- Resulting free-boson Hamiltonian H_b (quote it), with Lagrange multiplier μ enforcing the
  constraint on average; Fourier transform + Bogoliubov diagonalization → bosonic quasiparticle
  bands (one sentence, no algebra).
- Key vocabulary sentence: the pattern of {A_ij, B_ij} on the lattice — the *Ansatz* — is what
  defines a particular spin liquid.
- Note the paper's methodological stance (one sentence): rather than trusting self-consistent
  mean-field values, systematically scan Ansätze — this sets up Ch. 5.

### 4.3 Condensation vs. gap, and the IGG (~0.75 p)
- The bridge (the single most important conceptual step in the report — make it explicit):
  tune μ / couplings; if the lowest boson band touches E = 0, bosons condense at some k and the
  condensate reconstructs exactly one of the classical textures (A1, B1, C, …) ⇒ magnetic order.
  If the band stays gapped, no order — the same Ansatz instead describes a fractionalized,
  long-range-entangled state: the *neighboring* spin liquid of that ordered phase.
- Invariant gauge group: the subgroup of the U(1) gauge redundancy that leaves the Ansatz
  invariant. Real A_ij only → IGG = U(1); adding imaginary B_ij generically breaks it down to
  the sign flip b → −b, IGG = Z₂.
- Why it matters (connect back to 4.1's Savary content): IGG determines the low-energy gauge
  structure, hence the nature and stability of the spin liquid — U(1) generically unstable
  (confinement) in 2D, Z₂ a stable topological phase with vison excitations.
- Source: paper Sec. III first half + Savary Secs. 1, 3 + slides 10–13.

## 5. Nearby spin liquids and the altermagnetic spin liquid (~1.75 p)

Depth: the results chapter. One figure: the Ansätze panel (paper Fig. 2) — worth the space,
it's "the heart of the nearby-spin-liquids story." Little new formalism; the work here is
interpretation.

### 5.1 Strategy and the Ansatz catalog (~0.75 p)
- The reverse-engineering recipe, as a numbered list (mirrors slide 14): choose {A_ij, B_ij} on
  NN and NNN bonds → diagonalize → tune μ to condensation → check the condensate reproduces the
  target classical phase → the *gapped* regime of that same minimal Ansatz is the neighboring
  QSL. Note: NN + NNN suffices for all six phases, no unit-cell enlargement.
- Walk Fig. 2 briefly: blue arrows = real A_ij, black/gray = real/imaginary B_ij; colored
  ellipses = ⟨S_EP⟩ evaluated *in the spin-liquid regime* (no condensate).
- The inheritance statement: each spin liquid reproduces the discrete-symmetry pattern of its
  parent phase in ⟨S_EP⟩/⟨χ_EP⟩ — A1/A2/A3 liquids fully symmetric, B1/B2 liquids nematic.
  Give the IGG assignments (Table I last column): A1, B1, B2 → U(1); A2, A3, C → Z₂.

### 5.2 The altermagnetic spin liquid (~1 p) — the climax, give it room
- Phase C's Ansatz is the only one requiring imaginary B_ij and the only one with nonzero
  chirality in the spin-liquid regime; IGG = Z₂.
- In the gapped (uncondensed) regime: ⟨Sᵢ⟩ = 0, SR symmetry fully restored, ⟨S_EP⟩ isotropic
  (C₄z intact in the spin sector) — but ⟨χ_EP⟩ ∝ (−1,1,−1,1) persists: T still broken in the
  chirality sector with exactly the altermagnetic T·C₄z pattern.
- State the result in one clean sentence: Z₂ topological order + surviving altermagnetic
  chirality = the altermagnetic spin liquid — a symmetry-enriched topological phase; the
  altermagnetic character outlives the spin order that originally defined it.
- Excitations: as a Z₂ liquid it hosts visons, associated with local distortions of the
  chirality/magnetization pattern — the natural target for local probes (bridge to Ch. 6).

## 6. Conclusion and outlook (~0.75 p)

- Three take-home points, matching the talk's summary slide almost verbatim: (i) the checkerboard
  J₁–J₂–K model hosts, besides collinear/nematic phases, a noncoplanar orbital altermagnet with
  staggered scalar chirality invariant under T·C₄z; (ii) via Schwinger bosons every classical
  phase has a neighboring spin liquid inheriting its discrete symmetries through S_EP and χ_EP;
  (iii) the orbital AM's neighbor is an altermagnetic Z₂ spin liquid — no spin order, persistent
  altermagnetic chirality, topological order.
- Experimental outlook (short — 3–4 sentences, from the talk's closing): most direct route is
  local probes sensitive to bond chirality (STM, local susceptibility; vison detection);
  candidate frustrated altermagnetic materials Mn₅Si₃ thin films and CsCr₃Sb₅; frustrated
  altermagnets largely unexplored — "this paper opens the map."
- Optional one-liner acknowledging what was cut: the same framework extends to doped/itinerant
  systems (paper Sec. IV) — out of scope here, but signals the report's boundary deliberately.

---

## Figure plan (counts toward the page budget)

1. Lattice + couplings (Ch. 2) — paper Fig. 1(a) or redraw.
2. Classical phase diagram + textures (Ch. 3) — paper Fig. 1(b),(c); optionally (d),(e) cuts.
3. Table of phases (Ch. 3) — condensed version of paper Table I (S_EP, χ_EP, M, symmetries, IGG).
4. Ansätze with ⟨S_EP⟩/⟨χ_EP⟩ overlays (Ch. 5) — paper Fig. 2.

If reproducing paper figures, note the paper is CC-BY-4.0 — cite the source in each caption.

## Reference list (minimum)

- Sobral, Mandal, Scheurer, Phys. Rev. Research 7, 023152 (2025) — primary.
- Savary & Balents, Rep. Prog. Phys. 80, 016502 (2017) — QSL/gauge-theory background.
- 1–2 altermagnetism reviews for Ch. 1 (take from the paper's intro citations, e.g. Šmejkal et
  al. PRX 12, 040501).
- Mn₅Si₃ / CsCr₃Sb₅ experimental refs (paper's refs [68, 69, 48]) for intro + outlook.

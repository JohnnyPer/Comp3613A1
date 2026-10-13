# student-judge competency report

**Judged at:** 2026-10-12
**Student / session:** COMP 3613 Student Accommodation; name and ID for the PDF cover still need confirmation
**Evidence pass:** Re-read both available native Copilot chats and current `docs/report.md`, use-case JSON/PNG, wireframe, and refreshed transcript markdown; prior `docs/judge.md` ignored
**Artifact:** Two native GitHub Copilot Guide chats, one user-provided partial Phase 1 excerpt, current report and diagrams, wireframe, and Guide-written transcript markdown
**Phases in evidence:** 1–5 (COMP 3613); Phase 6 deployment not completed

### Totals
| | Count / value |
|--|--|
| Metrics on rubric | 12 (M1–M12) |
| N/A (excluded) | 0 |
| Metrics scored | 12 |
| Scoreable max | 12 × 4 |
| Awarded total | 42 / 48 |
| **Overall (avg of scored)** | **3.5 / 4** |
| Impression mark | 18 / 20 |

## Scorecard

| ID | Metric | Score / 4 | In avg | Evidence |
|----|--------|----------:|:------:|----------|
| M1 | Phase discipline | 3 | yes | The Phase 1 excerpt and later native chats show phase handoffs, a student wireframe before Phase 5 implementation, and workflow-by-workflow build and polish. Phase 6 remains pending. |
| M2 | Problem framing | 3 | yes | The student named three workflows, supplied entity/property and relationship decisions, and specified “Explore listings includes Search listings” and “View tenants includes Search tenants.” |
| M3 | Decision ownership | 3 | yes | Student owned the domain fields and relationships, accepted `Accommodation.imageUrl` after seeing it in the wireframe, and steered repeated UI corrections including “its still too far to the left.” |
| M4 | Artefact-before-code | 4 | yes | Student said “start phase 4 wireframe added”; the composite wireframe covers all three workflows, and the later build tracks those screens and the model. |
| M5 | Verification habit | 3 | yes | Student reported tenant and redirect failures, gave feedback after checking the Read Reviews layout, and finally confirmed “both the centering of the button and the bob/admin redirect errors have been fixed.” |
| M6 | Assignment fit | 4 | yes | Report and code-check evidence show routes calling services, repository persistence, ERD-aligned models, and workflow-specific UI; checks mark the route snippets `architecture_ok: yes`. |
| M7 | Slice explanation | 3 | yes | Student completed model, repository, service, and route snippets. The thin-route checks passed, though explanatory prose was brief and several details needed guided corrections. |
| M8 | Prompt quality | 3 | yes | Phase-specific prompts and concrete, observable refinements included “move the button to the center of the empty space” and the Phase 2 include decisions. |
| M9 | Response to pushback | 4 | yes | Student kept reporting that the button remained left or unchanged, prompting a layout and cache-busting correction, then confirmed the result. |
| M10 | Integrity | 4 | yes | The readable chats show ordinary workflow decisions and refinement, not paste-back or evasion; `docs/report.md` records `student-build:skill-integrity` as `pass`. |
| M11 | Provenance continuity | 4 | yes | The Phase 2 include changes updated the existing use-case diagram and report; later polish adjusted the same named workflows and wireframe implementation. |
| M12 | Sincerity trajectory | 4 | yes | No suspicion rounds were needed; no sincerity blocks or abandonment are present in the available Guide chats. |

## Strengths
- Student supplied the three named workflows, domain entities and properties, relationship choices, and business-rule constraints.
- The student-authored wireframe covers all three workflows; the model and implementation notes track its fields and flows.
- Student snippets covered model, repository, service, and thin-route layers, with architecture-respecting checks recorded.
- Student reported mismatches, requested iterative polish, and confirmed the centering and Bob/Admin redirect fixes.
- Two native Copilot Guide chats and the partial Phase 1 excerpt are represented in the refreshed transcript package; the course skill-integrity marker passes.

## Gaps (priority order)
1. Phase 6 deployment is incomplete: `docs/report.md` still has `https://` rather than a public Render URL. Deployment should follow Phase 5 polish.

## Phase gate status
| Phase | Status | Note |
|-------|--------|------|
| 1 | met | The available student-provided excerpt records Student Accommodation and the three workflows; the original Phase 1 chat is only partially available. |
| 2 | met | Student specified the Search listings and Search tenants includes; the use-case diagram records listing details and the reviews extension. |
| 3 | met | Student supplied entity fields, relationships, foreign-key ownership, and booking/review rules. |
| 4 | met | Student wireframe covers all three workflows; `Accommodation.imageUrl` was added after the wireframe review. |
| 5 | met | Theming, implementation, student verification, and iterative polish are recorded, including final confirmation of the button and redirect fixes. |
| 6 | not met | No public deployed URL is recorded; the report's deployment field remains `https://`. |

## Recommended next practice
- Deploy the polished app to Render and record the public app URL and marker logins in `docs/report.md`.

## Integrity note
- Clean: no evidence of external-assist/paste-back, evasion, or edited course skills in the readable record; the skill-integrity marker passes.

## Provenance flags
- Phase 1 evidence is a user-provided partial excerpt rather than the full native chat. Two later phases have native Copilot chat records; no other provenance concern found.

## Sincerity log summary
- Blocks found: 0 | max round: N/A | min/mean/final confidence: N/A | trend: N/A | cleared: not needed

## Skips
- Skips: 0/3 used. No skipped-question assumptions are recorded in the available chats.

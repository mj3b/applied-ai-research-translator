# References

Applied AI Research Translator is a research software artifact. This file records the external source base that informed the repository’s governance model, safety-policy intake gate, translation method, traceability logic, limitation register, schema-validation posture, archival metadata, and AI safety and policy framing.

This bibliography is curated rather than exhaustive. It is meant to make the project’s intellectual dependencies visible to researchers, reviewers, auditors, and contributors. Inclusion does not imply legal compliance, regulatory certification, endorsement, or completeness. The repository’s claims remain artifact-level and methodological: it provides a governed path from research source to decision record.

---

## How to Use This File

Use this file as the project-level bibliography.

| Use Case | How to Use the References |
|---|---|
| Scholarly review | Inspect the external frameworks, safety literature, and research-integrity sources that inform the repository’s design |
| Governance review | Compare the repository’s controls against recognized governance concepts such as risk mapping, documentation, human oversight, auditability, and decision accountability |
| Contribution review | Check whether a proposed schema, pack, or document change should cite an existing source category |
| Release review | Confirm that citation metadata, DOI records, and versioned release notes remain aligned |
| ORCID or Zenodo review | Use the software-citation and archival references to support repository description and citable software status |

The main documents should cite only the most relevant sources locally. This file should hold the broader bibliography.

---

## Source Selection Standard

References were included when they support one or more of the following repository functions:

| Repository Function | Reference Basis |
|---|---|
| Safety-policy intake | Sources concerning AI capability, misuse, loss of control, compute governance, model-weight security, liability, international governance, and concentration of power |
| Governance model | Frameworks and standards concerning risk management, human oversight, documentation, accountability, and institutional review |
| Translation method | Sources concerning research-to-decision movement, evidence preservation, evaluation, abstention, and task containment |
| Traceability model | Sources concerning documentation, reproducibility, audit reconstruction, software citation, and machine-readable records |
| Limitation register | Sources that clarify what the repository does not prove, certify, or automate |
| Release and citation layer | Sources that define research-software citation, DOI archival practice, and GitHub repository metadata |

---

## 1. Project-Specific Source Maps

These documents are included because they shaped the safety-policy and technical reading map used to design the safety-policy intake gate. They are source maps, not compliance authorities.

| Reference | Relevance to Repository |
|---|---|
| AISST Policy Fellowship Syllabus. Spring 2026. Google Docs. https://docs.google.com/document/d/1uMUIz8M31MDaJ1Fly4C4xQFZHk_TeIvkFuly_7XbtQY/edit?usp=sharing | Provided the policy structure behind the safety-policy intake gate: capability timelines, misuse, loss of control, theories of victory, radical optionality, liability, private governance, international governance, compute, model weights, career planning, and concentration of power |
| AISST Technical Curriculum. Spring 2026. Google Docs. https://docs.google.com/document/d/1D1CtFaW09htjCdVLZwyOGaD5qk4KNKI2kgwKl6qN5S8/edit?usp=sharing | Provided the technical structure behind the safety-policy intake gate: ML foundations, reward misspecification, RLHF, deception, goal misgeneralization, mechanistic interpretability, probing and steering, control, scalable oversight, red-teaming, and AI policy intervention points |

---

## 2. Core AI Governance Frameworks and Standards

These references support the repository’s governance model, especially the distinction between source intake, risk mapping, evidence generation, human review, and final decision authority.

| Reference | Project Use |
|---|---|
| National Institute of Standards and Technology. 2023. *Artificial Intelligence Risk Management Framework (AI RMF 1.0).* https://www.nist.gov/itl/ai-risk-management-framework | Supports the repository’s Govern, Map, Measure, and Manage framing for source-risk classification, evaluation, and decision accountability |
| National Institute of Standards and Technology. 2023. *AI RMF Core: Govern, Map, Measure, Manage.* https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ | Supports the ordering logic behind safety-policy intake before measurement, management, and downstream decision records |
| National Institute of Standards and Technology. 2024. *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile.* NIST AI 600-1. https://doi.org/10.6028/NIST.AI.600-1 | Supports the repository’s treatment of generative AI risks, provenance, pre-deployment testing, incident disclosure, governance, misuse, and uncertainty |
| Organisation for Economic Co-operation and Development. 2019, updated 2024. *OECD AI Principles.* https://www.oecd.org/en/topics/sub-issues/ai-principles.html | Supports the repository’s emphasis on trustworthy AI, human-centred values, transparency, robustness, safety, and accountability |
| European Union. 2024. *Regulation (EU) 2024/1689: Artificial Intelligence Act.* EUR-Lex. https://eur-lex.europa.eu/eli/reg/2024/1689/oj | Supports the repository’s documentation, transparency, human oversight, record-keeping, and high-risk AI governance mappings |
| ISO/IEC. 2023. *ISO/IEC 42001:2023, Information technology, Artificial intelligence, Management system.* https://www.iso.org/standard/42001 | Supports the repository’s mapping to AI management system concepts, while preserving the boundary that this repository does not certify ISO compliance |
| ISO. 2024. *Building a Responsible AI: How to Manage the AI Ethics Debate.* https://www.iso.org/artificial-intelligence/responsible-ai-ethics | Supports background framing on responsible AI, ethics, and organizational management context |
| California Legislature. 2025. *SB-53 Artificial intelligence models: large developers, Transparency in Frontier Artificial Intelligence Act.* https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260SB53 | Supports the safety-policy intake fields for frontier AI frameworks, catastrophic risk assessment, critical safety incidents, model-weight security, internal governance, and transparency reporting |

---

## 3. AI Safety and Policy Source Base

These references support the safety-policy intake gate. They are used to justify why AI safety and policy sources require classification before claim extraction and task design.

### Capability, Timelines, and Autonomy

| Reference | Project Use |
|---|---|
| Kwa, T., West, B., Becker, J., Deng, A., Garcia, K., Hasin, M., Jawhar, S., Kinniment, M., Rush, N., Von Arx, S., Bloom, R., Broadley, T., Du, H., Goodrich, B., Jurkovic, N., Miles, L. H., Nix, S., Lin, T., Parikh, N., Rein, D., Sato, L. J. K., Wijk, H., Ziegler, D. M., Barnes, E., & Chan, L. 2025. *Measuring AI Ability to Complete Long Tasks.* METR. https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/ | Supports the intake fields for task horizon, autonomy level, tool-use scope, and frontier relevance |
| Kwa, T. et al. 2025. *Measuring AI Ability to Complete Long Tasks.* arXiv:2503.14499. https://arxiv.org/abs/2503.14499 | Paper version supporting the same capability-horizon framing |
| Epoch AI. 2024. *Can AI Scaling Continue Through 2030?* https://epoch.ai | Supports background analysis for capability-scaling and compute-trajectory considerations |
| Aschenbrenner, L. 2024. *Situational Awareness: The Decade Ahead.* https://situational-awareness.ai/ | Supports the policy syllabus category on capability timelines, national security, frontier capability, and strategic governance debate |
| Narayanan, A., & Kapoor, S. 2025. *AI as Normal Technology.* Knight First Amendment Institute. https://knightcolumbia.org/content/ai-as-normal-technology | Supports countervailing analysis against treating AI as exceptional in every governance context |
| Alexander, S. 2025. *AI as Profoundly Abnormal Technology.* AI Futures Project. https://ai-futures.org/ | Supports the opposing governance frame that frontier AI may require extraordinary institutional treatment |

### Misuse, Dual-Use Risk, and Catastrophic Risk

| Reference | Project Use |
|---|---|
| Center for AI Safety. 2023. *Statement on AI Risk.* https://www.safe.ai/statement-on-ai-risk | Supports the safety-policy intake category for catastrophic-risk relevance |
| Bostrom, N. 2019. *The Vulnerable World Hypothesis.* *Global Policy.* https://nickbostrom.com/papers/vulnerable.pdf | Supports the misuse and vulnerable-world framing behind restricted translation boundaries |
| Shevlane, T., Farquhar, S., Garfinkel, B., Phuong, M., Whittlestone, J., Leung, J., Kokotajlo, D., Marchal, N., Anderljung, M., Kolt, N., Ho, L., Siddarth, D., Avin, S., Hawkins, W., Kim, B., Gabriel, I., Bolina, V., Clark, J., Bengio, Y., Christiano, P., & Dafoe, A. 2023. *Model Evaluation for Extreme Risks.* arXiv:2305.15324. https://arxiv.org/abs/2305.15324 | Supports the repository’s evaluation and extreme-risk intake logic |
| UK Government. 2024. *Frontier AI Safety Commitments, AI Seoul Summit 2024.* https://www.gov.uk/government/publications/frontier-ai-safety-commitments-ai-seoul-summit-2024/frontier-ai-safety-commitments-ai-seoul-summit-2024 | Supports the source-risk classification fields for frontier development, risk identification, evaluation, and deployment safeguards |

### Loss of Control, Deception, and Alignment Failure

| Reference | Project Use |
|---|---|
| Anthropic. 2024. *Alignment Faking in Large Language Models.* https://www.anthropic.com/research/alignment-faking | Supports intake fields for strategic behavior, deception risk, oversight failure, and loss-of-control review |
| Greenblatt, R. et al. 2024. *Alignment Faking in Large Language Models.* arXiv. https://arxiv.org/abs/2412.14093 | Paper version of the alignment-faking research |
| Ngo, R., Chan, L., & Mindermann, S. 2022. *The Alignment Problem from a Deep Learning Perspective.* arXiv:2209.00626. https://arxiv.org/abs/2209.00626 | Supports the technical curriculum categories for alignment difficulty, goal-directed behavior, and loss of control |
| Shah, R., Varma, V., Kumar, R., Phuong, M., Krakovna, V., Uesato, J., & Kenton, Z. 2022. *Goal Misgeneralization: Why Correct Specifications Aren’t Enough for Correct Goals.* arXiv:2210.01790. https://arxiv.org/abs/2210.01790 | Supports intake and screening fields for goal misgeneralization and task-boundary failure |
| Krakovna, V. et al. 2020. *Specification Gaming: The Flip Side of AI Ingenuity.* DeepMind. https://deepmind.google/discover/blog/specification-gaming-the-flip-side-of-ai-ingenuity/ | Supports failure-condition logic around proxy objectives and evaluation gaming |
| Scheurer, J., Balesni, M., & Hobbhahn, M. 2023. *Large Language Models Can Strategically Deceive Their Users When Put Under Pressure.* arXiv:2311.07590. https://arxiv.org/abs/2311.07590 | Supports the loss-of-control and oversight-failure intake categories |
| Hubinger, E. et al. 2024. *Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training.* arXiv:2401.05566. https://arxiv.org/abs/2401.05566 | Supports restricted-handling and safety-evaluation boundaries for model organisms of misalignment |

### Model Weights, Compute Governance, and Infrastructure Control

| Reference | Project Use |
|---|---|
| Nevo, S., Lahav, D., Karpur, A., Bar-On, Y., Bradley, H. A., & Alstott, J. 2024. *Securing AI Model Weights: Preventing Theft and Misuse of Frontier Models.* RAND. https://www.rand.org/pubs/research_reports/RRA2849-1.html | Supports intake fields for model-weight relevance, access control, exfiltration risk, and security review |
| Sastry, G., Heim, L., Belfield, H., Anderljung, M., Brundage, M., Hazell, J., O’Keefe, C., Hadfield, G. K., Ngo, R., Pilz, K., Gor, G., Bluemke, E., Shoker, S., Egan, J., Trager, R., Avin, S., Weller, A., Bengio, Y., & Coyle, D. 2024. *Computing Power and the Governance of Artificial Intelligence.* arXiv:2402.08797. https://arxiv.org/abs/2402.08797 | Supports intake fields for compute governance, regulatory visibility, allocation, verification, and concentration risk |
| Heim, L. 2024. *How US Export Controls Have and Haven’t Curbed Chinese AI.* https://www.rand.org/ | Supports policy framing for compute, export controls, international governance, and strategic constraint analysis |
| Trager, R. et al. 2023. *International Governance of Civilian AI: A Jurisdictional Certification Approach.* https://www.governance.ai/ | Supports international governance and verification framing |

### Control, Oversight, and Red-Teaming

| Reference | Project Use |
|---|---|
| Greenblatt, R., & Shlegeris, B. 2024. *The Case for Ensuring That Powerful AIs Are Controlled.* https://www.alignmentforum.org/ | Supports the repository’s distinction between bounded evidence production and human-controlled authorization |
| Greenblatt, R. et al. 2024. *AI Control: Improving Safety Despite Intentional Subversion.* https://www.alignmentforum.org/ | Supports the safety-policy category for control under possible intentional subversion |
| Irving, G., Christiano, P., & Amodei, D. 2018. *AI Safety via Debate.* arXiv:1805.00899. https://arxiv.org/abs/1805.00899 | Supports scalable oversight and adjudication framing |
| Bowman, S. R. et al. 2022. *Measuring Progress on Scalable Oversight for Large Language Models.* arXiv:2211.03540. https://arxiv.org/abs/2211.03540 | Supports oversight and human review methodology |
| Frondal, M. et al. 2025. *Petri: An Open-Source Auditing Tool to Accelerate AI Safety Research.* https://github.com/ | Supports the repository’s open-source audit-tool context |

---

## 4. Research Integrity, Reproducibility, and Auditability

These references support the repository’s reconstructability and traceability model.

| Reference | Project Use |
|---|---|
| National Academies of Sciences, Engineering, and Medicine. 2019. *Reproducibility and Replicability in Science.* The National Academies Press. https://nap.nationalacademies.org/catalog/25303/reproducibility-and-replicability-in-science | Supports the repository’s emphasis on source preservation, inspectable methods, reproducibility limits, and reviewer challenge |
| National Academies of Sciences, Engineering, and Medicine. 2019. *Reproducibility and Replicability in Science: Overview.* https://www.nationalacademies.org/projects/DBASSE-BBCSS-17-03/publication/25303 | Supports the same reproducibility and replicability framing |
| ACM. 2020. *Artifact Review and Badging.* https://www.acm.org/publications/policies/artifact-review-and-badging-current | Supports the repository’s interest in artifacts, reproducibility, and reviewability |
| Wilkinson, M. D. et al. 2016. *The FAIR Guiding Principles for Scientific Data Management and Stewardship.* *Scientific Data.* https://doi.org/10.1038/sdata.2016.18 | Supports findability, accessibility, interoperability, and reuse as data and artifact principles |
| Katz, D. S., Chue Hong, N. P., Clark, T., Muench, A., Stall, S., Bouquin, D., Cannon, M., Edmunds, S., Faez, T., Feeney, P., Fenner, M., Friedman, M., Grenier, G., Harrison, M., Heber, J., Leary, A., MacCallum, C., Murray, H., Pastrana, E., Perry, K., Schuster, D., Stockhause, M., & Yeston, J. 2021. *Recognizing the Value of Software: A Software Citation Guide.* https://doi.org/10.12688/f1000research.26932.2 | Supports software citation and research software recognition |

---

## 5. Software Citation, DOI Archival, and Repository Metadata

These references support the project’s release, citation, ORCID, and Zenodo practices.

| Reference | Project Use |
|---|---|
| Citation File Format. *Citation File Format Documentation.* https://citation-file-format.github.io/ | Supports `CITATION.cff` as the machine-readable citation metadata file |
| GitHub Docs. *About CITATION Files.* https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files | Supports GitHub-native citation display and repository citation metadata |
| Zenodo Help. *CITATION.cff File.* https://help.zenodo.org/docs/github/describe-software/citation-file/ | Supports Zenodo use of CFF metadata in GitHub-linked archival release workflows |
| Zenodo Help. *GitHub Integration.* https://help.zenodo.org/docs/github/ | Supports release-to-DOI archival logic |
| Software Heritage. *Software Heritage Identifiers.* https://docs.softwareheritage.org/devel/swh-model/persistent-identifiers.html | Supports future persistent identifier strategy for source-code archival |
| ORCID. *Works and Peer Review.* https://support.orcid.org/hc/en-us/categories/360000661673-Works-and-peer-review | Supports ORCID work-entry and citation-context decisions |

---

## 6. Schema, Validation, and Workflow Automation

These references support the repository’s machine-readable artifact contracts and validation workflow.

| Reference | Project Use |
|---|---|
| JSON Schema. *JSON Schema Documentation.* https://json-schema.org/ | Supports schema-based artifact contracts |
| JSON Schema. *JSON Schema Validation.* https://json-schema.org/draft/2020-12/json-schema-validation | Supports validation vocabulary and conformance framing |
| Python `jsonschema` Documentation. https://python-jsonschema.readthedocs.io/ | Supports the repository’s validation scripts |
| GitHub Docs. *Workflow Syntax for GitHub Actions.* https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions | Supports `.github/workflows/validate-artifacts.yml` and automated validation |
| GitHub Docs. *About GitHub Actions.* https://docs.github.com/en/actions | Supports CI workflow framing |

---

## 7. Legal, Regulatory, and Institutional Governance Context

These references are included because the repository’s governance documents discuss legal and standards-facing evidence. The repository does not claim legal compliance.

| Reference | Project Use |
|---|---|
| European Union. 2024. *Regulation (EU) 2024/1689, Artificial Intelligence Act.* EUR-Lex. https://eur-lex.europa.eu/eli/reg/2024/1689/oj | Supports the EU AI Act mapping, documentation, record-keeping, transparency, human oversight, and high-risk system analysis |
| ArtificialIntelligenceAct.eu. *High-Level Summary of the AI Act.* https://artificialintelligenceact.eu/high-level-summary/ | Secondary navigation aid for AI Act concepts, used only as a readability supplement to EUR-Lex |
| California Legislature. 2025. *SB-53, Artificial intelligence models: large developers.* https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260SB53 | Supports frontier AI framework, critical safety incident, catastrophic risk, whistleblower, transparency, and model-weight governance references |
| White House. 2025. *Removing Barriers to American Leadership in Artificial Intelligence.* https://www.whitehouse.gov/presidential-actions/2025/01/removing-barriers-to-american-leadership-in-artificial-intelligence/ | Included as current U.S. federal AI policy context |
| National Institute of Standards and Technology. *AI Risk Management Framework.* https://www.nist.gov/itl/ai-risk-management-framework | Supports U.S. voluntary AI risk management context |
| OECD. *OECD AI Principles.* https://www.oecd.org/en/topics/sub-issues/ai-principles.html | Supports international trustworthy AI principles |

---

## 8. Repository-Specific Internal References

These are internal documents and artifacts that should be cited when discussing the repository itself.

| Internal Reference | Use |
|---|---|
| `README.md` | Primary project overview and quick start |
| `RESEARCH-RATIONALE.md` | Rationale for governed research translation |
| `TRANSLATION-METHOD.md` | Method for converting sources into claims, tasks, verdicts, runs, gates, and decision summaries |
| `GOVERNANCE-MODEL.md` | Governance boundary, human authority model, refusal capacity, safety-policy intake, and audit posture |
| `TRACEABILITY.md` | Source-to-decision reconstruction model |
| `LIMITATIONS.md` | Known limitations, disclosure language, anti-overclaiming rules |
| `CITATION.cff` | Machine-readable citation metadata |
| `.zenodo.json` | Zenodo metadata override for archival release |
| `packs/README.md` | Pack structure, maturity levels, and review logic |
| `schemas/README.md` | Schema inventory and artifact contract logic |
| `scripts/README.md` | Validation order and local execution guidance |
| `docs/governance/safety-policy-intake.md` | Governance explanation of the safety-policy intake artifact |
| `packs/multi_agent_failure_modes_e0228882/safety_policy_intake.json` | Worked example of safety-policy intake and negative translation |
| `packs/multi_agent_failure_modes_e0228882/decision_summary.json` | Worked example of governed refusal |
| `docs/release/v1.1-release-notes.md` | Research-grade archival release description |
| `docs/release/v1.1.1-release-notes.md`, if added | Safety-policy intake enhancement release description |

---

## 9. Suggested Local Citation Practice

Use concise local references in major documents. Avoid turning every file into a literature review.

| Document | Recommended Citation Style |
|---|---|
| `RESEARCH-RATIONALE.md` | Cite NIST AI RMF, OECD AI Principles, National Academies reproducibility work, and CFF or Zenodo |
| `TRANSLATION-METHOD.md` | Cite NIST AI RMF Core, JSON Schema, and selected AI safety references relevant to intake |
| `GOVERNANCE-MODEL.md` | Cite NIST AI RMF Core, EU AI Act, ISO/IEC 42001, OECD AI Principles, and SB-53 where relevant |
| `TRACEABILITY.md` | Cite National Academies reproducibility, GitHub citation files, CFF, Zenodo, and JSON Schema |
| `LIMITATIONS.md` | Cite NIST AI RMF, NIST GenAI Profile, National Academies, and regulatory boundary sources |
| `docs/governance/safety-policy-intake.md` | Cite METR, Anthropic alignment faking, RAND model weights, compute governance, Seoul commitments, SB-53, and the AISST source maps |

---

## 10. Citation Boundary

These references support the repository’s design and interpretation. They do not make the repository a certified compliance system, production AI platform, legal instrument, or empirical proof of AI safety.

The strongest supported claim is narrower:

```text
Applied AI Research Translator provides a governed, schema-validated, human-gated research-to-decision artifact chain for studying how applied AI research can be translated, restricted, rejected, or authorized under audit.
```

# Safety Policy Intake Template

This folder contains the template for `safety_policy_intake.json`, the first review gate for AI safety and policy sources.

The template exists because safety and policy papers should not move directly into task design. The reviewer first has to classify the source: what risk domain it touches, what autonomy level it implies, what misuse or loss-of-control pathways it raises, and what translation boundary applies.

Use this template when creating a new pack from material that touches capability forecasting, misuse, loss of control, structural risk, compute governance, model-weight security, liability, private governance, international governance, or concentration of power.

## How to use this template

Copy `safety_policy_intake.json` into the new pack directory and replace every placeholder with source-specific information. The completed intake should answer four questions before claims become tasks:

1. What kind of source is being translated?
2. What AI safety or policy domains does it touch?
3. What operational authority should the source be allowed to have?
4. Should the pack proceed to task design, remain evaluation-only, remain policy-mapping-only, or stop for human review?

## Governance boundary

This template is not evidence. It is a drafting aid. A pack should not be described as safety-policy classified until the copied intake file is completed, validated, and reviewed by a human decision owner.

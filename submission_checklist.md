# Submission Checklist - Lab 11 / Assignment 11

## 13 TODO Coverage

| # | TODO | Status | Evidence |
|---|---|---|---|
| 1 | Write 5 adversarial prompts | Implemented | [src/attacks/attacks.py](src/attacks/attacks.py) |
| 2 | Generate attack test cases with AI | Implemented | [src/attacks/attacks.py](src/attacks/attacks.py) |
| 3 | Injection detection (regex) | Implemented | [src/guardrails/input_guardrails.py](src/guardrails/input_guardrails.py) |
| 4 | Topic filter | Implemented | [src/guardrails/input_guardrails.py](src/guardrails/input_guardrails.py) |
| 5 | Input Guardrail Plugin | Implemented | [src/guardrails/input_guardrails.py](src/guardrails/input_guardrails.py) |
| 6 | Content filter (PII, secrets) | Implemented | [src/guardrails/output_guardrails.py](src/guardrails/output_guardrails.py) |
| 7 | LLM-as-Judge safety check | Implemented | [src/guardrails/output_guardrails.py](src/guardrails/output_guardrails.py) |
| 8 | Output Guardrail Plugin | Implemented | [src/guardrails/output_guardrails.py](src/guardrails/output_guardrails.py) |
| 9 | NeMo Guardrails Colang config | Implemented | [src/guardrails/nemo_guardrails.py](src/guardrails/nemo_guardrails.py) |
| 10 | Rerun 5 attacks with guardrails | Implemented | [src/testing/testing.py](src/testing/testing.py) |
| 11 | Automated security testing pipeline | Implemented | [src/testing/testing.py](src/testing/testing.py), [src/testing/defense_pipeline.py](src/testing/defense_pipeline.py) |
| 12 | Confidence Router | Implemented | [src/hitl/hitl.py](src/hitl/hitl.py) |
| 13 | Design 3 HITL decision points | Implemented | [src/hitl/hitl.py](src/hitl/hitl.py) |

## Deliverables Checklist

### Part A - Notebook / Code

- End-to-end runnable `.ipynb` or `.py`: Yes, via [src/main.py](src/main.py)
- Rate Limiter output shown: Yes, in economy run output and [src/testing/defense_pipeline.py](src/testing/defense_pipeline.py)
- Input Guardrails output shown: Yes, in economy run output and [src/guardrails/input_guardrails.py](src/guardrails/input_guardrails.py)
- Output Guardrails output shown: Yes, in economy run output and [src/guardrails/output_guardrails.py](src/guardrails/output_guardrails.py)
- LLM-as-Judge output shown: Implemented, but economy mode skips live judge calls to avoid quota
- `audit_log.json` with at least 20 entries: Yes, [src/audit_log.json](src/audit_log.json) has 32 entries
- Clear comments/docstrings for functions and classes: Mostly yes; core functions/classes are documented in code

### Part B - Individual Report

- 1-2 page Markdown/PDF report: Yes, [individual_report_economy.md](individual_report_economy.md)
- Layer analysis table for Test 2: Yes
- False positive analysis: Yes
- 3 gap-analysis prompts: Yes
- Production readiness discussion: Yes
- Ethical reflection: Yes

## Notes

- The economy mode is designed to complete the deliverables locally without requiring additional Gemini quota.
- If you need a live LLM-as-Judge screenshot/output for grading, rerun Part 2B or Part 3 in non-economy mode when quota is available.
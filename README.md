# Ngày 11 - Guardrails, HITL & Trí tuệ nhân tạo có trách nhiệm

Ngày 11 — Guardrails, HITL & Trí tuệ nhân tạo có trách nhiệm: Làm thế nào để làm cho các ứng dụng AI agent an toàn?

## Mục tiêu

- Hiểu tại sao guardrails là bắt buộc đối với các sản phẩm AI
- Triển khai input guardrails (phát hiện tiêm injection, bộ lọc chủ đề)
- Triển khai output guardrails (bộ lọc nội dung, LLM-as-Judge)
- Sử dụng NeMo Guardrails (NVIDIA) với Colang
- Thiết kế quy trình HITL với định tuyến dựa trên độ tin cậy
- Thực hiện kiểm tra an niệm cơ bản

## Cấu trúc dự án

```
Day-11-Guardrails-HITL-Responsible-AI/
├── notebooks/
│   ├── lab11_guardrails_hitl.ipynb            # Phòng lab sinh viên (Colab)
│   └── lab11_guardrails_hitl_solution.ipynb   # Giải pháp (chỉ hướng dẫn viên)
├── src/                                       # Phiên bản Python cục bộ
│   ├── main.py                    # Điểm vào — chạy tất cả hoặc chọn một phần
│   ├── core/
│   │   ├── config.py              # Thiết lập khóa API, chủ đề được phép/bị chặn
│   │   └── utils.py               # Trợ giúp chat_with_agent()
│   ├── agents/
│   │   └── agent.py               # Tạo agent không an toàn & được bảo vệ
│   ├── attacks/
│   │   └── attacks.py             # TODO 1-2: Các lời nhắc đối kháng & kiểm tra nhóm đỏ AI
│   ├── guardrails/
│   │   ├── input_guardrails.py    # TODO 3-5: Phát hiện injection, bộ lọc chủ đề, plugin
│   │   ├── output_guardrails.py   # TODO 6-8: Bộ lọc nội dung, LLM-as-Judge, plugin
│   │   └── nemo_guardrails.py     # TODO 9: NeMo Guardrails với Colang
│   ├── testing/
│   │   └── testing.py             # TODO 10-11: So sánh trước/sau, pipeline
│   └── hitl/
│       └── hitl.py                # TODO 12-13: Bộ định tuyến độ tin cậy, thiết kế HITL
├── requirements.txt
└── README.md
```

## Thiết lập

### Cấu hình cục bộ (Python modules — không cần Colab)

```bash
cd src/
pip install -r ../requirements.txt
export OPENAI_API_KEY="your-api-key-here"

# Chạy phòng lab đầy đủ
python main.py

# Hoặc chạy các phần cụ thể
python main.py --part 1    # Phần 1: Các cuộc tấn công
python main.py --part 2    # Phần 2: Guardrails
python main.py --part 3    # Phần 3: Pipeline kiểm tra
python main.py --part 4    # Phần 4: Thiết kế HITL

# Hoặc kiểm tra các mô-đun riêng lẻ
python guardrails/input_guardrails.py
python guardrails/output_guardrails.py
python testing/testing.py
python hitl/hitl.py
```

### Công cụ được sử dụng

- **OpenAI API** — ChatGPT backend (gpt-4-turbo)
- **NeMo Guardrails** — Khung công việc NVIDIA với Colang (quy tắc an toàn khai báo)

## Cấu trúc phòng lab (2,5 giờ)

| Part | Content | Duration |
|------|---------|----------|
| Part 1 | Attack unprotected agent + AI red teaming | 30 min |
| Part 2A | Implement input guardrails (injection, topic filter) | 20 min |
| Part 2B | Implement output guardrails (content filter, LLM-as-Judge) | 20 min |
| Part 2C | NeMo Guardrails with Colang (NVIDIA) | 20 min |
| Part 3 | Before/after comparison + automated testing pipeline | 30 min |
| Part 4 | Design HITL workflow | 30 min |

## Deliverables

1. **Security Report**: Before/after comparison of 5+ attacks (ADK + NeMo)
2. **HITL Flowchart**: 3 decision points with escalation paths

## 13 TODOs

| # | Description | Framework |
|---|-------------|-----------|
| 1 | Write 5 adversarial prompts | - |
| 2 | Generate attack test cases with AI | Gemini |
| 3 | Injection detection (regex) | Python |
| 4 | Topic filter | Python |
| 5 | Input Guardrail Plugin | Google ADK |
| 6 | Content filter (PII, secrets) | Python |
| 7 | LLM-as-Judge safety check | Gemini |
| 8 | Output Guardrail Plugin | Google ADK |
| 9 | NeMo Guardrails Colang config | NeMo |
| 10 | Rerun 5 attacks with guardrails | Google ADK |
| 11 | Automated security testing pipeline | Python |
| 12 | Confidence Router (HITL) | Python |
| 13 | Design 3 HITL decision points | Design |

## References

- [OWASP Top 10 for LLM](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails)
- [Google ADK Documentation](https://google.github.io/adk-docs/)
- [Official Google's Gemini cookbook](https://github.com/google-gemini/cookbook/blob/main/examples/gemini_google_adk_model_guardrails.ipynb)
- [AI Safety Fundamentals](https://aisafetyfundamentals.com/)
- [AI Red Teaming Guide](https://github.com/requie/AI-Red-Teaming-Guide)
- [antoan.ai - AI Safety Vietnam](https://antoan.ai)


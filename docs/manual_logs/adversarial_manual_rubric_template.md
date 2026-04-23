# Manual Rubric Template (Adversarial Evaluation)

Filled with manual labels and notes from run outputs.

| query_id | mode | run | auto_label | manual_label(correct/partial/incorrect) | notes |
|---|---|---:|---|---|---|
| r11_pdf_failure_nhf_invoice | rag | 1 | incorrect | incorrect | Abstains; required factual values are not provided. |
| r11_pdf_failure_nhf_invoice | pure_llm | 1 | incorrect | incorrect | Unsupported or generic answer; required facts missing. |
| r11_pdf_failure_nhf_invoice | rag | 2 | incorrect | incorrect | Abstains; required factual values are not provided. |
| r11_pdf_failure_nhf_invoice | pure_llm | 2 | incorrect | incorrect | Unsupported or generic answer; required facts missing. |
| r11_pdf_failure_nhf_invoice | rag | 3 | incorrect | incorrect | Abstains; required factual values are not provided. |
| r11_pdf_failure_nhf_invoice | pure_llm | 3 | incorrect | incorrect | Unsupported or generic answer; required facts missing. |
| r12_pdf_failure_dacf_btas | rag | 1 | incorrect | incorrect | Unsupported or generic answer; required facts missing. |
| r12_pdf_failure_dacf_btas | pure_llm | 1 | incorrect | incorrect | Unsupported or generic answer; required facts missing. |
| r12_pdf_failure_dacf_btas | rag | 2 | incorrect | incorrect | Unsupported or generic answer; required facts missing. |
| r12_pdf_failure_dacf_btas | pure_llm | 2 | incorrect | incorrect | Unsupported or generic answer; required facts missing. |
| r12_pdf_failure_dacf_btas | rag | 3 | incorrect | incorrect | Unsupported or generic answer; required facts missing. |
| r12_pdf_failure_dacf_btas | pure_llm | 3 | incorrect | incorrect | Unsupported or generic answer; required facts missing. |
| r13_pdf_failure_appendix_7b | rag | 1 | incorrect | incorrect | Abstains; required factual values are not provided. |
| r13_pdf_failure_appendix_7b | pure_llm | 1 | partial | partial | Contains some required facts but misses key details. |
| r13_pdf_failure_appendix_7b | rag | 2 | partial | partial | Contains some required facts but misses key details. |
| r13_pdf_failure_appendix_7b | pure_llm | 2 | partial | partial | Contains some required facts but misses key details. |
| r13_pdf_failure_appendix_7b | rag | 3 | incorrect | incorrect | Abstains; required factual values are not provided. |
| r13_pdf_failure_appendix_7b | pure_llm | 3 | partial | partial | Contains some required facts but misses key details. |
| r14_pdf_failure_ten_output | rag | 1 | correct | correct | Contains required key facts for this query. |
| r14_pdf_failure_ten_output | pure_llm | 1 | partial | partial | Contains some required facts but misses key details. |
| r14_pdf_failure_ten_output | rag | 2 | correct | correct | Contains required key facts for this query. |
| r14_pdf_failure_ten_output | pure_llm | 2 | partial | partial | Contains some required facts but misses key details. |
| r14_pdf_failure_ten_output | rag | 3 | correct | correct | Contains required key facts for this query. |
| r14_pdf_failure_ten_output | pure_llm | 3 | partial | partial | Contains some required facts but misses key details. |
| r15_csv_failure_ga_shortform | rag | 1 | incorrect | incorrect | Unsupported or generic answer; required facts missing. |
| r15_csv_failure_ga_shortform | pure_llm | 1 | incorrect | incorrect | Unsupported or generic answer; required facts missing. |
| r15_csv_failure_ga_shortform | rag | 2 | incorrect | incorrect | Unsupported or generic answer; required facts missing. |
| r15_csv_failure_ga_shortform | pure_llm | 2 | incorrect | incorrect | Unsupported or generic answer; required facts missing. |
| r15_csv_failure_ga_shortform | rag | 3 | incorrect | incorrect | Abstains; required factual values are not provided. |
| r15_csv_failure_ga_shortform | pure_llm | 3 | incorrect | incorrect | Unsupported or generic answer; required facts missing. |
| r16_csv_failure_ndc_shortform | rag | 1 | correct | correct | Contains required key facts for this query. |
| r16_csv_failure_ndc_shortform | pure_llm | 1 | partial | partial | Contains some required facts but misses key details. |
| r16_csv_failure_ndc_shortform | rag | 2 | correct | correct | Contains required key facts for this query. |
| r16_csv_failure_ndc_shortform | pure_llm | 2 | partial | partial | Contains some required facts but misses key details. |
| r16_csv_failure_ndc_shortform | rag | 3 | correct | correct | Contains required key facts for this query. |
| r16_csv_failure_ndc_shortform | pure_llm | 3 | partial | partial | Contains some required facts but misses key details. |

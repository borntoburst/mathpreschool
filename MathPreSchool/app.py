import os
import streamlit as st
from models.section_config import SectionConfig
from models.config import WorksheetConfig

from generators.counting import CountingGenerator
from generators.missing_number import MissingNumberGenerator
from generators.comparison import ComparisonGenerator
from generators.pattern import PatternGenerator
from generators.multistep import MultiStepGenerator

from core.worksheet_builder import WorksheetBuilder

from exporters.pdf_exporter import PDFExporter
from exporters.answer_exporter import AnswerExporter

os.makedirs("output", exist_ok=True)

st.set_page_config(
    page_title="MathPreSchool",
    layout="wide"
)

st.title("🧮 MathPreSchool Worksheet Generator")

# ===========================
# CONFIG
# ===========================

min_number = st.number_input(
    "Min Number",
    min_value=0,
    value=0
)

max_number = st.number_input(
    "Max Number",
    min_value=10,
    value=100
)

finger_limit = st.number_input(
    "Finger Limit",
    min_value=5,
    max_value=10,
    value=10
)

# ===========================
# GENERATE
# ===========================

if st.button("Generate Worksheet"):

    config = WorksheetConfig(
        min_number=min_number,
        max_number=max_number,
        finger_limit=finger_limit
    )

    sections = [
        SectionConfig(title="CÂU 1. ĐẾM THÊM - ĐẾM BỚT",generator=CountingGenerator(),count=config.q1_count,priority=5,color="#4CAF50"),
        SectionConfig(title="CÂU 2. ĐIỀN SỐ CÒN THIẾU",generator=MissingNumberGenerator(),count=config.q2_count,priority=5,color="#2196F3"),
        SectionConfig(title="CÂU 3. SO SÁNH",generator=ComparisonGenerator(),count=config.q3_count,priority=4,color="#FFC107"),
        SectionConfig(title="CÂU 4. TÌM QUY LUẬT",generator=PatternGenerator(),count=config.q4_count,priority=3,color="#9C27B0"),
        SectionConfig(title="CÂU 5. TÍNH NHIỀU BƯỚC",generator=MultiStepGenerator(),count=config.q5_count,priority=4,color="#FF5722")
    ]

    # ===========================
    # BUILD WORKSHEET
    # ===========================

    builder = WorksheetBuilder(sections)
    worksheet_data, all_answers = builder.build(config)

    # ===========================
    # PREVIEW
    # ===========================
    print(type(section))
    print(section)
    for section in worksheet_data:
        st.subheader(section["title"])
        for q in section["questions"]:
            st.write(q.text)

    # ===========================
    # ANSWER KEY
    # ===========================

    st.divider()

    st.header("Answer Key")

    for item in all_answers:

        st.write(
            f'{item["question"]} → {item["answer"]}'
        )

    # ===========================
    # EXPORT PDF
    # ===========================

    worksheet_pdf = "output/mathpreschool_worksheet.pdf"
    answer_pdf = "output/mathpreschool_answers.pdf"

    PDFExporter().export(
        worksheet_pdf,
        worksheet_data
    )

    AnswerExporter().export(
        answer_pdf,
        all_answers
    )

    # ===========================
    # DOWNLOAD
    # ===========================

    col1, col2 = st.columns(2)

    with col1:

        with open(worksheet_pdf, "rb") as file:

            st.download_button(
                label="📄 Download Worksheet",
                data=file,
                file_name="mathpreschool_worksheet.pdf",
                mime="application/pdf"
            )

    with col2:

        with open(answer_pdf, "rb") as file:

            st.download_button(
                label="✅ Download Answer Key",
                data=file,
                file_name="mathpreschool_answers.pdf",
                mime="application/pdf"
            )

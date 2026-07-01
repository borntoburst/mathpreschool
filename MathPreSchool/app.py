import streamlit as st
import os

os.makedirs("output", exist_ok=True)
from exporters.pdf_exporter import PDFExporter
from exporters.answer_exporter import AnswerExporter
from models.config import WorksheetConfig
from utils.uniqueness import UniqueQuestionGenerator
from generators.counting import CountingGenerator
from generators.missing_number import MissingNumberGenerator
from generators.comparison import ComparisonGenerator
from generators.pattern import PatternGenerator
from generators.multistep import MultiStepGenerator

unique_checker = UniqueQuestionGenerator()
st.title("MathPreSchool Worksheet Generator")

min_number = st.number_input(
    "Min Number",
    value=0
)

max_number = st.number_input(
    "Max Number",
    value=100
)

finger_limit = st.number_input(
    "Finger Limit",
    value=10
)

if st.button("Generate"):

    config = WorksheetConfig(
        min_number=min_number,
        max_number=max_number,
        finger_limit=finger_limit
    )

    generators = [
        (
            "CÂU 1. ĐẾM THÊM - ĐẾM BỚT",
            CountingGenerator(),
            config.q1_count
        ),
    
        (
            "CÂU 2. ĐIỀN SỐ CÒN THIẾU",
            MissingNumberGenerator(),
            config.q2_count
        ),
    
        (
            "CÂU 3. SO SÁNH",
            ComparisonGenerator(),
            config.q3_count
        ),
    
        (
            "CÂU 4. TÌM QUY LUẬT",
            PatternGenerator(),
            config.q4_count
        ),
    
        (
            "CÂU 5. TÍNH NHIỀU BƯỚC",
            MultiStepGenerator(),
            config.q5_count
        )
    ]

    answers = []
    worksheet_data = []
    all_answers = []

    for title, gen, count in generators:

        st.subheader(title)
        section_questions = []
        for _ in range(count):

            while True:

                q = gen.generate(config)
            
                if unique_checker.add(q.text):
                    break

            st.write(q.text)
            section_questions.append(q)
            
            all_answers.append({
                "question": q.text,
                "answer": q.answer
            })
        worksheet_data.append({
            "title": title,
            "questions": section_questions
        })
    st.divider()
    st.subheader("Answer Key")

    for item in all_answers:

        st.write(
            f"{item['question']} → {item['answer']}"
        )

    for q,a in answers:
        st.write(
            f"{q} → {a}"
        )

    pdf_exporter = PDFExporter()

    pdf_exporter.export(
        "output/mathpreschool_worksheet.pdf",
        worksheet_data
    )

    answer_exporter = AnswerExporter()

    answer_exporter.export(
        "output/mathpreschool_answers.pdf",
        all_answers
    )

    with open(
        "output/mathpreschool_worksheet.pdf",
        "rb"
    ) as file:

        st.download_button(
            "Download Worksheet PDF",
            file,
            file_name="mathpreschool_worksheet.pdf"
        )

    with open(
        "output/mathpreschool_answers.pdf",
        "rb"
    ) as file:

        st.download_button(
            "Download Answer PDF",
            file,
            file_name="mathpreschool_answers.pdf"
        )

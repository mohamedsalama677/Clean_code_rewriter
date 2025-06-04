# tasks/agent_tasks.py
from crewai import Task

def analysis_task(agent, code):
    return Task(
        description=f"""
        Analyze the provided {code} for clean code violations 
        using Robert C. Martin's Clean Code principles. Identify issues such as poor naming conventions, complex logic, and lack of comments.
        Provide a structured analysis report with identified issues and suggestions for the generator agent and educator agent.
    """,
        expected_output="A detailed analysis report identifying specific Clean Code violations with locations and descriptions.",
        agent=agent
    )


def create_refactoring_task(agent, code):
    return Task(
        description=f"""Refactor the {code} based on the analysis report to improve its quality.
          But keep the original as it does not change the functionality.
          
          """,
        expected_output="Complete refactored code that addresses all identified issues while preserving functionality.",
        agent=agent,
        dependencies=[analysis_task]
    )

def create_education_task(agent, code):
    return Task(
        description=f"""Provide educational content about the identified issues from the analysis report.
        but provide the content based on the analysis report only that provided according to {code}.
        provide the lessons after the refactoring task is completed, and the generated code is provided.""",
        # This task does not depend on the analysis task, as it is meant to provide general clean code lessons
        expected_output="""
        1- **output code of the refactoring task**
        2- Educational content explaining Clean Code principles and best practices relevant to the analyzed code.
        """,
        agent=agent,
        dependencies=[analysis_task]
    )

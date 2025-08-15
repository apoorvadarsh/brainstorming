from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import SerperDevTool
from typing import List


@CrewBase
class ArticleWriter():
    """ArticleWriter crew"""

    agents: List[BaseAgent]
    tasks: List[Task]


    @agent
    def junior_developer(self) -> Agent:
        return Agent(
            config=self.agents_config['junior_developer'], # type: ignore[index]
            verbose=True
        )

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'], # type: ignore[index]
            verbose=True,
            tools=[SerperDevTool()]
        )

    @agent
    def senior_developer(self) -> Agent:
        return Agent(
            config=self.agents_config['senior_developer'], # type: ignore[index]
            verbose=True,
            tools=[SerperDevTool()]
        )

    @agent
    def visionary(self) -> Agent:
        return Agent(
            config=self.agents_config['visionary'], # type: ignore[index]
            verbose=True,
            tools=[SerperDevTool()]
        )

    @task
    def junior_developer_task(self) -> Task:
        return Task(
            config=self.tasks_config['junior_developer_task']
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'], # type: ignore[index]
        )

    @task
    def senior_developer_task(self) -> Task:
        return Task(
            config=self.tasks_config['senior_developer_task'], # type: ignore[index]
        )

    @task
    def visionary_task(self) -> Task:
        return Task(
            config=self.tasks_config['visionary_task'], # type: ignore[index]
            output_file= "./output/ideas.md"
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Resercher crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            output_file="./output/ideas.md"
        )
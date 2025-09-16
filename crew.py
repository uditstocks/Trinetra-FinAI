import os
from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
	FileReadTool,
	SerperDevTool
)





@CrewBase
class LocalAiFinancialAnalysisSystemCrew:
    """LocalAiFinancialAnalysisSystem crew"""

    
    @agent
    def comprehensive_financial_data_analyst(self) -> Agent:
        
        return Agent(
            config=self.agents_config["comprehensive_financial_data_analyst"],
            
            
            tools=[
				FileReadTool(),
				FileReadTool()
            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model='ollama/llama3.2:1b',
                temperature=0.7,
            ),
        )
    
    @agent
    def comprehensive_financial_health_change_analyst(self) -> Agent:
        
        return Agent(
            config=self.agents_config["comprehensive_financial_health_change_analyst"],
            
            
            tools=[
				SerperDevTool()
            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="ollama/llama3.2:1b",
                temperature=0.7,
            ),
        )
    
    @agent
    def investment_research_market_analyst(self) -> Agent:
        
        return Agent(
            config=self.agents_config["investment_research_market_analyst"],
            
            
            tools=[
				SerperDevTool()
            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model='ollama/llama3.2:1b',
                temperature=0.7,
            ),
        )
    
    @agent
    def udit(self) -> Agent:
        
        return Agent(
            config=self.agents_config["udit"],
            
            
            tools=[
				SerperDevTool()
            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model='ollama/llama3.2:1b',
                temperature=0.7,
            ),
        )
    
    @agent
    def strategic_financial_report_writer(self) -> Agent:
        
        return Agent(
            config=self.agents_config["strategic_financial_report_writer"],
            
            
            tools=[
				SerperDevTool()
            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model='ollama/llama3.2:1b',
                temperature=0.7,
            ),
        )
    














    
    @task
    def comprehensive_financial_data_extraction_and_analysis(self) -> Task:
        return Task(
            config=self.tasks_config["comprehensive_financial_data_extraction_and_analysis"],
            markdown=False,
        )
    
    @task
    def comprehensive_financial_health_change_analysis(self) -> Task:
        return Task(
            config=self.tasks_config["comprehensive_financial_health_change_analysis"],
            markdown=False,
        )
    
    @task
    def phase_1_udit_s_data_extraction_delegation_review(self) -> Task:
        return Task(
            config=self.tasks_config["phase_1_udit_s_data_extraction_delegation_review"],
            markdown=False,
        )
    
    @task
    def competitive_market_analysis_investment_valuation(self) -> Task:
        return Task(
            config=self.tasks_config["competitive_market_analysis_investment_valuation"],
            markdown=False,
        )
    
    @task
    def phase_2_udit_s_financial_health_analysis_delegation_review(self) -> Task:
        return Task(
            config=self.tasks_config["phase_2_udit_s_financial_health_analysis_delegation_review"],
            markdown=False,
        )
    
    @task
    def phase_3_udit_s_market_analysis_delegation_review(self) -> Task:
        return Task(
            config=self.tasks_config["phase_3_udit_s_market_analysis_delegation_review"],
            markdown=False,
        )
    
    @task
    def phase_4_udit_s_strategic_report_creation_delegation(self) -> Task:
        return Task(
            config=self.tasks_config["phase_4_udit_s_strategic_report_creation_delegation"],
            markdown=False,
        )
    
    @task
    def phase_5_strategic_investment_report_creation(self) -> Task:
        return Task(
            config=self.tasks_config["phase_5_strategic_investment_report_creation"],
            markdown=False,
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the LocalAiFinancialAnalysisSystem crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )

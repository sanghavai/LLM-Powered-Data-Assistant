from langchain.agents import initialize_agent, Tool, AgentExecutor
from langchain.agents.agent_types import AgentType
from utils.llm_utils import get_mistral_llm
from utils.pandas_data_tool import PandasDataTool

def create_agent(df):
    llm = get_mistral_llm()
    pandas_tool = PandasDataTool(df=df)

    tools = [
        Tool(
            name=pandas_tool.name,
            func=pandas_tool._run,  # use _run method, not run
            description=pandas_tool.description
        )
    ]

    # Initialize the agent executor normally (verbose=True for debugging)
    base_agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    # Wrap base agent in AgentExecutor with parsing error handling enabled
    agent_executor = AgentExecutor.from_agent_and_tools(
        agent=base_agent.agent,  # low-level agent inside
        tools=tools,
        handle_parsing_errors=True,
        verbose=True
    )

    return agent_executor

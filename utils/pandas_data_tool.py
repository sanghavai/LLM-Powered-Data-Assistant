from langchain.tools import BaseTool
import pandas as pd
from pydantic import BaseModel, Field

class PandasDataTool(BaseTool, BaseModel):
    name: str = "pandas_data_tool"
    description: str = "Useful for running python code on the pandas DataFrame."
    df: pd.DataFrame = Field(..., exclude=True)

    def _run(self, query: str) -> str:
        try:
            local_vars = {"df": self.df, "pd": pd}
            result = eval(query, {}, local_vars)
            return str(result)
        except Exception as e:
            return f"Error running query: {e}"

    async def _arun(self, query: str) -> str:
        raise NotImplementedError("Async not implemented.")

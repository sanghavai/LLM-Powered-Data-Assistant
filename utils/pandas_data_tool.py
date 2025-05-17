from langchain.tools import BaseTool
import pandas as pd
from pydantic import BaseModel, Field

class PandasDataTool(BaseTool, BaseModel):
    name: str = "pandas_data_tool"
    description: str = "Use this tool to run safe Python pandas code on the uploaded DataFrame."
    df: pd.DataFrame = Field(..., exclude=True)

    def _run(self, query: str) -> str:
        try:
            # Simple unsafe keyword check
            unsafe_keywords = ["import", "open(", "os.", "sys.", "eval", "exec", "__"]
            if any(kw in query for kw in unsafe_keywords):
                return "❌ Rejected: Unsafe code detected."

            # Evaluate code safely
            local_vars = {"df": self.df, "pd": pd}
            result = eval(query, {"__builtins__": {}}, local_vars)

            return str(result)
        except Exception as e:
            return f"❌ Error running query: {e}"

    async def _arun(self, query: str) -> str:
        raise NotImplementedError("Async not supported.")

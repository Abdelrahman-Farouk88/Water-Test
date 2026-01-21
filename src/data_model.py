from pydantic import BaseModel

class Water(BaseModel):
    ph: float
    Hardness: float
    Solids: float
    Chloramines: float
    Conductivity: float
    Sulfate: float
    Organic_carbon: float
    Trihalomethanes: float
    Turbidity: float    
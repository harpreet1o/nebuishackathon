import json

from app.models.schema import TargetSchema
from app.profiler.profile import profile_dataframe
from app.profiler.profile import load_excel

def main():
    with open("schemas/velocity.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    target_schema = TargetSchema.model_validate(data)

    print("Target Schema")
    # Load messy Excel file
    df = load_excel("data/input/Book1.xlsx")

    # Profile the messy data
    profile = profile_dataframe(df)
    print("Data Profile")
    print("------------")
    print(profile)

if __name__ == "__main__":
    main()
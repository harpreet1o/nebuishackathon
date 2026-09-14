import json

from app.schema import TargetSchema


def main():
    with open("schemas/velocity.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    target_schema = TargetSchema.model_validate(data)

    print("Target Schema")
    print("-------------")

    for field in target_schema.fields:
        print(
            f"{field.name} | "
            f"type={field.type} | "
            f"required={field.required}"
        )


if __name__ == "__main__":
    main()
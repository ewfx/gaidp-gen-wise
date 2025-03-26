with open("trainmodel.py", "r", encoding="utf-8") as file:
    content = file.read()

# Remove non-breaking spaces and other non-printable characters
cleaned_content = content.replace("\u00A0", " ")

with open("trainmodel.py", "w", encoding="utf-8") as file:
    file.write(cleaned_content)

print("File cleaned successfully!")
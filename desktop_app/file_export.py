import csv
from prettytable import PrettyTable
from desktop_app.repository import get_all_contacts

def export_contacts_to_csv(file_path):
    contacts = get_all_contacts()
    try:
        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['First name', 'Last name', 'Phone', 'Email'])
            for contact in contacts:
                writer.writerow([
                    contact.first_name,
                    contact.last_name,
                    contact.phone,
                    contact.email,
                ])
            print(f"Contacts exported to {file_path}")
    except(IOError, PermissionError) as e:
        print(f"Error exporting to {file_path}: {e}")

def export_contacts_to_txt(file_path):
    contacts = get_all_contacts()
    table = PrettyTable()
    table.field_names = ["First name", "Last name", "Phone", "Email"]
    try:
        for contact in contacts:
            table.add_row([
                contact.first_name,
                contact.last_name,
                contact.phone,
                contact.email,
            ])
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(str(table))
        print(f"Contacts exported to {file_path}")
    except(IOError, PermissionError) as e:
        print(f"Error exporting to {file_path}: {e}")

def export_contacts_to_md(filepath="contacts_export.md"):
    contacts = get_all_contacts()
    with open(filepath, "w", encoding="utf-8") as file:
        file.write("| First Name | Last Name | Phone | Email |\n")
        file.write("|------------|-----------|-------|-------|\n")
        for c in contacts:
            file.write(f"| {c.first_name} | {c.last_name} | {c.phone} | {c.email or ''} |\n")
    print(f"Exported to {filepath}")
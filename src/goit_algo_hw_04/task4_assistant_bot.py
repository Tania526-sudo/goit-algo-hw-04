# src/goit_algo_hw_04/task4_assistant_bot.py
from typing import Tuple, Dict

Contacts = Dict[str, str]

def parse_input(user_input: str) -> Tuple[str, list[str]]:
    cmd, *args = user_input.split()
    return cmd.strip().lower(), args

def add_contact(args: list[str], contacts: Contacts) -> str:
    if len(args) != 2:
        return "Usage: add <name> <phone>"
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args: list[str], contacts: Contacts) -> str:
    if len(args) != 2:
        return "Usage: change <name> <new_phone>"
    name, phone = args
    if name not in contacts:
        return "Contact not found."
    contacts[name] = phone
    return "Contact updated."

def show_phone(args: list[str], contacts: Contacts) -> str:
    if len(args) != 1:
        return "Usage: phone <name>"
    name = args[0]
    return contacts.get(name, "Contact not found.")

def show_all(_: list[str], contacts: Contacts) -> str:
    if not contacts:
        return "No contacts."
    lines = [f"{name}: {phone}" for name, phone in contacts.items()]
    return "\n".join(lines)

def main() -> None:
    contacts: Contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ("close", "exit"):
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

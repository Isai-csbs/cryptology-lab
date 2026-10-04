# Metasploit Framework - Safe Workflow Simulation
# Purpose: Demonstrate basic Metasploit commands for educational use.
# This program does NOT execute exploits or connect to real targets.

def show_help():
    print("\n========== METASPLOIT HELP ==========")
    print("search  -> Search modules")
    print("info    -> Display module information")
    print("show    -> Display available options/items")
    print("back    -> Return from selected module")
    print("exit    -> Exit Metasploit")
    print("=====================================")


def search_modules():
    print("\n========== WINDOWS EXPLOIT MODULES ==========")
    modules = [
        "exploit/windows/example/example_module",
        "exploit/windows/http/example_module",
        "exploit/windows/smb/example_module",
        "exploit/windows/fileformat/example_module"
    ]

    for i, module in enumerate(modules, 1):
        print(f"{i}. {module}")

    return modules


def show_module_info(module):
    print("\n========== MODULE INFORMATION ==========")
    print("Module Name :", module)
    print("Description : Example Windows vulnerability module")
    print("Platform    : Windows")
    print("Targets     : Authorized test systems only")
    print("References  : Security vulnerability documentation")
    print("Purpose     : Educational vulnerability assessment")
    print("========================================")


def show_options():
    print("\n========== MODULE OPTIONS ==========")
    print("RHOSTS  -> Remote host(s) to be assessed")
    print("RPORT   -> Remote service port")
    print("TARGET  -> Target type")
    print("\nNote: No real target is configured or contacted.")
    print("===================================")


def main():
    print("==============================================")
    print("     METASPLOIT FRAMEWORK STUDY SIMULATION")
    print("==============================================")

    print("\nStep 1 — Open Terminal")
    print("Terminal opened successfully.")

    print("\nStep 2 — Start Metasploit")
    print("Command: msfconsole")
    print("msf6 >")

    while True:
        print("\n----------------------------------------------")
        print("1. help")
        print("2. search type:exploit platform:windows")
        print("3. info <module-name>")
        print("4. show options")
        print("5. back")
        print("6. exit")
        print("----------------------------------------------")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_help()

        elif choice == "2":
            modules = search_modules()

        elif choice == "3":
            module_name = input(
                "\nEnter module name for inspection: "
            )

            if module_name.strip():
                show_module_info(module_name)
            else:
                print("No module selected.")

        elif choice == "4":
            show_options()

        elif choice == "5":
            print("\nReturned to the main Metasploit console.")
            print("msf6 >")

        elif choice == "6":
            print("\nStep 10 — Exit")
            print("Metasploit study session terminated.")
            print("\nStep 12 — Exit Metasploit")
            print("Step 13 — Stop the experiment.")
            break

        else:
            print("Invalid choice. Please select 1 to 6.")

    print("\n========== RESULT ==========")
    print("Metasploit Framework workflow was studied successfully.")
    print("Windows exploit modules were simulated and inspected.")
    print("Module information and options were examined.")
    print("No real target was configured or attacked.")
    print("============================")


if __name__ == "__main__":
    main()

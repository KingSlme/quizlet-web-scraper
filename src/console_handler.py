from colorama import Fore, Style
from scraper import get_content
import file_handler


def display_logo():
    print(Fore.LIGHTBLUE_EX, end="")
    print("---------------------------------------------------")
    print("|                Quizlet Web Scraper              |")
    print(r"| https://github.com/KingSlme/quizlet-web-scraper |")
    print("---------------------------------------------------")
    print(Style.RESET_ALL)


def get_output_option():
    print(f"{Fore.LIGHTBLUE_EX}Output to File?{Style.RESET_ALL}")
    print(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}Y{Fore.WHITE}]{Style.RESET_ALL}")
    print(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}N{Fore.WHITE}]{Style.RESET_ALL}")

    response = input(f"{Fore.LIGHTYELLOW_EX}->{Fore.WHITE} ")
    if response.lower() not in ["y", "n"]:
        print(f"{Fore.LIGHTRED_EX}{response} is not a valid choice!{Style.RESET_ALL}\n")
        return get_output_option()
    return response.lower()


def get_verbose_option():
    print(f"{Fore.LIGHTBLUE_EX}Verbose?{Style.RESET_ALL}")
    print(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}Y{Fore.WHITE}]{Style.RESET_ALL}")
    print(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}N{Fore.WHITE}]{Style.RESET_ALL}")

    response = input(f"{Fore.LIGHTYELLOW_EX}->{Fore.WHITE} ")
    if response.lower() not in ["y", "n"]:
        print(f"{Fore.LIGHTRED_EX}{response} is not a valid choice!{Style.RESET_ALL}\n")
        return get_output_option()
    return response.lower()


def get_file_name():
    print(f"{Fore.LIGHTBLUE_EX}Name for Output File?{Style.RESET_ALL}")

    response = input(f"{Fore.LIGHTYELLOW_EX}->{Fore.WHITE} ")
    if not file_handler.check_valid_file_name(response):
        print(f"{Fore.LIGHTRED_EX}Invalid File Name{Style.RESET_ALL}\n")
        return get_file_name()
    return file_handler.construct_file_name(response)


def get_custom_user_agent_option():
    print(f"{Fore.LIGHTBLUE_EX}Custom User Agent?{Style.RESET_ALL}")
    print(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}Y{Fore.WHITE}]{Style.RESET_ALL}")
    print(f"{Fore.WHITE}[{Fore.LIGHTGREEN_EX}N{Fore.WHITE}]{Style.RESET_ALL}")

    response = input(f"{Fore.LIGHTYELLOW_EX}->{Fore.WHITE} ")
    if response.lower() not in ["y", "n"]:
        print(f"{Fore.LIGHTRED_EX}{response} is not a valid choice!{Style.RESET_ALL}\n")
        return get_custom_user_agent_option()
    return response.lower()


def get_custom_user_agent():
    print(f"{Fore.LIGHTBLUE_EX}User Agent?{Style.RESET_ALL}")
    response = input(f"{Fore.LIGHTYELLOW_EX}->{Fore.WHITE} ")
    return response


def get_url():
    print(f"{Fore.LIGHTBLUE_EX}URL?{Style.RESET_ALL}")
    response = input(f"{Fore.LIGHTYELLOW_EX}->{Fore.WHITE} ")
    return response


def handle_console_flow():
    # Logo
    display_logo()
    # Output Option
    output_option = get_output_option()
    file_name = None
    if output_option == "y":
        file_name = get_file_name()
    print()
    # Verbose Option
    verbose_option = get_verbose_option()
    print()
    if "y" not in [output_option, verbose_option]:
        print(f"{Fore.LIGHTRED_EX}At least one option must be enabled!{Style.RESET_ALL}")
        return
    # Custom User Agent Option
    user_agent_option = get_custom_user_agent_option()
    custom_user_agent = None
    if user_agent_option == "y":
        custom_user_agent = get_custom_user_agent()
    print()
    # Url
    url = get_url()
    # Getting Questions and Answers
    contents = get_content(url, custom_user_agent)
    if not contents:
        print(f"{Fore.LIGHTRED_EX}Data retrieval failed{Style.RESET_ALL}")
        return
    # Output
    if file_name:
        print()
        with open(file_name, "w") as file:
            for i, content in enumerate(contents, 1):
                # Separate Question and Answer Groupings by an additional line
                if i % 2 == 0:
                    file.write(f"{content}\n\n")
                else:
                    file.write(f"{content}\n")
    if verbose_option == "y":
        print("\n")
        for i, content in enumerate(contents, 1):
            # Separate Questions and Answer Groupings by an additional line and add color alternation
            if i % 4 == 1 or i % 4 == 2:
                if i % 2 == 0:
                    print(f"{Fore.LIGHTGREEN_EX}{content}{Style.RESET_ALL}\n")
                else:
                    print(f"{Fore.LIGHTGREEN_EX}{content}{Style.RESET_ALL}")
            else:
                if i % 2 == 0:
                    print(f"{Fore.LIGHTMAGENTA_EX}{content}{Style.RESET_ALL}\n")
                else:
                    print(f"{Fore.LIGHTMAGENTA_EX}{content}{Style.RESET_ALL}")
    if file_name:
        print(f"\n{Fore.LIGHTBLUE_EX}File saved to {file_name}{Style.RESET_ALL}")
from traceback import print_tb
from colorama import Back, Fore, Style
import os
import json
import time
from rich.console import Console
from rich.table import Table
from rich import box
from rich.syntax import Syntax
import requests
from bs4 import BeautifulSoup

console = Console()

class terminal:
    def __init__(self):
        os.system("cls")
        self.projectCD = os.getcwd()
        while True:
            with open("C:/Terminal/user.json", encoding="utf-8") as f:
                self.user = json.load(f)
                f.close()
            if self.user["name"] == "None":
                self.newStart()
            with open("C:/Terminal/user.json", encoding="utf-8") as f:
                self.user = json.load(f)
                self.username = self.user["name"]
                f.close()
            with open("C:/Terminal/github.json", encoding="utf-8") as f:
                self.github_get = json.load(f)
                f.close()

            self.current_directory = os.getcwd()
            print(Fore.LIGHTYELLOW_EX+f"({self.current_directory}) "+Fore.LIGHTGREEN_EX+"("+self.username+") "+Fore.LIGHTBLUE_EX+"prompt "+Fore.WHITE+"$ ", end="")
            self.command = input("")
            self.return_ = self.getCommand(self.command)
            if self.return_ is not None: pass
            if self.return_ == "exit": break


    def getCommand(self, command):
        self.command = command
        if self.command.startswith("cmd"):
            try:
                print("\n"+Fore.LIGHTBLUE_EX+"CMD↴ "+Style.RESET_ALL+"\n")
                self.command = self.command.split(" ")[1]

                os.system(self.command)
            except Exception as e:
                print(Fore.RED+f"Error: {e}")
        elif self.command == "help":
            print("")
            print(" ~ "+Fore.LIGHTYELLOW_EX+"help                "+Style.RESET_ALL+" Get help")
            print(" ~ "+Fore.LIGHTYELLOW_EX+"ls                  "+Style.RESET_ALL+" List files and directories")
            print(" ~ "+Fore.LIGHTYELLOW_EX+"pwd                 "+Style.RESET_ALL+" Print the current working directory")
            print(" ~ "+Fore.LIGHTYELLOW_EX+"cd <directory>      "+Style.RESET_ALL+" Change the current working directory")
            print(" ~ "+Fore.LIGHTYELLOW_EX+"mkdir <directory>   "+Style.RESET_ALL+" Create a new directory")
            print(" ~ "+Fore.LIGHTYELLOW_EX+"rmdir <directory>   "+Style.RESET_ALL+" Remove a directory")
            print(" ~ "+Fore.LIGHTYELLOW_EX+"cat <file>          "+Style.RESET_ALL+" Read the contents of a file")
            print(" ~ "+Fore.LIGHTYELLOW_EX+"rm <file>           "+Style.RESET_ALL+" Remove a file")
            print(" ~ "+Fore.LIGHTYELLOW_EX+"exit                "+Style.RESET_ALL+" Exit the terminal")
            print(" ~ "+Fore.LIGHTYELLOW_EX+"cmd <command>       "+Style.RESET_ALL+" Run the CMD command")
            print(" ~ "+Fore.LIGHTYELLOW_EX+"gs <site-link>      "+Style.RESET_ALL+" Gets the codes of the given site")
            print(" ~ "+Fore.LIGHTYELLOW_EX+"clear               "+Style.RESET_ALL+" Clears the terminal")
            print(" ~ "+Fore.LIGHTYELLOW_EX+"github┐             "+                " -------GITHUB-------")
            print("   "+Fore.LIGHTYELLOW_EX+"      ├create       "+Style.RESET_ALL+" Create github repos.")
            print("   "+Fore.LIGHTYELLOW_EX+"      ├delete       "+Style.RESET_ALL+" Delete github repos.")
            print("   "+Fore.LIGHTYELLOW_EX+"      └save         "+Style.RESET_ALL+" Save your github token.")
            print(" ~ "+Fore.LIGHTYELLOW_EX+"run <app-name>      "+Style.RESET_ALL+" Runs the application you specify located in the current directory.")
            print(" ~ "+Fore.LIGHTYELLOW_EX+"reset               "+Style.RESET_ALL+" Resets the terminal.")
            print(" ~ "+Fore.LIGHTYELLOW_EX+"new┐                "+                " ----NEW--PROJECT----")
            print("   "+Fore.LIGHTYELLOW_EX+"   ├name*           "+Style.RESET_ALL+" Project name.")
            print("   "+Fore.LIGHTYELLOW_EX+"   └type*           "+Style.RESET_ALL+" 'python', 'web' or ex..")
            print(" ~ "+Fore.LIGHTYELLOW_EX+"open┐               "+                " ---OPEN---PROJECT---")
            print("   "+Fore.LIGHTYELLOW_EX+"    └name*          "+Style.RESET_ALL+" Project name.")
            print(" ~ "+Fore.LIGHTYELLOW_EX+"update              "+Style.RESET_ALL+" Update the terminal.")

        elif self.command == "exit": return "exit"
        elif self.command.startswith("ls"):self.listFilesAndDirectories()
        elif self.command.startswith("clear"): os.system("cls")
        elif self.command.startswith("new"):
            try:
                project_name = self.command.split(" ")[1]
                project_type = self.command.split(" ")[2]
                if project_type not in ["python", "web"]:
                    print(Fore.RED+"Error: Invalid project type. Use 'python' or 'web'.")
                    return
                os.makedirs(project_name)
                if project_type == "python":
                    with open(f"{project_name}/LICENSE", "w", encoding="utf-8") as f:
                        f.write("MIT License\n\n")
                        f.close()
                    with open(f"{project_name}/README.md", "w", encoding="utf-8") as f:
                        f.write("# "+project_name+"\n")
                        f.close()
                    with open(f"{project_name}/main.py", "w", encoding="utf-8") as f:
                        f.write(f"""print("Hello, World!") #{project_name}\main.py""")
                        f.close()
                    print(" ~ "+Fore.GREEN+"Project created successfully."+Style.RESET_ALL)
                    print(f" ~ You can open your project by typing 'open {project_name}'.")
                elif project_type == "web":
                    with open(f"{project_name}/index.html", "w", encoding="utf-8") as f:
                        f.write(f"""<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{project_name} #Created with 'Ars BASH'</title>
    <link rel="stylesheet" href="style.css">
    <script src="script.js"></script>
</head>
<body>
    
</body>
</html>
""")
                        f.close()

                    with open(f"{project_name}/LICENSE", "w", encoding="utf-8") as f:
                        f.write("MIT License\n\n")
                        f.close()
                    
                    with open(f"{project_name}/README.md", "w", encoding="utf-8") as f:
                        f.write("# "+project_name+"\n")
                        f.close()

                    with open(f"{project_name}/style.css", "w", encoding="utf-8") as f:
                        f.write("""/* Your CSS goes here */""")
                        f.close()
                    
                    with open(f"{project_name}/script.js", "w", encoding="utf-8") as f:
                        f.write("""// Your JavaScript goes here...""")
                        f.close()

                    print(" ~ "+Fore.GREEN+"Project created successfully."+Style.RESET_ALL)
                    print(f" ~ You can open your project by typing 'open {project_name}'.")
            except Exception as e:
                print(Fore.RED+"Error: "+str(e))
        
        elif self.command.startswith("open"):
            project_name = self.command.split(" ")[1]
            try:
                os.chdir(project_name)
                os.system(f"code .")
            except Exception as e:
                print(Fore.RED+"Error: "+str(e))

        elif self.command == "reset":
            print(Fore.LIGHTYELLOW_EX+" >>> "+Style.RESET_ALL+"Are you sure you want to reset? [Y/n] : ", end="")
            self.resetWant = input()
            if self.resetWant == "y" or self.resetWant == "Y": self.resetTerm()
            else: print("Pass")

        elif self.command.startswith("run"):
            try:
                self.command = self.command.split(" ")[1]
                os.startfile(os.getcwd()+"/"+self.command)
            except Exception as e:
                print(Fore.RED+"Error: "+str(e))

        elif self.command.startswith("pwd"): print(Fore.LIGHTYELLOW_EX+"Current working directory: "+Fore.WHITE+self.current_directory)

        elif self.command.startswith("cd"):
            try:
                directory = self.command.split(" ")[1]
                os.chdir(directory)
                self.current_directory = os.getcwd()
                with open("C:/Terminal/config.json", "w", encoding="utf-8") as f:
                    json.dump({"$default.folder": self.current_directory}, f, ensure_ascii=False)
                    f.close()
            except Exception as e:
                print(Fore.RED+"Error: "+str(e))

        elif self.command.startswith("mkdir"):
            directory = self.command.split(" ")[1]
            os.mkdir(directory)

        elif self.command.startswith("rmdir"):
            directory = self.command.split(" ")[1]
            os.rmdir(directory)

        elif self.command == "update":
            os.startfile("update.py")
            os.system("exit")

        elif self.command.startswith("cat"):
            file = self.command.split(" ")[1]
            try:
                with open(file, 'r', encoding="utf-8") as f:
                    print(Fore.LIGHTYELLOW_EX+"File content: "+Style.RESET_ALL)
                    _, uzanti = os.path.splitext(file)

                    # Uzantılara göre dosya türünü belirle
                    dosya_turleri = {
                        '.txt': 'text',
                        '.js': 'javascript',
                        '.java': 'java',
                        '.png': 'png',
                        '.docx': 'word',
                        '.xlsx': 'excel',
                        '.py': 'python',
                        '.html': 'html',
                        '.json': 'json',
                        '.mp4': 'video'}
                    syntax = Syntax(f.read(), dosya_turleri[uzanti], theme="dracula", line_numbers=True)
                    console.print(syntax)
            except FileNotFoundError:
                print(Fore.RED+"Error: File not found.")

        elif self.command.startswith("github"):

            action = self.command.split(" ")[1]
            if action == "create":
                if self.github_get["token"] == "None":
                    print(Fore.LIGHTYELLOW_EX+"Github Token: "+Style.RESET_ALL, end="")
                    token = input()
                    print(Fore.LIGHTYELLOW_EX+"Github Username: "+Style.RESET_ALL, end="")
                    uname = input()
                else:
                    token = self.github_get["token"]
                    uname = self.github_get["name"]
                print(Fore.LIGHTYELLOW_EX+"Repo Name: "+Style.RESET_ALL, end="")
                self.rname = input()
                print(Fore.LIGHTYELLOW_EX+"Repo State (Private[Y]/Public[n]): "+Style.RESET_ALL, end="")
                self.rstate = input()
                while True:
                        if self.rstate == "Y" or self.rstate == "y":
                            self.rstate = True
                            break
                        elif self.rstate == "N" or self.rstate == "n":
                            self.rstate = False
                            break
                        else:
                            print(Fore.RED+"Error: Invalid choice. Please enter 'Y' for Private or 'N' for Public.")
                            print(Fore.LIGHTYELLOW_EX+"Repo State (Private[Y]/Public[n]): "+Style.RESET_ALL, end="")
                            self.rstate = input()
                            continue
                self.create_github_repo(token=token, owner=uname, repo_name=self.rname, state=self.rstate)
            elif action == "delete":
                if self.github_get["token"] == "None":
                    print(Fore.LIGHTYELLOW_EX+"Github Token: "+Style.RESET_ALL, end="")
                    token = input()
                    print(Fore.LIGHTYELLOW_EX+"Github Username: "+Style.RESET_ALL, end="")
                    uname = input()
                else:
                    token = self.github_get["token"]
                    uname = self.github_get["name"]

                print(Fore.LIGHTYELLOW_EX+"Repo Name: "+Style.RESET_ALL, end="")
                self.rname = input()
                self.delete_github_repo(token=token, owner=uname, repo_name=self.rname)
            elif action == "save":
                print(Fore.LIGHTYELLOW_EX+"Github Token: "+Style.RESET_ALL, end="")
                self.save_token = input()
                print(Fore.LIGHTYELLOW_EX+"Github Username: "+Style.RESET_ALL, end="")
                self.save_g_name = input()
                self.saveGit = {
                    "token": self.save_token,
                    "name": self.save_g_name
                }
                with open("C:/Terminal/github.json", "w", encoding="utf-8") as f:
                    json.dump(self.saveGit, f, ensure_ascii=False)
                    f.close()
                    print("Github token saved successfully.")
            else:
                print("Invalid action. Use 'create','delete' or 'token'.")

        elif self.command.startswith("gs"):
            try:
                site = self.command.split(" ")[1]
                response = requests.get(site)

                # HTML kaynak kodunu al
                html_content = response.text

                # Güzel bir biçimde parse etme
                soup = BeautifulSoup(html_content, "html.parser")
                syntax = Syntax(soup.prettify(), "html", theme="dracula", line_numbers=True)
                console.print(syntax)
            except Exception as e:
                print(Fore.RED+f"Error: {e}.")


        elif self.command.startswith("rm"):
            file = self.command.split(" ")[1]
            try:
                os.remove(file)
                print(Fore.LIGHTYELLOW_EX+"File removed: "+Fore.WHITE+file)
            except FileNotFoundError:
                print(Fore.RED+"Error: File not found.")

        elif self.command.startswith(""): ...

        else:
            if self.command != "":
                print("\n"+Fore.LIGHTBLUE_EX+"CMD↴ "+Style.RESET_ALL+"\n")
                os.system(self.command)

        if self.command != "" and self.command != "reset" and self.command != "clear":
            print()

    def listFilesAndDirectories(self):
        try:
            files = os.listdir()
            print()
            for file in files:
                if os.path.isdir(file):
                    print(Fore.YELLOW+" / "+Fore.LIGHTBLACK_EX+file)
                else:
                    print(Fore.CYAN+" ~ "+Fore.WHITE+file)
        except Exception as e:
            print(Fore.RED+"Error: "+str(e))

    def resetTerm(self):
        self.user["name"] = "None"
        self.delGit = {
            "token": "None",
            "name": "None"
        }
        with open("C:/Terminal/user.json", "w", encoding="utf-8") as f:
            json.dump(self.user, f, ensure_ascii=False)
            f.close()
        with open("C:/Terminal/github.json", "w", encoding="utf-8") as f:
            json.dump(self.delGit, f, ensure_ascii=False)
            f.close()
        os.system("cls")
        print("Terminal resetted.")
        time.sleep(1)
        os.system("cls")
        self.newStart()

    def newStart(self):
        print(Fore.LIGHTYELLOW_EX+"NAME: "+Style.RESET_ALL, end="")
        self.uname = input()
        with open("C:/Terminal/user.json", "w", encoding="utf-8") as f:
            json.dump({"name": self.uname}, f, ensure_ascii=False)
            f.close()
        os.system("cls")
        print("Welcome, "+self.uname+"!")
        time.sleep(1)
        os.system("cls")

    def create_github_repo(self, token, owner, repo_name, state):
        self.url = "https://api.github.com/user/repos"
        self.headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }
        self.data = {
            "name": repo_name,
            "private": state  # True yaparsan özel repo olur
        }
        self.response = requests.post(self.url, headers=self.headers, json=self.data)

        if self.response.status_code == 201:
            print(Fore.LIGHTYELLOW_EX+f"Repository created successfully: {Style.RESET_ALL+repo_name}")
        else:
            print(Fore.LIGHTYELLOW_EX+f"Failed to create repository: {Style.RESET_ALL+str(self.response.status_code)}")
            print(self.response.json())

    def delete_github_repo(self, token, owner, repo_name):
        self.url = f"https://api.github.com/repos/{owner}/{repo_name}"
        self.headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }

        self.response = requests.delete(self.url, headers=self.headers)

        if self.response.status_code == 204:
            print(f"Repository successfully deleted: {Style.RESET_ALL+repo_name}")
        else:
            if self.response.status_code == 203:
                print(Fore.LIGHTYELLOW_EX+f"Repository could not be deleted: {Style.RESET_ALL}Make sure you grant token authorizations correctly.")
            print(self.response.json())

if __name__ == '__main__':
    term = terminal()

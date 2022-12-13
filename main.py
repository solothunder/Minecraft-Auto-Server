import server_add
import server_control
from els import els

def yes_no_input():
    while True:
        print("注意！このプログラムはβ版なので　不具合発生する可能性があります。\nもし不具合が発生した場合には、githubの Issuesにお知らせください。")
        print("FastServerみたいなもん作ってみた（Python）")
        choice = input("サーバーを作成するか管理するか選択してください。 'add' か 'control' [a/c]: ").lower()
        if choice in ['a', 'ad', 'add']:
            server_add.main()
        elif choice in ['c', 'co', 'con', 'cont', 'contr', 'contro', 'control']:
            server_control.main()
        else:
            print("存在しません")
            return False

def main():
    path = ["server_add.py", "server_control.py", "minecraft.py", "els/els.py", "temp/server.properties", "temp/eula.txt"]
    for pathcount in path:
        els.check_file_dir(pathcount, "True", "True")
    if yes_no_input():
        print('OK!')

if __name__ == "__main__":
    main()
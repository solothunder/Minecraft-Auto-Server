from els import els
import minecraft
import sys
import os

def yes_no_input():
    while True:
        choice = input("作成しますか？ 'yes' か 'no' [y/N]: ").lower()
        if choice in ['y', 'ye', 'yes']:
            return True
        elif choice in ['n', 'no']:
            sys.exit()

def main_run():
    els.check_ping("google.com", "3", "True", "True")
    check_dir = els.check_file_dir("minecraft/", "false", "false")
    if (check_dir == "error"):
        os.mkdir("minecraft")
    print("FastServerみたいなもん作ってみた（Python） サーバー作成")
    if yes_no_input():
        print('作成します!')
    minecraft_main_port = input("ポート番号を入力してください（何も入力しなければデフォルトで:25565）:")
    print("マインクラフトサーバー(PaperMC)をダウンロードします")
    minecraft.minecraft_download()
    minecraft.minecraft_install_yes_no(minecraft_main_port)
    minecraft.minecraft_eula_edit()
    minecraft.minecraft_port(minecraft_main_port)
    els.global_ip("False", "True")

    print("注意：まだサーバーを起動していません。")
import urllib.request
import shutil
import sys
import subprocess
#同意用プログラム
def yes_no_input(text):
    while True:
        choice = input(text).lower()
        if choice in ['y', 'ye', 'yes']:
            return True
        elif choice in ['n', 'no']:
            sys.exit()
# papermc dl
def minecraft_download():
    print("PaperMC ダウンロード中 (V.1.19.2 #307)")
    url='https://api.papermc.io/v2/projects/paper/versions/1.19.2/builds/307/downloads/paper-1.19.2-307.jar'
    save_name='minecraft/paper-1.19.2.jar'
    urllib.request.urlretrieve(url, save_name)
    print("PaperMC ダウンロード完了")
# 入れた情報がいいかどうか？
def minecraft_install_yes_no(port):
    if not port:
        port = "25565(デフォルト)"
    else:
        pass
    print("入力情報：\nサーバーメインポート：",port)
    yes_no_input("これでよろしいでしょうか？（編集したい場合はプログラムを終了してもう一回設定してください。） yes か　no [y/n]：")
# eula 同意（yes no あり）
def minecraft_eula_edit():
    print("Minecraft EULA（使用許諾契約 / 利用許諾契約）に同意しますか？")
    print("MinecraftのEULA は https://www.minecraft.net/ja-jp/terms/r3 こちらを参照してください。")
    yes_no_input("同意しますか? 'yes' か 'no' [y/N]: ")
    shutil.copyfile("temp/eula.txt", "minecraft/eula.txt")
    print("同意しました。")
# minecraft 実行
def minecraft_exec(xmx, xms):
    print("サーバー起動")
    print("java -jar -Xmx"+xmx+"G -Xms"+xms+"M minecraft\paper-1.19.2.jar --nogui")
    cmd = "java -Xmx"+xmx+"G -Xms"+xms+"G -jar paper-1.19.2.jar --nogui"
    subprocess.call(cmd, shell=True, cwd=r"minecraft/")
    print("サーバー停止")
# 行編集
def replace_func(fname, replace_set):
    target, replace = replace_set
    
    with open(fname, 'r') as f1:
        tmp_list =[]
        for row in f1:
            if row.find(target) != -1:
                tmp_list.append(replace)
            else:
                tmp_list.append(row)
    
    with open(fname, 'w') as f2:
        for i in range(len(tmp_list)):
            f2.write(tmp_list[i])

def minecraft_port(port):
    print("ポート設定中")
    if not port:
        port = "25565"
    else:
        pass
    path = 'temp/server.properties'
    port_text = "server-port="+port+"\n"
    replace_setA = ('server-port=', port_text) # (検索する文字列, 置換後の文字列)
    # call func
    replace_func(path, replace_setA)
    shutil.copyfile("temp/server.properties", "minecraft/server.properties")

    print("ポート設定完了")
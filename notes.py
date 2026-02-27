import subprocess
import sys
import os

def run_git_command(command, description):
    """执行 Git 命令并处理输出"""
    print(f"\n  正在{description}...")
    try:
        result = subprocess.run(
            command,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            cwd=os.path.dirname(os.path.abspath(__file__))
        )
        print(f" {description}成功！")
        if result.stdout.strip():
            print(f"   输出：{result.stdout.strip()}")
        return True
    except subprocess.CalledProcessError as e:
        print(f" {description}失败！")
        print(f"   错误信息：{e.stderr.strip()}")
        return False

def main():
    print("="*50)
    print("   Obsidian 笔记一键同步到 GitHub")
    print("="*50)

    # 1. 检查是否在 Git 仓库根目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    if not os.path.exists(os.path.join(script_dir, ".git")):
        print(" 错误：请将此脚本放在 GitHub 仓库根目录下！")
        input("\n按回车键退出...")
        sys.exit(1)

    # 2. 检查 Git 是否安装
    try:
        subprocess.run(
            ["git", "--version"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
    except FileNotFoundError:
        print(" 错误：未检测到 Git，请先安装 Git 并配置环境变量！")
        input("\n按回车键退出...")
        sys.exit(1)

    # 3. 获取用户输入的提交注释
    while True:
        commit_msg = input("\n 请输入本次同步的注释内容（不能为空）：").strip()
        if commit_msg:
            break
        print(" 注释不能为空，请重新输入！")

    # 4. 开始同步流程
    print("\n" + "="*50)
    print("   开始同步...")
    print("="*50)

    # 步骤1：拉取远程最新内容
    if not run_git_command(["git", "pull", "origin", "main"], "拉取远程最新内容"):
        input("\n按回车键退出...")
        sys.exit(1)

    # 步骤2：添加所有更改
    if not run_git_command(["git", "add", "."], "添加本地更改"):
        input("\n按回车键退出...")
        sys.exit(1)

    # 步骤3：提交更改
    if not run_git_command(["git", "commit", "-m", commit_msg], "提交本地更改"):
        # 特殊情况：没有需要提交的更改
        input("\n按回车键退出...")
        sys.exit(1)

    # 步骤4：推送到 GitHub
    if not run_git_command(["git", "push", "origin", "main"], "推送到 GitHub"):
        input("\n按回车键退出...")
        sys.exit(1)

    # 同步完成
    print("\n" + "="*50)
    print(" 所有同步已完成！")
    print("="*50)
    input("\n按回车键退出...")

if __name__ == "__main__":
    main()
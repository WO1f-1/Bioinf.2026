import subprocess
import sys
import os


def run_git_command(command, description, show_output=True):
    """执行 Git 命令并处理输出"""
    print(f"\n▶️  正在{description}...")
    try:
        result = subprocess.run(
            command,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            cwd=os.path.dirname(os.path.abspath(__file__))
        )
        print(f"✅ {description}成功！")
        if show_output and result.stdout.strip():
            print(f"   输出：{result.stdout.strip()}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description}失败！")
        error_msg = e.stderr.strip()
        if error_msg:
            print(f"   错误信息：{error_msg}")
        return False


def main():
    print("=" * 60)
    print(" Obsidian 笔记本地 → GitHub 一键同步工具")
    print("=" * 60)
    print(" 注意：本工具只会把你本地的修改推送到 GitHub，不会覆盖本地笔记！")

    # --------------------------
    # 1. 环境检查
    # --------------------------
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # 检查是否在 Git 仓库根目录
    if not os.path.exists(os.path.join(script_dir, ".git")):
        print("\n 错误：请将此脚本放在 GitHub 仓库根目录下！")
        print("   （和 obsidian-notes 文件夹同级的位置）")
        input("\n按回车键退出...")
        sys.exit(1)

    # 检查 Git 是否安装
    try:
        subprocess.run(
            ["git", "--version"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
    except FileNotFoundError:
        print("\n 错误：未检测到 Git，请先安装 Git 并配置环境变量！")
        input("\n按回车键退出...")
        sys.exit(1)

    # --------------------------
    # 2. 检查本地是否有修改
    # --------------------------
    print("\n 正在检查本地笔记修改...")
    status_result = subprocess.run(
        ["git", "status", "--porcelain"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        cwd=script_dir
    )

    if not status_result.stdout.strip():
        print("\nℹ  本地没有检测到笔记修改，无需同步。")
        print("   （请确保你修改的笔记放在了 obsidian-notes 文件夹里）")
        input("\n按回车键退出...")
        sys.exit(0)

    # 显示有哪些修改
    print("\n 检测到以下本地修改：")
    for line in status_result.stdout.strip().split('\n'):
        print(f"   {line.strip()}")

    # --------------------------
    # 3. 获取用户输入的提交注释
    # --------------------------
    while True:
        commit_msg = input("\n✏️  请输入本次同步的注释内容（不能为空）：").strip()
        if commit_msg:
            break
        print("  注释不能为空，请重新输入！")

    # --------------------------
    # 4. 开始同步流程（本地 → GitHub）
    # --------------------------
    print("\n" + "=" * 60)
    print("   开始同步（本地笔记 → GitHub）...")
    print("=" * 60)

    # 步骤1：先拉取远程最新内容（避免冲突，不会覆盖本地未提交的修改）
    print("\n 先拉取远程最新内容，防止冲突...")
    if not run_git_command(["git", "pull", "origin", "main"], "拉取远程最新内容"):
        print("\n💡 提示：如果拉取失败，可能是网络问题，或者有冲突需要手动解决。")
        input("\n按回车键退出...")
        sys.exit(1)

    # 步骤2：添加所有本地修改
    if not run_git_command(["git", "add", "."], "添加本地笔记修改"):
        input("\n按回车键退出...")
        sys.exit(1)

    # 步骤3：提交本地修改
    if not run_git_command(["git", "commit", "-m", commit_msg], "提交本地笔记修改"):
        input("\n按回车键退出...")
        sys.exit(1)

    # 步骤4：推送到 GitHub（关键一步：本地 → 远程）
    print("\n 正在将本地笔记推送到 GitHub...")
    if not run_git_command(["git", "push", "origin", "main"], "推送本地笔记到 GitHub"):
        print("\n 提示：如果推送失败，可能是网络问题，或者没有权限。")
        input("\n按回车键退出...")
        sys.exit(1)

    # --------------------------
    # 5. 同步完成
    # --------------------------
    print("\n" + "=" * 60)
    print(" 同步成功！你的本地笔记已经上传到 GitHub 了！")
    print("=" * 60)
    print(" 现在可以去 GitHub 仓库页面查看更新了。")
    input("\n按回车键退出...")


if __name__ == "__main__":
    main()
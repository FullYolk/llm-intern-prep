import sys
import platform
import subprocess
def get_cmd_output(cmd):
    try:
        result = subprocess.run(cmd,capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except Exception as e:
        return f"Not Available{e}"

def main():
    print("Environment Check")
    print(f"Python Version:{sys.version}")
    print(f"Platform:{platform.platform()}")
    tools = {
        "git" : ["git","--version"],
        "docker" :["docker","--version"],
        "node" :["node","--version"],
        "npm" :["npm.cmd","--version"],
        "pnpm" :["pnpm.cmd","--version"],
        "uv" :["uv","--version"],
    }
    for name, cmd in tools.items():
        print(f"{name}:{get_cmd_output(cmd)}")
if __name__ == "__main__":
    main()
          
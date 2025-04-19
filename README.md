# apt-cli

**apt-cli** is an advanced REPL (Read-Eval-Print Loop) interface for APT package management, designed for users who demand both power and elegance in system administration. It combines traditional terminal workflows with modern interactive features, offering a seamless bridge between CLI efficiency and GUI-like accessibility.

## Features
- **Interactive Rich-Text Menu** with categorized actions
- **Multi-Modal Input Support** (CLI, GUI via `dialog`, Rainbow CLI via `lolcat`)
- **AI-Native Interface** with natural language processing capabilities
- **17 Essential APT Operations** including version pinning, dependency analysis, and dry-run simulations
- **Real-Time Command Visualization** with colorized output
- **System Sanitization Tools** (cache cleaning, orphan removal, full purges)
- **Dependency Intelligence** (recommended packages, reverse dependencies)
- **Safety Features** including simulation mode and confirmation prompts
- **Cross-Platform Readiness** with hybrid terminal/GUI workflows

## Installation

### Requirements
- Python 3.8+
- APT-based system (Debian/Ubuntu derivatives)
- `dialog` package for GUI input (`sudo apt install dialog`)
- `lolcat` for rainbow output (`sudo gem install lolcat`)
- Python dependencies: `rich`

### System-Wide Setup
```bash
curl -O https://raw.githubusercontent.com/beautifulsh2/apt-cli/main/apt-cli.py
chmod +x apt-cli.py
sudo mv apt-cli.py /usr/local/bin/apt-cli
```

### Dependency Installation
```bash
sudo apt install python3-pip dialog
sudo gem install lolcat
pip3 install rich
```

## Usage

### Interactive Mode
```bash
apt-cli
```

### AI Natural Language Mode
```bash
apt-cli --ai
```

### Keybindings
- **Numerical Selection**: Choose actions via number keys
- **Hybrid Input**: Switch between CLI/GUI input methods mid-session
- **Session History**: Arrow keys for command recall
- **Flow Control**: Ctrl+C to abort current operation

## Command Reference

### Core Operations
| Command              | Functionality                          |
|----------------------|----------------------------------------|
| `apt-cli`            | Launch interactive REPL environment    |
| `apt-cli --ai`       | Activate natural language processing   |

### AI Pattern Matching
The AI engine recognizes these core phrases:
- "Install security updates"
- "Remove orphaned dependencies"
- "Show kernel versions"
- "Audit package history"
- "Verify repository integrity"
- "Diagnose dependency conflicts"

## Examples

### Menu-Driven Workflow
```bash
$ apt-cli
1) Install security patches
2) Rollback problematic update
3) Audit third-party repositories
> 1
[+] Running: apt full-upgrade --only-upgrade-security
```

### AI-Driven Workflow
```bash
$ apt-cli --ai
AI> Harden system with latest security patches
[+] Executing: apt update && apt upgrade --only-upgrade-security -y
```

### Advanced Usage
```bash
# Multi-package install with version constraints
apt-cli
> 2
Input: nginx=1.18.0-0ubuntu1.2 nodejs=12.22.1~dfsg-1ubuntu1

# Dependency graph analysis
apt-cli --ai
AI> Show dependency tree for postgresql-14
[+] Running: apt-cache depends --recurse --no-recommends postgresql-14
```

## License

Distributed under MIT License. See [LICENSE](https://github.com/beautifulsh2/apt-cli/blob/main/LICENSE) for full text.

## Contributing

Architecture contributions welcome. Submit PRs to the development branch with:
- Detailed change rationale
- Impact analysis on existing workflows
- Test cases for complex operations

## Acknowledgments

- **Rich Terminal Toolkit**: Textualize/rich
- **UNIX Philosophy**: Doug McIlroy
- **APT Maintainers**: Debian Packaging Team

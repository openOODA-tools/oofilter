# oofilter: Sovereign Boolean Logic & Stream Predicate Filter

<div align="center">

```
================================================================================
                                oofilter
               Sovereign openOODA Stream Predicate Filter
================================================================================
```

**Sovereign Boolean Logic & Stream Predicate Filter**  
*Evaluates boolean logic expressions against structured stream line objects without ambient authority.*  
*Two Faces, One Engine:* Modern POSIX terminal ergonomics • Streaming JSON-RPC 2.0 MCP for AI agents  
Written in 100% pure [openOODA](https://github.com/openOODA).

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![openOODA](https://img.shields.io/badge/openOODA-1.0-emerald.svg)](https://openooda.org)
[![Architecture: x86_64 | aarch64](https://img.shields.io/badge/Arch-x86__64%20%7C%20aarch64-lightgrey.svg)]()
[![Release: v0.2.0](https://img.shields.io/badge/Release-v0.2.0-blue.svg)](https://github.com/openOODA-tools/oofilter/releases/tag/v0.2.0)

</div>

---

## 1. Quick Install

### Automated Installer (Linux x86_64 & aarch64)
```bash
curl -fsSL https://openooda-tools.github.io/oofilter/install.sh | bash
```

### Native Package Managers
```bash
# Arch Linux (AUR / PKGBUILD)
yay -S oofilter-bin
# Or manual PKGBUILD:
cd packaging/arch && makepkg -si

# Debian / Ubuntu (.deb)
curl -fsSL https://openooda-tools.github.io/oofilter/install.sh | bash -s -- --deb

# Fedora / RHEL (.rpm)
curl -fsSL https://openooda-tools.github.io/oofilter/install.sh | bash -s -- --rpm
```

### Uninstallation
```bash
oofilter-uninstall
# or: curl -fsSL https://openooda-tools.github.io/oofilter/uninstall.sh | bash -s -- --uninstall
```

---

## 2. CLI Usage

```
usage: oofilter [options] [-e EXPR] [FILE...]

Evaluates boolean logic expressions against structured stream line objects.

POSIX Options:
  -e, --expr EXPR       boolean predicate expression (e.g. '$1 == "admin" && $2 > 10')
  -v, --invert-match    invert sense of matching (select non-matching lines)
  -c, --count           output only a count of matching lines
  -n, --line-number     prefix each output line with 1-based line number
  -F, -d, --delimiter D field delimiter (default: whitespace)
  -j, --json            output matching lines and fields as JSON Lines
  -D, --demo            interactive multi-predicate stream filtering showcase
      --test            execute internal subsystem verification suite
      --mcp             run as Model Context Protocol JSON-RPC stdio server
  -v, --version         output version information and exit
      --help            display this help and exit
```

### Supported Syntax & Operators
* **Field References**: `$0` (entire line), `$1..$N` (1-based positional tokens), `NR` / `line` (line number).
* **Logical Operators**: `&&` / `and`, `||` / `or`, `!` / `not`, grouping parentheses `( ... )`.
* **Relational Comparisons**: `==` (or `=`), `!=`, `<`, `<=`, `>`, `>=`.
* **Pattern & Containment**: `=~` (match), `!~` (not match), `contains`.

### Examples
```bash
# Filter lines where first column is ERROR
cat server.log | oofilter -e '$1 == "ERROR"'

# Multi-column predicate with line numbers
oofilter -n -e '$1 == "INFO" && $4 == "status=200"' access.log

# Invert match: drop management records
oofilter -v -e '$3 == "management"' staff.txt

# Count matching records with comma delimiter
cat data.csv | oofilter -c -F "," -e '$2 > 100 && $3 == "active"'

# Output structured JSON matches
cat auth.log | oofilter -j -e '$2 == "failure"'
```

---

## 3. Model Context Protocol (MCP)

When invoked with `--mcp`, `oofilter` runs a JSON-RPC 2.0 stdio server providing streaming structured tools for AI coding agents:

```bash
oofilter --mcp
```

### Registered Tools
| Tool Name | Parameters | Description |
|---|---|---|
| `filter_evaluate` | `line` (string), `expr` (string), `delimiter` (string) | Evaluates boolean predicate against a single line context |
| `filter_stream` | `text` (string), `expr` (string), `delimiter` (string), `invert` (bool), `json_mode` (bool) | Filters streaming text records matching a boolean expression |
| `filter_compile_ast` | `expr` (string) | Parses and compiles a predicate expression into an AST summary |
| `filter_predicates` | *(none)* | Lists supported operators, syntax rules, and field selectors |
| `filter_demo` | *(none)* | Runs interactive multi-predicate stream filtering showcase |

---

## 4. Security & Zero Ambient Authority

* **Pure Capability Bounded:** Operates strictly with explicit tokens (`&FsReadCap`, `&ProcessCap`, `&EnvCap`). Physical absence of ambient disk or network leakage.
* **Negative-Trust Architecture:** Strict expression grammar, recursive descent without eval or subprocess shells.
* **Hermetic Binary:** Standalone zero-dependency executable.

---

## 5. License

Apache License, Version 2.0. See [LICENSE](LICENSE) for details.
